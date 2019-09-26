#Arianne Tan
#this program returns the corresponding number of day given the year, month, day
#input: function(2000,12,31); output: 366
#input: function(2019,1,1); output: 1

def isLeapYear(year): #check if leap year
    if year%4 != 0:
        return False
    elif year%100 != 0:
        return True
    elif year%400 != 0:
        return False
    else:
        return True

def daysInMonth(year,month): #return no of days in a month
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year >= 1582 and month < 13 and month > 0: #check if the year and month is valid
        if isLeapYear(year):
            days[1] = 29 #changing no of days of february
        return days[month-1]

#1st solution using daysInMonth()
# def dayCalendar(year,month,day):
#     expectedDays = daysInMonth(year, month)
#     total = 0
#     if expectedDays and expectedDays >= day and day > 0: #check if the day is valid and expectedDays is not empty
#         for i in range(month):
#             total += daysInMonth(year,i+1) #summation of no of days but with excess of the no of days of the given month
#         return total-expectedDays%day #less the excess


#2nd solution
def dayCalendar(year,month,day):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year >= 1582 and month < 13 and month > 0 and day > 0 and day < 32: #check validity of the input
        if isLeapYear(year):
            days[1] = 29 #changing no of days of february
        return sum(days[:month]) - days[month-1]%day

print(dayCalendar(2012,3,28))
