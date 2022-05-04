from typing import Dict, Optional

import numpy as np
from scipy import stats  # type: ignore
from typing_extensions import TypedDict
from whylogs_sketching import kll_doubles_sketch  # type: ignore

from whylogs.core.view.dataset_profile_view import DatasetProfileView  # type: ignore
from whylogs.viz.utils.frequent_items_calculations import (
    FrequentStats,
    get_frequent_stats,
)

QUANTILES = [0.0, 0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99, 1.0]


class ColumnDriftValue(TypedDict):
    p_value: float
    test: str


def _ks_test_compute_p_value(
    target_distribution: kll_doubles_sketch, reference_distribution: kll_doubles_sketch
) -> Optional[ColumnDriftValue]:
    """
    Compute the Kolmogorov-Smirnov test p-value of two continuous distributions.
    Uses the quantile values and the corresponding CDFs to calculate the approximate KS statistic.
    Only applicable to continuous distributions.
    The null hypothesis expects the samples to come from the same distribution.

    Parameters
    ----------
    target_distribution : datasketches.kll_floats_sketch
        A kll_floats_sketch (quantiles sketch) from the target distribution's values
    reference_distribution : datasketches.kll_floats_sketch
        A kll_floats_sketch (quantiles sketch) from the reference (expected) distribution's values
        Can be generated from a theoretical distribution, or another sample for the same feature.

    Returns
    -------
        p_value : float
        The estimated p-value from the parametrized KS test, applied on the target and reference distributions'
        kll_floats_sketch summaries

    """

    D_max = 0
    target_quantile_values = target_distribution.get_quantiles(QUANTILES)
    ref_quantile_values = reference_distribution.get_quantiles(QUANTILES)

    num_quantiles = len(QUANTILES)
    i, j = 0, 0
    while i < num_quantiles and j < num_quantiles:

        if target_quantile_values[i] < ref_quantile_values[j]:
            current_quantile = target_quantile_values[i]
            i += 1
        else:
            current_quantile = ref_quantile_values[j]
            j += 1

        cdf_target = target_distribution.get_cdf([current_quantile])[0]
        cdf_ref = reference_distribution.get_cdf([current_quantile])[0]
        D = abs(cdf_target - cdf_ref)
        if D > D_max:
            D_max = D

    while i < num_quantiles:
        cdf_target = target_distribution.get_cdf([target_quantile_values[i]])[0]
        cdf_ref = reference_distribution.get_cdf([target_quantile_values[i]])[0]
        D = abs(cdf_target - cdf_ref)
        if D > D_max:
            D_max = D
        i += 1

    while j < num_quantiles:
        cdf_target = target_distribution.get_cdf([ref_quantile_values[j]])[0]
        cdf_ref = reference_distribution.get_cdf([ref_quantile_values[j]])[0]
        D = abs(cdf_target - cdf_ref)
        if D > D_max:
            D_max = D
        j += 1

    m, n = sorted([target_distribution.get_n(), reference_distribution.get_n()], reverse=True)
    en = m * n / (m + n)

    p_value = stats.distributions.kstwo.sf(D_max, np.round(en))

    return {"p_value": p_value, "test": "ks"}


def _compute_chi_squared_test_p_value(
    target_distribution: FrequentStats, reference_distribution: FrequentStats
) -> Optional[ColumnDriftValue]:
    """
    Calculates the Chi-Squared test p-value for two discrete distributions.
    Uses the top frequent items summary, unique count estimate and total count estimate for each feature,
    to calculate the estimated Chi-Squared statistic.
    Applicable only to discrete distributions.

    Parameters
    ----------
    target_distribution : ReferenceDistributionDiscreteMessage
        The summary message of the target feature's distribution.
        Should be a ReferenceDistributionDiscreteMessage containing the frequent items,
        unique, and total count summaries.
    reference_distribution : ReferenceDistributionDiscreteMessage
        The summary message of the reference feature's distribution.
        Should be a ReferenceDistributionDiscreteMessage containing the frequent items,
        unique, and total count summaries.

    Returns
    -------
        p_value : float
        The estimated p-value from the Chi-Squared test, applied on the target and reference distributions'
        frequent and unique items summaries
    """
    target_freq_items = target_distribution["frequent_items"]
    target_total_count = target_distribution["total_count"]
    target_unique_count = target_distribution["unique_count"]
    ref_total_count = reference_distribution["total_count"]

    if ref_total_count <= 0 or target_total_count <= 0:
        return None

    ref_dist_items = dict()
    for item in reference_distribution["frequent_items"]:
        ref_dist_items[item["value"]] = item["estimate"]

    proportion_ref_dist_items = {k: v / ref_total_count for k, v in ref_dist_items.items()}

    chi_sq = 0.0
    for item in target_freq_items:
        target_frequency = item["estimate"]
        if item["value"] in ref_dist_items:
            ref_frequency = int(proportion_ref_dist_items[item["value"]] * target_total_count)
        else:
            ref_frequency = 0

        if ref_frequency == 0:
            chi_sq = np.inf
            break
        chi_sq += (target_frequency - ref_frequency) ** 2 / ref_frequency

    degrees_of_freedom = target_unique_count - 1
    degrees_of_freedom = degrees_of_freedom if degrees_of_freedom > 0 else 1
    p_value = stats.chi2.sf(chi_sq, degrees_of_freedom)
    return {"p_value": p_value, "test": "chi-squared"}


def calculate_drift_values(
    target_view: DatasetProfileView, ref_view: DatasetProfileView
) -> Dict[str, Optional[ColumnDriftValue]]:
    drift_values: Dict[str, Optional[ColumnDriftValue]] = {}
    target_col_views = target_view.get_columns()
    ref_col_views = ref_view.get_columns()
    for target_col_name in target_col_views:
        if target_col_name in ref_col_views:
            target_col_view = target_col_views[target_col_name]
            ref_col_view = ref_col_views[target_col_name]

            if not target_col_view or not ref_col_view:
                continue

            if target_col_view.get_metric("dist") and ref_col_view.get_metric("dist"):
                target_dist_metric = target_col_view.get_metric("dist")
                target_kll_sketch = target_dist_metric.kll.value

                ref_dist_metric = ref_col_view.get_metric("dist")
                ref_kll_sketch = ref_dist_metric.kll.value

                ks_p_value = _ks_test_compute_p_value(target_kll_sketch, ref_kll_sketch)
                drift_values[target_col_name] = ks_p_value
            elif target_col_view.get_metric("fi") and ref_col_view.get_metric("fi"):

                target_frequent_stats: FrequentStats = get_frequent_stats(target_col_view, config=None)
                ref_frequent_stats: FrequentStats = get_frequent_stats(ref_col_view, config=None)

                if target_frequent_stats and ref_frequent_stats:
                    chi2_p_value = _compute_chi_squared_test_p_value(target_frequent_stats, ref_frequent_stats)
                else:
                    chi2_p_value = None
                drift_values[target_col_name] = chi2_p_value

    return drift_values
