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

operation = args[0]
while True:
    if operation == "new":
        try:
            arg_title = args[1].title
        except IndexError:
            arg_title = input("Please write the title: ")
            
        # if len(args) != 2:
        #     print("invalid used")
        #     print(f"Please you need specify one title")
        #     print("e.x: python alenotes.py new 'title'")
        #     sys.exit(1)
        
        # TODO: I need include exceptions
        # title = args[1]
        text = [
            f"{arg_title}",
            input("tag: ").strip(),
            input("note:\n").strip(),
        ]
        # \t - tsv
        with open(filepath, "a") as file_:
            file_.write("\t".join(text) + "\n")

    if operation == "read":
        try:
            arg_tag = args[1].lower()
        except IndexError:
            arg_tag = input("Please write what tags you want see?: ").lower()

        # if len(args) != 2:
        #     print("invalid used")
        #     print(f"Please you need specify one tag")
        #     print("e.x: python alenotes.py new minhatag")
        #     sys.exit(1)
        
        for line in open(filepath):
            title, tag, text = line.split("\t")
            if tag.lower() == arg_tag:
                print(f"{tag} | {title}")
                print(f"{text}")
                print(":" * 50)
                print()

    answer = input(f"Wish continue the {operation} ? [N/y]").strip().lower()
    if answer != "y":
        break
