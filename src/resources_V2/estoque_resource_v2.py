from src.models.estoque_model import EstoqueModel
from src.models.produto_model import ProdutoModel
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from src.util import *

def get_argumentos():

    argumentos = reqparse.RequestParser(bundle_errors=True)

    argumentos.add_argument('quantidade', help='Informe a quantidade de produto que serão armazenados em estoque',
                             required=True ,type=int)

    argumentos.add_argument('produto_codigo', help="Informe o codigo do produto", required=True,
                            type=int)

    args = argumentos.parse_args()

    return args


class EstoquesResource(Resource):
    def get(self):
        try:
            estoque = EstoqueModel().query.all()
            estoque =  [e.json() for e in estoque]
            return {'estoque': estoque}

        except Exception as ex:
            msg = ex.args
            error = raise_error(msg, 'Error ao buscar estoque.', 410)
            return {'error': error}, 500

    @jwt_required()
    def post(self):
        dados = get_argumentos()
        try:
            estoque = EstoqueModel(quantidade=dados['quantidade'])
            produto_codigo = ProdutoModel.find(dados['produto_codigo'])
            if produto_codigo is None:
                raise Exception('ProdutoError, Produto não encontrado')
            estoque.produto = produto_codigo
            estoque.save()
            return {'estoque':estoque.json(),
                    'msg':'produto cadastrado no estoque com sucesso.'}, 201

        except Exception as ex:
            msg = ex.args
            error = raise_error(msg, 'Error ao cadastrar estoque.', 410)
            return {'error': error}, 500


class EstoqueResource(Resource):
    @jwt_required()
    def delete(self,codigo):
        try:
            estoque = EstoqueModel.find(codigo)
            if estoque:
                estoque.delete()
                return {'msg': 'estoque deletado com sucesso.'}
            return {'msg': 'estoque não encontrado.'}

        except Exception as ex:
            msg = ex.args
            error = raise_error(msg, 'Error ao deletar estoque.', 410)
            return {'error': error}, 500
    @jwt_required()
    def put(self, codigo):
        dados = get_argumentos()
        try:
            estoque = EstoqueModel.find(codigo)
            produto_codigo = ProdutoModel.find(codigo)
            if estoque:
                estoque.quantidade = dados['quantidade']
                estoque.produto = produto_codigo
                return {'estoque': estoque.json(),
                        'msg': 'estoque atualizado com successo.'}, 201

            return {'msg':'Estoque não encontrado.'}

        except Exception as ex:
            msg = ex.args
            error = raise_error(msg, 'Error ao atualizar estoque.', 410)
            return {'error': error}, 500
