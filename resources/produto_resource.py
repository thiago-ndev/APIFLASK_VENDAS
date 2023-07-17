from flask_restful import Resource, reqparse
from models.categoria_model import CategoriaModel
from models.produto_model import ProdutoModel
from flask_jwt_extended import jwt_required
from util import raise_error

def get_argumentos(chek=True):
    argumentos = reqparse.RequestParser(bundle_errors=True)

    argumentos.add_argument('nome', required=True, help='Informe o nome', type=str)

    argumentos.add_argument('preco', required=True, help='Informe o preco', type=float)

    if chek==False:
        args = argumentos.parse_args()
        return args

    argumentos.add_argument('categoria_codigo', required=True,
                            help='Informe o codigo da categoria', type=int)

    args = argumentos.parse_args()
    return args
    pass


# Métodos do API -> POST, GET, DELETE, UPDATE
# -> Sem parâmetros -> GET -> todos os produtos, POST -> Cadastrar
class ProdutosResource(Resource):

    # Get -> todos os produtos
    def get(self):
        try:
            produtos = ProdutoModel().query.all()
            produtos = [p.json() for p in produtos]
            return {'produtos' :  produtos}, 200

        except Exception as ex:
            msg = ex.args
            error = raise_error(msg, 'Erro ao listar produtos', 410)
            return {'error' :  error }, 500


    @jwt_required()
    def post(self):
        dados = get_argumentos()
        try:
            produto = ProdutoModel(nome=dados['nome'], preco=dados['preco'])
            categoria = CategoriaModel.find(dados['categoria_codigo'])
            if categoria is None:
                raise Exception('CategoriaError, categoria não encontrada.')
            produto.categoria = categoria
            categoria.produtos.append(produto)
            produto.save()
            return {'produto': produto.json()}, 201
        except Exception as ex:
            msg = ex.args
            error = raise_error(msg, 'Erro ao cadastrar produto', 409)
            return {'error' : error}, 500



# GET, DELETE, PUT
# Com parâmetros

class ProdutoResource(Resource):
    def get(self, codigo):
        try:
            produto = ProdutoModel().find(codigo)
            if produto:
                return {'produto':produto.json()}

            return {'mensage':' produto não encontrado'}, 404

        except Exception as ex:
            error = raise_error(ex.args,"Error ao buscar produto", 410), 500
            return {'error', error}, 500

    @jwt_required()
    def delete(self,codigo):
        try:
            produto = ProdutoModel().find(codigo)
            if produto:
                if produto.estoque:
                    produto.estoque.delete()
                produto.delete()
                return {'mensage': 'produto deletado'}

            return {'mensage': 'produto não encontrado'}

        except Exception as ex:
            error = raise_error(ex.args, "Error ao deletar produto", 410), 500
            return {'error': error}, 500

    @jwt_required()
    def put(self, codigo):
        dados = get_argumentos(chek=False)
        try:
            produto = ProdutoModel().find(codigo)
            if produto:
                produto.nome = dados['nome']
                produto.preco = dados['preco']
                produto.update(produto)
                return {'mensage': 'produto atualizado.'}

            return {'mensage': 'Produto não encontrado.'}

        except Exception as ex:
            error = raise_error(ex.args, "Error ao Atualizar o produto.", 410), 500
            return {'error':error}, 500

        #vai funcionar