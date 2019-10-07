#Arianne Tan

#find all the pair of numbers in the given list that when added is equal to the given sum

lists = [1,2,3,4,5] #given list
total = 8 #given sum

#1st Solution
#Run time - O(n^2) or Quadratic
pairs = []
if not lists:
    print("Empty list")
else:
    for i in range(len(lists)):
        for j in range(1,len(lists)):
            if lists[i] + lists[j] == total and lists[i] not in pairs:
                pairs.append(lists[i])
                pairs.append(lists[j])

    print(pairs)

#2nd Solution
#Run time - O(n^2) or Quadratic since the ave running time of finding an element in a list is O(n)
pairs = []
if not lists:
    print("Empty list")
else:
    for i in range(len(lists)):
        complement = total - lists[i]
        if complement in lists and lists[i] not in pairs:
            pairs.append(lists[i])
            pairs.append(complement)
    print(pairs)

#3rd Solution
#Run time - O(n^2) or Quadratic but much elegant looking than solution no 2
#should get a pair of number from different position or index
pairs = []
if not lists:
    print("Empty list")
else:
    for i in lists:
        complement = total - i
        if complement in lists and i not in pairs and lists.index(complement) != lists.index(i):
            pairs.append(i)
            pairs.append(complement)
    print(pairs)

#can be improved using hash tables