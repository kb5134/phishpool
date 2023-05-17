import locale
from app import db
from bs4 import BeautifulSoup
from time import sleep
from app.models.tables import tb_produto
from requests import request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def logica_scrappy(produto, preco_informado,url_produto,status):
    opts = webdriver.FirefoxOptions()
    opts.add_argument("--width=400")
    opts.add_argument("--height=800")
    # opts.add_argument('--headless')

    navegador = webdriver.Firefox(options=opts)
    navegador.get('https://www.promobit.com.br')
    elemento = navegador.find_element(By.CSS_SELECTOR, "[aria-label='Mostrar barra de busca']")
    elemento.click()

    sleep(0.5)
    elemento = navegador.find_elements(By.CSS_SELECTOR, "[placeholder='O que você procura?']")[-1]
    elemento.click()
    sleep(0.5)
    elemento.send_keys(produto)
    elemento.send_keys(Keys.ENTER)

    sleep(2)
    conteudo = navegador.page_source
    site = BeautifulSoup(conteudo, 'html.parser')

    sleep(3)
    valores = []
    for i in range(3):
        teste = site.find('div', attrs={'class': 'flex flex-col rounded-2 bg-white dark:bg-gray-850 mt-4 overflow-hidden pt-4'})
        produtos = teste.findAll('span', attrs={'class': ['text-base font-bold lg:text-xl whitespace-nowrap text-blue-800 dark:text-blue-200']})[i].text
        print(produtos)
        if len(produtos) <= 6:
            valores.append(float(produtos.replace(",", ".")))
        else:
            teste = produtos.replace(".", "_").replace(",", ".")
            locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
            valores.append(float(locale.atof(teste)))

    selectproduto = f"SELECT * FROM produtos where nome_produto = '{produto}'" 
    selectproduto = db.session.execute(selectproduto)
    print(selectproduto)
    cadastro = tb_produto(nome_produto=produto,
                            preco_informado=preco_informado,
                            media_preco = round(sum(valores)/len(valores),2),
                            url_produto=url_produto,
                            status=status)
    db.session.add(cadastro)
    db.session.commit()
    tb_produto.query.all()