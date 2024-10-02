from src.services.base_service import BaseService
from src.repositories.pessoa_repository import PessoaRepository

class PessoaService:
    def __init__(self):
        self.repository = PessoaRepository()

    def get_pessoa(self, pessoa_id):
        return self.repository.get(pessoa_id)

    def list_pessoas(self):
        return self.repository.list()

    def create_pessoa(self, pessoa_data):
        pessoa = Pessoa(**pessoa_data)
        self.repository.create(pessoa)

    def update_pessoa(self, pessoa_id, pessoa_data):
        pessoa = self.repository.get(pessoa_id)
        if pessoa:
            for key, value in pessoa_data.items():
                setattr(pessoa, key, value)
            self.repository.update(pessoa)

    def  delete_pessoa(self, pessoa_id):
        self.repository.delete(pessoa_id)
