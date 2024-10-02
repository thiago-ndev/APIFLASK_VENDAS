from src.infra.sql_alchemy import banco
from src.models.pessoa_model import PessoaModel
from src.repositories.base_repository import BaseRepository


class PessoaRepository(BaseRepository):
    def get(self, pessoa_id):
        return banco.session.query(PessoaModel).filter_by(id=pessoa_id).first()

    def list(self):
        return banco.session.query(PessoaModel).all()

    def create(self, pessoa):
        try:
            banco.session.add(pessoa)
            banco.session.commit()
        except Exception as ex:
            banco.session.rollback()
            raise ex

    def update(self, pessoa):
        try:
            banco.session.merge(pessoa)
            banco.session.commit()
        except Exception as ex:
            banco.session.rollback()
            raise ex

    def delete(self, pessoa_id):
        try:
            pessoa = self.get(pessoa_id)
            if pessoa:
                banco.session.delete(pessoa)
                banco.session.commit()
        except Exception as ex:
            banco.session.rollback()
            raise ex