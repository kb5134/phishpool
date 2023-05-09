import pandas as pd
from app import app
from bs4 import BeautifulSoup
from time import sleep
from flask import render_template, flash, redirect, url_for, request
from app.models.form import LoginForm, BuscarValores
from app.models.tables import User
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from flask_login import login_user, logout_user, login_required, current_user
import locale

@app.route("/", methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("dashboard"))
        else:
            flash('Login Invalido')
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('Deslogado')
    return redirect(url_for('index'))

@login_required
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@login_required
@app.route("/account/<user>")
@app.route("/account/", defaults={'user':'user'})
def acoount(user):
    return render_template('account.html', user=user)

@login_required
@app.route('/envio')
def envio():
    form = BuscarValores()
    return render_template('enviar.html',form=form )


@login_required
@app.route('/dados', methods=['POST'])
def dados():
    produto = request.form['nome_produto']
    
    opts = webdriver.FirefoxOptions()
    opts.add_argument("--width=400")
    opts.add_argument("--height=800")
    #opts.add_argument('--headless')
    navegador = webdriver.Firefox(options=opts)

    navegador.get('https://www.promobit.com.br')

    elemento = navegador.find_element(By.CLASS_NAME, 'css-oghyru')
    elemento.click()

    sleep(0.5)

    elemento = navegador.find_element(By.ID, '40')
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
            teste = produtos.replace(".","_").replace(",",".")
            locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
            valores.append(float(locale.atof(teste)))

    valor_medio = round(sum(valores)/len(valores),2)
    dados = []
    dados.append([produto, valor_medio])
    print(dados)
    relatorio = pd.DataFrame(dados, columns=['Nome Produto', 'Valor Médio'])
    relatorio.to_csv('valores_retornados.csv', index=False, header=False, mode='a')
    return 'Os dados enviados foram: {}'.format(produto)
