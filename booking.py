#!/usr/bin/env python3
"""
"""
import sys
import logging

# Step 1 : get values from rooms
rooms = {}

try:
    for line in open("booking-rooms.txt"):
        code, name, price = line.strip().split(",")
        rooms[int(code)] = {
            "name": name,
            "price": float(price), # TODO: need change to Decimal
            "available": True,
        }
    
except FileNotFoundError:
    logging.error("The file 'booking-rooms.txt' not found")
    sys.exit(1)

# Step 2 : ask the user what rooms he want to use

for code, datas in rooms.items():
    name = datas["name"]
    price = datas["price"]
    available = "N" if not datas["available"] else "A"
    # available = datas["available"] and "A" or "N"

    # TODO: change point for virgula '.' -> ','
    print(f"{code} > {name} - $ {price:.2f} ({available})")
print(f"\n{'-' * 20}\nA : Available - N : Not available")

 
