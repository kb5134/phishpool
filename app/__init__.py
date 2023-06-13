from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from datetime import timedelta


app = Flask(__name__)
app.config.from_object('config')
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=1)
#run_with_ngrok(app, auth_token='2FgufYFYVmF47Oh5O0EJ5mraGg9_4KUBtPyfTWMNTmQ3WmUiB')

db = SQLAlchemy(app)
migrate = Migrate(app, db) # A instancia do migrate cuida das migrações pra isso ele recebe a aplicação e o banco

lm = LoginManager()
lm.init_app(app)

from app.models import tables, form
from app.models import tables
from app.controllers import default

#Admin
admin = Admin(app)
class ProdutoView(ModelView):
    can_delete = False  # disable model deletion
    can_create = False # disable model creation
    page_size = 50  # the number of entries to display on the list view
    column_searchable_list = ('nome_produto', 'url_produto')
    column_sortable_list = ('nome_produto','preco_informado','media_preco','url_produto','status')
    column_editable_list  = ['status']
    form_choices = {
    'status': [
        ('Analise', 'Analise'),
        ('Aprovado', 'Aprovado'),
        ('Reprovado', 'Reprovado'),
        ]
    }
    form_widget_args  = {
        'nome_produto': {
            'Disabled': ''
        },
        'preco_informado': {
            'Disabled': ''
        },
        'media_preco': {
            'Disabled': ''
        },
        'url_produto': {
            'Disabled': ''
        },
    }
admin.add_view(ProdutoView(tables.tb_produto, db.session))
