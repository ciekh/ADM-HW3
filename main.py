import heapq
import json
import os
import pandas as pd
from numpy import dot
from numpy.linalg import norm
from utils import CleanData
os.chdir(r'C:\Users\cecco\Desktop\PagWeb')


def searchEngine_1(query):
    query = str(query)
    query = CleanData(query)
    # I load the vocabulary and the inverted index so as not to have to calculate them at the moment
    inverted_index = json.loads(open("inverted_index.json").read())
    vocabulary = json.loads(open("vocabulary.json").read())
    index = []
    #I get the word id from the vocabulary
    for par in set(query):
        if par in vocabulary.keys():
            index.append(vocabulary[par])
    docs = []
    if len(index) != len(set(query)):
        # not all words are in the dictionary
        return print("There are no results that match your query.")
    else:
        # I get the set of all the articles they have all the words from
        for indices in index:
            docs.append(set(inverted_index[str(indices)]))
        docs = set.intersection(*docs)
        if len(docs) == 0:
            #no film has all the words
            return print('there are no articles that contain all the words.')
        else:
            # creo un db con l'insieme dei film e per ognuno stampo title intro plot e url
            result = pd.DataFrame()
            d_url = json.loads(open("d_url.json").read())
            for doc in docs:
                z = d_url[doc]
                df1 = pd.DataFrame({'link': z}, index=[0])
                df = pd.read_csv(doc + ".tsv",delimiter="\t")
                result1 =df[['title','intro','plot']]
                result2 = pd.concat([result1,df1],axis = 1)
                result = result.append(result2)
            result.reset_index(drop=True, inplace=True)
            print(result)



def searchEngine_2(query):
    query = CleanData(query)
    inverted_index = json.loads(open("inverted_index.json").read())
    inverted2_index = json.loads(open("inverted2_index.json").read())
    vocabulary = json.loads(open("vocabulary.json").read())
    Idf_dict = json.loads(open("Idf_dict.json").read())
    index = []
    # I calculate the tf of the word in the query since the query is a set is always given by 1 fraction the length of the set
    query_words_tf = 1/len(query)
    query = set(query)
    # this part is identical to the search engine 1
    for par in query:
        if par in vocabulary.keys():
            index.append(vocabulary[par])
    docs = []
    if len(index) != len(query):
        return print("There are no results that match your query.")
    else:
        for indices in index:
            docs.append(set(inverted_index[str(indices)]))
        docs = set.intersection(*docs)
        if len(docs) == 0:
            return print('there are no articles that contain all the words.')
        else:
            lst2 = []
            # for each document
            for d in docs:
                lst = []
                lst1 = []
                # for word in the document i calculate the cosine similarity between words in the document and words in the query
                for i in index:
                    c = inverted2_index[str(i)]
                    for val in c:
                        if val[0] == d:
                            lst.append(val[1])
                    b = Idf_dict[str(i)]
                    for val1 in b:
                        if val1[0] == d:
                            lst1.append(val1[1]*query_words_tf)
                cosine  = [d,round(dot(lst, lst1) / (norm(lst) * norm(lst1)),3)]
                lst2.append(cosine)
                # I create a maxheap where I keep documents with relative similarity
            q = [(x[1], x[0]) for x in lst2]
            heapq._heapify_max(q)
            k = 5
            lst4 = []
            for i in range(k):
                    try:
                        c = heapq._heappop_max(q)
                        lst4.append(c)
                    except IndexError:
                        break
            result = pd.DataFrame()
            # I create the db to be returned with the first 5 elements with greater similarity
            d_url = json.loads(open("d_url.json").read())
            for tupla in lst4:
                z = d_url[tupla[1]]
                df2 = pd.DataFrame({'similarity' : tupla[0]},index=[0])
                df1 = pd.DataFrame({'link': z}, index=[0])
                df = pd.read_csv(tupla[1] + ".tsv", delimiter="\t")
                result1 = df[['title', 'intro', 'plot']]
                result2 = pd.concat([result1, df1,df2], axis=1)
                result = result.append(result2)
            result.reset_index(drop=True, inplace=True)
            print(result)

# I have the user choose which dimilarity to use and the query to insert
n = input("Enter query number: ")
if n== str(1):
    query = input("Please, write a query: ")
    searchEngine_1(query)
if n == str(2):
    query = input("Please, write a query: ")
    searchEngine_2(query)

