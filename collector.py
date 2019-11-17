import random
import time
from bs4 import BeautifulSoup
import os
import urllib
import requests
#I create a beautifulsoup object
url = 'https://raw.githubusercontent.com/CriMenghini/ADM/master/2019/Homework_3/data/movies2.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
os.chdir(r'C:\Users\cecco\Desktop\AllMovies')
lst = []
i = 0
for link in soup.find_all('a'):
# with 'href' i take all links
    x = link.get('href')
    lst.append(x)
for v in lst:
    try:
        # i store the response in a file html
        url = v
        response = urllib.request.urlopen(url)
        c = "article_" + str(i)
        webContent = response.read()
        f = open(c + '.html', 'wb')
        f.write(webContent)
        f.close
        time.sleep(random.randint(1, 5))
        # I repeat the operation if I generate an excpetion timeout I stop 1200 seconds
    except requests.exceptions.Timeout as e:
        time.sleep(1200)
        url = v
        response = urllib.request.urlopen(url)
        c = "article_" + str(i)
        webContent = response.read()
        f = open(c + '.html', 'wb')
        f.write(webContent)
        f.close
        time.sleep(random.randint(1, 5))
        # if I generate an exception for some other reason I skip the file
    except Exception as e:
        continue
    finally:
        i += 1
