from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from models import Address, User, Product, ShoppingCart

app = FastAPI()

user_dict = {}
product_dict = {}


@app.get("/", response_class=HTMLResponse)
async def welcome():
    html = """
    <ul>
        <li>
        <h2><span style="font-family:tahoma,geneva,sans-serif"><strong>Ol&aacute;</strong>,<span style="font-size: 12px"><em> amigos de todos os cantos do</em></span>&nbsp;<strong>mundo</strong>!&nbsp;<img alt="cool" height="23" src="https://clevert.com.br/lib/ckeditor/plugins/smiley/images/shades_smile.png" title="cool" width="23" /></span></h2>
        </li>
    </ul>

    <h4><span style="font-family:tahoma,geneva,sans-serif">Esta &eacute; minha primeira APIRest&nbsp;e&nbsp;foi desenvolvida com o framework FastApi. O projeto &eacute; uma proposta feita pelo&nbsp;Bootcamp LuizaCode do <em>Magazine Luiza</em> do qual estou participando. Decidi usar&nbsp;uma tematica nada convencional que &eacute; World of Warcraft (<strong>#forthehorde</strong>) onde os usu&aacute;rios s&atilde;o personagens do jogo e os produtos s&atilde;o itens do jogo. Divirtam-se!&nbsp;<img alt="laugh" height="23" src="https://clevert.com.br/lib/ckeditor/plugins/smiley/images/teeth_smile.png" title="laugh" width="23" /></span></h4>

    <p>&nbsp;</p>

    <ul>
        <li>
        <h2><span style="font-family:tahoma,geneva,sans-serif"><strong>Hello</strong>,<span style="font-size: 12px"><em> friends from all over the</em></span>&nbsp;<strong>world</strong>!&nbsp;<img alt="cool" height="23" src="https://clevert.com.br/lib/ckeditor/plugins/smiley/images/shades_smile.png" title="cool" width="23" /></span></h2>
        </li>
    </ul>

    <h4><span style="font-family:tahoma,geneva,sans-serif">This is my first APIRest and it was developed with the FastApi framework. The project is a proposal made by Bootcamp LuizaCode from <em>Magazine Luiza</em> in which I am participating. I decided to use an unconventional theme that is World of Warcraft <strong>(#forthehorde</strong>) where users are game characters and products are game items. Have fun!&nbsp;<img alt="laugh" height="23" src="https://clevert.com.br/lib/ckeditor/plugins/smiley/images/teeth_smile.png" title="laugh" width="23" /></span></h4>

    <p>&nbsp;</p>
    """

    return html


@app.post("/user/")
async def create_user(user: User):
    if user.document in user_dict:
        return "A user is already registered with the the given document number."
    user_dict[user.document] = user
    return user_dict


@app.get("/user/document/{document}")
async def return_user_by_document(document: str):
    if document in user_dict:
        return user_dict[document]

    return "User not found."


@app.get("/user/name/{search}")
async def return_user_by_name(search: str):
    user_name_list = []

    for user in user_dict:
        if search.lower() in user_dict[user].name.lower():
            user_name_list.append(user_dict[user])

    if len(user_name_list) > 0:
        return user_name_list

    return "No user names match your search."


@app.delete("/user/{document}")
async def delete_user(document: str):
    if document in user_dict:
        user_dict.pop(document)
        return f"User {document} removed from database."

    return "User not found."


@app.post("/user/{document}/address/")
async def create_address(document: str, address: Address):
    if document not in user_dict:
        return "User not found."
    user = user_dict[document]

    for i in user.addresses:
        if address.id == i.id:
            return (
                "An address for this user is already registered with the the given id."
            )

    user.addresses.append(address)
    return user


@app.get("/user/{document}/address/")
async def return_user_addresses(document: str):
    if document in user_dict:
        user = user_dict[document]
        return user.addresses

    return "User not found."


@app.get("/user/{document}/address/{address_id}")
async def return_user_addresses_by_id(document: str, address_id: int):
    if document in user_dict:
        user = user_dict[document]
        for address in user.addresses:
            if address_id == address.id:
                return address

        return "Address ID not found."

    return "User not found."


@app.delete("/user/{document}/address/{address_id}")
async def delete_address_by_id(document: str, address_id: int):
    if document not in user_dict:
        return "User not found."

    user = user_dict[document]
    for address in user.addresses:
        if address_id == address.id:
            user.addresses.remove(address)
            return f"Address {address_id} removed from user addresses"

    return "Address ID not found."


@app.delete("/user/{document}/address/")
async def delete_addresses(document: str):
    if document not in user_dict:
        return "User not found."

    user = user_dict[document]
    user.addresses[:] = []
    return user


@app.post("/product/")
async def create_product(product: Product):
    if product.id in product_dict:
        return "A product is already registered with the the given id."

    product_dict[product.id] = product
    return product_dict


@app.get("/product/id/{id}")
async def return_product_by_id(id: str):
    if id in product_dict:
        return product_dict[id]

    return "Product not found."


@app.post("/user/{document}/cart/product/{id_product}")
async def add_product_to_cart(document: str, id_product: str):
    if document not in user_dict:
        return "User not found."

    if id_product not in product_dict:
        return "Product not found."

    user = user_dict[document]
    product = product_dict[id_product]

    user.shopping_cart.products.append(product)
    user.shopping_cart.price_credit += product.price
    user.shopping_cart.price_debit = (user.shopping_cart.price_credit) * 0.9
    user.shopping_cart.number_of_items += 1

    return user.shopping_cart.products


@app.delete("/user/{document}/cart/product/{search}")
async def remove_product_from_cart(document: str, search: str):
    if document not in user_dict:
        return "User not found."

    if search not in product_dict:
        return "Product not found."

    user = user_dict[document]
    index = 0
    while index < len(user.shopping_cart.products):
        if user.shopping_cart.products[index].id == search:
            user.shopping_cart.price_credit -= user.shopping_cart.products[index].price
            user.shopping_cart.price_debit = (user.shopping_cart.price_credit) * 0.9
            user.shopping_cart.number_of_items -= 1
            user.shopping_cart.products.remove(user.shopping_cart.products[index])
            index -= 1
        index += 1
    return f"All products {search} were excluded from cart."


@app.delete("/user/{document}/cart/")
async def clear_cart(document: str):
    if document not in user_dict:
        return "User not found."

    user = user_dict[document]
    user.shopping_cart.products[:] = []
    user.shopping_cart.price_credit = 0
    user.shopping_cart.price_debit = 0
    user.shopping_cart.number_of_items = 0
    return f"All products were excluded from user cart."


@app.delete("/product/{search}")
async def delete_product(search: str):
    if search in product_dict:
        for user in user_dict:
            await remove_product_from_cart(user, search)

        product_dict.pop(search)
        return f"Product {search} removed from database."

    return "Product not found."


@app.get("/user/{document}/cart")
async def cart_total(document: str):
    if document not in user_dict:
        return "User not found."

    user = user_dict[document]
    credit = user.shopping_cart.price_credit
    debit = user.shopping_cart.price_debit
    items = user.shopping_cart.number_of_items

    msg = f"Your cart has {items} item(s). The total cost of the products is {credit}. Pay with credit card or get 10% discount and pay only {debit} on debit."
    return msg
