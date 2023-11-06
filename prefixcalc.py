#!/usr/bin/env python
"""Prefix Calculator

function:
<operator> [n1] [n2]

Operators:
sum -> +
sub -> -
mul -> *
div -> /

Use
$ prefixcalc.py sum 5 2
7
$ prefixcalc.py mul 10 2
20
$ prefixcalc.py
operation: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"
__author__ = "alefuentes"
__licence__ = "Unlicence"

import os
import sys
from datetime import datetime

arguments = sys.argv[1:]
# set valid operators
operators = { "sum", "sub", "mul", "div" }

# Validation
if not arguments:
    operation = input(f"what operation (e.x. ${operators}): ")
    n1 = input("n1: ")
    n2 = input("n2: ")
    arguments = [operation, n1, n2]
if len(arguments) != 3:
    print(f"Invalid nums arguments\n\ne.g.:\npython prefixcalc.py sum 5 2")
    sys.exit(-1)

operation, *nums = arguments

if operation not in operators:
    print(f"Invalid operator, please select between:\n{operators}\n")
    sys.exit(1)

validated_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Invalid number, please select numbers with next digits:\n1 2 3 4 5 6 7 8 9 0 .\n")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

try:
    n1, n2 = validated_nums
except ValueError as e:
    print(f"[ERROR] {str(e)}")
    sys.exit(1)


if operation == "sum":
    result = n1 + n2    
if operation == "sub":
    result = n1 - n2
if operation == "mul":
    result = n1 * n2
if operation == "div":
    result = n1 / n2


print(f"The result is {result}")

path = os.curdir
filepath = os.path.join(path, "prefixcalc.log") 
timestamp = datetime.now().isoformat()
user = os.getenv("USER", "anonymous")

try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} | {user} | The result of '{operation} {n1} {n2}' = {result}\n")
except PermissionError as e:
# TODO: logging
    print(f"[ERROR] {str(e)}")
    sys.exit(1)


# print(f"The result of '{operation} {n1} {n2}' = {result}", file=open(filepath, "a"))


# for arg in sys.argv[1:]:
#     if arg in operators:
#         print("Ok...")
#     else:
#         print(f"Invalid operator, please select between:\n{operators}")

