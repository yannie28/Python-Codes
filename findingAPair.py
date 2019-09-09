#Arianne Tan - 9/9/2019

#find all the pair of numbers in the given list that when added is equal to the given sum

lists = [1,2,3,4,5] #given list
total = 7 #given sum

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
#Run time - O(n) or Linear
pairs = []
complements = []
if not lists:
    print("Empty list")
else:
    for i in range(len(lists)):
        complement = total - lists[i]
        if complement in lists and lists[i] not in pairs:
            pairs.append(lists[i])
            pairs.append(complement)
    print(pairs)
