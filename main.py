import requests
from bs4 import BeautifulSoup

for pag in range(1,26):
    req = requests.get('https://www.tnh1.com.br/noticias/resultado-de-busca/pagina/{}/busca/ufal/'.format(pag))
    if req.status_code == 200:
        print('Requisição bem sucedida!')
        content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    noticias = soup.find_all(name='li', attrs={'class':'noticias-listagem__lista__item'})
    for objcont in noticias:
        cont = str(objcont)
        if 'ufal' in cont:
           link = objcont.find(name = 'a')['href']
           print(link)