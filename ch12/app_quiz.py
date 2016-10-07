import csv

fhand = open('TSE_sample_data.csv')
csv_f = csv.reader(fhand)

date2words = dict()

with open('TSE_sample_data.csv') as fhand:
    next(csv_f)
    
    for row in csv_f:
        begin_date = int(row[13])
        if begin_date < 1283731200:
            if begin_date not in date2words:
                date2words[begin_date] = row[16]

    a_list = date2words.keys()
    a_list.sort()
        
for key in a_list:
    print key, date2words[key]