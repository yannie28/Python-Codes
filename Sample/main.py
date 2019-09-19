# main.py

from module import __counter, suml, prodl

print(__counter)

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))