from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, URLField, DecimalField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class BuscarValores(FlaskForm):
    nome_produto = StringField('Nome do Produto', validators=[DataRequired()])
    preco_produto = DecimalField('Preço do Produto', validators=[DataRequired()])
    url = URLField('URL Suspeita', validators=[DataRequired()])