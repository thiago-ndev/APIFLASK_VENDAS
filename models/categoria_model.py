from sql_alchemy import banco
class CategoriaModel(banco.Model):
    __tablename__ = 'categoria'
    codigo = banco.Column(banco.Integer(), primary_key=True)
    nome = banco.Column(banco.String(80), nullable=False)
    sigla= banco.Column(banco.String(20), nullable=False)

    produtos = banco.relationship('ProdutoModel', back_populates='categoria')

    def __int__(self, codigo = None, nome = None, sigla= None):
        self.codigo =codigo
        self.nome = nome
        self.sigla = sigla
        

    def __str__(self):
        return '{}, {}, {}'.format(self.codigo, self.sigla, self.nome)

    def __repr__(self):
        return '{}, {}, {}'.format(self.codigo, self.sigla, self.nome)

    def json(self, check = True):
        if check:
            return{
                'codigo' : self.codigo,
                'nome' :  self.nome,
                'sigla' : self.sigla,
                'produtos' :  [p.json(False) for p in self.produtos]
            }
        return {
            'codigo': self.codigo,
            'nome': self.nome,
            'sigla': self.sigla,
        }

        # CRIAR OS METODOS DO CRUD

    def save(self):
        banco.session.add(self)
        banco.session.commit()
        

    def update(self, obj):
        self.nome = obj.nome
        self.sigla = obj.sigla
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
        

    
