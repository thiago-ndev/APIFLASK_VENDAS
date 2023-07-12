from flask_restful import Resource,reqparse
from models.perfil_model import PerfilModel
from util import *
from flask_jwt_extended import create_access_token, jwt_required

from werkzeug.security import safe_str_cmp
from blacklist import *

from flask import make_response, jsonify

class PerfisResource(Resource):

    def get_argumentos(self):
        argumentos = reqparse.RequestParser(bundle_errors=True)

        argumentos.add_argument('perfil', required=True,
                                help='Informe o perfil',
                                type=str)

        argumentos.add_argument('sigla', required=True,
                                help='Informe a sigla',
                                type=str)


        args = argumentos.parse_args()
        return args
    def get(self):
        try:
            perfis = PerfilModel.query.all()

            # Compreensão de lista
            perfis = [p.json() for p in perfis]

            return {'perfis' : perfis}

        except Exception as ex:
            msg = ex.args
            error = {
                'status': 410,
                'msg_sys': msg,
                'msg_user': 'Error ao criar lista perfis'
            }
            return {'error': error}, 500


        pass

    def post(self):
        dados = self.get_argumentos()
        try:

            perfil = PerfilModel(sigla=dados['sigla'],
                                 perfil=dados['perfil'])
            perfil.save()
            return {'perfil': perfil.json()}, 201


        except Exception as ex:
            msg = ex.args
            error = {
                'status': 410,
                'msg_sys': msg,
                'msg_user': 'Error ao criar o perfil'
            }
            return {'error': error}, 500

    pass

    # DELETE, PUT, GET
    class PerfilResource(Resource):

        def get(self, codigo):
            try:
                perfil = PerfilModel.find(codigo)

                if perfil is not None:
                    return {'produto': perfil.json()}, 200

                raise Exception('FindError, Perfil não encontrado')


            except Exception as ex:
                msg = ex.args
                error = {
                    'status': 410,
                    'msg_sys': msg,
                    'msg_user': 'Error ao buscar perfil'
                }
                return {'error': error}, 500

            pass

        @jwt_required()
        def delete(self, codigo):
            try:
                perfil = PerfilModel.find(codigo)

                if perfil is not None:
                    perfil.delete()
                    return {'msg': 'Perfil deletado com sucesso'}, 200

                raise Exception('DeleteError, perfil incorreto.')

            except Exception as ex:
                msg = ex.args
                error = {
                    'status': 410,
                    'msg_sys': msg,
                    'msg_user': 'Error ao deletar perfil'
                }
                return {'error': error}, 500