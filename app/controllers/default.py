from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.models.form import LoginForm, BuscarValores
from app.models.tables import User, tb_produto
from flask_login import login_user, logout_user, login_required, current_user
from app.models.Scrappy import logica_scrappy

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
    Analise = "SELECT count(*) FROM produtos where status = 'Analise'"
    qtdAnalise = db.session.execute(Analise)
    Aprovado = "SELECT count(*) FROM produtos where status = 'Aprovado'"
    qtdAprovado = db.session.execute(Aprovado)
    Reprovado = "SELECT count(*) FROM produtos where status = 'Reprovado'"
    qtdReprovado = db.session.execute(Reprovado)
    return render_template('dashboard.html', Analise=qtdAnalise,Aprovado=qtdAprovado,Reprovado=qtdReprovado)

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
    logica_scrappy(request.form['nome_produto'],request.form['preco_produto'],request.form['url'],'Analise' )

    return 'meu ovo'