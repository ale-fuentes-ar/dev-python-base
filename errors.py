#!/usr/bin/env python

import os
import sys

# LBYL - Look Before You Leap
if os.path.exists('names.txt'):
    # names = ['ale', 'jandro', 'fuentes']
    input("...") # Race Condition
    names = open('names.txt').readlines()
else:
    print("[ERROR] : File name.txt not found")
    sys.exit(1)


if len(names) >= 4:
    print(names)
    print(len(names))
    print(names[3])
else:
    print("[ERROR] : Missing name in the list")
    sys.exit(1)
 
