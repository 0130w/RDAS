from pyspark.sql.dataframe import DataFrame
import re
import nltk
import string
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import MWETokenizer
from nltk.corpus import wordnet
from pyspark.ml.feature import RegexTokenizer
from pyspark.ml.feature import StopWordsRemover
import re
import string
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from main import spark
from pyspark.sql.functions import *




def epic3_task4_task6(review_df: DataFrame):
    wnl = WordNetLemmatizer()
    def get_word_pos(tag):
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
        regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
        nopunct = regex.sub(" ", text)
        return nopunct
    
    punct_remover = udf(lambda x: remove_punct(x))
    #去标点符号分词
    df_clean = review_df.select('text').withColumn('remove_punctuation',punct_remover('text')).drop('text') #可以添加除了text的其他字段
    tokenizer = RegexTokenizer(inputCol="remove_punctuation", outputCol="tokenized",pattern='\\s+')
    tokenized_df = tokenizer.transform(df_clean)
    #去停用词
    remover = StopWordsRemover(inputCol="tokenized", outputCol="remove_stop_words")
    remove_stop_words_df = remover.transform(tokenized_df.drop('remove_punctuation'))
    remove_stop_words_df.drop('tokenized').show(5,truncate=False)
    word_dict = {}
    remove_stop_words_list_modified = []
    val = remove_stop_words_df.select('remove_stop_words').collect()
    remove_stop_words_list = [ ele.__getattr__('remove_stop_words') for ele in val]
    for t in remove_stop_words_list:
        refiltered =nltk.pos_tag(t)
        lemmas_sent = []
        for wordtag in refiltered:
            wordnet_pos = get_word_pos(wordtag[1]) or wordnet.NOUN
            word = wnl.lemmatize(wordtag[0], pos=wordnet_pos)
            lemmas_sent.append(word) # 词形还原
            word_dict[word] = word_dict.get(word,0)+1
        remove_stop_words_list_modified.append(lemmas_sent)

    wordfreq = pd.DataFrame({'word':word_dict.keys(),'freq':word_dict.values()})
    wordfreq = wordfreq.sort_values(by='freq', ascending=False)
        
    return spark.createDataFrame(wordfreq)