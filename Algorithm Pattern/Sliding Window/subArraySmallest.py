#Arianne Tan
# Given an array of positive numbers and a positive number ‘S’, 
# find the length of the smallest subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.


#O(n) running time
def subArraySmallest(array, s):
    start, total= 0, 0
    minimum = float('inf')
    subArray = []
    
    for end in range(len(array)):
        total += array[end]
        while total >= s:
            if (end - start + 1) < minimum:
                minimum = (end - start + 1)
                subArray = array[start:end+1]
            total -= array[start]
            start += 1
    if minimum == float('inf'):
        return "No subarray exists"
    else:
        return subArray

print(subArraySmallest([2, 1, 5, 2, 3, 2], 7))
