from pyspark.sql.functions import udf
from pyspark.sql.types import FloatType, ArrayType, StringType
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords


@udf(FloatType())
def analyze_sentiment(text):
    """ Analyze sentiment
    Parameters:
        text (str): Input text
    Returns:
        float -- Sentiment
        None if text is None
    """
    if text:
        sentiment = TextBlob(text).sentiment.polarity
        return sentiment
    else:
        return None


def extract_keywords(text: str) -> list:
    """ Extract adjectives and adverbs from input text
    Parameters:
        text (str): Input text
    Returns: list - List of adjectives and adverbs
    """
    if text:
        words = nltk.word_tokenize(text)
        tagged = nltk.pos_tag(words)
        keywords = [word for word, pos in tagged
                    if pos in ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS'] and
                    word not in stopwords.words('english')]
        return keywords
    else:
        return []
