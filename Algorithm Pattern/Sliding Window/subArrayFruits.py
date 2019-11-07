#Arianne Tan
# Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. 
# The only restriction is that each basket can have only one type of fruit.
# You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, 
# i.e., you will stop when you have to pick from a third fruit type.
# Write a function to return the maximum number of fruits in both the baskets.

# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

#O(n) running time
#O(1) space complexity
def basketFruit(s):
    baskets = {}
    maximumLength = 0
    start = 0

    for i in range(len(s)):
        if s[i] not in baskets:
            baskets[s[i]] = 0
        baskets[s[i]] += 1

        while len(baskets) > 2:
            baskets[s[start]] -= 1
            if baskets[s[start]] == 0:
                del baskets[s[start]]
            start += 1
        
        maximumLength = max(maximumLength, i - start + 1)
    
    return maximumLength

print(basketFruit(['A', 'B', 'C', 'A', 'C']))