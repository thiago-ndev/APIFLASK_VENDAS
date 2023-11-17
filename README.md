# APIFLASK_VENDAS
A APIFLASK_VENDAS é um projeto que demonstra a criação de uma API RESTfull para controle de produtos, cadastro de clientes e usuarios no sistema.

## Documentação da API 
    https://documenter.getpostman.com/view/25608627/2s946iaqNW

## Instalação 
- Python 3.6+
- Flask 2.0.3
install using pip:


1. Clone o repositório para o seu ambiente local:
     https://github.com/thiago-ndev/APIFLASK_VENDAS.git
2. Acesse o diretório do projeto: 
3. Crie um ambiente Virtual para o projeto(venv)

4. baixe as bibliotecas necessarias para rodar o projeto que estão no arquivo requirements.txt; 
    pip install -r requirements.txt

5. execute o comando para rodar o projeto no terminal;
    flask run



## Tecnologias utilizadas 

- Flask - Framework python para desenvolvimento de Aplicações.
- Flask-RESTful - framework para criação da APIs RESTful.
- SQLAlchemy - mapeamento objeto-relacional SQL 
- MySQL - banco de dados para armazenamento
- POSTMAN - Para teste e documentação da API


## Endpoints

O endpoint de conexão com a API REST JSON

é: [https://apiflaskvendas.up.railway.app/](https://apiflaskvendas.up.railway.app/)

Produtos: 
https://apiflaskvendas.up.railway.app//produtos 

categorias:
https://apiflaskvendas.up.railway.app//categorias 

Estoque: 
https://apiflaskvendas.up.railway.app//estoque 

Pessoas: 
https://apiflaskvendas.up.railway.app//pessoas

perfis: 
https://apiflaskvendas.up.railway.app//perfis


## Recursos disponíveis

Atualmente existem os seguintes recursos abaixo que você pode manipular através dos métodos GET, POST, PUT e DELETE:

- Pessoas(customers)
- Perfis (customers)
- Produtos (product)
- Categorias (category)
    

StartFragment

## Tratamento de dados

Todos os dados enviados e recebidos pela API estão/deverão ser em formato JSON (application/json).

StartFragment

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request com melhorias, correções de bugs ou novas funcionalidades.


## Autenticação

Para poder trabalhar com todos os métodos disponíveis você precisa estar logado no sistema como cliente ou como úsuario e fornercer o seu access_token para cadastras produtos, categorias e perfis.

Primeiro faça o cadastro de uma pessoa no sistema informando nome, email, senha, type(cliente ou usuario)

Em posse de Email e _Senha_ você precisará fazer o login e gerar o seu access_token no Header.

Exemplo: `Authorization: Bearer seu access_token`

O resultado que você deverá enviar no HEADER de todas as requisições será semelhante a: `Authorization: Bearer d2JfdXN1YXJpbzp3Yl9zZW5oYQ`O mesmo processo deve ser feito para efetuar o Logout do sistema.

Qualquer dúvida que surgir durante a implantação, entre em contato através do e-mail [thiago.ndev@gmail.com]()

Suas sugestoes e feedbacks de melhorias são muito importante para o min se possivel deixe seu feedback, Obrigado.
