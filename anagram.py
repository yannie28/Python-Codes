#Arianne Tan
# assume that two empty strings are not anagrams;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent

#O(n^2) in worst time since the ave cost of finding an element in a list is O(n)
#can be improved using hash tables
def anagram(message1, message2):
    answer = False

    if len(message1) == len(message2) and message1 and message2: #check if the 2 strings are equal in length and is not empty
        message1 = message1.replace(" ", "").lower() #change to lowercase and remove spaces
        message2 = list(message2.replace(" ", "").lower()) #change to list, lowercase and remove spaces
        for i in message1: #traverse message1
            if i in message2: #if element in message1 found in message2
                del message2[message2.index(i)] #del the element found in message2

        if not message2: #if message2 is empty...
            answer = True #return True

    return answer #return False

print(anagram("", ""))