from sql_alchemy import banco

association_table = banco.Table(
    "pessoas_perfis", banco.metadata,
    banco.Column("pessoa_codigo", banco.ForeignKey("pessoa.codigo"), primary_key=True),
    banco.Column("perfil_codigo", banco.ForeignKey("perfil.codigo"), primary_key=True),
)

class PerfilModel(banco.Model):
    __tablename__ = 'perfil'
    codigo = banco.Column(banco.Integer(), primary_key=True)
    perfil = banco.Column(banco.String(80), nullable=False)
    sigla = banco.Column(banco.String(20), nullable=False)

    pessoas = banco.relationship("PessoaModel", secondary="pessoas_perfis", back_populates="perfis")

    def __init__(self, codigo = None, perfil = None, sigla = None):
        self.codigo = codigo
        self.sigla = sigla
        self.perfil = perfil
        


    def __str__(self):
        return '{}, {}, {}'.format(self.codigo, self.perfil, self.sigla)

    def __repr__(self):
        return '{}, {}, {}'.format(self.codigo, self.perfil, self.sigla)

    def json(self):
        return {
            'codigo' :  self.codigo,
            'perfil' :  self.perfil,
            'sigla' : self.sigla
        }

    def save(self):
        banco.session.add(self)
        banco.session.commit()
        

    def update(self, obj):
        self.perfil = obj.perfil
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
        


    




