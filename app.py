from flask import Flask
from flask_restful import Resource, Api
import gunicorn
import blacklist
from resources.produto_resource import ProdutosResource, ProdutoResource
from resources.categoria_resource import CategoriasResource,CategoriaResource
from resources.pessoa_resource import PessoasResource,PessoaResource,PessoaPerfisResource
from resources.login_resource import LoginResource, LogoutResource
from sql_alchemy import banco
from flask_migrate import Migrate
from models.produto_model import ProdutoModel
from models.categoria_model import CategoriaModel
from models.estoque_model import EstoqueModel
from models.pessoa_model import *
from models.perfil_model import *
from flask_jwt_extended import JWTManager, get_jwt_header, jwt_required
from blacklist import BLACKLIST
from flask import jsonify
from config_json import *


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://b9bc569a3e06eb:5f601623@us-cdbr-''east-06.cleardb.net/heroku_e90ccb38ab628f6'
app.config['SQLALCHEMY_DATABASE_URI']= DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['JWT_SECRET_KEY']= 'APREST001'
app.config['JWT_BLACKLIST_ENABLE'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True

jwt = JWTManager(app)

api = Api(app)
# configurando a migração
migrate = Migrate(app, banco)
app.debug = True

# Inicializar o banco de dados
banco.init_app(app)
@app.route('/')
def index():
    return '<h1> Deploy realizado com sucesso.'

@jwt.token_in_blocklist_loader
def verificar_blacklist(jwt_header, jwt_payload: dict):
    jti = jwt_payload['jti']
    print('JTI VERIFICADA: ' + jti)
    print(BLACKLIST)
    return jti in BLACKLIST

@jwt.revoked_token_loader
def token_invalido(jwt_header, jwt_payload: dict):
    print('DENTRO DO REVOKED TOKEN')
    print(blacklist.BLACKLIST)
    return jsonify({'mensage': 'token invalidado'})


api.add_resource(PessoasResource, '/pessoas')
api.add_resource(PessoaResource, '/pessoas/<int:codigo>')
api.add_resource(PessoaPerfisResource, '/pessoas/<int:codigo>/perfis')

api.add_resource(LoginResource, '/login')
api.add_resource(LogoutResource, '/logout')

api.add_resource(ProdutosResource, '/produtos')
api.add_resource(ProdutoResource, '/produtos/<int:codigo>')

api.add_resource(CategoriasResource, '/categorias')
api.add_resource(CategoriaResource, '/categorias/<int:codigo>')

@app.before_first_request
def cria_banco():
    banco.create_all()


app.run(debug=True)
