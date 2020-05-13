"""
    Carrega todos os enunciados da página oficial das olimpiadas e os 
    converte para markdown
"""

import requests
from bs4 import BeautifulSoup
import tomd

def _extract_filename(url):
    elems = url.split('/')
    while '' in elems: 
        elems.remove('')
    return elems.pop()

def _save_file(content, filename):
    file = open(f'{filename}.md', 'w')
    file.write(content)
    file.close()

def _remove_form(statement):
    form = statement.select('div[role="main"] > form')
    if len(form) > 0:
        _ = form[0].extract()
    return statement

def _extract_statement(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    statement = soup.select('div[role="main"]')
    if len(statement) == 0:
        print('We cannot find the statement content!')
        return None
    return _remove_form(statement[0])

def extract_statement(url):
    req = requests.get(url)
    filename = _extract_filename(url)
    if req.status_code == 200:
        statement = _extract_statement(req.content)
        markdown = tomd.convert(str(statement))
        _save_file(markdown, filename)
        print('Successful download!')
    else:
        print('We cannot get the request!')
    
extract_statement('https://olimpiada.ic.unicamp.br/pratique/pj/2019/f1/domino/')
