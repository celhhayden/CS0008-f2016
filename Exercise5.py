# name   : Celest Hayden
# email  : chh147@my.pitt
# date   : 13 September 2016
# Class  : CS0008-f2016
# instructor : Max Noveli
#
#Description    : Chapter 3, Programing Exercise 5
#
#Notes: calculating an object's mass
#
#prompt for the mass
mass = float(input("Please input the mass: "))
#calculate the weight
weight = mass * 9.8
print("Weight of the object is ", str(weight))
#determine if object is too light/heavy
if weight > 500:
    print("Object is too heavy.")
elif weight < 100:
    print("Object is too light.")