import csv

fhand = open('TSE_sample_data.csv')
csv_f = csv.reader(fhand)

#Create a disctionary to store a key-value pairs.
#In this scenario, a key is a users start date and a value is the corresponding word in the words column.
date_and_word = dict()

with open('TSE_sample_data.csv') as fhand:
    
    #Skip the first line of headers
    next(csv_f)
    
    for row in csv_f:
        
        #Note, all dates in TSE_sample_data.csv are represented as a unix timestamp.
        #The 13th index of each row is the users start date.

        start_date = int(row[13])
        
        #We can use a python comparison operator to identify users who started before 09-10-2010.
        #The unix timestamp for 09-10-2010 is 1283731200.
        
        if start_date < 1283731200:                     #Check if user started before 09-10-2010.
            date_and_word[start_date] = row[16]         #If so, create a new key-value pair for our dictionary.
                                                        #Each key is a users start day. Each value is the corresponding word in the words column. 
                                                    
    a_list = date_and_word.keys()                       #Make a list of the keys, then sort it. 
    a_list.sort()                                       
        
for key in a_list:                                      #Loop through the sorted list.
    print key, date_and_word[key]                       #Print out key-value pairs in sorted order. 