#Let python know we will be using the csv module in our program
import csv

#Create a dictionary to store key-value pairs. In this scenario, a key is a users start date 
#and a value is the corresponding word in the words column. 
date_and_word = dict()

#Open file, use my_csv_file to refer to TSE_sample_data.csv then close file once we process data.
with open('TSE_sample_data.csv') as my_csv_file:
    
    #Use the csv modules reader function to parse TSE_sample_data.csv and return a list of rows.
    csv_f = csv.reader(my_csv_file)
    
    #Skip the first line of headers
    next(csv_f)
    
    #For each row in TSE_sample_data.csv do the following steps 
    for row in csv_f:
    
        #We know that all dates in TSE_sample_data.csv are represented as a unix timestamp and 
        #the 13th index of each row is the users start date.
    
        start_date = int(row[13])
        
        #Use a python comparison operator to identify users who started before 09-10-2010.
        #The unix timestamp for 09-10-2010 is 1283731200.
        
        #If the user started before 09-10-2010
        if start_date < 1283731200:           
            
            #Create a new key-value pair for our dictionary.
            #Each key is a users start day. 
            #Each value is the corresponding word in the 16th index of each row. 
            date_and_word[start_date] = row[16]         
                                                        
    #Make a list of the keys then sort it.                                                     
    a_list = date_and_word.keys()                       
    a_list.sort()                                       
        
#Loop through the sorted list of keys and print out corresponding values. 
for key in a_list:                                      
    print key, date_and_word[key]                       