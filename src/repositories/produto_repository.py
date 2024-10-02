from src.infra.sql_alchemy import banco
from src.models.produto_model import ProdutoModel
from src.repositories.base_repository import BaseRepository


class ProdutoRepository(BaseRepository):
    def get(self, produto_id):
        return banco.session.query(ProdutoModel).filter_by(id=produto_id).first()

    def list(self):
        return banco.session.query(ProdutoModel).all()

    def create(self, produto):
        try:
            banco.session.add(produto)
            banco.session.commit()
        except Exception as ex:
            banco.session.rollback()
            raise ex
    def update(self, produto):
        try:
            banco.session.merge(produto)
            banco.session.commit()
        except Exception as ex:
            banco.session.rollback()
            raise ex

    def delete(self, produto_id):
        try:
            produto = self.get(produto_id)
            if produto:
                banco.session.delete(produto)
                banco.session.commit()
        except Exception as ex:
            banco.session.rollback()
            raise ex