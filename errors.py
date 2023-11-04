#!/usr/bin/env python

import os
import sys

# EAFP - Easy to Ask Forgiveness than Permission
try:
    raise RuntimeError("A error ocurred")
except Exception as e:
    print(str(e))


try:
    names = open('names.txt').readlines()
except FileNotFoundError as e:
    print(f"{str(e)}")
    sys.exit(1)
    # TODO: will use retry
else:
    print("Sucess !!!")
finally:
    print("Execute always...")
try:
    print(names[2])
except:
    print("[ERROR] : Missing name in the list")
    sys.exit(1)
 
