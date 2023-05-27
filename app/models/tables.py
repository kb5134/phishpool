from app import db
from app import lm

@lm.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))



    def __init__(self, username, password):
        self.username = username
        self.password = password


    def __repr__(self):
        return "<User %r>" % self.username

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

class tb_produto(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)
    nome_produto = db.Column(db.String(50), unique=False)
    preco_informado = db.Column(db.Float()) 
    media_preco = db.Column(db.Float())
    status_media = db.Column(db.String(10), default='Analise')
    url_produto = db.Column(db.String(255), unique=False)
    status = db.Column(db.String(10), default='Analise')