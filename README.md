# APIFLASK_VENDAS

StartFragment

## Endpoint

O endpoint de conexão com a API REST JSON

é: [https://apiflaskvendas-0ebff1c9ea31.herokuapp.com]()

StartFragment

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
