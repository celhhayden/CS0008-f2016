
#this is the code at the point where i needed to find out how to take the two lists
#of names and distances and convert them into a dictionary

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
total_distances = sum([float(item.strip('\n').split(',')[1]) for item in data])

#the data must now be turned into a dictioary in order to assign each name their
#distance and be able to call upon the distances when the names are called
#however, there are duplicates of names so there has to be a way to add the values
#together to form the dictionary without removing the original value completely
#and we need to also obtain the minimum distance run by said participants, as well
#as how many people ran more than once

#"
#and this is where i begin testing the dictionary stuff

#i first looked for a solution online. i had an idea of how to aproach it,
#something like:
##dictionary = dict(names,distances)
#but not with that syntax of course, so i found something online and tested it:
dictionary2 = dict(zip(names, distances))

print(dictionary2)
print(len(dictionary2))

#but then simply doing this resulted in the merging of names that were duplicates
#and thus removing any values associated with runners who had different times
#so then i thought of trying to use a for loop that would involve an accumulator,
#finding the min distance for each runner, and then finding how many times each
#person ran, and then trying to insert it into a dictionary

#again i went online since i had nearly no clue how to approach finding duplicate names

#one solution:
#this only provides the names that were duplicated; i feel like i could use this but
#i could not find a way to do so so i kept the original code w/ my variables
testlist = []
dupelist = []
for person in names:
    if testlist.__contains__(person):
        print(person)
        dupelist.append(person)
    else:
        testlist.append(person)
#print(testlist)
print(dupelist)
#print(len(testlist))
print(len(dupelist))
#second:
#i found out most of these online solutions are actually in 2.x and not 3.x
#so this was not helping, with errors and such popping up
#i used double ## to show that it is actually code and not just comments; i needed
#to disable it to
##import collections
##items = collections.defaultdict(list)
##for person, item in enumerate(names):
##  items[item].append(person)
##for item, locs in items.iteritems():
##  if len(locs) > 1:
##    print("duplicates of", item, "at", locs)

#i tried doing this on my own but i know that the name will just refer to itself
#during the loop and not if there are any other names like it further on
##for name in names:
    ##if name == name:
        ##print('a duplicate')
    ##else:
        ##print('no dupe')








