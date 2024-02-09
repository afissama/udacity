"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    unique = []
    for row in texts:
        if not row[0] in unique:
            unique.append(row[0])
        if not row[1] in unique:
            unique.append(row[1])
    print("There are {} different telephone numbers in the records.".format(len(unique)))
    

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    unique = []
    for row in calls:
        if not row[0] in unique:
            unique.append(row[0])
        if not row[1] in unique:
            unique.append(row[1])
    print("There are {} different telephone numbers in the records.".format(len(unique)))



"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
