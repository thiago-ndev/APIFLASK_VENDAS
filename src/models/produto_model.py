from src.infra.sql_alchemy import banco
from src.models.estoque_model import EstoqueModel
from src.models.categoria_model import CategoriaModel

class ProdutoModel(banco.Model):
    __tablename__ = 'produto'
    codigo = banco.Column(banco.Integer(), primary_key=True)
    nome = banco.Column(banco.String(80), nullable=False)
    preco = banco.Column(banco.Float(precision=1), nullable=False)

    # Chave estrangeira
    categoria_codigo = banco.Column(banco.Integer(), banco.ForeignKey("categoria.codigo"),
                                    nullable=False)



    estoque = banco.relationship(EstoqueModel, back_populates='produto', uselist=False)
    categoria = banco.relationship(CategoriaModel, back_populates='produtos')

    def __init__(self, codigo = None, nome = None, preco = None):
        self.codigo = codigo
        self.preco = preco
        self.nome = nome

    def __str__(self):
        return '{}, {}, {}'.format(self.codigo, self.nome, self.preco)

    def __repr__(self):
        return '{}, {}, {}'.format(self.codigo, self.nome, self.preco)

    # Serializador -> JSON
    def json(self, check = True):
        if check:
            return {
                'codigo' :  self.codigo,
                'nome': self.nome,
                'preco' : self.preco,
                'categoria' : self.categoria.json(False),
                'estoque': str(self.estoque)
            }
        return {
            'codigo': self.codigo,
            'nome': self.nome,
            'preco': self.preco,
        }

    def save(self):
        banco.session.add(self)
        banco.session.commit()


    def update(self, obj):
        self.nome = obj.nome
        self.preco = obj.preco
        self.codigo = obj.codigo
        self.save()


    def delete(self):
        banco.session.delete(self)
        banco.session.commit()


    # Método de classe
    @classmethod
    def find(cls, codigo):
        obj = cls.query.filter_by(codigo=codigo).first()
        if obj:
            return obj
        return None



