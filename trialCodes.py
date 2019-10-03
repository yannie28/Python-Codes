# l1 = ["A", "B", "C"]
# l2 = l1
# l3 = l2

# del l1[0]
# del l2[:]

# print(l3)

#board[day][time]
# temp = [[i+1 for i in range(3)] for j in range(3)]
# print(temp)

# for day in temp:
#     print(day[1])

# list = [0,1,2,3]
# for i in range(-1,0):
#     print(list[i])

# list = [1,2,3]
# for v in range(3):
#     list.insert(1,list[v])
# print(list)

# for c in range(5):
#     print(c)

# for i in range(1):
#     print("#")
# else:
#     print("#")
# list = [1,1,1,1]
# lists = list[:]

# print(print(5))
# def myFunction():
#     var = 2
#     global var

#     print("Do I know that variable?", var)

# var = 1
# myFunction()
# print(var)

# a="asdasd"
# print(a[0]) #output: a

# a = [1,2,3]
# b = a
# del a[0]

# print(b)

# dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# b = dict
# del b['a']
# print(dict)
# tuples = (5,4,3,2,1)
# del tuples
# print(tuples)
# for i in dict:
#     print(dict[i] + (1,))

# for i in dict.items():
#   print(i[1])
# dict['f'] = 7
# dict.update({'f': 6})
# print(dict)
# print(dict.popitem())
# print(dict)

#print(sorted(dict, reverse=True))

# for i in tuples:
#     print(i+1)

#schoolClass = {}

# while True:
#     name = input("Enter the student's name (or type exit to stop): ")
#     if name == 'exit':
#         break
    
#     score = int(input("Enter the student's score (0-10): "))
    
#     if name in schoolClass:
#         print(schoolClass[name])
#         schoolClass[name] += [score]
#     else:
#         schoolClass[name] = [score]

# print(schoolClass)
# for name in sorted(schoolClass.keys()):
#     sum = 0
#     counter = 0
#     for score in schoolClass[name]:
#         sum += score
#         counter += 1
#     print(name, ":", sum / counter)

# d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
# d2 = {'Mary Louis':'A', 'Patrick White':'C'}
# d3 = {}

# for item in (d1, d2):
#     d3.update(item)

# print(d3)
# print((d1,d2))

# colors = {
#     "white" : (255, 255, 255),
#     "grey"  : (128, 128, 128),
#     "red"   : (255, 0, 0),
#     "green" : (0, 128, 0)
#     }

# for col, rgb in colors.items():
#     print(col, ":", rgb)

# def fun(a=1,b=4):
#     return a*b

# print(fun(3))

# def fun(in=2, out=3):
#     return in * out

# from random import randrange

# for i in range(1):
#     print(randrange(1, 10))

# boards = {1: (0,0), 2: (0,1), 3: (0,2),
#               4: (1,0), 5: (1,1), 6: (1,2),
#               7: (2,0), 8: (2,1), 9: (2,2)}

# print(boards[9][1])

# a = []

# def b():
#     a.append(1)

# b()
# print(a)

# a,b,c = 0,1,2
# print(a,b,c)
# def a():
#     global avail
#     avail = 'hahahaha'

# avail = ['asdasdasd']
# a()
# print(avail)
# if True and avail:
#     print(True)
# else:
#     print(False)

import math
#sin(x),cos(x),tan(x),sinh(x),cosh(x),tanh(x),asinh(x),acosh(x),atanh(x) -> accepts rad instead of degree rad = degree*pi/180
#asin(x),acos(x),atan(x) -> returns a rad
#pi, radians(x), degrees(x)
# e, log(x) -> base e, log(x,b) -> log of x base b, log10(x) -> base 10, log2(x) -> base 2, exp(x) -> e raise to x
#floor(x) -> round down, ceil(x) -> round up, trunc(x) -> removes the decimal place, hypot(x,y), factorial(x)

import random
#random(x) -> [0.0 - 1.0), randrange(x,y,z) -> x = beg; y = stop-1; z = increment
#randint(x,y) -> [x - y]
#choice(x) -> selects from the x list
#sample(x, y) -> selects from the x list with y no of elements
#seed() -> pseudonumber * based on time
#seed(x) -> pseudonumber * integer x

import platform
#platform(alias=True|False,terse=True|False) -> describe the environment
#machine() and processor() -> describe the processor
#system() -> describe the OS
#version() -> describe the version of the OS
#python_implementation() -> returns type of python
#python_version_tuple() -> returns version of python

# print("a", "b", "c", sep="sep")

# tup = (0,1)
# tup = tup[0] + tup[1]

# print("The number is:", v)
# b = "a".center(6) == "  a   "
# print(b)

