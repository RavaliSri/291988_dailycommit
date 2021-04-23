year = int(input("Input a year: "))

if (year % 400 == 0):
    leap = True
elif (year % 100 == 0):
    leap = False
elif (year % 4 == 0):
    leap =True
else:
    leap = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
     length = 31
elif month == 2:
    if leap:
        length = 29
    else:
        length = 28
else:
        length = 30


day = int(input("Input a day [1-31]: "))

if day < length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [dd-mm-yyyy] %d-%d-%d." % (day, month, year))
