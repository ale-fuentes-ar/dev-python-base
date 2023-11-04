#!/usr/bin/env python3
"""add products"""
__version__ = "0.1.0"
__author__ = "alefuentes"

# import pprint
# from pprint import pprint

product = {
    "name": "some product",
    "cor": [],
    "price": 3.76,
    "size": {
        "height": 10,
        "width": 2,
    },
    "has_stock": True,
    "Code": 24251,
    "BarCode": None,  
}

customer = {
    "name": "alefuentes"
}

shopping_cart = {
    "customer":  customer,
    "product": product,
    "quantity": 3 
}

# current_buy = ("Alefuentes", product["name"], 3)
total_value = shopping_cart["quantity"] * shopping_cart["product"]["price"]

# pprint.pprint(shopping_cart)
# pprint(shopping_cart)
print()
print(
    f"The client {shopping_cart['customer']['name']}"
    f" bought {shopping_cart['quantity']} "
    f" of '{shopping_cart['product']['name']}' and pay u$ {total_value}"
)
