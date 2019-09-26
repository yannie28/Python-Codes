#Arianne Tan

#bubble sort in increasing order
lists = [2,3,4,6,5]
flag = True
passes = 0
swap = 0

while flag:
    passes += 1
    flag = False
    for i in range(len(lists)-1):
        if lists[i] > lists[i+1]:
            flag = True
            swap += 1
            lists[i], lists[i+1] = lists[i+1], lists[i]
            
print("Increasing Order: ", lists)
print("No of passes: ", passes)
print("No of swaps: ", swap, end="\n\n")

#bubble sort in decreasing order
lists = [2,3,4,6,5]
flag = True
passes = 0
swap = 0

while flag:
    passes += 1
    flag = False
    for i in range(len(lists)-1):
        if lists[i] < lists[i+1]:
            flag = True
            swap += 1
            lists[i], lists[i+1] = lists[i+1], lists[i]
            
print("Decreasing Order: ", lists)
print("No of passes: ", passes)
print("No of swaps: ", swap)
