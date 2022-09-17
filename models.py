from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    id: int
    street: str
    zipcode: str
    city: str
    state: str

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
    addresses: List[Address] = []
    payment_method: str
    shopping_cart: ShoppingCart