import json
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

from bs4 import BeautifulSoup
import os
stopwords = set(stopwords.words('english'))

def CleanData(text):
    valid_word = []
    ps = PorterStemmer()
    text = word_tokenize(text)
    for word in text:
        if word.isalpha() or word.isdigit():
            x = word.lower()
            z = ps.stem(x)
            if z not in stopwords:
                valid_word.append(z)
    return valid_word


def RemoveDuplicates(lst,lst1):
    s=set(lst).union(set(lst1))
    return s

def ExtractUrl():
    os.chdir(r'C:\Users\cecco\Desktop\PagWeb')
    d_url  = {}
    for i in range(100):
        try:
            with open(r'C:\Users\cecco\Desktop\WebPages\article_' + str(i) + '.html', 'r', encoding='utf8') as f:
                html = f.read()
                soup = BeautifulSoup(html, 'html.parser')
                links = soup.find("link",{"rel":"canonical"})
                url = links.get('href')
                d_url["article_" + str(i)] = url
        except FileNotFoundError as e:
            continue
    with open("d_url.json", "w", encoding="utf8") as myfile:
        myfile.write(json.dumps(d_url))

CleanData('100 house,,,home')