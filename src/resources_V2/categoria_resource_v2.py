# from flask_restful import Resource, reqparse
# #from src.models.categoria_repositories import  CategoriaRepositories
# from src.util import raise_error
#
# def get_argumentos():
#     argumentos = reqparse.RequestParser(bundle_errors=True)
#
#     argumentos.add_argument('nome', required=True,
#                             help='Informe o nome.' , type=str )
#
#     argumentos.add_argument('sigla', required=True,
#                             help='Informe a sigla.', type=str)
#
#     args = argumentos.parse_args()
#     return args
#
#
#
#
# class CategoriasController(Resource):
#
#     def get(self):
#         try:
#
#             categorias = CategoriaModel().query.all()
#             # SERIALIZAR -> JSON()
#             categorias = [c.json() for c in categorias]
#             return {'categorias' : categorias}, 200
#
#         except Exception as ex:
#             msg = ex.args
#             error = raise_error(msg, 'Erro ao listar categorias.', 410)
#             return  {'error' :  error}, 500
#
#
#     def post(self):
#         dados = get_argumentos()
#         try:
#             categoria = CategoriaModel()
#             categoria.nome = dados['nome']
#             categoria.sigla = dados['sigla']
#             categoria.save()
#             return {'categoria':  categoria.json()}, 201
#
#         except Exception as ex:
#             msg= ex.args
#             error = raise_error(msg, 'Erro ao cadastrar categoria.', 409)
#             return {'error' : error}, 500
#
#
# class CategoriaController(Resource):
#     def get(self, codigo):
#         try:
#             categoria = CategoriaModel().find(codigo)
#             if categoria:
#                 return {'categoria': categoria.json()}
#             return {'mensage': 'categoria não encontrada'}
#
#         except Exception as ex:
#             error = raise_error(ex.args, "Erro ao buscar categoria", 410),500
#             return {'error':error },500
#
#
#     def put(self, codigo):
#         dados = get_argumentos()
#         try:
#             categoria = CategoriaModel().find(codigo)
#             if categoria:
#                 categoria.nome = dados["nome"]
#                 categoria.sigla = dados["sigla"]
#                 categoria.update(categoria)
#                 return {'categoria':categoria.json()}
#
#             return {'mensage': 'categoria não encontrada'}
#
#         except Exception as ex:
#             error = raise_error(ex.args, 'Erro ao Atualizar categoria.', 410), 500
#             return {'error': error}, 500
#
#     def delete(self, codigo):
#         try:
#             categoria = CategoriaModel().find(codigo)
#             if categoria:
#                 categoria.delete()
#                 return {'mensage': 'Categoria deletada.'}, 404
#
#             return {'mensage': 'Categoria não encontrada'}
#
#
#         except Exception as ex:
#             error = raise_error(ex.args,"Erro ao Deletar categoria.", 410), 500
#             return {"error": error}, 500
