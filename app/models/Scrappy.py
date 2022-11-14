from bs4 import BeautifulSoup
from requests import request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

produto = input('insira o produto a ser buscado: ')

navegador = webdriver.Firefox()

navegador.get('https://shopping.google.com.br/')

elemento = navegador.find_element(By.ID, 'REsRA')

elemento.send_keys(produto + Keys.ENTER)

