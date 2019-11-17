import os
from bs4 import BeautifulSoup
import csv
from parser_utils import SplitWord

for i in range(29992):
    with open(r'C:\Users\cecco\Desktop\AllMovies\article_'+str(i)+'.html' ,encoding ='utf8') as f:
        html = f.read()
    lst2 = []
    soup = BeautifulSoup(html,'html.parser')
    intro = ''
    plot = ''
    #check if the infobox vevent table exists if it does not exist
    # #very probably it will not be a film so discard the file I think is a right tradeoff
    table = soup.find('table', {'class': 'infobox vevent'})
    if table == None:
        continue
    #I extract  all paragraph of into and plot
    #I start to scroll through the paragraphs after the table because the html files are so structured
    else:
        tag = table.find_next_sibling('p')
        tag1 = ''
        while tag.name == 'p':
                    intro += tag.text
                    tag = tag.find_next_sibling()
        tag1 = tag.find_next_sibling('p')
        if tag1 == None:
            plot == 'NA'
        else:
            while tag1.name == 'p':
                    plot += tag1.text
                    tag1 = tag1.find_next_sibling()
        d1 = {}
        # I take the fields from the table
        for rows in table.find_all('tr')[2:]:
            if rows.th!= None:
                if rows.th.text == 'Directed by':
                    d1['Directed by'] = SplitWord(rows.td.text.replace("\n"," ").strip())
                elif rows.th.text == 'Produced by':
                    d1['Produced by'] = SplitWord(rows.td.text.replace("\n", " ").strip())
                elif rows.th.text == 'Written by':
                    d1['Written by'] = SplitWord(rows.td.text.replace("\n", " ").strip())
                elif rows.th.text == 'Starring':
                    d1['Starring'] = SplitWord(rows.td.text.replace("\n", " ").strip())
                elif rows.th.text == 'Music by':
                    d1['Music by'] = SplitWord(rows.td.text.replace("\n", " ").strip())
                elif rows.th.text == 'Release date':
                    d1['Release date'] = SplitWord(rows.td.text.replace("\n", " ").strip())
                elif rows.th.text == 'Running time':
                    d1['Running time'] = SplitWord(rows.td.text.replace("\n", " ").strip())
                elif rows.th.text == 'Country':
                    d1['Country'] = SplitWord(rows.td.text.replace("\n", " ").strip())
                elif rows.th.text == 'Language':
                    d1['Language'] = SplitWord(rows.td.text.replace("\n", " ").strip())
                elif rows.th.text =='Budget':
                    d1['Budget'] = SplitWord(rows.td.text.replace("\n", " ").strip())
        d = {}
        d['title'] = soup.title.text.replace("\n", " ").strip()
        d['intro'] = intro.replace("\n", " ").strip()
        d['plot'] = plot.replace("\n", " ").strip()
        d['film_name'] = table.find('tr').text.replace("\n", " ").strip()
        for x in list(d1):
            if x == 'Directed by':
                d['director'] = d1['Directed by']
            elif x == 'Produced by':
                d['producer'] = d1['Produced by']
            elif x == 'Written by':
                d['written'] = d1['Written by']
            elif x == 'Starring':
                d['starring'] = d1['Starring']
            elif x == 'Music by':
                d['music'] = d1['Music by']
            elif x == 'Release date':
                d['release date'] = d1['Release date']
            elif x == 'Running time':
                d['runtime'] = d1['Running time']
            elif x == 'Country':
                d['country'] = d1['Country']
            elif x == 'Language':
                d['language'] = d1['Language']
            elif x == 'Budget':
                d['budget'] = d1['Budget']
        dtags = ['director', 'producer', 'written', 'starring', 'music', 'release date', 'runtime', 'country', 'language', 'budget']
        for x in dtags:
            if x not in list(d):
                d[x] = 'NA'
    os.chdir(r'C:\Users\cecco\Desktop\PagWeb')
    # i create a file tsv
    with open('article_'+str(i)+'.tsv','w',encoding='utf8') as f:
        fieldnames = ['title','intro','plot','film_name','director', 'producer', 'written', 'starring', 'music', 'release date', 'runtime', 'country', 'language', 'budget']
        writer = csv.DictWriter(f, fieldnames=fieldnames,dialect="excel-tab")
        writer.writeheader()
        writer.writerow(d)

