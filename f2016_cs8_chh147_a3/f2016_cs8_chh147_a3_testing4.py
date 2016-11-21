
#this is the combination of examples that were used to




#celest's flie opening code
#i also added an accumulator value in order to find the total number of
#files read in the code
#""

#the first part consists of getting the data from the correct files and manipulating
#the data to make it more accessible throughout the program
#most of this will pull help from the review in class, while also including
#any personal edits needed to make it work accordingly with this specific project

#open the master file to access list of data file names
masterfilename='C:\\Users\Celest\CS0008\CS0008-f2016\\f2016_cs8_chh147_a3\\f2016_cs8_a3.data\\f2016_cs8_a3.data.txt'
fh = open(masterfilename, 'r')
filelist = fh.readlines()
fh.close()

#the following sequences of code were borrowed from the in-class examples

#strip the lines of \n
filelist = [item.strip('\n') for item in filelist]

#initialize data container
#data is an empty list
data = []
#accumulator values
files_read = 0
total_lines_read = 0
#loop on all data files
for source in filelist:
    #there was an error in finding the right directory so i made a string containing the
    #full directory name, but still allowing for each file to open
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

total_distance = sum([float(item.strip('\n').split(',')[1]) for item in data])

#""
#what i did was remove the creation of the lists names and distances, and the
#total distance and then just added the following code

#from testing 3/ max's code
#""

#code courtesy of Max Novelli:
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
   #here you had data instead of the dictionary ddata
   if name not in ddata.keys():
       #make a list for each duplicate name to hold their running values
      ddata[name] = []
    #put each distance associated with each name into their list and use the
    #list as the value associated with the key (name)
   ddata[name].append(float(dist))

#""
#the data still printed well

#what i was previously trying to work on was going to end up being very
#inefficient compared to this
#i was going to try and create a list of the duplicates and ues a for loop
#to add the names and distances lists i created to be put into a dictionary
#the duplicate name list would be used to identify if the name currently
#being added to the dictionary had musltiple values, and then to add the
#values together to associate a person's total distance, but this caused a
#problem where the minimum distance and how many times the person ran would
#be lost because it wouldn't keep track of how many values were being added

#trying to do that would take up a lot of time, so thank you for the help
#with the code in creating a dictionary

#the number of participants
how_many_people = len(ddata)

#now to find the maximum and minimum distances ran, as well as the people who
#ran them

#i received help with the following code for finding min and max

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



#look for runners who have ran more than once
#if so, how many times?
#find total distance
#apply all of this to a file

#looked online for some help since i didnt know python actually made a file itself
#if one wasnt already there
#i made it a write file in the case that if one were to open this file but there
#were more/less data files open, it wouldnt just append the same data
#i know there would be a downside to making a write file, but it did seem more
#appropriate in this situation

#give the new file a name
new_data_file = 'test_f2016_cs8_chh147_a3.data.output.csv'
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

#now to print the values found in an orderly fashion
#im doing this here before copying everything over to the final file since this is
#the last step I need to do in order to complete the assignment


print("Number of Input files read\t: ", files_read)
print("Total number of lines read\t: ", total_lines_read)
print('')
print("Total distance run\t\t\t: ", total_distance)
print('')
print("max distance run  \t\t\t: ", pmax)
print("\tby participant\t\t\t: ", maxrunner)
print('')
print("min distance run  \t\t\t: ", pmin)
print("\tby participant\t\t\t: ", minrunner)
print('')
print("Total number of participants: ", how_many_people)
print("Number of participants\nwith multiple records  \t\t: ", people_running_more)


#most of the notes relating to things such as obtaining code from external sources
#were removed from the final file in order to keep a sense of "formal" programming
#as well as anything about trying different methods
#anything related to how the code works will remain