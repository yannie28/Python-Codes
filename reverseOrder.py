#Arianne Tan
#printing myList in reverse order

myList = [10, 1, 8, 3, 5]
length = len(myList)

for i in range(length // 2):
    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]

print(myList)

#alternative solution
for i in range(length // 2):
    myList[i], myList[i-(2*i+1)] = myList[i-(2*i+1)], myList[i]

print(myList)
