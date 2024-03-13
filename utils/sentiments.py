from pyspark.sql.functions import udf
from pyspark.sql.types import FloatType
from textblob import TextBlob


@udf(FloatType())
def analyze_sentiment(text):
    if text:
        sentiment = TextBlob(text).sentiment.polarity
        return sentiment
    else:
        return None
