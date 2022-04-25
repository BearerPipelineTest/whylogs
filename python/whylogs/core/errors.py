class Error(Exception):
    """Base error type for this module."""


class DeserializationError(Error):
    """Exception raised when deserializing data."""


class SerializationError(Error):
    """Exception raised when serializing data."""


class UnsupportedError(Error):
    """Exception raised when an operation is not supported."""
