from flask_jwt_extended import create_access_token
from src.app import app, banco
import pytest

@pytest.fixture(scope='function')
def app_context():
    """Configura um contexto da aplicação Flask para os testes."""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Banco em memória
    with app.app_context():
        banco.create_all()  # Cria as tabelas no banco em memória
        yield app
        banco.session.remove()
        banco.drop_all()  # Limpa as tabelas após os testes

@pytest.fixture
def client(app_context):
    """Cria um cliente de teste Flask"""
    return app_context.test_client()

@pytest.fixture
def jwt_token(app_context):
    """Cria um token JWT para ser usado nos testes"""
    with app_context.app_context():  # Certifique-se de que está no contexto do app
        token = create_access_token(identity={"email": "test@example.com"})
    return token
