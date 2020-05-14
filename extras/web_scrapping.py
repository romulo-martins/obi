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

def _remove_duplicates(array, param):
    while param in array: 
        array.remove(param)
    return array

def _extract_name(url):
    elems = url.split('/')
    elems = _remove_duplicates(elems, '')
    return elems.pop()

def _save_file(content, filename):
    dirname = 'data'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
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

def extract_statement(url):
    req = requests.get(url)
    name = _extract_name(url)
    if req.status_code == 200:
        statement = _extract_statement(req.content)
        markdown = tomd.convert(str(statement))
        _save_file(markdown, name)
        print(f'Successful download of {name}!')
    else:
        print(f'We cannot get the request of {name}!')
    
def extract_main_links(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    links = soup.select('a[href*="/pratique/p"]')
    links = [l.get('href') for l in links]
    for link in links:
        extract_statement(f'{BASE_URL}{link}')

extract_main_links('https://olimpiada.ic.unicamp.br/pratique/pj/')
