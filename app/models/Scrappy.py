from bs4 import BeautifulSoup
from requests import request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep

produto = input('insira o produto a ser buscado: ')

opts = Options()
opts.add_argument("--headless")
navegador = webdriver.Firefox()

navegador.get('https://shopping.google.com.br/')

elemento = navegador.find_element(By.ID, 'REsRA')
elemento.send_keys(produto)
elemento.submit()

sleep(2)

conteudo = navegador.page_source
site = BeautifulSoup(conteudo, 'html.parser')

sleep(2)
produtos = site.findAll('div', attrs={'class':'sh-pr__product-results-grid sh-pr__product-results'})
for produto in produtos:
    for i in range(3):
        preco_produto = produto.findAll('span', attrs={'aria-hidden':'true'})[i]
        if 'R$' in str(preco_produto):
            print(preco_produto.text)

