#libraries:
from bs4 import BeautifulSoup
import csv
#for loop to crawl all the html file that we downloaded before
for i in range(29992):
    with open(r'C:\Users\shekoufeh\movies3\article_'+str(i)+'.html' ,encoding ='utf8') as f:
        html = f.read()
    soup = BeautifulSoup(html,'html.parser')
    dict={}
#title
    title=(soup.select('.firstHeading'))[0].text
    dict['title']=title.replace("\n"," ").strip() 

#intro
    
    for items in soup.select(".toc"):
        
#the paragraphs before class="toc" are in the intro cluster. so we find and merge them as a intro
        
        intro = [item.text for item in items.find_previous_siblings() if item.name=="p"]
#this method find the paragrapghs from end to top of the page. so we reverse them to be in the correct order
    intro.reverse()
    
    intro="".join(intro)
    dict['intro']=intro.replace("\n"," ").strip()   
    
#plot
       
    try:
        plot = []

# find the node with id of "Plot"
        mark = soup.find(id="Plot")
        
# walk through the siblings of the parent (H2) node until we reach the next H2 node
        for elt in mark.parent.nextSiblingGenerator():
            if elt.name == "h2":
                break
            if hasattr(elt, "text"):
                plot.append(elt.text)
        
# convert to text 
        plot="".join(plot)
    except:
        plot=''
    
    finally:
        dict['plot']=plot.replace("\n"," ").strip()
    
#extract infobox
    table=(soup.select(".infobox"))[0]

    output_rowc1 = []
    output_rowc0 = []
#gather each columns of infobox in a separate list 
    for table_row in table.findAll('tr'):
        rowc1 = table_row.findAll('td')
        rowc0 = table_row.findAll('th')
        
        for row in rowc1:
            output_rowc1.append(row.text)
        for row in rowc0:
            output_rowc0.append(row.text)

#add information in infobox to dictionary
            
    #film_name
    dict['film_name']=output_rowc0[0]

##search information in the lists, if they were available, we add them to a dictionary, otherwise, we add "NA" to dictionary  
    
    #director
    a = [output_rowc0.index(i) for i in output_rowc0 if "direct" in i.lower()]
    if len(a)>0:
        dict['director']=output_rowc1[a[0]].replace("\n","").strip() 
    else:
        dict['director']="NA"
    
    #producer
    a = [output_rowc0.index(i) for i in output_rowc0 if "produce" in i.lower()]
    if len(a)>0:
        dict['producer']=output_rowc1[a[0]].replace("\n","").strip()  
    else:
        dict['producer']="NA"
    
    #writer
    a = [output_rowc0.index(i) for i in output_rowc0 if "writ" in i.lower()]
    if len(a)>0:
        dict['written']=output_rowc1[a[0]].replace("\n","").strip()
    else:
        dict['written']="NA"
    
    #starring
    a = [output_rowc0.index(i) for i in output_rowc0 if "star" in i.lower()]
    if len(a)>0:
        dict['starring']=output_rowc1[a[0]].replace("\n","").strip()
    else:
        dict['starring']="NA"
    
    #music
    a = [output_rowc0.index(i) for i in output_rowc0 if "music" in i.lower()]
    if len(a)>0:
        dict['music']=output_rowc1[a[0]].replace("\n","").strip()
    else:
        dict['starring']="NA"
    
    #release date
    a = [output_rowc0.index(i) for i in output_rowc0 if "release" in i.lower()]
    if len(a)>0:
        dict['release date']=output_rowc1[a[0]].replace("\n","").strip()
    else:
        dict['release date']="NA"
    
    #running time
    a = [output_rowc0.index(i) for i in output_rowc0 if "run" in i.lower()]
    if len(a)>0:
        dict['runtime']=output_rowc1[a[0]].replace("\n","").strip()
    else:
        dict['runtime']="NA"
    
    #country
    a = [output_rowc0.index(i) for i in output_rowc0 if "country" in i.lower()]
    if len(a)>0:
        dict['country']=output_rowc1[a[0]].replace("\n","").strip()
    else:
        dict['country']="NA"
    
    #language
    b = [output_rowc0.index(i) for i in output_rowc0 if "language" in i.lower()]
    if len(a)>0:
        dict['language']=output_rowc1[a[0]].replace("\n","").strip()
    else:
        dict['language']="NA"
    
    #budget
    a = [output_rowc0.index(i) for i in output_rowc0 if "budget" in i.lower()]
    if len(a)>0:
        dict['budget']=output_rowc1[a[0]].replace("\n","").strip()
    else:
        dict['budget']="NA"
        
#create tsv files
        
    with open('article_'+str(i)+'tsv','w',encoding='utf8') as f:
        fieldnames = ['title','intro','plot','film_name','director', 'producer', 'written', 'starring', 'music', 'release date', 'runtime', 'country', 'language', 'budget']
        writer = csv.DictWriter(f, fieldnames=fieldnames,dialect="excel-tab")
        writer.writeheader()
        writer.writerow(dict)