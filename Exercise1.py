# name   : Celest Hayden
# email  : chh147@my.pitt
# date   : 13 September 2016
# Class  : CS0008-f2016
# instructor : Max Noveli
#
#Description    : Chapter 3, Programing Exercise 1
#
#Notes  : program to list days of the week
#
#input a day of the week
day = float(input("Input a number 1-7 to represent a day of the week: "))

print("Day of the week:")
#if-elif-else to assign each number a day of the week; if nothing corresponds, an error message plays
if day == 1:
    print(" Monday")
elif day == 2:
    print(" Tuesday")
elif day == 3:
    print(" Wednesday")
elif day == 4:
    print(" Thursday")
elif day == 5:
    print(" Friday")
elif day == 6:
    print(" Saturday")
elif day == 7:
    print(" Sunday")
else:
    print("Error: Value was not 1-7")
