#Arianne Tan
# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.

#Solution 1
#O(nlogn) - running time because of some maximum sorting algorithm running time
def firstPos(given):
    given.sort()
    min = 0
    for i in given: #traverse the given list
        if i == min+1: #check if the element is equal to the min, if yes...
            min += 1 #the minimum number will increment by 1, otherwise just continue
    
    if min == 0: #this is for the list with all numbers < 1
        return min+1 #return 1

    return min+1
    
print(firstPos([1,2,3]))