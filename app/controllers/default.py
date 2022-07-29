from flask import render_template
from app import app
from app.models.formularios import loginForm

@app.route("/")
def index():
    form = loginForm
    return render_template("login.html", form=form)

@app.route("/account/<user>")
@app.route("/account/", defaults={'user':'user'})
def acoount(user):
    return render_template('account.html', user=user)

@app.route('/envio')
def envio():
    return render_template('enviar.html')