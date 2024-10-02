from src.infra.sql_alchemy import banco
from src.models.estoque_model import EstoqueModel
from src.repositories.base_repository import BaseRepository


class ProdutoRepository(BaseRepository):
    def get(self, estoque_id):
        return banco.session.query(EstoqueModel).filter_by(id=estoque_id).first()

    def list(self):
        return banco.session.query(EstoqueModel).all()

    def create(self, estoque):
        try:
            banco.session.add(estoque)
            banco.session.commit()
        except Exception as ex:
            banco.session.rollback()
            raise ex

    def update(self, estoque):
        try:
            banco.session.merge(estoque)
            banco.session.commit()
        except Exception as ex:
            banco.session.rollback()
            raise ex

    def delete(self, estoque_id):
        try:
            estoque = self.get(estoque_id)
            if estoque:
                banco.session.delete(estoque)
                banco.session.commit()
        except Exception as ex:
            banco.session.rollback()
            raise ex