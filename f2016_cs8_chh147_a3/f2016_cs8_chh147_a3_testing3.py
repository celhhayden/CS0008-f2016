
#this is what i did to test with the help that you sent over the weekend
#on how you would set up the dictionary.
#i would have continued it on testing2 but I wanted a somewhat clean slate to
#try out the method and build off of it without all of the other code I tried


#this is the code i had so far
#"

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
#loop on all data files
for source in filelist:
    #there was an error in finding the right directory so i made a string containing the
    #full directory name, but still allowing for each file to open
    fullname = 'C:\\Users\Celest\CS0008\CS0008-f2016\\f2016_cs8_chh147_a3\\f2016_cs8_a3.data\\' + str(source)
    #open current file for reading
    fh = open(fullname, 'r')
    #loop on all lines
    for line in fh:
        #check if its a header
        if not 'distance' in line:
            #read the whole file in and edit out \n
            data.append(line.strip('\n'))
            #append allows the lists to all be put into one list
    fh.close()

#after obtaining all the data from the files, it turns all of the data into a
#list of other lists, each mini list containing the pair of name and distance
#so now they have to be separated into their own values

#take all the names and make them individual values
names = [str(item.strip('\n').split(',')[0]) for item in data]
    #str turns the list values into a string, strip removes \n, split takes the list
    #and pulls the names as individual values, [0] shows what position in the list,
    #and for loop does it for each mini list
#using same method to just get numerical values
distances = [float(item.strip('\n').split(',')[1]) for item in data]
#adding all the distances at once in order to use this data later
total_distance = sum([float(item.strip('\n').split(',')[1]) for item in data])

#the data must now be turned into a dictioary in order to assign each name their
#distance and be able to call upon the distances when the names are called
#however, there are duplicates of names so there has to be a way to add the values
#together to form the dictionary without removing the original value completely
#and we need to also obtain the minimum distance run by said participants, as well
#as how many people ran more than once

#"
#here is where i start testing the code from the email

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
   ddata[name].append(dist)

print(ddata)

#after i used a print to see what would come up, it seemed to have worked out
#any names that were duplicated had multiple values saved under the keys
#then i made a new test file to see if your code was simply a more efficient
#way to complete what my code did plus incorporate the dictionary

















