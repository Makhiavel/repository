import requests
from bs4 import BeautifulSoup


url = (r'http://g1.globo.com/ultimas-noticias.url', 'r')
with open(url) as html_file:
	soup = BeautifulSoup(r.html_file, 'lxml')

article = soup.find('div', class_='article')
print(article)

headline = article.h2.a.text
