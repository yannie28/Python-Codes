import math

def isPrime(number):
    for i in range(2, math.floor(math.sqrt(number))+1):
        if number%i == 0:
            return False
    return True

print("Prime Numbers within 100")
for i in range(2,101):
    if isPrime(i):
        print(i, end=' ')