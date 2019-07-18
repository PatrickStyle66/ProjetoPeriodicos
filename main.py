import requests
from bs4 import BeautifulSoup
def s_tnh1(soup):
    return soup.find_all(name = 'p',attrs={'class':'bodytext'})

def s_alagoas24(soup):
    return soup.find_all(name = 'p')

def search_cont(link,site):
    req = requests.get(link)
    if req.status_code == 200:
        content = req.content
    soup = BeautifulSoup(content,'html.parser')
    title = soup.find(name='title')
    title = title.get_text()
    print('Título: {}'.format(title))
    body = site(soup)
    print('Conteúdo:')
    for text in body:
        print(text.get_text())
        if text.find(name='a') != None:
            reference = text.find(name='a')['href']
            print(reference)
    print('\n')

def tnh1():
    pag = 1
    while True:
        req = requests.get('https://www.tnh1.com.br/noticias/resultado-de-busca/pagina/{}/busca/ufal/'.format(pag))
        if req.status_code == 200:
            print('Requisição {} bem sucedida!'.format(pag))
            content = req.content
        soup = BeautifulSoup(content, 'html.parser')
        prox = soup.find_all(name='a', attrs={'title': 'Próxima Página'})
        if prox == []:
            break
        noticias = soup.find_all(name='li', attrs={'class': 'noticias-listagem__lista__item'})
        for objcont in noticias:
            cont = str(objcont)
            if 'pesquisa' in cont:
                link = objcont.find(name='a')['href']
                search_cont(link,s_tnh1)
        pag += 1

def alagoas24():
    pag = 1
    req = requests.get('http://www.alagoas24horas.com.br/page/{}/?s=ufal'.format(pag))
    if req.status_code == 200:
        print('Requisição {} bem sucedida!'.format(pag))
        content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    noticias = soup.find_all(name='h3',attrs={'class':'title'})
    for objcont in noticias:
        cont = str(objcont)
        if 'pesquisa' in cont:
            link = objcont.find(name='a')['href']
            search_cont(link,s_alagoas24)


#alagoas24()
#tnh1()
