#libraries needed
import requests
from bs4 import BeautifulSoup

#creates a variable for my desired html page
url = (r'http://g1.globo.com/ultimas-noticias.url', 'r')
#should open the html and change the visualization of it
with open(url) as html_file:
	soup = BeautifulSoup(r.html_file, 'lxml')
#scope the data goals
article = soup.find('div', class_='article')
print(article)
#still working on the next steps
headline = article.h2.a.text
