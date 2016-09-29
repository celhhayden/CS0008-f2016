# name   : Celest Hayden
# email  : chh147@my.pitt
# date   : 13 September 2016
# Class  : CS0008-f2016
# instructor : Max Noveli
#
#Description: Assignement #1
#
#Notes: getting the person's distance and gas, converting it into other units, then presenting them to user
#
#prompt the user for system of measurement, their distance, and gas consumed
system = input("Is this in USC/Metric? (Please capitalize): ")
distance = float(input("Input the distance travelled: "))
gas = float(input("Input the gas consumed: "))
#do conversions for if person types a certain unit (convert USC to Metirc and vice versa)
if system == 'USC':
    USC_dist = distance
    USC_gas = gas
    Metric_dist = distance * 1.60934
    Metric_gas = gas * 3.78541
elif system == 'Metric':
    USC_dist = distance * 0.621371
    USC_gas = gas * 0.264172
    Metric_dist = distance
    Metric_gas = gas
else:
    print("Error: incorrect unit of measurement input")
    exit()

#need to get mpg and 1/100Km by using specific formulas
mpg = USC_dist / USC_gas
Km = 100 * Metric_gas / Metric_dist

#determine the consumption category according to chart
if Km > 20:
    category = "Extremely poor"
elif 15 < Km <= 20:
    category = "Poor"
elif 10 < Km <= 15:
    category = "Average"
elif 8 < Km <= 10:
    category = "Good"
elif 0 < Km <= 8:
    category = "Excellent"
else:
    print("Error")
    exit()

#listing the distance, gas, consumption, and category using formats
    #the \t is used to tab over to the next column
print("\t\t\t\t USC\t\t\t\tMetric")
#using \t to try to line the variables up, and make sure it has 3 decimal pooints and enough for 100,000
    # used \ to reduce lengthiness and make look nicer and show individual format
print("Distance:\t",\
      format(USC_dist, '10.3f')," miles\t\t",\
      format(Metric_dist, '10.3f'), " Km")
#copied and pasted first format to reduce typing; changed corresponding variables
print("Gas:\t\t",\
      format(USC_gas, '10.3f'), " gallons\t",\
      format(Metric_gas, '10.3f'), " Liters")
print("Consumption:",\
      format(mpg, '10.3f'), " mpg\t\t",\
      format(Km, '10.3f')," 1/100Km")
#need to unclue gas rating but need an extra space between lines
print(" ")
print("Gas Consumption Rating: ", category)