from flask import render_template, flash, redirect, url_for
from app import app
from app.models.form import LoginForm
from app.models.tables import User
from flask_login import login_user, logout_user, login_required, current_user


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
    return render_template('enviar.html')