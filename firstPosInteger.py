#Arianne Tan
# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.

#Solution 1
#O(nlogn) - running time because of some maximum sorting algorithm
def firstPos(given):
    given.sort()
    min = 0
    for i in given: #traverse the given list
        if i == min+1: #check if the element is equal to the min, if yes...
            min += 1 #the minimum number will increment by 1, otherwise just continue

    return min+1

#Solution 2
#O(n) - running time
#O(1) - space
def firstPos2(given):
    counter = 0 #counting number of positive numbers
    for i in range(len(given)): #traverse the given list
        if given[i] > 0: #check if element is greater than 0, if yes...
            given[counter] = given[i] #place the element to the index of counter so that all the positive numbers will be at the left side of the list
            counter += 1 #increment counter
    
    del given[counter:] #delete all negative and zeroes | all the elements to the right of the counter

    for i in given: #traverse the list
        x = abs(i) #get the absolute value of the element
        if x <= len(given) and given[x-1] > 0: #check if the element is greater than or equal to the length of list, if yes...
            given[x-1] = -given[x-1] #change the value of the element with index x to negative, to mark the index x that the positive element is found
    
    for i in given: #traverse the list
        if i > 0: #check the first positive number in the list
            return given.index(i)+1 #return the first missing positive integer

    return len(given)+1 #len plus 1 because of index 0
    
print(firstPos2([0,0,0,3,2,1,8,9,5,10,4,-1,6,7]))