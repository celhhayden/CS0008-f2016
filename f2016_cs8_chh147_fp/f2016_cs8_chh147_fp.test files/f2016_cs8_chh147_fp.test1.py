

#1st test with instinctual programming
#very simple start
#this is with very little help from external sources
#i would sometimes check teacher solution to see if i was at least
#headed in the right direction but i did not change anything here
#if i found it was wrong
#instead i put comment so i knew where to look to fix problems
#during another test program write

#begin with class and defining the methods

#class name is runner
class Runner:
    #define properties
    #runner's name
    name = 'not found'
    #runner's distance
    distance = 0
    #runner's times ran
    runs = 0

    #initializer method
    def __init__(self, name, distance=0):
        #the name comes from runner name in file
        self.name = name
        #accumulate the total distance for the runner
        self.distance += distance
            #initial problem here is that in def, distance = 0
            #so it would not work
            #and this is not supposed to be in this function
        #accumulate the times ran
        self.runs += 1

    #define adding distances
    def addDistance(self, distance):
        #add additional distances
        self.distance += distance
        #accumulate times run per distance
        self.runs += 1
    #this function adds runs even if runner ran 0 distance
    #this would not work out

    #defining adding multiple distances at once
    def addDistances(self, ld):
        #define list of distances
        ld = []
            #this is wrong since the list is coming from outside
            #otherwise there is just an empty list that we are
            #trying to do things with
        #loop adding items in list
        for item in ld:
            #accumulate add distance item
            self.item += item
            #accumulate runs per distance
            self.runs += 1
    #adds run acumulation even if distance = 0
    #needs if dist > 0

    def getDistance(self):
        self.distance
    #needs a return

    def getName(self):
        self.name
    #needs return

    #format how string is presented
    def __str__(self):
        #format results for printing when necessary
               #name is right align wit 20 characters and is string
        format(self.name, '>20s', \
               #distance is 9 characters with 4 decimal and float
               self.distance, '9.4f',\
               #runs is 4 characters and integer
               self.runs, '4n')
#end class Runner


#print disclaimer for user to ensure the file paths are input in
#a way that the program can read it
print('When inputinf file info, please place necessary backlashes at end of file directory, and double every backslash')

#copied file open from assignment 3 with slight edits

#get master file
#use input function to make sure user is able to put in their own
#file path w/o directly changing code
masterfilename=str(input("what is the location of the master file? "))
#student personal computer for testing use:
    #C:\\Users\Celest\CS0008\CS0008-f2016\\f2016_cs8_chh147_fp\\f2016_cs8_fp.data\\f2016_cs8_fp.data.txt
fh = open(masterfilename, 'r')
filelist = fh.readlines()
fh.close()

#strip the lines of \n
filelist = [item.strip('\n') for item in filelist]
#now have a list containing files' names to open and use

#create list to hold the names and distances dictionaries
data = []
#accumulator values for access later in the program
files_read = 0
#total lines includes the line headers in the files
total_lines_read = 0
#loop on all data files
for source in filelist:
    #create string that contains full file name each time
    #will take the same access route each time to open the specific file in
    #efficient manner
    #rewrote as input to make it accessible to user's specific file location
    fullname = str(input('What is the path to the file containing the data?')+ str(source))
        #C:\\Users\Celest\CS0008\CS0008-f2016\\f2016_cs8_chh147_fp\\f2016_cs8_fp.data\\
        #copy and paste for personal computer use
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

#get total distance across all runners
total_distance = sum([float(item.strip('\n').split(',')[1]) for item in data])


#initialize a dictionary to store values
ddata = {}
#begin loop to insert data correctly
for line in data:
    #take each line and separate the name and distance at the comma into
    #2 separate values
    name,dist = line.split(',')
    #remove the spaces from the names
    name = name.strip('  ')
    #if there is a name not in dictionary, do this
    #i did refer to your code for help with this part
    if name not in ddata.keys():
       #make a list for each duplicate name to hold their running values
        ddata[name] = Runner(name)
    #put each distance associated with each name into their list and use the
    #list as the value associated with the key (name)
    ddata[name].addDistance(dist)
#this loop resulted in an error so i started a new test file to fix
#previous mistakes i left to see if that would help

#how many people ran
how_many_people = len(ddata)


#find maximum run distance
maximum = 0
maxrunner = ''
#begin loop to iterate through class to find max disance and
#associated runner
for name, object in ddata.items():
    #assign each value iterated through to tmax
    maxPlaceholder = max(object.getDistance)
    #if pmax is less than tmax
    if maximum < maxPlaceholder:
        #Turn pmax into tmax
        #what this does is everytime it goes through the loop, it will compare
        #the current pmax to the new tmax.  if tmax is not greater, then it will
        #move on until it finds no value greater than the current pmax
        maximum = maxPlaceholder
        #assign the name of the person who ran current distance
        maxrunner = name, object

print('total distance',total_distance)
print('how many people', how_many_people)
print('maximum distance', maximum)
print('maximum runner', maxrunner)













