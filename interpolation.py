#!/usr/bin/bash
"""automated mail

"""
__version__ = "0.1.0"
__author__ = "ale fuentes"
__license__ = "Unlicense"

import sys
import os


arguments = sys.argv[1:]

if not arguments:
    print("Please write the name template file and customers file !")
    sys.exit(1)
if len(arguments) != 2:
    print("Please the some param missing!\n\ne.g.: interpolation.py file-customer file-template")
    sys.exit(1)

filecustomers = arguments[0]
filetemplate = arguments[1]

path = os.curdir
customerspath = os.path.join(path, filecustomers)
templatepath = os.path.join(path, filetemplate)

# customers = []
# for line in open(filecustomers):
#     # name, email = line.split(",")
#     # TODO: change for list comprehension
#     customers.append(line.split(","))
# 
# for name, email in customers:

for line in open(filecustomers):
    # TODO: change for send email function
    name, email = line.split(",")
    print(f"email {email}:\n")
    print(
        open(templatepath).read()
        %{
            "name": name,
            "product": "pen",
            "description": "Pen whit ecology ink",
            "link": "https://link.buy.world.com",
            "quantity": 13,
            "price": 3.2,
        } 
    )
    print(":" * 50)
