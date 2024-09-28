from src.resources.pessoa_resource import PessoasResource,PessoaResource,PessoaPerfisResource
from src.resources.produto_resource import ProdutoResource, ProdutosResource
from src.resources.estoque_resource import EstoquesResource,EstoqueResource
from src.resources.categoria_resource import CategoriasResource,CategoriaResource
from src.resources.login_resource import LoginResource, LogoutResource
from src.resources.perfil_resource import PerfisResource, PerfilResource
from src.infra.sql_alchemy import banco
from src.blacklist import BLACKLIST
from src.ext import configuration
from src.ext import auth
from flask import Flask, render_template
from flask_migrate import Migrate
from flask import jsonify
from flask_restful import Api
from src import blacklist



app = Flask(__name__, template_folder='templates')
configuration.init_app(app)
auth.init_app(app)
api = Api(app)

# configurando a migração
migrate = Migrate(app, banco)
app.debug = app.config['DEBUG']

# Inicializar o banco de dados
banco.init_app(app)
@app.route('/')
def index():
    return render_template("index.html")


# Rotas
api.add_resource(PessoasResource, '/pessoas')
api.add_resource(PessoaResource, '/pessoas/<int:codigo>')
api.add_resource(PessoaPerfisResource, '/pessoas/<int:codigo>/perfis')

api.add_resource(PerfisResource, '/perfis')
api.add_resource(PerfilResource, '/perfis/<int:codigo>')

api.add_resource(LoginResource, '/login')
api.add_resource(LogoutResource, '/logout')

api.add_resource(ProdutosResource, '/produtos')
api.add_resource(ProdutoResource, '/produtos/<int:codigo>')

api.add_resource(EstoquesResource, '/estoque')
api.add_resource(EstoqueResource, '/estoque/<int:codigo>')

api.add_resource(CategoriasResource, '/categorias')
api.add_resource(CategoriaResource, '/categorias/<int:codigo>')

@app.before_first_request
def cria_banco():
    banco.create_all()

if __name__ == '__main__':
    app.run(debug=True)
