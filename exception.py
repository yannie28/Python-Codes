#EXCEPTIONS
#ZeroDivisionError -> number divide by zero, 
#IndexError -> index non existing, 
#ValueError -> expects an integer but enters a string or something similar, 
#AssertionError -> uses the assert keyword

def readint(prompt, min, max):
    
    while True:
        try:
            number = int(input(prompt))
            assert number <= 10 and number >= -10
            break
        except AssertionError:
            print("Error the value is not within permitted range (-10..10)")
        except ValueError:
            print("Error: wrong input")
    return number

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)