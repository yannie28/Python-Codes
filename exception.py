#EXCEPTIONS
#ZeroDivisionError -> number divide by zero, 
#IndexError -> index non existing
#KeyError -> key non existing
#ValueError -> correct type but incorrect value, ex. int(String) - input 'dog' - correct String type but erroneous value, empty value
#AssertionError -> uses the assert keyword
#TypeError -> data type error, assignment operator in tuple, expects an integer but enters a string
#NameError -> if the variable is not defined


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