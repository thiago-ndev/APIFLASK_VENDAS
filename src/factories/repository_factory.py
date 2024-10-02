
from src.repositories.pessoa_repository import PessoaRepository
#from src.repositories.produto_repository import ProdutoRepository

class RepositoryFactory:
    @staticmethod
    def get_repository(repo_name):
        if repo_name == 'pessoa':
            return PessoaRepository()

        else:
            raise ValueError(f"Repository {repo_name} not found")
