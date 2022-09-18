# projeto-carrinho-01
**Olá**, amigos de todos os cantos do **mundo**!!
Este código é a resolução de uma proposta de projeto do Bootcamp LuizaCode do Magazine Luiza do qual estou participando. Estou usando uma tematica nada convencional que é World of Warcraft **#forthehorde**, onde os usuários são personagens do jogo e os produtos são itens do jogo.
Este é um carrinho de compras de e-commerce feito com o framework FastAPI. Não estou usando nenhum banco de dados ou arquivos para armazenamento, estou usando dicionarios. Os cadastros são feitos no "banco de dados" via requisições. Fiz todas elas utilizando o RestClient e o documento com a listagem completa de requisições usadas por mim estão no arquivo "requests.http". A API possui as seguintes funcionalidades:


- Pagina raiz com uma mensagem em HTML;


- Cadastro de usuários (documento, nome, e-mail, senha, forma de pagamento, carrinho de compras e uma lista de endereços);
- Consulta usuários por documento;
- Consulta usuários por nome;
- Remove usuários por documento;


- Cadastra endereço(s) do usuário (id, rua, CEP, cidade e estado);
- Consulta endereço do usuário pelo id;
- Consulta endereço do usuário pelo documento do usuário e id do endereço;
- Remove endereço do usuário pelo documento do usuário e id do endereço;
- Remove todos os endereços de um usuário;


- Cadastra produtos (nome, descrição, preço e id);
- Consulta produtos pelo id;
- Remove produtos pelo id;


- Adiciona produtos ao carrinho de compras;
- Remove todos os produtos de mesmo id do carrinho de compras pelo id;
- Remove todos os itens do carrinho de compras do usuário;
- Calcula os valores totais (a vista e a prazo) do carrinho.
