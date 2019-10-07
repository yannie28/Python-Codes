#Arianne Tan
#Given an array, find the average of all subarrays of size ‘K’ in it
#Input: Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
#Output: Output: [2.2, 2.8, 2.4, 3.6, 2.8]

#1st solution
#O(n) running time using the sliding window algorithm

def subArrayAverage(array, k):
    total, start, windowSize = 0, 0, 0 #initialize the total, start, windowSize
    output = [] #this is the output result

    for i in array: #traverse the array
        windowSize += 1 #increment the windowSize to be included
        total += i #add the current value to the value
        if windowSize == k: #check if the windowSize is already equal to k
            output.append(total/k) #average the 5 elements and append it to the output result
            total -= array[start] #remove the start pointer from the total to be reused by other sub arrays
            windowSize -= 1 #since, the average is already computer, remove also the windowSize by 1 for other sub arrays
            start += 1 #move the start pointer by 1
    return output

print(subArrayAverage([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))


