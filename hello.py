#!/usr/bin/env python3
"""Hello World Multy-Languages
by alefu

This program see language of System, 
next use this language for to gretting.

Usage:

Environment var LANG has need configurated.

    export LANG=en_US.UTF-8

Execution

    python3 hello.py
    or
    ./hello.py
"""
# Dunder: definition var that start with tow underlines
# and finish with two underline
__version__ = "0.1.2"
__author__ = "Alejandro Fuentes"
__licence__ = "Unlicense"

# built-in
import os

# snake case: format of names vars and functions.
current_language = os.getenv("LANG", "en_US.utf8").split(".")[0]
print(current_language)


# I can to configure my LANG, ussing 'export LANG=<idiom>'
# I can eraser var LANG, ussing 'unset LANG'
# Time Complexity = O(n)
msg = "Gretting generic!"

if current_language == "en_US":
    msg = "Hello, World - variavel!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg)

# sets (Hash Table) - O(1) - constant
# dicts (Has Table)
msg_dict = {
    "en_US": "Hello, World!",
    "es_SP": "Hola, Mundo!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "fr_FR": "Ça va, Monde!",
}

print(msg_dict[current_language])

