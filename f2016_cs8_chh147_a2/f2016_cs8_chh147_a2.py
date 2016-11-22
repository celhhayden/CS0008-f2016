# name   : Celest Hayden
# email  : chh147@my.pitt
# date   : 13 September 2016
# Class  : CS0008-f2016
# instructor : Max Noveli
#
#Description : Assignment 2
#
#notes: the user needs to be able to access files and their data
#       and be able to see the results of people's accumulated distances
#
#assigning proccessing functions and files before beginning input
#sequences to make sure everything works and to reduce
#as much clutter as possible
#the format function will be towards the end where it is
#more relevant

#opening the files to get ready for the functions
#there were complications taking the file names from user inputs
#so that they would actually read as files, so the prompts will come
#up later for the user to still specify which file they want
#
# MN: why do you open the files here? 
#     ...and more so why do you hard code the file names here? 
file1 = open('f2016_cs8_a2.data.1.csv', 'r')
file2 = open('f2016_cs8_a2.data.2.csv', 'r')

#this is to see if the file is being read properly and that
#the strings appear as separate from names and distances.
#this will also return the accumulator so the number of lines
#in each file appears and is not set at 50 in the case something is
#actually edited in the file
def testForReadlines(filenum):
    accumulator = 0
    #
    # MN: why you do range to 50? what if a file has more than 50 lines?
    for line in range(50):
        accumulator += 1
        string = filenum.readline().rstrip('\n').split(' , ')
        #the print function can be initiated once ## is removed.
        #it is currently inactive in order to make sure
        #the program does not show a list of 100 lines that are
        #not necessary for the user to see, but is still present if
        #anything needs to be fixed/overviewed to assure the
        #program is reading the files correctly
        ##print(string)
    #make sure the accumulator is accessible outside function
    return(accumulator)



#file processing for the files
#fh stands for file handle
#find the number of lines in each file
#find the total distance
def processFile(fh):
    #set up accumulators to find total number of lines and distance
    #by using '+=' to accumulate values
    total_distance = 0
    #begin loop to read each individual line
    #
    # MN: same comment as above: why only to 50? what happens if the file has more than 50 lines?
    for line in range(50):
        #begin accumulating lines
        #start receiving the llines
        string = fh.readline()
        #take the strings and remove non numerical characters
        individual_distances = string[string.find(',') + 1:].rstrip('\n')
        #convert numericals to float; can't change strings direclty
        #so using a new variable to express the float value
        new_format_distance = float(individual_distances)
        #use isintance to test if new_format_distance is a float
        #accumulate the distances
        total_distance += new_format_distance
    return(float(total_distance))

#there was trouble keeping the processFile as a float if the distance
#variables were put into the loop, so they are not directly included
#in the loops, but rather are refered to by other variables
distance1 = processFile(file1)
distance2 = processFile(file2)


#function acts as a formatting template to reduce
#the amount of space taken in code and make more simple
def printKV(key, value, klen = 0):
    #find the length of the key to find amount of spaces
    #needed in the row
    length = len(key)
    #establish number of spaces
    for n in range(30 - length):
        for l in range(length):
            klen = ' ' * n
    if isinstance(value, str):
        right = format(value, '30s')
    elif isinstance(value, int):
        right = format(value, '<10n')
    elif isinstance(value, float):
        right = format(value, '<10.3f')
    print(key,klen,' : ', right)

#initiate with the user
prompt = input("Please provide the file name : ")
while prompt != ('q' and 'quit'):
    # 
    # MN: what if I enter a file that has the right format but a different file name?
    #
    if prompt == 'f2016_cs8_a2.data.1.csv':
        #the amount of lines in the file
        lines1 = testForReadlines(file1)
        #reassignment for distance1 so it remains a float
        re_dist1 = distance1
        #insert printKV to create list
        printKV('File read', prompt)
        printKV('Partial Total # of lines', lines1)
        printKV('Partial distance run', re_dist1)
    elif prompt == 'f2016_cs8_a2.data.2.csv':
        #the amount of lines in the file
        lines2 = testForReadlines(file2)
        #reassignment of distance2 so it remains a float
        re_dist2 = distance2
        printKV('File read', prompt)
        printKV('Partial Total # of lines', lines2)
        printKV('Partial distance run', re_dist2)
    else:
        print("File not found; if you want to terminate program, please insert 'q' or 'quit', and your total will be calculated.")
    prompt = input("Please provide the file name : ")
#close the files to avoid corruption
file1.close()
file2.close()
#print the final added results using printKV template
printKV('Total # of lines', lines1 + lines2)
printKV('Total distance run', re_dist1 + re_dist2)

