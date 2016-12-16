# name   : Celest Hayden
# email  : chh147@my.pitt
# date   : 21 November 2016
# Class  : CS0008-f2016
# instructor : Max Novelli
#
#Description: Final Assignmet
#
#Notes: create a program that accesses x amount of data files and pulls lists of
#       names and their associated running distances. use a class and other
#       functions in order to iterate all of the data in an
#       orderly fashion, present it to the user, and print some collected data
#       onto a new file accessible to the user
#       code can be used from assignment #3 to reduce work
#
#the first part involves the creation of the class and the methods held within in
#order to utiilize it later in the program
#
#second part involves accessing the files necessary to run the program
#and to process all of the data into a dictionary and then the class
#
#the third part is finding the minimum and maximums in the collection of data
#and then taking all data and printing to a new file
#
#the fourth part is taking all of the runner data and putting it into a print
#output for the user

#part 1

# class name is runner
class Runner:
    # define properties
    # runner's name
    name = 'not found'
    # runner's distance
    distance = 0
    # runner's times ran
    runs = 0

    # initializer method
    def __init__(self, name, distance=0):
        # the name comes from runner name in file
        self.name = name
        # accumulate the total distance for the runner
        if distance > 0:
            self.distance += distance
            # accumulate the times ran per distance added
            self.runs += 1

    # define adding distances
    def addDistance(self, distance):
        if distance > 0:
            # add additional distances
            self.distance += distance
            # accumulate times run per distance
            self.runs += 1

    # defining adding multiple distances at once
    def addDistances(self, ld):
        # loop adding items in list
        for item in ld:
            if item > 0:
                # accumulate add distance item
                self.distance += item
                # accumulate runs per distance
                self.runs += 1

    def getDistance(self):
        return self.distance

    def getName(self):
        return self.name

    def getRuns(self):
        return self.runs

    # format how string is presented when called
    def __str__(self):
        # format results for printing when necessary
        # name is right align wit 20 characters and is string
        name = format(self.name, '>20s')
               # distance is 9 characters with 4 decimal and float
        distance = format(self.distance, '9.4f')
               # runs is 4 characters and integer
        runs = format(self.runs, '4n')
        return str('Name : ' + name + \
                   '. Distance : ' + distance + \
                   '. Runs : ' + runs)
# end class Runner


#part 2

# print disclaimer for user to ensure the file paths are input in
# a way that the program can read it
print('When inputing file info, please place necessary backlashes at end of file directory, and double every backslash')


# get master file
# use input function to make sure user is able to put in their own
# file path w/o directly changing code
masterfilename= str(input("What is the location of the master file? "))
# student personal computer for testing use:
# C:\\Users\Celest\CS0008\CS0008-f2016\\f2016_cs8_chh147_fp\\f2016_cs8_fp.data\\f2016_cs8_fp.data.txt
fh = open(masterfilename, 'r')
filelist = fh.readlines()
fh.close()

# strip the lines of \n
filelist = [item.strip('\n') for item in filelist]

# now have a list containing files' names to open and assign as objects

# create list to hold the names and distances dictionaries
data = []

# accumulator values for access later in the program
files_read = 0

# total lines includes the line headers in the files
total_lines_read = 0

# ask for file destination so it doesnt continuously ask within loop
filedestination = str(input('What is the path to the file containing the data? '))
# C:\\Users\Celest\CS0008\CS0008-f2016\\f2016_cs8_chh147_fp\\f2016_cs8_fp.data\\
# copy and paste for personal computer use
# loop on all data files
for source in filelist:
    # create string that contains full file name each time
    fullname = filedestination + str(source)
    # open current file for reading
    fh = open(fullname, 'r')
    files_read += 1
    # loop on all lines
    for line in fh:
        total_lines_read += 1
        # check if its a header
        if not 'distance' in line:
            # read the whole file in and edit out \n
            data.append(line.strip('\n'))
            # append allows the lists to all be put into one list
    fh.close()


# get total distance across all runners
total_distance = sum([float(item.strip('\n').split(',')[1]) for item in data])


# initialize a dictionary to store values
ddata = {}
# begin loop to insert data correctly
for line in data:
    # take each line and separate the name and distance at the comma into
    # 2 separate values
    name, dist = line.split(',')
    # remove the spaces from the names
    name = name.strip('  ')
    # if there is a name not in dictionary, do this
    if name not in ddata.keys():
        # make a list for each duplicate name to hold their running values
        ddata[name] = Runner(name)
    # put each distance associated with each name into their list and use the
    # list as the value associated with the key (name)
    ddata[name].addDistance(float(dist))


# how many people ran
how_many_people = len(ddata)

#part 3

# find maximum run distance
maximum = 0
maxrunner = ''
# begin loop to iterate through class to find max distance and
# associated runner
for name, object in ddata.items():
    # assign each value iterated through to placeholder
    maxPlaceholder = object.getDistance()
    # if maximum is less than placeholder
    if maximum < float(maxPlaceholder):
        # Turn maximum into placeholder
        maximum = maxPlaceholder
        # assign the name of the person who ran current distance
        maxrunner = name


# find runner with minimum distance
# assign minimum as maximum so it is known that every value is below it
minimum = maximum
minrunner = ''
# for loop iterate through dictionary
for name, object in ddata.items():
    # assign placeholder value to each value iterated
    minPlaceholder = object.getDistance()
    # if minimum is greater than placeholder
    if minimum > float(minPlaceholder):
        #turn minimum into placeholder
        minimum = minPlaceholder
        # assign the runner's name with the minimum distance
        minrunner = name


#give the new file a name
new_data_file = 'f2016_cs8_chh147_fp.data.output.csv'
#assign the file path
new_file_path = str(input('Where do you want to save the new file? '))
#student file path
#C:\\Users\Celest\CS0008\CS0008-f2016\\f2016_cs8_chh147_fp\\f2016_cs8_fp.data\\
full_new_file_name = new_file_path + str(new_data_file)
#open the full file name
fptr = open(full_new_file_name, 'w')

#loop over each name
people_running_more = 0
for name, object in ddata.items():
    runner_name = name
    runner_times_ran = int(object.getRuns())
    if runner_times_ran > 1:
        people_running_more += 1
    runner_total_distance = str(object.getDistance())
    full_runner_data_string = str(runner_name) + ', ' + str(runner_times_ran) + ', ' +  str(runner_total_distance) + '\n'
    fptr.write(full_runner_data_string)

#create print output for user

#print information about files
print('')
print("Number of Input files read   : ", files_read)
print("Total number of lines read   : ", total_lines_read)
print('')
#print total distance from every runner together
print("Total distance run           : ", total_distance)
print('')
#print the max distance, as well as who ran it
print("max distance run             : ", maximum)
print("  by participant             : ", maxrunner)
print('')
#print min distance, as well as who ran it
print("min distance run             : ", minimum)
print("  by participant             : ", minrunner)
print('')
#total number of people, as well as how many ran more than once
print("Total number of participants: ", how_many_people)
print("Number of participants\nwith multiple records        : ", people_running_more)