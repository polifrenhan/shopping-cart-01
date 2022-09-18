# projeto-carrinho-01
**Olá**, amigos de todos os cantos do **mundo**!!
Este código é a resolução de uma proposta de projeto do Bootcamp LuizaCode do Magazine Luiza que estou participando. No meu projeto eu decidi alterar um pouco os requerimentos do exercício original, adicionando algumas funcionalidades extras e alterando outros para se adequarem melhor às regras de negócio do meu projeto, mas de modo geral as funcionalidades são bem similares.
Eu estou criando "carrinho de compras" de e-commerce utilizando FastAPI. Estou usando uma tematica nada converncional que é World of Warcraft **#forthehorde**, onde os usuários são personagens do jogo e os produtos são itens do jogo. Nesta etapa inicial do projeto ainda não fiz nenhuma conexão com o banco de dados, o armazenamento é feito em memória, usando dicionarios. Os cadastros são feitos no "banco" via requisições (estou usando a RestClient pra me ajudar nisso). Todas as requisições estão no arquivo "requests.http" e todos os dados cadastrados por elas estão no arquivo "db.txt". A API possui as seguintes funcionalidades:


- Ter na página raiz uma saudação de boas vindas;


- Cadastrar usuários com código identificador único, nome, e-mail, senha, forma de pagamento, carrinho de compras e uma lista de endereços;
- Consultar usuários pelo código identificador;
- Consultar usuários por nome;
- Remover usuários pelo código identificador;


- Cadastrar endereço(s) do usuário;
- Consultar endereços do usuário pelo código identificador do usuário;
- Consultar endereços do usuário pelo código identificador do usuário e id do endereço;
- Remover endereço do usuário pelos códigos identificadores do usuário e do endereço;
- Remover todos os endereços de um usuário;


- Cadastrar produtos com nome, descrição, preço e um código identificador único;
- Consultar produtos pelo código identificador;
- Remover produtos pelo código identificador;


- Adicionar produtos ao carrinho de compras;
- Remover todos os produtos de mesmo código do carrinho de compras pelo codigo identificador do produto; (falta implementar)
- Remover todos os produtos do carrinho de compras; (falta implementar)
- Remover todos os itens do carrinho de compras; (falta implementar)
- Calcular os valores totais (a vista e a prazo) do carrinho. (falta implementar)
