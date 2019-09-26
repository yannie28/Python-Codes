#Arianne Tan
#!/usr/bin/env python3 

'''This is an AddingStack overriding the Stack class - uses inheritance'''

from sys import path
path.append("A:\\GitHub\\Python-Codes\\Data Structure\\ds")

from Stack import Stack

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def getSum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

stackObject = AddingStack()

for i in range(5):
    stackObject.push(i)
print(stackObject.getSum())

for i in range(5):
    print(stackObject.pop())