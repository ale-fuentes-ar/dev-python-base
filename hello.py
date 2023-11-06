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
__version__ = "0.1.3"
__author__ = "Alejandro Fuentes"
__licence__ = "Unlicense"

# built-in
import os
import sys
import logging

# TODO: convert setting logs in a function
# TODO: use lib, example 'logguru'
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("ale", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)



# print(f"{sys.argv=}")
args = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You need to use `=` You passed %s. Try with --key=value e.x: --lang=es_SP: %s",
            arg,
            str(e)
        )
        sys.exit(1)

    # LBYL
    key = key.lstrip("-").strip()
    value = value.strip()
      
    if key not in args:
        print(f"Invalid Option '{key}'")
        sys.exit()

    args[key] = value

# snake case: format of names vars and functions.
current_language = args["lang"]
print(f"{current_language=}")
if current_language is None:
     # TODO: to use loop
    if "LANG" in os.environ:
        current_language =  os.getenv("LANG")
    else:
        current_language = input(
            "Choose a language please: "
        )

# current_language = current_language.split(".")[0]
current_language = current_language[:5]

# I can to configure my LANG, ussing 'export LANG=<idiom>'
# I can eraser var LANG, ussing 'unset LANG'
# Time Complexity = O(n)
# msg = "Gretting generic!"
# 
# if current_language == "en_US":
#     msg = "Hello, World - variavel!"
# elif current_language == "it_IT":
#     msg = "Ciao, Mondo!"
# 
# print(msg)

# sets (Hash Table) - O(1) - constant
# dicts (Has Table)
msg_dict = {
    "en_US": "Hello, World!",
    "es_SP": "Hola, Mundo!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "fr_FR": "Ça va, Monde!",
}


"""
# try with default value
message = msg_dict.get(current_language, msg_dict["en_US"]) 
"""

"""
# LBYL
if current_language in msg_dict:
    message = msg_dict[current_language]
else:
    print(f"Lenguage not found.\nValid languages {list(msg_dict.keys())}")
    sys.exit(1)
"""

# EAFP
try:
    message = msg_dict[current_language]
except KeyError as e:
    log.error(
        "Lenguage not found.\nValid languages %s : %s",
        list(msg_dict.keys()),
        str(e)
    )
    sys.exit(1)

print(f"{message}\n" * int(args["count"]))
