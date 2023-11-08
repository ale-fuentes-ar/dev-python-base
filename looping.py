#!/usr/bin/env python3
"""
"""

__author__ = "alefuentes"
__license__ = "Unlicense"


# NUMBER

# list use memory for each item
# numbers = [1, 2, 3, 4, 5, ]

# range use only three data in memory:
# start, next, stop
numbers = range(1, 5)
# print(numbers[0])
# print(numbers[-1])

# Iterable
# for number in numbers:
#     pair = number % 2 == 0
#     if pair:
#         print(number)
#     else:
#         continue
#     print(f"Hi number {number}...")

# # FILES
# 
# dados = {}
# 
# for line in open("post.txt"):
#     if line == "---\n":
#         break
#     key, value = line.split(":")
#     dados[key] = value.strip()
# 
# print(dados)

# Interative, Structuring Programing
# For loops 
origin_list = [1,2,3,4]
new_list = []
for nr in origin_list:
    new_list.append(nr * 2)

print(new_list)


# Funcional
# List Comprehension 
doubling = [n * 2 for n in origin_list]
print(doubling)

# Dict Comprehension
datas = {
    line.split(":")[0]: line.split(":")[1].strip()
    for line in open("post.txt")
    if ":" in line}
print(datas)


# While

ind = 0
while ind < 10:
    if ind % 2 == 0:
        ind += 1
        continue
    print(ind)
    ind += 1
