#!/usr/bin/env python3
"""List pair number in range of 1...200

ex. 
`python3 num_pair.py`
2
4
...
200
"""
# op 1
for number in range(2,21, 2):
    print(number)

# op 2
for number in range(1,21):
    if number % 2 != 0:
        continue
    print(number)
