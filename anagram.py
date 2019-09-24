# assume that two empty strings are not anagrams;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent

def anagram(message1, message2):
    answer = False

    if len(message1) == len(message2) and message1 and message2:
        message1 = message1.replace(" ", "").lower()
        message2 = list(message2.replace(" ", "").lower())
        for i in message1:
            if i in message2:
                del message2[message2.index(i)]

        if not message2: 
            answer = True

    return answer

print(anagram("race car", "car race"))