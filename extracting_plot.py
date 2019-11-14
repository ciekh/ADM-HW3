from bs4 import BeautifulSoup
import os
import numpy as np
#Put html files in the same directory. In this example "/home/computer/Downloads/test"
possibles = ['Plot','Synopsis','Plot_synopsis','Plot_summary', 
             'Story','Plotline','The_Beginning','Summary',
            'Content','Premise']
all_htmls=os.listdir("/home/computer/Downloads/test")
h=1
for html_file in all_htmls:
	try:
		html=open("/home/computer/Downloads/test/"+html_file)
		plot=[]
		file = BeautifulSoup(html, 'html.parser')
	except:
		file=np.NaN
	
	try:
		for j in possibles:
			if file.select_one("#"+j) != None:
				tag = file.select_one("#"+j).find_parent('h2').find_next_sibling()
				while tag.name == 'p':
					plot.append(tag.text)
					tag = tag.find_next_sibling()
				p = ','.join(plot)
				film_plot = p.replace('\n','').replace("\'","")
				print(h,"-->",html_file, "(Plot)")
				print("-----------")
				print(film_plot, "\n")
	except:
		film_plot=np.NaN
	h=1+h


#Make sure you put only html fies in the same (eg: "/home/computer/Downloads/test")
#YOU CAN RUN THIS SCRIPT IN WHATEVER DIRECTORY
