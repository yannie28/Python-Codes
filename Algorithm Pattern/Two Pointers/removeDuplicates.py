#Arianne Tan
# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; 
# after removing the duplicates in-place return the new length of the array.

# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

def removeDuplicate(a):
    marker = 1
    for i in range(1,len(a)):
        if a[marker-1] != a[i]:
            a[marker] = a[i]
            marker += 1
    
    return marker

print("The length of the array with all unique character is",removeDuplicate([2, 3, 3, 3, 6, 9, 9]))
        