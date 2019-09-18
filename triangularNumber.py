import math
#check if the positive number is a triangular number (Summation of i to n where i is 0) and output n (maximum height of the triangle)
#Input=0; Output=True
#Input=8; Output=False
#Input=10; Output=True

number = 11#given
print("Given number:",number,end="\n\n")

#Solution no 1
#Run time: O(n) or Linear
total = 0
i = 0
answer = "Not a Triangular Number"
while total<=number:
    if total == number:
        answer = "A Triangular Number"
    i+=1
    total+=i
print(answer)
print("Maximum height of the triangle:", i-1)
print("Excess of",number%(total-i),end="\n\n")

#Solution no 2
#Run time: O(sqrt(n)) or Square Root
#number = (n(n+1))/2
answer = "Not a Triangular Number"
n = (-1+math.sqrt(1+4*2*number))/2 #solving for n using quadratic formula
total = math.floor(n)*(math.floor(n)+1)//2
if math.floor(n) == n:
    answer = "A Triangular Number"
print(answer)
print("Maximum height of the triangle:", math.floor(n))
print("Excess of",number%total)
