#this is a file i will use to test opening the files and
#test how to manipulate to see how i want the final
#program organized and to also possibly run
#any troubleshooting or debugging throughout the process
#i also took reference from the examples from tuesday and
#took reference for some of them as a base for syntax i used
#i also looked back on previous assignments for help

#access master access file to get names for data files
##masterfilename = 'C:\\Users\Celest\CS0008\CS0008-f2016\\f2016_cs8_chh147_a3\\f2016_cs8_a3.data\\f2016_cs8_a3.data.txt'
##fulldoc = fh.readlines()

#this is where i had trouble thinking about how i could split
#the string into pieces where the file names would remain
#in tact and so i could assign them each to their own variable
#while also considering if the user wanted to add their own
#files, meaning i would need to be able to allot each file
#to more than just 3 given variables
#i also did not want to alter the original file

#attempt 1
#took help from class on thursday
##for line in fulldoc:
    ##str(file) = line.rstrip('\n')
    #originally an error came up so i added the file path
    ##words = open('C:\\Users\Celest\CS0008\CS0008-f2016\\f2016_cs8_chh147_a3\\f2016_cs8_a3_data\\', 'r')



#finding a way to make the whole file one string to avoid error


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

#this portion was also copied from examples

#now we need to take the individual names and values and split them into their
#own variables
#split list at the comma and separate name and dist
##data = [item.strip('\n').split(',') for item in data]


#take all the names and make them individual values
names = [str(item.strip('\n').split(',')[0]) for item in data]
#using same method to just get numerical values
distances = [float(item.strip('\n').split(',')[1]) for item in data]
#adding all the distances at once
total_distances = sum([float(item.strip('\n').split(',')[1]) for item in data])

#originally there was an error because instead of using () i accidentally used []
#to determine where the program should split, but once i solved the error i proceeded




