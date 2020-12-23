"""
Class and functions for whylogs logging
"""
import  datetime 
import typing
from typing import List, Optional

import pandas as pd
from pandas._typing import FilePathOrBuffer

from whylogs.app.writers import Writer
from whylogs.core import DatasetProfile

TIME_ROTATION_VALUES= [ "s", "m", "h", "d"] 

class Logger:
    """
    Class for logging whylogs statistics.

    :param session_id: The session ID value. Should be set by the Session boject
    :param dataset_name: The name of the dataset. Gets included in the DatasetProfile metadata and can be used in generated filenames.
    :param dataset_timestamp: Optional. The timestamp that the logger represents
    :param session_timestamp: Optional. The time the session was created
    :param tags: Optional. Dictionary of key, value for aggregating data upstream
    :param metadata: Optional. Dictionary of key, value. Useful for debugging (associated with every single dataset profile)
    :param writers: List of Writer objects used to write out the data
    :param with_rotation_time. Whether to rotate with time.     
    :param verbose: enable debug logging or not
    :param cache: set how many dataprofiles to cache
    """

    def __init__(self,
        session_id: str,
        dataset_name: str,
        dataset_timestamp: Optional[datetime.datetime] = None,
        session_timestamp: Optional[datetime.datetime] = None,
        tags: typing.Dict[str, str] = None,
        metadata: typing.Dict[str, str] = None,
        writers = List[Writer],
        verbose: bool = False, 
        with_rotation_time: Optional[str] = None, 
        cache: int =1,
        ):
        """
        """
        if session_timestamp is None:
            self.session_timestamp = datetime.datetime.now(datetime.timezone.utc)
        else:
            self.session_timestamp= session_timestamp
        self.dataset_name = dataset_name
        self.writers = writers
        self.verbose = verbose
        self.cache=cache
        self.tags=tags
        self.session_id=session_id
        self.metadata= metadata
            
        self._profiles = [ DatasetProfile(
            self.dataset_name,
            dataset_timestamp=dataset_timestamp,
            session_timestamp=self.session_timestamp,
            tags=self.tags,
            metadata=self.metadata,
            session_id=self.session_id
        )]
        self._active = True
        # intialize to seconds in the day
        self.interval = 60*60*24
        self.with_rotation_time = with_rotation_time
        self.set_rotation(with_rotation_time)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def profile(self):
        """
        :return: the last backing dataset profile
        :rtype: DatasetProfile
        """
        return self._profiles[-1]


    def set_rotation(self,with_rotation_time: str = None):

        if with_rotation_time is not None:
            self.with_rotation_time= with_rotation_time.lower()

            if self.with_rotation_time  == 's':
                self.interval = 1 # one second
                self.suffix = "%Y-%m-%d_%H-%M-%S"
                self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}(\.\w+)?$"
            elif self.with_rotation_time  == 'm':
                self.interval = 60 # one minute
                self.suffix = "%Y-%m-%d_%H-%M"
                self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}(\.\w+)?$"
            elif self.with_rotation_time  == 'h':
                self.interval = 60 * 60 # one hour
                self.suffix = "%Y-%m-%d_%H"
                self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}(\.\w+)?$"
            elif self.with_rotation_time  == 'd':
                self.interval = 60 * 60 * 24 # one day
                self.suffix = "%Y-%m-%d"
                self.extMatch = r"^\d{4}-\d{2}-\d{2}(\.\w+)?$"
            else:
                raise TypeError("Invalid choice of rotation time, valid choices are {}".format(TIME_ROTATION_VALUES))
            #time in seconds
            current_time = int(datetime.datetime.utcnow().timestamp())
            self.rotate_at = self.rotate_when(current_time)
        else:
            ValueError("with_rotation_time required")
    def rotate_when(self, time):

        result = time + self.interval
        return result

    def should_rotate(self,):
        
        if self.with_rotation_time is None:
            return False

        current_time = int(datetime.datetime.utcnow().timestamp())
        if current_time >= self.rotate_at:
            return True
        return False

    def rotate_time(self):
        """
        rotate with time add a suffix 
        """
        current_time=int(datetime.datetime.utcnow().timestamp())
        # get the time that this current logging rotation started 
        sequence_start = self.rotate_at - self.interval
        timeTuple = datetime.datetime.fromtimestamp(sequence_start)
        rotation_suffix ="." + timeTuple.strftime(self.suffix)


        self.flush(rotation_suffix)

        if len(self._profiles)>self.cache:
            self._profiles[-self.cache-1]=None

        self._profiles.append(DatasetProfile(
            self.dataset_name,
            dataset_timestamp=datetime.datetime.now(datetime.timezone.utc),
            session_timestamp=self.session_timestamp,
            tags=self.tags,
            metadata=self.metadata,
            session_id=self.session_id
        ))

        #compute new rotate_at and while loop in case current function
        #takes longer than interval
        self.rotate_at = self.rotate_when(current_time)
        while self.rotate_at <= current_time:
            self.rotate_at += self.interval


    def flush(self,rotation_suffix:str =None):
        """
        Synchronously perform all remaining write tasks
        """
        if not self._active:
            print("WARNING: attempting to flush a closed logger")
            return None

        for writer in self.writers:
            if rotation_suffix is None:
                writer.write(self._profiles[-1])
            else:
                writer.write(self._profiles[-1],rotation_suffix)
        

    # def load_from_file():

        
    def close(self) -> Optional[DatasetProfile]:
        """
        Flush and close out the logger, outputs the last profile
        
        :return: the result dataset profile. None if the logger is closed
        """
        if not self._active:
            print("WARNING: attempting to close a closed logger")
            return None
        if self.with_rotation_time is None:
            self.flush()
        else:
            self.rotate_time()       
            _ = self._profiles.pop()

        self._active = False
        profile = self._profiles[-1]
        self._profiles = None
        return profile

    def log(
        self,
        features: typing.Dict[str, any] = None,
        feature_name: str = None,
        value: any = None,
    ):
        """
        Logs a collection of features or a single feature (must specify one or the other).

        :param features: a map of key value feature for model input
        :param feature_name: a dictionary of key->value for multiple features. Each entry represent a single columnar feature
        :param feature_name: name of a single feature. Cannot be specified if 'features' is specified
        :param value: value of as single feature. Cannot be specified if 'features' is specified

        """
        if not self._active:
            return None

        if self.should_rotate():
            self.rotate_time()

        if features is None and feature_name is None:
            return

        if features is not None and feature_name is not None:
            raise ValueError("Cannot specify both features and feature_name")

        if features is not None:
            self._profiles[-1].track(features)
        else:
            self._profiles[-1].track_datum(feature_name, value)

    def log_csv(self, filepath_or_buffer: FilePathOrBuffer, **kwargs):
        """
        Log a CSV file. This supports the same parameters as :func`pandas.red_csv<pandas.read_csv>` function.

        :param filepath_or_buffer: the path to the CSV or a CSV buffer
        :type filepath_or_buffer: FilePathOrBuffer
        :param kwargs: from pandas:read_csv
        """
        if not self._active:
            return
        if self.should_rotate():
            self.rotate_time()

        df = pd.read_csv(filepath_or_buffer, **kwargs)
        self._profiles[-1].track_dataframe(df)

    def log_dataframe(self, df):
        """
        Generate and log a whylogs DatasetProfile from a pandas dataframe

        :param df: the Pandas dataframe to log
        """
        if not self._active:
            return None
        if self.should_rotate():
            self.rotate_time()
        
        self._profiles[-1].track_dataframe(df)

    def is_active(self):
        """
        Return the boolean state of the logger
        """
        return self._active
