#this program checks if the number is Prime or not
#used theorem: if both a and b is greater than the square root of n, then a*b is greater than n
#hence, there should be one factor that is less than the square root of n

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