from fastapi import FastAPI #, APIRouter, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
from models import Address, User, Product, ShoppingCart
from typing import List

app = FastAPI()

OK = "OK"
ERROR = "ERROR"

user_dict = {}
product_dict = {}
adress_dict = {}
cart_dict = {}

@app.get("/")
async def welcome():
    return "Bem vindos. Esta é a página inicial do meu primeiro carrinho de compras feito utilizando o framework FastAPI!"

@app.post("/user/")
async def create_user(user: User):
    if user.document in user_dict:
        return ERROR

    if "@" not in user.email:
        return ERROR

    if len(user.password) < 8:
        return ERROR

    user_dict[user.document] = user
    # return OK
    return user_dict

@app.get("/user/document/{document}")
async def return_user_by_document(document: str):
    if document in user_dict:
        return user_dict[document]

    return ERROR

#------------------------------------- ERRO NESTA
@app.get("/user/name/{name_search}")
async def return_user_by_name(name_search: str):
    user_name_list = []

    for user_document in user_dict:
        slice = user_dict[user_document]
        if name_search in slice["name"]:
            user_name_list.append(slice)

    if len(user_name_list) > 0:
        return user_name_list
    
    # return user_name_list
    return ERROR
#------------------------------------- ERRO NESTA

@app.delete("/user/{document}")
async def delete_user(document: str):
    if document in user_dict:
        user_dict.pop(document)
        return user_dict
        # return OK

    return ERROR
