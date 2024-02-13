"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def getOutgoingCall(numbers):
    """"""
    return [number[0] for number in numbers]

def ans():
    company_numbers = sorted(set(getOutgoingCall(calls)))
    print(len(company_numbers))
    for number in calls:
        if number[1] in company_numbers:
            company_numbers.remove(number[1])
    
    for msg in texts:
        if msg[0] in company_numbers:
            company_numbers.remove(msg[0])
        if msg[1] in company_numbers:
            company_numbers.remove(msg[1])
    print("These numbers could be telemarketers: {}".format(company_numbers))
    print(len(company_numbers))
ans()

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

