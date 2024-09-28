import pytest
from src.models.pessoa_model import PessoaModel

@pytest.fixture
def pessoa():
    return PessoaModel(nome="João", email="joao@example.com", senha="senha123")

def test_pessoa_create(pessoa, client):
    pessoa.save()
    result = PessoaModel.find(pessoa.codigo)
    assert result.nome == "João"
    assert result.email == "joao@example.com"

def test_pessoa_update(pessoa, client):
    pessoa.save()
    pessoa.nome = "João Atualizado"
    pessoa.update(pessoa)
    updated_pessoa = PessoaModel.find(pessoa.codigo)
    assert updated_pessoa.nome == "João Atualizado"

def test_pessoa_delete(pessoa, client):
    pessoa.save()
    pessoa.delete()
    result = PessoaModel.find(pessoa.codigo)
    assert result is None

def test_find_by_email(pessoa, client):
    pessoa.save()
    result = PessoaModel.find_by_email("joao@example.com")
    assert result is not None
    assert result.email == "joao@example.com"
