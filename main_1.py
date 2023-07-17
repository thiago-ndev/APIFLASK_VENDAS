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

categoria = CategoriaModel.find(1)

produto.categoria = categoria

produto.save()


ProdutoModel().query.all()

estoque = EstoqueModel()
estoque.quantidade = 10
estoque.produto = ProdutoModel.find(1)
estoque.save()