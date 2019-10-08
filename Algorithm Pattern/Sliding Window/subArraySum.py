#Arianne Tan
#Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
#array = [1,2,4,8,16], k = 3; output: 28
#array = [2,5,3,8], k = 2; output: 11

#1st solution
#O(n^2) running time
def sub(array, k):
    x = len(array)-k #no of sub arrays
    max = 0 #maximum no
    for i in range(0, x+1):
        sum = 0
        for j in range(0, k): #size k
            sum = sum + array[j+i] #add every element
            if max < sum: #check if sum is greater than the current max, if yes...
                max = sum # NOTE: change max to sum
    return max

print(sub([90,2,4,70], 3))

#2nd solution
#O(n) running time
def subArraySum(array, k):
    total, max, start = 0,0,0

    for i in range(len(array)):
        total += array[i]

        if i >= k-1:
            if total > max:
                max = total
            total -= array[start]
            start += 1
    
    return max

print(subArraySum([90,2,4,70], 3))




