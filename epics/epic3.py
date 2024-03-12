from pyspark.sql.dataframe import DataFrame
import nltk
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from pyspark.ml.feature import RegexTokenizer
from pyspark.ml.feature import StopWordsRemover
import string
import matplotlib.pyplot as plt
from pyspark.sql.functions import *
import numpy as np
import networkx as nx
import multidict as multidict
from PIL import Image
from wordcloud import WordCloud
import re
from utils import cal_freq

def epic3_task1(review_df: DataFrame):
    """
    Parameters:
        review_df: DataFrame from review.json
    Returns: None(Displays a bar chart of the number of reviews per year)"""
    review_df = review_df.withColumn('year',year('date')).drop('date')
    comments_count_by_year = review_df.groupBy("year").count()
    comments_count_by_year = comments_count_by_year.orderBy("year")
    pdf = comments_count_by_year.toPandas()

    plt.figure(figsize=(10, 6))
    plt.bar(pdf['year'], pdf['count'], color='lightblue', label='Count', width=0.4, align='center')
    plt.plot(pdf['year'], pdf['count'], color='red', marker='o', linestyle='-', linewidth=2, markersize=8, label='Trend')
    plt.xlabel('Year')
    plt.ylabel('Review Count')
    plt.title('Yearly Review Count Visualization')
    plt.xticks(pdf['year'])  
    plt.legend()
    plt.show()

def epic3_task2(review_df: DataFrame):
    """
    Parameters:
        review_df: DataFrame from review.json
    Returns: None(Displays a bar chart of the number of cool, funny, and useful comments per year)"""
    review_df = review_df.withColumn('year',year('date')).drop('date')
    cool_comments_count_by_year = review_df.filter(review_df.cool == 1).groupBy("year").count().orderBy("year")
    funny_comments_count_by_year = review_df.filter(review_df.funny == 1).groupBy("year").count().orderBy("year")
    useful_comments_count_by_year = review_df.filter(review_df.useful == 1).groupBy("year").count().orderBy("year")

    cool_pdf = cool_comments_count_by_year.toPandas()
    funny_pdf =funny_comments_count_by_year.toPandas()
    useful_pdf = useful_comments_count_by_year.toPandas()

    plt.figure(figsize=(10, 18))  

    plt.subplot(3, 1, 1)  # (rows, columns, panel number)
    plt.bar(cool_pdf['year'], cool_pdf['count'], color='skyblue', label='Cool Count', width=0.4)
    plt.plot(cool_pdf['year'], cool_pdf['count'], marker='o', linestyle='-', color='blue', label='Cool Trend')
    plt.title('Cool Comments Count by Year')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.bar(funny_pdf['year'], funny_pdf['count'], color='lightgreen', label='Funny Count', width=0.4)
    plt.plot(funny_pdf['year'], funny_pdf['count'], marker='o', linestyle='-', color='green', label='Funny Trend')
    plt.title('Funny Comments Count by Year')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.bar(useful_pdf['year'], useful_pdf['count'], color='lightcoral', label='Useful Count', width=0.4)
    plt.plot(useful_pdf['year'], useful_pdf['count'], marker='o', linestyle='-', color='red', label='Useful Trend')
    plt.title('Useful Comments Count by Year')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.legend()

    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.5)

    plt.show()

def epic3_task3(review_df: DataFrame):
    """
    Parameters:
        review_df: DataFrame from review.json
    Returns: DataFrame(Displays the top 20 users with the most comments)"""
    user_df = review_df.groupBy("user_id").count()
    user_comments_rank = user_df.orderBy(col("count").desc())
    user_comments_rank.show(20)
    return user_comments_rank


def epic3_task4(review_df: DataFrame):
    """
    Parameters:
        review_df: DataFrame from review.json
    Returns: None(Displays a word cloud of the most frequently used words in the comments)"""

    def makeImage(text):
        alice_mask = np.array(Image.open("/home/ariselr/1.png"))
        wc = WordCloud(background_color="white", max_words=1000, mask=alice_mask)
        # generate word cloud
        wc.generate_from_frequencies(text)
    
    word_dict, _ = cal_freq.get_word_dict(review_df)
    makeImage(word_dict)
    
def epic3_task5(review_df: DataFrame):
    """
    Parameters:
        review_df: DataFrame from review.json
    Returns: DataFrame(The top 20 most frequently used words in the comments)"""

    word_dict, _ = cal_freq.get_word_dict(review_df)
    wordfreq = pd.DataFrame({'word':word_dict.keys(),'freq':word_dict.values()})
    wordfreq = wordfreq.sort_values(by='freq', ascending=False)
        
    return spark.createDataFrame(wordfreq[:20])


def epic3_task6(review_df: DataFrame):
    """
    Parameters:
        review_df: DataFrame from review.json
    Returns: None(Displays a network graph of the top 50 most frequently used words in the comments)"""
 
    word_dict, remove_stop_words_list_modified = cal_freq.get_word_dict(review_df)

    wordfreq = pd.DataFrame({'word':word_dict.keys(),'freq':word_dict.values()})
    wordfreq = wordfreq.sort_values(by='freq', ascending=False)
        
    word_series = pd.Series(data=wordfreq['freq'].values, index=wordfreq['word'])

    keywords = word_series[:50].index
    matrix = np.zeros((len(keywords)+1)*(len(keywords)+1)).reshape(len(keywords)+1, len(keywords)+1).astype(str)
    matrix[0][0] = np.NaN
    matrix[1:, 0] = matrix[0, 1:] = keywords

    for i, w1 in enumerate(word_series[:50].index):
        for j, w2 in enumerate(word_series[:50].index):
            if w1 == w2:  
                continue
            count = 0
            for cont in remove_stop_words_list_modified:
                pairs = list(zip(cont, cont[1:]))
                if (w1, w2) in pairs or (w2, w1) in pairs:
                    count += 1
            matrix[i+1][j+1] = count
    kwdata_ = pd.DataFrame(data=matrix[1:, 1:], index=matrix[1:, 0], columns=matrix[0, 1:])
    kwdata_=kwdata_.astype(float)
    
    plt.figure(figsize=(10, 10))  
    graph1 = nx.from_pandas_adjacency(kwdata_)
    # 使用 spring_layout
    pos = nx.spring_layout(graph1, k=0.5)  
    nx.draw(graph1, pos, with_labels=True, node_color='yellow', font_size=10, node_size=300, edge_color='tomato')
    plt.show()


if __name__ == '__main__':
    from pyspark.sql import SparkSession
    from pyspark.sql.types import *
    from pyspark.sql.functions import *
    from pyspark.sql import functions as F
    # Driver
    spark = SparkSession \
        .builder \
        .master('local') \
        .appName('SparkProj') \
        .config("spark.driver.memory", "4g") \
        .config("spark.executor.memory", "4g") \
        .config("spark.memory.fraction", "0.8") \
        .config("spark.memory.storageFraction", "0.4") \
        .config("spark.shuffle.spill", "true") \
        .config("spark.shuffle.spill.compress", "true") \
        .getOrCreate()

    # define dataset files path
    business_path = 'dataset/yelp_academic_dataset_business.json'
    checkin_path = 'dataset/yelp_academic_dataset_checkin.json'
    review_path = 'dataset/yelp_academic_dataset_review.json'
    tip_path = 'dataset/yelp_academic_dataset_tip.json'
    user_path = 'dataset/yelp_academic_dataset_user.json'

    df = spark.read.json(review_path).limit(500)
    epic3_task5(df)
