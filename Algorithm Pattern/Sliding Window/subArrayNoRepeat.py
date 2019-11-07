#Arianne Tan
# Given a string, find the length of the longest substring which has no repeating characters.

# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".

#O(n) running time
#O(k) space complexity
def noRepeatingChar(s):
    frequency = {}
    maximumLength = 0
    start = 0

    for i in range(len(s)):
        if s[i] not in frequency:
            frequency[s[i]] = i
        else:
            value = frequency[s[i]]
            while start <= value:
                del frequency[s[start]]
                start += 1
            frequency[s[start]] = i
        
        maximumLength = max(maximumLength, i - start + 1)
    
    return maximumLength

print("Maximum Length of No Repeating Character",noRepeatingChar('aabccbbfghaba'))