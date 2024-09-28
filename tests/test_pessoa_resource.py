import pytest
from src.models.pessoa_model import PessoaModel

@pytest.fixture
def client():
    from src.app import app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_pessoa_get_all(client, app_context):
    response = client.get('/pessoas')
    assert response.status_code == 200
    assert 'pessoas' in response.get_json()
    assert response.get_json()['pessoas'] is not None


def test_pessoa_get_not_found(client, app_context):
    response = client.get('/pessoas/999')
    assert response.status_code == 404
    assert response.json['mensage'] == 'pessoa não encontrada'


def test_pessoa_get_by_id(client, app_context):

    pessoa = PessoaModel(codigo=1, nome="João", email="joao@example.com", senha="senha123")
    pessoa.save()
    #banco.session.commit()

    response = client.get(f'/pessoas/{pessoa.codigo}')
    assert response.status_code == 200
    assert response.json['pessoa']['nome'] == 'João'


def test_pessoa_delete(client, jwt_token):
    pessoa = PessoaModel(codigo=1, nome="João", email="joao@example.com", senha="senha123")
    pessoa.save()

    response = client.delete('/pessoas/1', headers={'Authorization': f'Bearer {jwt_token}'})
    assert response.status_code == 200
    assert response.json['mensage'] == 'pessoa deletada'




def test_pessoa_post_invalid_type(client):
    payload = {
        'nome': 'Carlos',
        'email': 'carlos@example.com',
        'senha': 'senha123',
        'type': 'invalido',
        'pr1': 'param1',
        'pr2': 'param2'
    }
    response = client.post('/pessoas', json=payload)
    assert response.status_code == 500
    assert 'error' in response.json
