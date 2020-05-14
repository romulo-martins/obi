#!/usr/bin/python

"""
    Carrega todos os enunciados da página oficial das olimpiadas e os 
    converte para markdown
"""

import requests
from bs4 import BeautifulSoup
import tomd
import os

BASE_URL = 'https://olimpiada.ic.unicamp.br'

def _remove_all(array, param):
    while param in array: 
        array.remove(param)
    return array

def _extract_name(url):
    elems = url.split('/')
    elems = _remove_all(elems, '')
    return elems.pop()

def _extract_dirname(url, filename = ''):
    url = url.replace(BASE_URL, '')
    url = url.replace(filename, '')
    names = _remove_all(url.split("/"), '')
    return "/".join(names)

def _save_file(content, filename, dirname = 'data'):
    if not os.path.exists(dirname):
        os.system(f'mkdir -p {dirname}')
    file = open(f'{dirname}/{filename}.md', 'w')
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

def download_statement(url):
    req = requests.get(url)
    filename = _extract_name(url)
    dirname = _extract_dirname(url)
    if req.status_code == 200:
        statement = _extract_statement(req.content)
        markdown = tomd.convert(str(statement))
        _save_file(markdown, filename, dirname)
        print(f'Successful download of {filename}!')
    else:
        print(f'We cannot get the request of {filename}!')
    
def exec_scraping(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    links = soup.select('a[href*="/pratique/p"]')
    links = [l.get('href') for l in links]
    for link in links:
        # print(f'{BASE_URL}{link}')
        download_statement(f'{BASE_URL}{link}')

exec_scraping('https://olimpiada.ic.unicamp.br/pratique/p1/')
