#check if the number is a triangular number (Summation of i to n where i is 0) and output n (maximum height of the triangle)
#Input=0; Output=True
#Input=8; Output=False
#Input=10; Output=True

number = 0#given

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
print("Maximum height of the triangle:", i)

