# name   : Celest Hayden
# email  : chh147@my.pitt
# date   : 21 November 2016
# Class  : CS0008-f2016
# instructor : Max Novelli
#
#Description: Assignement #3
#
#Notes: create a program that accesses x amount of data files and pulls lists of
#       names and their associated running distances. use functions such as
#       dictionaries, lists, etc. in order to iterate all of the data in an
#       orderly fasion, present it to the user, and print some collected data
#       onto a new file accessible to the user

#the first part consists of getting the data from the correct files and manipulating
#the data to make it more accessible throughout the program

#the second part involves taking the data and accessing it through a dictionary
#to get multiple values related to the data

#the third part involves applying certain aspects of the data onto a new file
#created by running the program

#the fourth part is taking all the requested data and printing it for the user

#open the master file to access list of data file names
masterfilename='C:\\Users\Celest\CS0008\CS0008-f2016\\f2016_cs8_chh147_a3\\f2016_cs8_a3.data\\f2016_cs8_a3.data.txt'
fh = open(masterfilename, 'r')
filelist = fh.readlines()
fh.close()

#strip the lines of \n
filelist = [item.strip('\n') for item in filelist]

#initialize data container
#data is an empty list
data = []
#accumulator values for access later in the program
files_read = 0
total_lines_read = 0
#loop on all data files
for source in filelist:
    #create string that contains full file name each time
    #will take the same access route each time to open the specific file in
    #efficient manner
    fullname = 'C:\\Users\Celest\CS0008\CS0008-f2016\\f2016_cs8_chh147_a3\\f2016_cs8_a3.data\\' + str(source)
    #open current file for reading
    fh = open(fullname, 'r')
    files_read += 1
    #loop on all lines
    for line in fh:
        total_lines_read += 1
        #check if its a header
        if not 'distance' in line:
            #read the whole file in and edit out \n
            data.append(line.strip('\n'))
            #append allows the lists to all be put into one list
    fh.close()

#obtain total distance of all runners combined
total_distance = sum([float(item.strip('\n').split(',')[1]) for item in data])

#initialize a dictionary to store values
ddata = {}
#begin loop to insert data correctly
for line in data:
    #take each line and separate the name and distance at the comma into
    #2 separate values
    name,dist = line.split(',')
    #remove the spaces from the names
    name = name.strip('  ' )
    #if there is a name not in dictionary, do this
    if name not in ddata.keys():
       #make a list for each duplicate name to hold their running values
        ddata[name] = []
    #put each distance associated with each name into their list and use the
    #list as the value associated with the key (name)
    ddata[name].append(float(dist))

#the number of participants combined
how_many_people = len(ddata)

#now to find the maximum and minimum distances ran, as well as the people who
#ran them

#find runner with maximum distance
#set pmax to 0 so nothing is less than it
pmax = 0
maxrunner=''
#start loop to iterate through dictionary
for person in ddata:
    #assign each value iterated through to tmax
    tmax = max(ddata.get(person))
    #if pmax is less than tmax
    if pmax < tmax:
        #Turn pmax into tmax
        #what this does is everytime it goes through the loop, it will compare
        #the current pmax to the new tmax.  if tmax is not greater, then it will
        #move on until it finds no value greater than the current pmax
        pmax = tmax
        #assign the name of the person who ran current distance
        maxrunner = person

#find runner with minimum distance
#assign pmin as pmax so it is known that every value is below it
pmin = pmax
minrunner=''
#for loop iterate through dictionary
for person in ddata:
    #assign tmin value to each value iterated
    tmin = min(ddata.get(person))
    #if pmin is greater than tmin
    if pmin > tmin:
        #pmin will become tmin until there is nothing left to go below the
        #current value of pmin, meaning that is the shortest distance ran
        pmin = tmin
        #assign the runner's name with the minimum distance
        minrunner = person

#create a file to hold the following data:
#look for runners who have ran more than once
#if so, how many times?
#find total distance
#apply all of this to a file

#give the new file a name
new_data_file = 'f2016_cs8_chh147_a3.data.output.csv'
#assign the file path
full_new_file_name = 'C:\\Users\Celest\CS0008\CS0008-f2016\\f2016_cs8_chh147_a3\\f2016_cs8_a3.data\\' + str(new_data_file)
#open the full file name
fptr = open(full_new_file_name, 'w')

#loop over each name
people_running_more = 0
for person in ddata:
    runner_name = person
    runner_times_ran = len(ddata.get(person))
    if runner_times_ran > 1:
        people_running_more += 1
    runner_total_distance = str(sum(ddata.get(person)))
    full_runner_data_string = runner_name + ', ' + str(runner_times_ran) + ', ' +  runner_total_distance + '\n'
    fptr.write(full_runner_data_string)

#close file to avoid corruption
fptr.close()


#now to print values found in an orderly fashion
#placed after creation of file in order to access variable not found beforehand
#and keep all print editing in one section
#print information about files
print("Number of Input files read\t: ", files_read)
print("Total number of lines read\t: ", total_lines_read)
print('')
#print total distance from every runner together
print("Total distance run\t\t\t: ", total_distance)
print('')
#print the max distance, as well as who ran it
print("max distance run  \t\t\t: ", pmax)
print("\tby participant\t\t\t: ", maxrunner)
print('')
#print min distance, as well as who ran it
print("min distance run  \t\t\t: ", pmin)
print("\tby participant\t\t\t: ", minrunner)
print('')
#total number of people, as well as how many ran more than once
print("Total number of participants: ", how_many_people)
print("Number of participants\nwith multiple records  \t\t: ", people_running_more)

#end of program