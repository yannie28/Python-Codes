#Arianne Tan
# assume that an empty string isn't a palindrome;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent;
# there are more than a few correct solutions - try to find more than one.

#1st Solution
# text = input("Enter text: ")

# text = text.replace(' ','')

# if len(text) > 1 and text.upper() == text[::-1].upper():
# 	print("It's a palindrome")
# else:
# 	print("It's not a palindrome")

#2nd Solution
def palindrome(message):
    message = message.replace(" ", "").lower()
    
    if not message:
        return "Not a Palindrome"

    j = -1
    for i in range(len(message)//2):
        if message[i] != message[j]:
            return "Not a Palindrome"
        j -= 1
    
    return "Palindrome"

print(palindrome("bbccc"))
