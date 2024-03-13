from pyspark.sql.dataframe import DataFrame
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from pyspark.ml.feature import RegexTokenizer
from pyspark.ml.feature import StopWordsRemover
import string
from pyspark.sql.functions import *
import re


def get_word_pos(tag):
    """
    This function is used to get the wordnet pos tag for the nltk pos tag
    Parameters:
        The nltk pos tag
    Returns:
        wordnet pos tag"""
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


def remove_punct(text):
    """
    This function is used to remove the punctuation from the text
    Parameters:
        The text
    Returns:
        The text without punctuation"""
    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    nopunct = regex.sub(" ", text)
    return nopunct


def get_word_dict(review_df: DataFrame):
    """
    This function is used to get the word dictionary from the review dataframe
    Parameters:
        The review dataframe
    Returns:
        The word dictionary and the modified list of words without stop words and punctuation
    """
    wnl = WordNetLemmatizer()
    punct_remover = udf(lambda x: remove_punct(x))
    df_clean = review_df.select('text').withColumn('remove_punctuation', punct_remover('text')).drop(
        'text')  # 可以添加除了text的其他字段
    tokenizer = RegexTokenizer(inputCol="remove_punctuation", outputCol="tokenized", pattern='\\s+')
    tokenized_df = tokenizer.transform(df_clean)
    remover = StopWordsRemover(inputCol="tokenized", outputCol="remove_stop_words")
    remove_stop_words_df = remover.transform(tokenized_df.drop('remove_punctuation'))
    remove_stop_words_df.drop('tokenized')
    word_dict = {}
    remove_stop_words_list_modified = []
    val = remove_stop_words_df.select('remove_stop_words').collect()
    remove_stop_words_list = [ele.__getattr__('remove_stop_words') for ele in val]
    for t in remove_stop_words_list:
        refiltered = nltk.pos_tag(t)
        lemmas_sent = []
        for wordtag in refiltered:
            wordnet_pos = get_word_pos(wordtag[1]) or wordnet.NOUN
            word = wnl.lemmatize(wordtag[0], pos=wordnet_pos)
            lemmas_sent.append(word)
            word_dict[word] = word_dict.get(word, 0) + 1
        remove_stop_words_list_modified.append(lemmas_sent)

    return word_dict, remove_stop_words_list_modified
