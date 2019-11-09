from bs4 import BeautifulSoup
import os
#Put html files in the same directory. In this example "/home/computer/Downloads/test"
all_htmls=os.listdir("/home/computer/Downloads/test")
for html_file in all_htmls:
	html=open(html_file)
	plot=[]
	file = BeautifulSoup(html, 'html.parser')
	tag = file.select_one('#Plot').find_parent('h2').find_next_sibling()
	while tag.name == 'p':
		plot.append(tag.text)
		tag = tag.find_next_sibling()
	p = ','.join(plot)
	film_plot = p.replace('\n','').replace("\'","")
	print(film_plot)