#Common Functions
#int("Data Type") -> converts to int
#str("Data Type") -> converts to string
#float("Data Type") -> converts to float
#list("Data Type") -> converts to list
#dict("Data Type") -> converts to dict
#tuple("Data Type") -> converts to tuple
#pow(x,y) -> x raise to y
#sum("Iterable of numbers", start=0) -> returns the sum + start
#min("Iterable of numbers" and a string) -> returns the minimum element
#max("Iterable of numbers" and a string) -> returns the maximum element
#ord("Character") -> returns the code point given a character
#chr("Code point") -> returns the corresponding character given a code point

#String common methods
#String.index("String"|Character) -> returns the position of the argument, not safe
#String.capitalize() -> returns a new "String" with the capitalized first character
#String.center(int,symbol) -> returns a new "String" - center the String by inserting the symbol at both ends of the String, 
# odd number will be inserted at the end
#String.endswitch("String") -> returns True|False if the "String" is found at the END of the String
#String.startswitch("String") -> returns True|False if the "String" is found at the START of the String
#String.find("String"|Character, start, end-1) -> returns the position of the FIRST found argument from Start to End-1, 
# safe because it returns -1 if not found
#String.rfind("String"|Character, start, end-1) -> returns the position of the LAST found argument from Start to End-1, 
# safe because it returns -1 if not found
#String.isalnum() -> returns True|False if the String only has characters or digits (no symbols and spaces)
#String.isalpha() -> returns True|False if the String only has characters (no symbols, spaces, and digits)
#String.isdigit() -> returns True|False if the String only has digits (no symbols, spaces, and characters)
#String.islower() -> returns True|False if the String is in lowercase
#String.isupper() -> returns True|False if the String is in uppercase
#String.isspace() -> returns True|False if the String is a space
#String.join(List of "Strings") -> returns a new "String" which is the combined "Strings" from List with the String as the separator
#String.lower() -> returns a new "String" with all lowercase characters
#String.upper() -> returns a new "String" with all uppercase characters
#String.title() -> returns a new "String" with capitalized first letter of every word
#String.swapcase() -> returns a new "String" with swapped case - lower to upper and vice versa
#String.strip() | String.strip("String"|Character") -> returns a newly created string formed from the original one by 
# removing all LEADING and TRAILING whitespaces or given Character
#String.lstrip() | String.lstrip("String"|Character") -> returns a newly created string formed from the original one by 
# removing all LEADING whitespaces or given Character
#String.rstrip() | String.rstrip("String"|Character") -> returns a newly created string formed from the original one by 
# removing all TRAILING whitespaces or given Character
#String.replace("Source", "Replacement") -> returns a new String in which all occurrences of the first argument | "Source"
# have been replaced by the second argument | "Replacement"
#String.split("Separator" | Default = " ") -> returns a list with the splitted String - removes the "Separator"

#Object Oriented Programming - functions
#hasattr(Class | Object, String name) -> checks if the argument has the corresponding String attribute
#getattr(Class | Object, String name) -> gets the value of the String in the Class of Object
#setattr(Class | Object, String name, Value) -> sets the value of the attribute String from the Class | Object
#isinstance(Object, Data type|Class) -> returns True|False if the Object is a Data Type or an instance of a class
#issubclass(Class1, Class2) -> returns True|False if Class1 is a subclass of Class2
#type(Data) -> returns the Class or the data type of the Data

#Object Oriented Programming - pre-equipped attributes, constructor and methods
#class.__dict__ | obj.__dict__ -> returns the instance variables
#class.__name__ -> returns the name of the class
#class.__module__ | obj.__module__ -> returns the name of the module which contains the definition of the class
#class.__bases__ -> returns the tuple that contains classes (not class names) which are direct superclasses for that class.
#__init__(self): -> contructor
#__str__(): -> overriding this method in a class will return a value when the object is printed (print(obj))
# a=Class(); print(a)
#super() -> get the superclass

#Introspection vs Reflection
#Introspection - examine the properties and methods of the given class during runtime
#Reflection - manipulate the properties and methods of the given class during runtime

#Generators
#is an object that is an iterable that can be formed using the iterator protocol or the yield keyword
#x = (y for y in range(5)) <- generator object

#Lambda function
#an 'anonymous function' useful for function parameters; lambda parameter:expression
#map(function-lambda,iteratable objects) -> returns a generator object with the result of the function applied using the iterable objects
#filter(function-lambda, iterable objects) -> returns a generator object with the result of the function applied using the iterable objects
# provided the function returns True

#Closure
#a function object that remembers the values in an enclosing scope even if they are not present in memory
# def a(x):
#     def b(y):
#         return y*x #remembers the value of x even if x is deleted from memory
#     return b #return a closure function

# sample = a(1)
# print(sample(3))

avail = {1:1, 2:2}
def a(avail, length):
    if length == 0:
        return 1
    newavail = avail.copy()
    del newavail[1]
    print(newavail)
    a(newavail, length-1)

a(avail,2)