#Let python know we will use the csv module in our program.
import csv

#Create a dictionary to store key-value pairs. In this scenario, a key is a users start date 
#and a value is the corresponding word in the words column. 
date_and_word = dict()

#Open file, use my_csv_file to refer to TSE_sample_data.csv then close file once we process data.
with open('TSE_sample_data.csv') as my_csv_file:
    
    #Use the csv modules reader function to parse TSE_sample_data.csv and return a list of rows.
    csv_f = csv.reader(my_csv_file)
    
    #Disregard the first row because we are not interested in headers.
    next(csv_f)
    
    #For each row in TSE_sample_data.csv do the following steps 
    for row in csv_f:
    
        #We know all dates in TSE_sample_data.csv are represented as a unix timestamp and 
        #we know the 13th index of each row is the users start date and 
        #the 16th index is the corresponding word from the words column. 
        start_date = int(row[13])
        words_column_word = row[16]
        
        #Use a python comparison operator to identify users who started before 09-10-2010. Its unix timestamp is 1283731200.

        #If the user started before 09-10-2010
        if start_date < 1283731200:           
            
            #Create a new key-value pair for our dictionary.
            #A key is a users start day and a value is the corresponding word from the words column.
            date_and_word[start_date] = words_column_word         
                                                        
    #Make a list of the keys then sort it.                                                     
    a_list = date_and_word.keys()                       
    a_list.sort()                                       
        
#Loop through the sorted list of keys and print out corresponding values. 
for key in a_list:                                      
    print key, date_and_word[key]                       