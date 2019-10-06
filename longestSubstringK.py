def longestSubstringK(k, s):
    output = [[], (0,0), 0] #unique chars, indices, length of string(max)
    strings, lenStrings = [], [] #initialize the characters and length of the characters; ex. [a,b,a,b,a,b],[1,1,2,3,2,1] 
    start = 0 #starting pointer
    for x in s: #traverse the string
        if x in output[0] and x == strings[len(strings)-1]: #check if the character is already in output[0] and the last character in strings[], if yes...
            lenStrings[len(lenStrings)-1] += 1 #increment the frequency of that character by 1
        elif x in output[0]: #if already in output[0] but repeated within the substring (ex. aaaabbba - the a is repeated but still considered within the substring),
            strings.append(x) #append the char in strings[] and 
            lenStrings.append(1) #add a frequency of 1 (note: the index of each strings corresponds to the frequency in lenStrings)
        else:
            if len(output[0]) < k: #if still not in output[0] and there is still a room for distinct char
                output[0].append(x) #append the char to the output[0] (the output[0] controls the max number of distinct chars)
            else: #if there is no room for new character, the 'window' will be moved
                value = sum(lenStrings) #get the value of the lenStrings - this represents the current length of the substring
                if value > output[2]: #check if value is greater that the max length
                    output[2] = value #if yes, change the max to value
                    output[1] = (start, start+value) #this is the index of the substring
                    start = sum(lenStrings[:k]) #change the start of the new substring since there is a new character incoming
                del strings[:k] #delete the values from the left side of the strings and lenStrings so a new character can come in the 'window'
                del lenStrings[:k]
                output[0] = strings[:] #the output[0] which is the controller of distinct characters will copy the value of the strings
            strings.append(x) #append the character in the strings
            lenStrings.append(1) #add a value of 1 to it

    value = sum(lenStrings) #last sum for the last substring
    if value > output[2]: #if greater than max, change the output[]
        output[2] = value
        output[1] = (start, start+value)
    if len(output[0]) == k: #check if there is enough unique substring from output[0]
        return "Max substring is: " + s[output[1][0]:output[1][1]] + " with length " + str(output[2])
    else: #else, not enough substring
        return "Not enough substring"

print(longestSubstringK(2, "aaaacbbbddd"))
