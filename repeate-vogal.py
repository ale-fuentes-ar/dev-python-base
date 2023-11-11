#!/usr/bin/env python3
"""Script that after wrote one sentence, print the same sentence
but wiht each vocal twice
"""

vogals = "AEIOUaeiou"
words = []
while True:

    phrase = input("You now try again [ENTER for exit] ? ").strip()
    
    if not phrase:
        break

    response = ""
    for char in phrase:
        response += char
        # TODO: use function to  extract accent
        if char in vogals:
            response += char

        # if ternario 
        # response += char * 2 if char in vogals else char

    words.append(response)

# use '*' for despack a list, dict, etc
print(*words, sep="\n")
