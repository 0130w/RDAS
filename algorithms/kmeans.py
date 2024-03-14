from pyspark.ml.clustering import KMeansModel, KMeans
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.sql.dataframe import DataFrame


def kmeans_scalar(features, user_data: DataFrame) -> DataFrame:
    """ Given a list of features and a DataFrame containing user data, 
        return the DataFrame containing the scaled features.
    Parameters:
    features: list - a list of features
    user_data: DataFrame - a DataFrame containing user data
    Returns:
    DataFrame - a DataFrame containing the scaled features
    """
    assembler = VectorAssembler().setInputCols(features).setOutputCol('features')
    user_feature_df = assembler.transform(user_data)
    scalar = StandardScaler(inputCol='features', outputCol='scaled_features', withStd=True, withMean=False)
    scalar_model = scalar.fit(user_feature_df)
    return scalar_model.transform(user_feature_df)


def kmeans_train(features, user_data: DataFrame):
    """ Given a list of features and a DataFrame containing user data, 
        train a KMeans model and save it to the models directory.
    Parameters:
    features: list - a list of features
    user_data: DataFrame - a DataFrame containing user data
    Returns:
    None
    """
    scaled_user_feature_df = kmeans_scalar(features, user_data)
    kmeans = (KMeans()
              .setK(2)
              .setSeed(100)
              .setMaxIter(2)
              .setFeaturesCol('scaled_features')
              .setPredictionCol('predict'))
    kmeans.fit(scaled_user_feature_df).save('models/kmeans.joblib')


def kmeans_predict(features, user_data: DataFrame) -> DataFrame:
    """ Given a list of features and a DataFrame containing user data, 
        return the DataFrame containing the predicted values.
    Parameters:
    features: list - a list of features
    user_data: DataFrame - a DataFrame containing user data
    Returns:
    DataFrame - a DataFrame containing the predicted values
    """
    scaled_user_feature_df = kmeans_scalar(features, user_data)
    kmeans_model = KMeansModel.load("models/kmeans.joblib")
    return kmeans_model.transform(scaled_user_feature_df)
