import requests
from bs4 import BeautifulSoup

def search_cont(link):
    req = requests.get(link)
    if req.status_code == 200:
        content = req.content
    soup = BeautifulSoup(content,'html.parser')
    title = soup.find(name='title')
    title = title.get_text()
    print('Título: {}'.format(title))
    body = soup.find_all(name = 'p',attrs={'class':'bodytext'})
    print('Conteúdo:')
    for text in body:
        print(text.get_text())
        if text.find(name='a') != None:
            reference = text.find(name='a')['href']
            print(reference)
    print('\n')

for pag in range(1,26):
    req = requests.get('https://www.tnh1.com.br/noticias/resultado-de-busca/pagina/{}/busca/ufal/'.format(pag))
    if req.status_code == 200:
        print('Requisição {} bem sucedida!'.format(pag))
        content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    noticias = soup.find_all(name='li', attrs={'class':'noticias-listagem__lista__item'})
    for objcont in noticias:
        cont = str(objcont)
        if 'pesquisa' in cont:
           link = objcont.find(name = 'a')['href']
           #print(link)
           search_cont(link)