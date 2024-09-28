import pytest
from src.models.pessoa_model import ClienteModel
from datetime import  datetime


@pytest.fixture
def cliente():
    return ClienteModel(
        nome="Maria",
        email="maria@example.com",
        senha="senha123",
        sexo="f",
        dataNasc= datetime.now())

def test_cliente_create(cliente, client):
    cliente.save()
    result = ClienteModel.find(cliente.codigo)
    assert result.nome == "Maria"
    assert result.sexo == "f" or result.sexo == "m"

def test_cliente_update(cliente, client):
    cliente.save()
    cliente.nome = "Maria Atualizada"
    cliente.update(cliente)
    updated_cliente = ClienteModel.find(cliente.codigo)
    assert updated_cliente.nome == "Maria Atualizada"

def test_cliente_delete(cliente, client):
    cliente.save()
    cliente.delete()
    result = ClienteModel.find(cliente.codigo)
    assert result is None
