# This module contains functions that need to be imported and used in the main script.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


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


def find_correlations(
    corr_df: pd.DataFrame, limits: list[float, float]
) -> pd.DataFrame:
    """
    This function finds correlations in a correlation matrix.
    Parameters:
    - corr_df: correlation matrix pandas DataFrame
    - limits: list, contains the lower and upper limits

    Returns:
    - DataFrame of strongly correlated pairs with their correlation values
    """
    corr_pairs = corr_df.stack().reset_index()
    corr_pairs.columns = ["feature1", "feature2", "correlation"]
    lower, upper = limits

    # alphabetically comparing the pairs ensures that we don't have duplicate pairs

    filtered_corr = corr_pairs.loc[
        lambda x: (x.feature1 < x.feature2)
        & (lower < x.correlation)
        & (x.correlation <= upper)
    ]

    filtered_corr = filtered_corr.sort_values("correlation", ascending=False)
    if filtered_corr.empty:
        return f"No correlations found in the range {lower} to {upper}"
    else:
        return filtered_corr
