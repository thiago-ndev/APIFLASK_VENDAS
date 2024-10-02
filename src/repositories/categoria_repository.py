from src.infra.sql_alchemy import banco
from src.models.categoria_model import CategoriaModel
from src.repositories.base_repository import BaseRepository


class ProdutoRepository(BaseRepository):
    def get(self, categoria_id):
        return banco.session.query(CategoriaModel).filter_by(id=categoria_id).first()

    def list(self):
        return banco.session.query(CategoriaModel).all()

    def create(self, categoria):
        try:
            banco.session.add(categoria)
            banco.session.commit()
        except Exception as ex:
            banco.session.rollback()
            raise ex.args


    def update(self, categoria):
        try:
            banco.session.merge(categoria)
            banco.session.commit()
        except Exception as ex:
            banco.session.rollback()
            raise ex.args

    def delete(self, categoria_id):
        try:
            categoria = self.get(categoria_id)
            if categoria:
                banco.session.delete(categoria)
                banco.session.commit()
        except Exception as ex:
            banco.session.rollback()
            raise ex.args