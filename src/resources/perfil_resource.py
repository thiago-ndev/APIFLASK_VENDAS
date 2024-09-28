from flask_jwt_extended import jwt_required
from flask_restful import Resource,reqparse
from src.models.perfil_model import PerfilModel
from src.util import *

def get_argumentos(self):
    argumentos = reqparse.RequestParser(bundle_errors=True)

    argumentos.add_argument('perfil', required=True,
                            help='informe o perfil', type=str)

    argumentos.add_argument('sigla', required=True,
                            help='informe a sigla', type=str)

    args = argumentos.parse_args()
    return args

class PerfisResource(Resource):

    def get(self):

        try:
            perfis = PerfilModel.query.all()

            perfis = [p.json() for p in perfis]

            return {'perfis': perfis}


        except Exception as ex:
            msg = ex.args
            error = raise_error(msg, 'Erro ao criar lista perfis', 410)
            return {'error':error}, 500


    @jwt_required()
    def post(self):

        dados = get_argumentos(self)

        try:
            perfil = PerfilModel(sigla=dados['sigla'],
                                 perfil=dados['perfil'])
            perfil.save()
            return {'perfil': perfil.json()}, 201


        except Exception as ex:
            msg = ex.args
            error = raise_error(msg, 'Erro ao criar pefil', 410)
            return {'error':error}


class PerfilResource(Resource):

    def get(self, codigo):
        try:
            perfil = PerfilModel.find(codigo)

            if perfil:
                return {'produto': perfil.json()}, 200

            raise Exception('FindError, Perfil não encontrado')

        except Exception as ex:
            msg = ex.args
            error = raise_error(msg, 'erro ao buscar perfil',410)
            return {'error': error}, 500

    @jwt_required()
    def delete(self, codigo):
        try:
            perfil = PerfilModel.find(codigo)

            if perfil:
                perfil.delete()
                return {'msg': 'Perfil deletado com sucesso.'}, 200

        except Exception as ex:
            msg = ex.args
            error = raise_error(msg, 'erro ao deletar perfil', 410)
            return {'error': error}, 500

    @jwt_required()
    def put(self, codigo):
        dados = get_argumentos(self)
        try:
            perfil = PerfilModel.find(codigo)
            if perfil:
                perfil.sigla = dados['sigla']
                perfil.perfil = dados['perfil']
                perfil.update(perfil)
                return {'msg': 'Perfil atualizado com suceso.'}
            return {'msg': 'Perfil não encontrado.'}

        except Exception as ex:
            msg = ex.args
            error = raise_error(msg, 'erro ao atualizar perfil', 410)
            return {'error':error}, 500
