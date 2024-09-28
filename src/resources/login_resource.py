from flask_restful import Resource, reqparse
from src.util import *
from hmac import compare_digest
from flask_jwt_extended import create_access_token, get_jwt, jwt_required
from src.blacklist import *
from flask import make_response, jsonify
from src.models.pessoa_model import PessoaModel

class LoginResource(Resource):

    def get_arguments(self):

        argumentos = reqparse.RequestParser(bundle_errors=True)
        argumentos.add_argument('email', required=True, help='informe o email.',
                                type=str)
        argumentos.add_argument('senha', required=True, help='informe a senha.',
                                type=str)

        args = argumentos.parse_args()
        return args


    def post(self):
        dados = self.get_arguments()
        try:
            pessoa = PessoaModel().find_by_email(dados['email'])
            if pessoa is None:
                raise Exception('PessoaNotFound, pessoa não cadastrada no sistema.')

            if compare_digest(pessoa.senha, crypt_password(dados['senha'])):
                token = create_access_token(pessoa.codigo)
                token = "Bearer "+ str(token)
                resp = make_response(jsonify({'pessoa' : pessoa.json()}), 200)
                resp.headers['access_token'] = token
                return resp

            raise Exception('UsuarioInvalidoError, usuario ou senha invalidos.')

        except Exception as ex:
            error = raise_error(ex.args,'Error ao efetuar Login', 410)
            return {'error': error}, 500


class LogoutResource(Resource):

    @jwt_required()
    def post(self):
        try:
            jwt_id = get_jwt()['jti']
            print(jwt_id)
            BLACKLIST.add(jwt_id)
            return {'mensage': 'deslogado'}

        except Exception as ex:
            error = raise_error(ex.args, 'Erro ao efetuar Logout', 410)
            return {'error': error}, 500