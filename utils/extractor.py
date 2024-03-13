from typing import List
from pyspark.sql.dataframe import DataFrame


def features_extractor(df: DataFrame, features: List[str]) -> DataFrame:
    """ Extract features from a given DataFrame
    Parameters:
        df (DataFrame): Dataframe to be extracted
        features (List[str]): List of features used for extracting features
    Returns:
        DataFrame: Extracted features DataFrame
    """
    extracted_features_df = df.select(features)
    return extracted_features_df
