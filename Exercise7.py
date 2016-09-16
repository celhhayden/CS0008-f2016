# name   : Celest Hayden
# email  : chh147@my.pitt
# date   : 13 September 2016
# Class  : CS0008-f2016
# instructor : Max Noveli
#
#Description    : Chapter 3, Programing Exercise 7
#
#Notes:
#
#


col1 = input("Please type a primary color (red/blue/yellow): ")
if col1 != 'red' and col1 != 'blue' and col1 != 'yellow':
    print("Error: color does not match")

col2 = input("Please type another primary color: ")
if col2 != 'red' and col2 != 'blue' and col2 != 'yellow':
    print("Error: color does not match")
elif col1 == col2:
    print("Error: color was already used")

if (col1 == 'red' and col2 == 'blue') or (col1 == 'blue' and col2 == 'red'):
    print("Your color is purple.")
elif (col1 == 'red' and col2 == 'yellow') or (col1 == 'yellow' and col2 == 'red'):
    print("Your color is orange.")
elif (col1 == 'yellow' and col2 == 'blue') or (col1 == 'blue' and col2 == 'yellow'):
    print("Your color is green.")
else:
    print("Error")