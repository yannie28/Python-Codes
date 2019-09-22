# module.py

#!/usr/bin/env python3 

#This is a doc string. The above comment is caled shabang or hashpling
""" module.py - an example of Python module """

__counter = 0

def suml(list):
	global __counter
	__counter += 1
	sum = 0
	for el in list:
		sum += el
	return sum

def prodl(list):
	global __counter	
	__counter += 1
	prod = 1
	for el in list:
		prod *= el
	return prod

if __name__ == "__main__": #test the function if working; will be ommitted when the code is imported
    print("I prefer to be a module, but I can do some tests for you")
    l = [i+1 for i in range(5)]
    print(l)
    print(suml(l) == 15)
    print(prodl(l) == 120)