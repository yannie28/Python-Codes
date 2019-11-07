#Arianne Tan
# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]

def pairSum(a,target):
    start, end = 0, len(a)-1

    while start < end:
        if a[start] + a[end] == target:
            return [start, end]
        elif a[start] + a[end] > target:
            end -= 1
        else:
            start += 1
    return "There is no existing pair equal to " + str(target)

print(pairSum([1,2,3,9,6], 6))
    
            
