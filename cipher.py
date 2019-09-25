#asks the user for one line of text to encrypt;
#asks the user for a shift value (an integer number from the range 1..25)
#prints out the encoded text.

def encrypt(message,shift):

    if shift > 25 or shift < 1:
        return 'Invalid shifting value. Please input 1..25'

    answer = ''
    for i in message:
        if i.isalpha():
            sum = ord(i) + shift
            print(ord(i))
            if sum >= 123:
                answer += chr(sum-122+96)
            elif sum >= 91 and ord(i) < 97:
                answer += chr(sum-90+64)
            else:
                answer += chr(sum)
        else:
            answer += i
    
    return answer

message = input("Enter your message: ")
try:
    shift = int(input("Enter shifting value: "))
    print("Encrypted message:", encrypt(message,shift))
except:
    print("Please input a valid number")



