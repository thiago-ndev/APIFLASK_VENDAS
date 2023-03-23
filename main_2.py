# flask shell
from util import crypt_password
from models.pessoa_model import *
cliente = ClienteModel(10, 'Ana', 'ana@gmail.com', '123456',
                       'f' , '02/04/1988')

cliente.save()

print(cliente)
print(cliente.json())

usuario = UsuarioModel(20, 'Marcos', 'marcos@gmail.com', '123456',
                       '121-121-111-12', '122-121-121-12')

usuario.save()

print(usuario)
print(usuario.json())


print(PessoaModel().query.all())


# ===============================

cliente = ClienteModel(nome="Thiago", email="Thiago@gmail.com",senha= crypt_password("123456"),
                       sexo="Masculino",dataNasc="30-05-2000")

cliente.save()


usuario = UsuarioModel(nome="BK", email="bk@gmail.com", senha=crypt_password("300520"),
                       rg="2146-84873", cpf="123-456-789-10")
usuario.save()

