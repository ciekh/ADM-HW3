import json
import os
from collections import defaultdict
import pandas as pd

from pre import CleanData, RemoveDuplicates

vocabulary ={}
inverted_idx=defaultdict(list)
cnt = 1
for i in range(5):
    #temoporaly create a dataframe from our tsv files
    try:
       db = pd.read_csv(r'C:\Users\cecco\Desktop\PagWeb\article_' + str(i) +'.tsv', sep='\t', encoding = 'utf8')
    except FileNotFoundError as e:
        continue
    intro = db['intro']
    plot = db['plot']
    for x in intro:
        IntroWords = CleanData(x)
    for y in plot:
        PlotWords = CleanData(y)
    AllWords = RemoveDuplicates(IntroWords,PlotWords)
    # update current vocabulary with the new words found in a document
    for token in AllWords:
        if token in vocabulary.keys():  # if word is already in general vocabulary skip it
            continue
        else:
            vocabulary.update({token:cnt})  # add a word to the vocabulary
            cnt += 1
    for w in AllWords:
        x = vocabulary[w]
        inverted_idx[x].append('article_' + str(i))
os.chdir(r'C:\Users\cecco\Desktop\PagWeb')
print(vocabulary)
print(inverted_idx)
with open("vocabulary.json", "w", encoding = "utf8") as myfile:
    myfile.write(json.dumps(vocabulary))
with open("inverted_index.json", "w", encoding = "utf8") as myfile:
    myfile.write(json.dumps(inverted_idx))
