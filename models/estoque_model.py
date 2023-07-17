from sql_alchemy import banco

class EstoqueModel(banco.Model):
    __tablename__ = 'estoque'
    codigo = banco.Column(banco.Integer(), primary_key=True)
    quantidade = banco.Column(banco.Integer(), nullable=False)

    produto_codigo = banco.Column(banco.Integer(),banco.ForeignKey("produto.codigo"),nullable=False, unique=True)

    # Relacionamento
    produto = banco.relationship('ProdutoModel', back_populates='estoque')

    def __init__(self, codigo = None, quantidade = None):
        self.codigo = codigo
        self.quantidade = quantidade
    

    def __str__(self):
        return '{}, {}'.format(self.codigo, self.quantidade)

    def __repr__(self):
        return '{}, {}'.format(self.codigo, self.quantidade)

    def json(self):
        return {
            'codigo': self.codigo,
            'quantidade': self.quantidade,
        }
        # CRIAR OS METODOS DO CRUD

    def save(self):
        banco.session.add(self)
        banco.session.commit()
        

    def update(self, obj):
        self.quantidade = obj.quantidade
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
        

    
