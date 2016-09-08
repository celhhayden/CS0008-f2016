# name   : Celest Hayden
# email  : chh147@my.pitt
# date   : 6 September 2016
# Class  : CS0008-f2016
# instructor : Max Noveli
#
# Description    : Starting with Python, Chapter 2, Exercise 4
#
# notes  : asks to find total of purchasing 5 items plus tax
#
# assign five items different prices using variables
bread = 1.50
milk = 2.00
eggs = 2.15
apple = 1.25
flour = 1.35
#program asks for the subtotal, and it is given
print("What is the total?")
#we need to find the subtotal
subtotal = bread + milk + eggs + apple + flour
print("Subtotal = ", subtotal)
#now to find sales tax and total
sales_tax = subtotal * .07
total = sales_tax + subtotal
print("Total =", total)