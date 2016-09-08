# name   : Celest Hayden
# email  : chh147@my.pitt
# date   : 6 September 2016
# Class  : CS0008-f2016
# instructor : Max Noveli
#
# Description    : Starting with Python, Chapter 2, Exercise 6
#
#notes  : asks to find the total of a sale after finding the values of different taxes
#
#book asks to create an input for the user to insert a price; we also need to turn it into a float
purchase = float(input('Enter the amount of purchase: '))
print("Amount of purchase:", purchase)
#the purchase has a state and county sales tax that needs calculated, as well as their total
#for the percentages, I looked online for a formating string to reduce the length of the decimal places to 2 to mae it more simple
state_tax = purchase * .05
print("State tax:", '% 10.2f' % state_tax)
county_tax = purchase * .025
print("County tax:", '% 10.2f' % county_tax)
total_tax = state_tax + county_tax
print("Total tax", '% 10.2f' % total_tax)
#now to add the purchase and tax
total_purchase = purchase + total_tax
print("Purchase total:", '% 10.2f' % total_purchase)