from bs4 import BeautifulSoup
from requests import request
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import locale

class scrappy():
    produto = input('insira o produto a ser buscado: ')

    opts = webdriver.FirefoxOptions()
    opts.add_argument("--width=400")
    opts.add_argument("--height=800")
    opts.add_argument('--headless')
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
    valores = []
    for i in range(3):
        produtos = site.findAll('span', attrs={'class': 'e1dhv8140'})[i].text
        if len(produtos) <= 6:
            valores.append(float(produtos.replace(",",".")))
        else:
            valores.append(float(produtos.replace(",",".").replace(".", ",")))

    valor_medio = round(sum(valores)/len(valores),2)
    dados = []
    dados.append([produto, valor_medio])
    print(dados)
    relatorio = pd.DataFrame(dados, columns=['Nome Produto', 'Valor Médio'])
    relatorio.to_csv('valores_retornados.csv', index=False, header=False, mode='a')