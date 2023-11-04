#!/usr/bin/env python3
"""
"""
__version__ = "0.1.0"
__author__ = "ale fuentes"
__license__ = "Unlicense"

import os
import sys

actions = ("new", "read")
path = os.curdir
filepath = os.path.join(path, "note.txt")

args = sys.argv[1:]
if not args:
    print("invalid used")
    print(f"Please you need specify one this actions: {actions}")
    print("e.x: python alenotes.py new")
    sys.exit(1)

if args[0] not in actions:
    print(f"Invalid actions, please type one this actions: {actions}")
    sys.exit(1)

if args[0] == "new":
    if len(args) != 2:
        print("invalid used")
        print(f"Please you need specify one title")
        print("e.x: python alenotes.py new 'title'")
        sys.exit(1)
    
    # TODO: I need include exceptions
    title = args[1]
    text = [
        f"{title}",
        input("tag: ").strip(),
        input("note:\n").strip(),
    ]
    # \t - tsv
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")

if args[0] == "read":
    if len(args) != 2:
        print("invalid used")
        print(f"Please you need specify one tag")
        print("e.x: python alenotes.py new minhatag")
        sys.exit(1)
    
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == args[1].lower():
            print(f"{tag} | {title}")
            print(f"{text}")
            print(":" * 50)
            print()
