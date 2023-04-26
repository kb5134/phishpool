
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, URLField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class BuscarValores(FlaskForm):
    nome_produto = StringField('Nome Produto', validators=[DataRequired()])
    url = URLField('URL Suspeita', validators=[DataRequired()])