# flask shell
from models.produto_model import ProdutoModel
from models.categoria_model import CategoriaModel
from models.estoque_model import EstoqueModel

categoria = CategoriaModel()

categoria.nome = "Eletrodomestico"
categoria.sigla = "ELET"
categoria.save()

CategoriaModel.query.all()

produto = ProdutoModel()
produto.nome = "Fogão"
produto.preco = 2000.0

categoria = CategoriaModel.find(4)

produto.categoria = categoria

produto.save()


ProdutoModel().query.all()
EstoqueModel().query.all()
estoque = EstoqueModel()

estoque.quantidade = 15
estoque.produto = ProdutoModel.find(54)
estoque.save()

estoque.query.all()
produto.query.all()

estoque.quantidade = 10
estoque.produto = ProdutoModel.find(4)
estoque.save()