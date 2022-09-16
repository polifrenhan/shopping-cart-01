from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    street: str
    zipcode: str
    city: str
    estate: str

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float

class ShoppingCart(BaseModel):
    products: List[Product] = []
    price_debit: float
    price_credit: float
    number_of_items: int

class User(BaseModel):
    document: str
    name: str
    email: str
    password: str
    adresses: List[Address] = []
    payment_method: int
    shopping_cart: ShoppingCart