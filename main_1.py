# flask shell
from models.produto_model import ProdutoModel
from models.categoria_model import CategoriaModel
from models.estoque_model import EstoqueModel

# Gravar uma categoria
categoria = CategoriaModel()

categoria.nome = "Eletrodomestico"
categoria.sigla = "ELET"
categoria.save()

# Buscar categorias
CategoriaModel.query.all()

produto = ProdutoModel()
produto.nome = "Fogão"
produto.preco = 2000.0
# Buscar a categoria
categoria = CategoriaModel.find(1)
# Relacionando a categoria com o produto
produto.categoria = categoria
# Gravando o produto categoria
produto.save()

# Buscar todos os produtos.
ProdutoModel().query.all()

estoque = EstoqueModel()
estoque.quantidade = 10
estoque.produto = ProdutoModel.find(1)
estoque.save()