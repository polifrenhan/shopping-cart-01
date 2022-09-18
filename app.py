from fastapi import FastAPI #, APIRouter, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
from models import Address, User, Product, ShoppingCart
from typing import List, Dict

app = FastAPI()

user_dict = {}
product_dict = {}

@app.get("/")
async def welcome():
    return "Bem vindos. Esta é a página inicial do meu primeiro carrinho de compras feito utilizando o framework FastAPI!"

@app.post("/user/")
async def create_user(user: User):
    if user.document in user_dict:
        return "User already registered."

    if "@" not in user.email:
        return "Invalid e-mail."

    if len(user.password) < 8:
        return "Invalid password"

    user_dict[user.document] = user
    return user_dict

@app.get("/user/document/{document}")
async def return_user_by_document(document: str):
    if document in user_dict:
        return user_dict[document]

    return "User not found."

@app.get("/user/name/{name_search}")
async def return_user_by_name(name_search: str):
    user_name_list = []

    for user_document in user_dict:
        if name_search in user_dict[user_document].name:
             user_name_list.append(user_dict[user_document])

    if len(user_name_list) > 0:
        return user_name_list
    
    return "User not found."

@app.delete("/user/{document}")
async def delete_user(document: str):
    if document in user_dict:
        user_dict.pop(document)
        return f"User {document} excluded."

    return "User not found."

@app.post("/user/{document}/address/")
async def create_address(document: str, address: Address):
    if document not in user_dict:
        return "User not found."
    user = user_dict[document]

    for i in user.addresses:
        if address.id == i.id:
            return "Address already exists."
    
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
            return user
    
    return "Address ID not found."

@app.delete("/user/{document}/address/")
async def delete_addresses(document: str):
    if document not in user_dict:
        return "User not found."

    user = user_dict[document]
    user.addresses = []
    return user

@app.post("/product/")
async def create_product(product: Product):
    if product.id in product_dict:
        return "Product already registered."

    product_dict[product.id] = product
    return product_dict

@app.get("/product/id/{id}")
async def return_product_by_id(id: str):
    if id in product_dict:
        return product_dict[id]

    return "Product not found."

# Função incompleta
@app.delete("/product/{id}")
async def delete_product(id: str):
    if id in product_dict:
        product_dict.pop(id)
        return f"Product {id} excluded."

    return "Product not found."
# Função incompleta

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
    user.shopping_cart.price_debit = (user.shopping_cart.price_credit)*0.9
    user.shopping_cart.number_of_items += 1

    return user.shopping_cart.products

# Função incompleta
@app.delete("/user/{document}/cart/product/{search}")
async def remove_product_from_cart(document: str, search: str):
    if document not in user_dict:
        return "User not found."

    if search not in product_dict:
        return "Product not found."

    user = user_dict[document]

    for cart_item in user.shopping_cart.products:
        if cart_item.id == search:
            user.shopping_cart.products.remove(cart_item)
            # adicionar atualização das variaveis price_debit, price_credit e number_of_items

    return user.shopping_cart.products
# Função incompleta

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
