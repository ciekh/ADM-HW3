import json
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import PorterStemmer


from bs4 import BeautifulSoup
import os
stopwords = set(stopwords.words('english'))
# with this i clean text
def CleanData(text):
    text = str(text)
    valid_word = []
    ps = PorterStemmer()
    text = word_tokenize(text)
    for word in text:
        # I take only the lowercase words that are numbers or simple words I do the stemming and control that are not in the set of stopwords
        if word.isalpha() or word.isdigit():
            x = word.lower()
            z = ps.stem(x)
            if z not in stopwords:
                valid_word.append(z)
    return valid_word


def RemoveDuplicates(lst,lst1):
    s=set(lst).union(set(lst1))
    return s
# with this function I extract the url for each html file
def ExtractUrl():
    os.chdir(r'C:\Users\cecco\Desktop\PagWeb')
    d_url  = {}
    for i in range(29992):
        try:
            with open(r'C:\Users\cecco\Desktop\AllMovies\article_' + str(i) + '.html', 'r', encoding='utf8') as f:
                html = f.read()
                soup = BeautifulSoup(html, 'html.parser')
                links = soup.find("link",{"rel":"canonical"})
                url = links.get('href')
                d_url["article_" + str(i)] = url
        except FileNotFoundError as e:
            continue
    #I create a file where I associate the url to each html file
    with open("d_url.json", "w", encoding="utf8") as myfile:
        myfile.write(json.dumps(d_url))

