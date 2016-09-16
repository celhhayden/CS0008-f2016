# name   : Celest Hayden
# email  : chh147@my.pitt
# date   : 13 September 2016
# Class  : CS0008-f2016
# instructor : Max Noveli
#
#Description    : Chapter 3, Programing Exercise 2
#
#Notes:
#
#finding the area for the first rectangle
length1 = float(input("Insert the length for rectangle 1: "))
width1 = float(input("Insert the width for rectangle 1: "))

rec1 = length1 * width1
print("     Area of rectangle 1 = ", str(rec1))

#finding the area of second rectangle
length2 = float(input("Insert the length for rectangle 2: "))
width2 = float(input("Insert the width for rectangle 2: "))

rec2 = length2 * width2
print("     Area of rectangle 2 = ", str(rec2))

#determining which rectangle is greater
if rec1 > rec2:
    print("Rectangle 1 is greater than rectangle 2.", str(rec1), ">", str(rec2))
elif rec1 == rec2:
    print("Rectangle 1 and rectangle 2 are both equal.", str(rec1), "=", str(rec2))
else:
    print("Rectangle 2 is greater than rectangle 1.", str(rec1), "<", str(rec2))