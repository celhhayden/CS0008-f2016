# name   : Celest Hayden
# email  : chh147@my.pitt
# date   : 13 September 2016
# Class  : CS0008-f2016
# instructor : Max Noveli
#
#Description    : Chapter 3, Programing Exercise 8
#
#Notes:
#
#ask user to input guest amount
guest = int(input("How many guests are attending?  "))
#get approximate number of bun packages
bun = guest // 8
#if there's a number not evenly divisible by 8, we need to make sure there's stil enough buns for everyone even if there's extra
if guest %8 == 0:
    bpack = bun
else:
    bpack = bun + 1
print("Number of hotdog bun packages: ", str(bpack))
#get approximate number of 'dog packages
dog = guest // 10
#make sure theres enough hotdogs for everyone even with extra left over
if guest %10 == 0:
    dpac = dog
else:
    dpac = dog + 1
print("Number of hotdog packages:  ", str(dpac))
#need to find leftovers for 'dogs and buns after party if everyone takes one
leftb = bpack * 8 - guest
print("Leftover buns: ", str(leftb))

leftd = dpac * 10 - guest
print("Leftover hotdogs: ", str(leftd))