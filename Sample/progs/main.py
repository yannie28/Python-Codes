# main.py
from sys import path
path.append('A:\\GitHub\\Python-Codes\\Sample\\modules')

import module

print(module.__counter)

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))