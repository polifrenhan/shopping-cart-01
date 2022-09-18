from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    id: int
    street: str
    zipcode: str
    city: str
    state: str

class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float

class ShoppingCart(BaseModel):
    products: List[Product] = []
    price_debit: float = 0
    price_credit: float = 0
    number_of_items: int = 0

class User(BaseModel):
    document: str
    name: str
    email: str
    password: str
    addresses: List[Address] = []
    payment_method: str
    shopping_cart: ShoppingCart