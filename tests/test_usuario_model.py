import pytest
from src.models.pessoa_model import UsuarioModel

@pytest.fixture
def usuario():
    return UsuarioModel(
        nome="Carlos",
        email="carlos@example.com",
        senha="senha123",
        cpf="123456789",
        rg="987654321")

def test_usuario_create(usuario, client):
    usuario.save()
    result = UsuarioModel.find(usuario.codigo)
    assert result.nome == "Carlos"
    assert result.cpf == "123456789"

def test_usuario_update(usuario, client):
    usuario.save()
    usuario.nome = "Carlos Atualizado"
    usuario.update(usuario)
    updated_usuario = UsuarioModel.find(usuario.codigo)
    assert updated_usuario.nome == "Carlos Atualizado"

def test_usuario_delete(usuario, client):
    usuario.save()
    usuario.delete()
    result = UsuarioModel.find(usuario.codigo)
    assert result is None
