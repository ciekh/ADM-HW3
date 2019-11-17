import json
import os
from collections import defaultdict
import pandas as pd
import math

from utils import CleanData, RemoveDuplicates
# with this function I create the vocabulary and the first index file
def index1():
    vocabulary ={}
    inverted_idx=defaultdict(list)
    cnt = 1
    for i in range(29992):
        try:
           db = pd.read_csv(r'C:\Users\cecco\Desktop\PagWeb\article_' + str(i) +'.tsv', sep='\t', encoding = 'utf8')
        except FileNotFoundError as e:
            continue
        # i take only intro and plot
        intro = db['intro']
        plot = db['plot']
        # i clean data and remove duplicates
        for x in intro:
            IntroWords = CleanData(x)
        for y in plot:
            PlotWords = CleanData(y)
        AllWords = RemoveDuplicates(IntroWords,PlotWords)
        # I add the words with their id to the vocabulary
        for token in AllWords:
            if token in vocabulary.keys():
                continue
            else:
                vocabulary.update({token:cnt})
                cnt += 1
        # in the index I add key of the word and articles in which it is found
        for w in AllWords:
            x = vocabulary[w]
            inverted_idx[x].append('article_' + str(i))
    os.chdir(r'C:\Users\cecco\Desktop\PagWeb')
    # I save the vocabulary and the inverted index in two file
    with open("vocabulary.json", "w", encoding = "utf8") as myfile:
        myfile.write(json.dumps(vocabulary))
    with open("inverted_index.json", "w", encoding = "utf8") as myfile:
        myfile.write(json.dumps(inverted_idx))


def index2():
    os.chdir(r'C:\Users\cecco\Desktop\PagWeb')
    inverted_index = json.loads(open("inverted_index.json").read())
    vocabulary = json.loads(open("vocabulary.json").read())
    inverted2_idx = defaultdict(list)
    Idf_dict = defaultdict(list)
    for i in range(29992):
        try:
            db = pd.read_csv(r'C:\Users\cecco\Desktop\PagWeb\article_' + str(i) + '.tsv', sep='\t', encoding='utf8')
        except FileNotFoundError as e:
            continue
        intro = db['intro']
        plot = db['plot']
        for x in intro:
            IntroWords = CleanData(x)
        for y in plot:
            PlotWords = CleanData(y)
        Plot_Intro = IntroWords + PlotWords
        # I take the length of intro and plot to calculate the tf
        lungh = len(Plot_Intro)
        AllWords = RemoveDuplicates(IntroWords, PlotWords)
        # update current vocabulary with the new words found in a document
        tfIdf = {}
        IDF = {}
        for token1 in AllWords:
            # I count the number of times the word appears in intro and plot always useful for calculating the tf
            x = Plot_Intro.count(token1)
            id_token = vocabulary[token1]
            doc_par = inverted_index[str(id_token)]
            # check in how many articles the word useful to calculate idf appears
            num_doc_par = len(doc_par)
            # calculate the tf
            tf = x / lungh
            # calculate idf
            Idf = 1 + math.log(29992 / num_doc_par)
            IDF[token1] = Idf
            # calculate tfidf
            tfIdf[token1] = tf * Idf

        for ww in AllWords:
            l = tfIdf[ww]
            p = IDF[ww]
            xx = vocabulary[ww]
            inverted2_idx[xx].append(('article_' + str(i), l))
            Idf_dict[xx].append(('article_' + str(i), p))
            # I create a file by copying into it a dictionary whose key is the id of the word and as values ​
            # a tuple formed by the document of belonging and its tfidf
    with open("inverted2_index.json", "w", encoding="utf8") as myfile:
        myfile.write(json.dumps(inverted2_idx))
        # I create a file by copying into it a dictionary whose key is the id of the word and as values ​
        # a tuple formed by the document of belonging and its idf this will be useful to calculate the tfidf of the words in the query
    with open("Idf_dict.json", "w", encoding="utf8") as myfile:
        myfile.write(json.dumps(Idf_dict))

