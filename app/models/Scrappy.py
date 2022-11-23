from bs4 import BeautifulSoup
from requests import request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


produto = input('insira o produto a ser buscado: ')

opts = webdriver.FirefoxOptions()
opts.add_argument("--width=400")
opts.add_argument("--height=800")

navegador = webdriver.Firefox(options=opts)

navegador.get('https://www.promobit.com.br')

elemento = navegador.find_element(By.CLASS_NAME, 'css-1kwy300')
elemento.click()

sleep(0.5)

elemento = navegador.find_element(By.ID, 'autocomplete_search_mobile_topbar_page')
elemento.send_keys(produto)
elemento.send_keys(Keys.ENTER)

sleep(2)

conteudo = navegador.page_source
site = BeautifulSoup(conteudo, 'html.parser')

sleep(2)
produtos = site.findAll(
    'div', attrs={'class': 'sh-pr__product-results-grid sh-pr__product-results'})
for produto in produtos:
    for i in range(3):
        preco_produto = produto.findAll(
            'span', attrs={'aria-hidden': 'true'})[i]
        if 'R$' in str(preco_produto):
            print(preco_produto.text)
