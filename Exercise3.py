# name   : Celest Hayden
# email  : chh147@my.pitt
# date   : 13 September 2016
# Class  : CS0008-f2016
# instructor : Max Noveli
#
#Description    : Chapter 3, Programing Exercise 3
#
#Notes: ask the user what their age is and give a response for each value
#
#prompt user for their age
age = float(input("What is your age? "))
#determine the title to go with each age value
if age <= 1:
    print("You are an infant.")
elif 1 < age < 13:
    print("You are a child.")
elif 13 <= age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")