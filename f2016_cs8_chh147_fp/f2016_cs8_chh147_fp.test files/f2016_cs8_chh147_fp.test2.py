

#test 1 was having some issues so i moved to a new file to be able to
#copy and fix without removing too much of the trial runs


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
        if distance > 0:
            self.distance += distance
            #accumulate the times ran per distance added
            self.runs += 1

    #define adding distances
    def addDistance(self, distance):
        if distance > 0:
        #add additional distances
            self.distance += distance
        #accumulate times run per distance
            self.runs += 1
    #this function adds runs even if runner ran 0 distance
    #this would not work out

    #defining adding multiple distances at once
    def addDistances(self, ld):
        #loop adding items in list
        for item in ld:
            if item > 0:
                #accumulate add distance item
                self.distance += item
                #accumulate runs per distance
                self.runs += 1
    #adds run acumulation even if distance = 0
    #needs if dist > 0

    def getDistance(self):
        return self.distance
    #needs a return

    def getName(self):
        return self.name
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
print('When inputing file info, please place necessary backlashes at end of file directory, and double every backslash')

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

#now have a list containing files' names to open and assign as objects

#create list to hold the names and distances dictionaries
data = []

#accumulator values for access later in the program
files_read = 0

#total lines includes the line headers in the files
total_lines_read = 0

#ask for file destination so it doesnt continuously ask within loop
filedestination = str(input('What is the path to the file containing the data? '))
# C:\\Users\Celest\CS0008\CS0008-f2016\\f2016_cs8_chh147_fp\\f2016_cs8_fp.data\\
# copy and paste for personal computer use

#borrowed code to see something related to a later part
#loop on all data files
for source in filelist:
    #create string that contains full file name each time
    #will take the same access route each time to open the specific file in
    #efficient manner
    #rewrote as input to make it accessible to user's specific file location
    fullname = filedestination + str(source)
    #open current file for reading
    fh = open(fullname, 'r')
    files_read += 1
    #loop on all lines
    for line in fh:
        total_lines_read += 1
        #check if its a header
        if not 'distance' in line:
            #read the whole file in and edit out \n
            #borrowed
            data.append(line.strip('\n'))
            #append allows the lists to all be put into one list
    fh.close()

#get total distance across all runners
total_distance = sum([float(item[1]) for item in data])


#initialize a dictionary to store values
ddata = {}
#begin loop to insert data correctly
for line in data:
    #if there is a name not in dictionary, do this
    if name not in ddata.keys():
       #make a list for each duplicate name to hold their running values
        ddata[name] = Runner(name)
    #put each distance associated with each name into their list and use the
    #list as the value associated with the key (name)
    ddata[name].addDistance(distance)
#all throughout this loop i would take reference to teacher code and continuously
#get "TypeError: string indicies must be integers" so i would remove the string
#and there would be errors in using the modules instead
#i think it is because of how i was manipulating the list with the line.split:
    #w/o notes
#for line in data:
    #name,dist = line.split(',')
    #name = name.strip('  ')
    #if name not in ddata.keys():
        #ddata[name] = Runner(name)
    #ddata[name].addDistance(distance)

#after removing the editing there was still a TypeError regarding not having integer

#how many people ran
how_many_people = len(ddata)

#test check
print('total distance',total_distance)
print('how many people', how_many_people)


#find maximum run distance
maximum = 0
maxrunner = ''
#begin loop to iterate through class to find max disance and
#associated runner
for name, object in ddata.items():
    #assign each value iterated through to tmax
    maxPlaceholder = object.getDistance
        #errors here because can't utilize a method like this even if it is
        #technically returning a value
    #if pmax is less than tmax
    if maximum < float(maxPlaceholder):
        #Turn pmax into tmax
        #what this does is everytime it goes through the loop, it will compare
        #the current pmax to the new tmax.  if tmax is not greater, then it will
        #move on until it finds no value greater than the current pmax
        maximum = maxPlaceholder
        #assign the name of the person who ran current distance
        maxrunner = name, object


