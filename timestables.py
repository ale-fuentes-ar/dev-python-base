#!/usr/bin/env python3
"""times tables
by alefuentes

show times tables between 1 and 10
----table of 1---
    1 * 1 = 1
    2 * 2 = 2
       ...
################
----table of 2---
    2 * 1 = 1
       ...
... on so on
"""
__version__ = "0.1.0"
__author__ = "Alejandro Fuentes"
__licence__ = "Unlicense"


numbers = list(range(1,11))

for n1 in numbers:
    iterations = ""

    print("{:-^25}".format(f"table times of {n1:02}"))
    print()
    for n2 in numbers:
        calculated = n1 * n2
        print("{:^25}".format(f"{n1} * {n2:02} = {calculated:3}"))
          
    print()
    print("#" * 25)
