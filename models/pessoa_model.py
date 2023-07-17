from sql_alchemy import banco
from .perfil_model import PerfilModel

class PessoaModel(banco.Model):
    __tablename__='pessoa'
    codigo = banco.Column(banco.Integer(), primary_key=True)
    nome = banco.Column(banco.String(80), nullable=False)
    email = banco.Column(banco.String(100), nullable=False, unique=True)
    senha = banco.Column(banco.String(255), nullable=False)
    type = banco.Column(banco.String(50))

    perfis = banco.relationship(PerfilModel, secondary="pessoas_perfis", back_populates="pessoas")

    __mapper_args__={
        "polymorphic_identity" : "pessoa",
        "polymorphic_on" : type,
    }

    def __init__(self, codigo = None, nome = None, email = None,
                 senha = None):
        self.codigo = codigo
        self.nome = nome
        self.senha = senha
        self.email = email
        

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.codigo, self.nome,
                                       self.email, self.senha)

    def __repr__(self):
        return '{}, {}, {}, {}'.format(self.codigo, self.nome,
                                       self.email, self.senha)

    def json(self):
        return {
            'codigo' : self.codigo,
            'nome' : self.nome,
            'email' : self.email,
            'senha' : self.senha,
            'perfis' : [p.json() for p in self.perfis]
        }
        # CRIAR OS METODOS DO CRUD

    def save(self):
        banco.session.add(self)
        banco.session.commit()
        

    def update(self, obj):
        self.nome = obj.nome
        self.senha = obj.senha
        self.email = obj.email
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

    @classmethod
    def find_by_email(cls, email):
        obj = cls.query.filter_by(email=email).first()
        if obj:
            return obj
        return None

class ClienteModel(PessoaModel):
    __tablename__ = "cliente"
    dataNasc = banco.Column(banco.DateTime, nullable=False)
    sexo = banco.Column(banco.String(10), nullable=False)
    codigo = banco.Column(banco.Integer(), banco.ForeignKey("pessoa.codigo"), primary_key=True)

    def __init__(self, codigo=None, nome=None, email=None,
                 senha=None, sexo = None, dataNasc = None):
        PessoaModel.__init__(self, codigo, nome, email, senha)
        self.dataNasc = dataNasc
        self.sexo = sexo
        

    __mapper_args__ = {
        "polymorphic_identity": "cliente",
    }

    def __str__(self):
        return '{}, {}, {}'.format(PessoaModel.__str__(self), self.dataNasc, self.sexo)

    def __repr__(self):
        return '{}, {}, {}'.format(PessoaModel.__str__(self), self.dataNasc, self.sexo)

    def json(self):
        return {
            'pessoa' : PessoaModel.json(self),
            'dataNasc' : str(self.dataNasc),
            'sexo' :  self.sexo
        }

    def update(self, obj):
        self.nome = obj.nome
        self.senha = obj.senha
        self.email = obj.email
        self.codigo = obj.codigo
        self.sexo = obj.sexo
        self.dataNasc = obj.dataNasc
        self.save()
        

    

class UsuarioModel(PessoaModel):

    __tablename__ = "usuario"

    codigo = banco.Column(banco.Integer(), banco.ForeignKey("pessoa.codigo"), primary_key=True)

    cpf = banco.Column(banco.String(30), nullable=False)
    rg = banco.Column(banco.String(30), nullable=False)


    def __init__(self, codigo=None, nome=None, email=None,
                 senha=None, cpf= None, rg = None):
        PessoaModel.__init__(self, codigo, nome, email, senha)
        self.cpf = cpf
        self.rg = rg
        

    __mapper_args__ = {
        "polymorphic_identity": "usuario",
    }

    def __str__(self):
        return '{}, {}, {}'.format(PessoaModel.__str__(self), self.cpf, self.rg)

    def __repr__(self):
        return '{}, {}, {}'.format(PessoaModel.__str__(self), self.cpf, self.rg)

    def json(self):
        return {
            'pessoa': PessoaModel.json(self),
            'cpf': self.cpf,
            'rg' : self.rg
        }


    def update(self, obj):
        self.nome = obj.nome
        self.senha = obj.senha
        self.email = obj.email
        self.codigo = obj.codigo
        self.cpf = obj.cpf
        self.rg = obj.rg
        self.save()
        

    

