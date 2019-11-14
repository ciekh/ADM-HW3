import json
import os
import pandas as pd


from pre import CleanData,ExtractUrl
os.chdir(r'C:\Users\cecco\Desktop\PagWeb')





def searchEngine_1(query):
    query = str(query)
    query = CleanData(query)
    inverted_index = json.loads(open("inverted_index.json").read())
    vocabulary = json.loads(open("vocabulary.json").read())
    index = []
    for par in set(query):
        if par in vocabulary.keys():
            index.append(vocabulary[par])
    docs = []
    try:
        for indices in index:
            docs.append(set(inverted_index[str(indices)]))
        docs = set.intersection(*docs)
    except:  # make a print of exception "result for your query doesn't exist"
        return print("There are no results that match your query.")  # it stops the function if there aren't match'''
    if len(docs) == 0:
        return print('there are no articles that contain all the words.')
    else:
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
searchEngine_1('night day')