#Arianne Tan
# 1st Solution
# def product(numbers):
#     product = 1
#     for i in numbers:
#         product *= i
#     return product

# 2nd Solution
given = [1,2,3,4,5]
after = []
product = 1
for i in range(1,len(given)+1):
    after.insert(0,product)
    product*=given[-i]

answer = []
before = 1
for i in range(len(given)):
    if len(given) == 1:
        answer.append(given[0])
    elif i == len(given)-1:
        answer.append(before)
    else:
        answer.append(before*after[i])
        #answer.append(before*product(given[i+1:]))
        before *= given[i]

print(answer)