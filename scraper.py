import requests 
from bs4 import BeautifulSoup


def scraper():
	r = requests.get("http://g1.globo.com/ultimas-noticias.html")
	soup = BeautifulSoup(r.content, 'lxml')
	for link in soup.find_all('a', class_='feed-post-link gui-color-primary gui-color-hover'):
		link.get("href")
		print("\nTitles and links\n")
		print (link.text)
		print (link.get("href"))

	
		r = requests.get(link.get("href"))
		soup = BeautifulSoup(r.content, 'lxml')
		
		for txt in soup.find_all('article'):
			txt.get('articleBody')
			print("\nContent\n")
			print(txt.text)
			break
			
		for time in soup.find_all('time'):
			time.get('datetime')
			print("\nData e horário\n")
			print (time.text)
			print("------------------------------------------------------------------------------------------------------------")
			break

print("\n*****************************Bem vindo ao G1 Webcrawler*****************************\n")
print("O programa está organizado para vizualisar as últimas 10 noticias do site G1 da Globo\n")
print("A ordem da visualização está em: Título, link, conteúdo completo e data com horário da postagem\n")

print("Deseja visualizar?")
input("Aperte Enter")
scraper()

input("Aperte Enter para sair")
	
