# name   : Celest Hayden
# email  : chh147@my.pitt
# date   : 13 September 2016
# Class  : CS0008-f2016
# instructor : Max Noveli
#
#Description    : Chapter 3, Programing Exercise 6
#
#Notes:
#
#prompt user for month, date, and year values
month = input("Input a month as numeric value: ")
day = input("input a day: ")
year = input("Input a year as a 2 digit value: ")

print("Date: ", str(month), "/", str(day), "/", str(year))
#if statement only takes floats, but i wanted to keep the printed date as integers so i converted afterwards
month = float(month)
day = float(day)
year = float(year)
#determine if date is "magic"
if month * day == year:
    print("You chose a magic date!")
else:
    print("Your date was not magic.")