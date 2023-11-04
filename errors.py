#!/usr/bin/env python

import os
import sys

# EAFP - Easy to Ask Forgiveness than Permission
try:
    names = open('names.txt').readlines() # FileNotFoundError
    1 / 1 #  ZeroDivisionError
    print(names.append) # AttributeError
# except: # Bare Except
except FileNotFoundError:
    print("[ERROR] : File name.txt not found")
    sys.exit(1)
except ZeroDivisionError:
    print("[ERROR] : You cant divide by zero")
    sys.exit(1)
except AttributeError:
    print("[ERROR] : List doesn't have oranges")
    sys.exit(1)

try:
    print(names[2])
except:
    print("[ERROR] : Missing name in the list")
    sys.exit(1)
 
