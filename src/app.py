from src.infra.sql_alchemy import banco
from src.ext import configuration
from src.ext import auth
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_restful import Api
from src.factories.service_factory import ServiceFactory

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
api.add_resource(ServiceFactory.get_service('pessoas'), '/pessoas')
api.add_resource(ServiceFactory.get_service('pessoa'), '/pessoas/<int:codigo>')
api.add_resource(ServiceFactory.get_service('pessoa_perfis'), '/pessoas/<int:codigo>/perfis')

api.add_resource(ServiceFactory.get_service('perfis'), '/perfis')
api.add_resource(ServiceFactory.get_service('perfil'), '/perfis/<int:codigo>')

api.add_resource(ServiceFactory.get_service('login'), '/login')
api.add_resource(ServiceFactory.get_service('logout'), '/logout')

api.add_resource(ServiceFactory.get_service('produtos'), '/produtos')
api.add_resource(ServiceFactory.get_service('produto'), '/produtos/<int:codigo>')

api.add_resource(ServiceFactory.get_service('estoques'), '/estoque')
api.add_resource(ServiceFactory.get_service('estoque'), '/estoque/<int:codigo>')

api.add_resource(ServiceFactory.get_service('categorias'), '/categorias')
api.add_resource(ServiceFactory.get_service('categoria'), '/categorias/<int:codigo>')

@app.before_first_request
def cria_banco():
    banco.create_all()

if __name__ == '__main__':
    app.run(debug=True)
