# shopping-cart-01

**Hello**, friends from all over the **world**!!
This code is the resolution of a Bootcamp LuizaCode project proposal by Magazine Luiza in which I am participating. I'm using an unconventional theme that is World of Warcraft (#forthehorde), where users are game characters and products are game items.
This is an e-commerce shopping cart made with the FastAPI framework. I'm not using any databases or files for storage, I'm using dictionaries. The entries are made in the "database" via requisitions. I made all of them using RestClient and the document with the complete listing of requests used by me is in the "requests.http" file. The API has the following features:


- Root page with an HTML message;


- Create users (document, name, email, password, payment method, shopping cart and a list of addresses);
- Find users by document;
- Find users by name;
- Remove users by document;


- Create user address(es) (id, street, zip code, city and state);
- Find user address by id;
- Find user address by user document and address id;
- Remove user address by user document and address id;
- Removes all addresses of a user;


- Create products (name, description, price and id);
- Find products by id;
- Remove products by id;


- Add products to the shopping cart;
- Removes all products with the same id from the shopping cart by id;
- Removes all items from the user's shopping cart;
- Calculates the total values (cash and term) of the cart.

## -----------------------------------------------------------------------------------

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
