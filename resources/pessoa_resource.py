from flask_restful import Resource, reqparse
from models.pessoa_model import *
from util import *

def get_arguments():
    argumentos = reqparse.RequestParser(bundle_errors=True)

    argumentos.add_argument('nome', required=True, help="Informe o nome da pessoa",
                            type=str)

    argumentos.add_argument('email', required=True, help="informe o email",
                            type=str)

    argumentos.add_argument('senha', required=True, help='informe a senha',
                            type=str)

    argumentos.add_argument('type', required=True, help='informe o tipo de pessoa.',
                            type=str)

    argumentos.add_argument('pr1', required=True, help='informe o parâmetro1',
                            type=str)

    argumentos.add_argument('pr2', required=True, help='informe o parâmetro2',
                            type=str)

    args = argumentos.parse_args()
    return args

class PessoasResource(Resource):
    def get(self):
        try:
            pessoas = PessoaModel().query.all()
            pessoas = [p.json() for p in pessoas]
            return {'pessoas': pessoas}, 200

        except Exception as ex:
            error = raise_error(ex.args,'Error ao buscar pessoas', 410), 500
            return {'error':error}, 500

    def post(self):
        dados = get_arguments()
        try:
            Type = dados['type']
            pessoa = None
            email = dados['email']
            if PessoaModel().find_by_email(email):
                raise Exception('EmailAlreadyExist, O email já está em uso')

            if Type == 'cliente':
                cliente = ClienteModel()
                cliente.nome = dados['nome']
                cliente.email = dados['email']
                cliente.senha = crypt_password(dados['senha'])
                cliente.dataNasc = dados['pr1']
                cliente.sexo = dados['pr2']
                pessoa = cliente
                pessoa.save()

            elif Type == 'usuario':
                 usuario = UsuarioModel()
                 usuario.nome = dados['nome']
                 usuario.email = dados['email']
                 usuario.senha = crypt_password(dados['senha'])
                 usuario.cpf = dados['pr1']
                 usuario.rg = dados['pr2']
                 pessoa = usuario
                 pessoa.save()

            else:
                raise Exception('PessoaTypeError, Somente cliente ou usuarios são permitidos.')

            return {'pessoa': pessoa.json()}, 201

        except Exception as ex:
            error = raise_error(ex.args,'error ao cadastrar pessoas', 410), 500
            return {'error': error}, 500

class PessoaResource(Resource):
    def get(self, codigo):
        try:
            pessoa = PessoaModel().find(codigo)
            if pessoa:
                return {'pessoa': pessoa.json()}, 200
            return {'mensage': 'pessoa não encontrada'}, 404

        except Exception as ex:
            error = raise_error(ex.args, 'Error ao buscar pessoa.', 410), 500
            return {'error': error}, 500

    def delete(self, codigo):
        try:
            pessoa = PessoaModel().find(codigo)
            if pessoa:
                pessoa.delete()
                return {'mensage':'pessoa deletada'}
            return {'mensage': 'pessoa não encontrada'}

        except Exception as ex:
            error = raise_error(ex.args,'Error ao deletar.', 410), 500
            return {'error': error}, 500

    def put(self, codigo):
            dados = get_arguments()
            try:
                Type = dados['type']
                if Type == 'cliente':
                    cliente = ClienteModel().find(codigo)
                    cliente.nome = dados['nome']
                    cliente.email = dados['email']
                    cliente.senha = crypt_password(dados['senha'])
                    cliente.dataNasc = dados['pr1']
                    cliente.sexo = dados['pr2']
                    pessoa = cliente
                    pessoa.update(cliente)
                    return {'mensagem': 'cliente atualizado com sucesso',
                            'cliente': pessoa.json()}, 201

                elif Type == 'usuario':
                    usuario = UsuarioModel().find(codigo)
                    usuario.nome = dados['nome']
                    usuario.email = dados['email']
                    usuario.senha = crypt_password(dados['senha'])
                    usuario.cpf = dados['pr1']
                    usuario.rg = dados['pr1']
                    pessoa = usuario
                    pessoa.update(usuario)
                    return {'mensagem': 'usuario atualizado com sucesso',
                            'usuario': pessoa.json()}, 201

                else:
                    raise Exception('PessoaTypeError, cliente ou usuario não entrado.')

            except Exception as ex:
                error = raise_error(ex.args,'Erro ao efetuar atualização.', 410), 500
                return {'error': error}, 500

class PessoaPerfisResource(Resource):

    def get_argumentos_perfis(self):

        argumentos = reqparse.RequestParser(bundle_errors=True)

        argumentos.add_argument('perfis', required=True, help='informe os perfis',
                                action='append', type=int)

        args = argumentos.parse_args()
        return args

    def post(self, codigo):
        dados = self.get_argumentos_perfis()
        try:
            pessoa = PessoaModel().find(codigo)
            perfis_codigos = dados['perfis']
            perfis = [PerfilModel().find(codigo) for codigo in perfis_codigos]
            for p in perfis:
                pessoa.perfis.append(p)

            #pessoa.perfis = perfis
            pessoa.save()
            return {'pessoa':pessoa.json()}, 200

        except Exception as ex:
            error = raise_error(ex.args, 'error ao criar perfil', 410)
            return {'error': error}, 500

