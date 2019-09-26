#Arianne Tan
#!/usr/bin/env python3 

'''This is a Stack implementation from scratch '''

class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val

    def getValues(self):
        return self.__stackList


if __name__ == "__main__":
    lists = Stack()
    lists = Stack()

    lists.push(3)
    lists.push(lists.pop())
    print(lists.getValues())