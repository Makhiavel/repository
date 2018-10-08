import requests
from bs4 import BeautifulSoup

url = 'http://g1.globo.com/ultimas-noticias.html'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

lista = soup.find_all('div', class_='bastian-feed-item')
lista2= soup.find_all('a', class_='feed-post-link gui-color-primary gui-color-hover')
links = soup.find_all('a', class_='feed-post-link gui-color-primary gui-color-hover')

def scraper():
	for item in links:
		print ('---Link---')
		print(item["href"]);
	for item in lista2:
		print ("---Título---")
		print(item.contents[0]);
	for item in lista:	
		print ("---Resumo---")
		print(item.contents[0].text);
	
	
print("\n********Bem vindo ao G1 Webcrawler********\n")
print("10 links, 10 titulos e 10 resumos respectivamente")

print("Deseja visualizar?")
input("Aperte Enter")
scraper()
	
