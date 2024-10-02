from abc import ABC, abstractmethod
from src.resources.pessoa_resource import PessoaResource,PessoasResource, PessoaPerfisResource
from src.resources.produto_resource import ProdutoResource,ProdutosResource
from src.resources.estoque_resource import EstoqueResource,EstoquesResource
from src.resources.categoria_resource import CategoriaResource,CategoriasResource
from src.resources.perfil_resource import PerfilResource, PerfisResource
from src.resources.login_resource import LoginResource, LogoutResource
from src.services.pessoa_service import PessoaService

class ServiceFactory(ABC):
    @staticmethod
    def get_service(service_name):
        try:
            if service_name == 'pessoas':
                return PessoasResource
            elif service_name == 'pessoa':
                return PessoaResource
            elif service_name == 'pessoa_service':
                return PessoaService
            elif service_name == 'pessoa_perfis':
                return PessoaPerfisResource
            elif service_name == 'perfis':
                return PerfisResource
            elif service_name == 'perfil':
                return PerfilResource
            elif service_name == 'login':
                return LoginResource
            elif service_name == 'logout':
                return LogoutResource
            elif service_name == 'produtos':
                return ProdutosResource
            elif service_name == 'produto':
                return ProdutoResource
            elif service_name == 'estoques':
                return EstoquesResource
            elif service_name == 'estoque':
                return EstoqueResource
            elif service_name == 'categorias':
                return CategoriasResource
            elif service_name == 'categoria':
                return CategoriaResource
            else:
                raise ValueError(f"Service {service_name} not found")
        except Exception as ex:
            print(ex.args)
