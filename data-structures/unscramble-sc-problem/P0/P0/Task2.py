"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def get_unique_phone_numbers(records):
    uniq = []
    for record in records:
        if not record[0] in uniq:
            uniq.append(record[0])
        if not record[1] in uniq:
            uniq.append(record[1])
    return uniq

def get_number_as_dict(recordList):
    mRecord = {}
    for r in recordList:
        mRecord[r] = 0
    return mRecord

def longest_time(records):
    """return the telephone number with the longest time"""
    numbers = get_number_as_dict(get_unique_phone_numbers(records))
    for call in records:
        numbers[call[0]] += int(call[3])
        numbers[call[1]] += int(call[3])

    keys = list(numbers.keys())
    max_call = keys[0]
    for key in keys:
        if numbers[max_call] < numbers[key]:
            max_call = key
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_call, numbers[max_call]))

longest_time(calls)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

