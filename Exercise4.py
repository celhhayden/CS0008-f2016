# name   : Celest Hayden
# email  : chh147@my.pitt
# date   : 13 September 2016
# Class  : CS0008-f2016
# instructor : Max Noveli
#
#Description    : Chapter 3, Programing Exercise 4
#
#Notes:
#
#display values 1-10 as Roman numerals; otherwise provide an error message
roman = float(input("Input a number 1-10    "))

print("Your number translates to:")
#designate each number to corresponding Roman numeral
if roman == 1:
    print("I")
elif roman == 2:
    print("II")
elif roman == 3:
    print("III")
elif roman == 4:
    print("IV")
elif roman == 5:
    print("V")
elif roman == 6:
    print("VI")
elif roman == 7:
    print("VII")
elif roman == 8:
    print("VIII")
elif roman == 9:
    print("IX")
elif roman == 10:
    print("X")
else:
    print("Your value did not fit in the range.")