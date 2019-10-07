#Arianne Tan
#creating a user defined method for split()
def mySplit(strings, separator=" "):
    
    lists = []
    temp = ""

    for i in range(len(strings)):
        if not isSeparator(strings[i], separator):
            temp += strings[i]
            if i == len(strings) - 1 and temp:
                lists.append(temp)
        elif temp:
            lists.append(temp)
            temp = ""

    return lists

def isSeparator(strings, separator):
    if separator == " ":
        return strings.isspace()
    else:
        return strings == separator

print(mySplit("To be or not to be, that is the question"))

