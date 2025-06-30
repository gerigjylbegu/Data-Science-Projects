import scipy.stats as stats
import numpy as np
import pandas as pd
from sklearn.feature_selection import chi2
from sklearn.model_selection import cross_validate
from sklearn.pipeline import Pipeline


def find_outliers_iqr(df: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies outliers in a DataFrame using the Interquartile Range (IQR) method.
    Parameters:
    df (pd.DataFrame): The input DataFrame containing numeric columns to check for outliers.
    Returns:
    pd.DataFrame: A DataFrame of the same shape as the input, with boolean values indicating
                  whether each value is an outlier (True) or not (False) for each numeric column.
    """

    numeric_columns = df.select_dtypes(include=[np.number]).columns
    outliers_df = pd.DataFrame(index=df.index)
    for column in numeric_columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers_df[f"{column}"] = (df[column] < lower_bound) | (
            df[column] > upper_bound
        )

    return outliers_df


def chi2_test(df, cat, target):
    result = chi2(df[cat], df[target])
    for i, stat in enumerate(zip(*result)):
        print(f"{cat[i]}: Chi2 Statistic = {stat[0]:.2f}, p-value = {stat[1]:.4f}")
        if stat[1] < 0.05:
            print(f"{cat[i]} is significantly associated with {target} (p < 0.05)\n")
        else:
            print(
                f"{cat[i]} is not significantly associated with {target} (p >= 0.05)\n"
            )


def mann_whitney_test(df, features, target):
    for feature in features:
        stat, p = stats.mannwhitneyu(
            df[feature][df[target] == 1], df[feature][df[target] == 0]
        )
        print(f"Mann-Whitney U test for {feature}: Statistic={stat}, p-value={p}")
        if p < 0.05:
            print(f"{feature} is statistically associated with {target} (p < 0.05).\n")
        else:
            print(
                f"{feature} is not statistically associated with {target} (p >= 0.05).\n"
            )


def mean_diff(x, y):
    return np.mean(x) - np.mean(y)


def calculate_ci(df, features, target, method="bootstrap"):
    for feature in features:
        group1 = df[df[target] == 1][feature]
        group2 = df[df[target] == 0][feature]
        if method == "bootstrap":
            ci = stats.bootstrap(
                (group1, group2),
                mean_diff,
                n_resamples=1000,
                confidence_level=0.95,
                random_state=42,  # type: ignore
                method="percentile",
            )
            lower, upper = ci.confidence_interval
            if upper - lower > 0:
                print(
                    f"{feature} has a significant difference between the two groups: CI_Bootstrap = ({lower:.2f}, {upper:.2f})"
                )
            else:
                print(
                    f"{feature} does not have a significant difference between the two groups: CI_Bootstrap = ({lower:.2f}, {upper:.2f})"
                )
        elif method == "analytical":
            ci = stats.ttest_ind(group1, group2, equal_var=False).confidence_interval(
                confidence_level=0.95
            )
            lower, upper = ci
            if upper - lower > 0:
                print(
                    f"{feature} has a significant difference between the two groups: CI_Analytical = ({lower:.2f}, {upper:.2f})"
                )
            else:
                print(
                    f"{feature} does not have a significant difference between the two groups: CI_Analytical = ({lower:.2f}, {upper:.2f})"
                )


def annotate_bars(ax):
    for p in ax.patches:
        height = p.get_height()
        if height == 0:
            continue
        ax.annotate(
            f"{height:.1f}%",
            (p.get_x() + p.get_width() / 2, height),
            ha="center",
            va="bottom",
        )
