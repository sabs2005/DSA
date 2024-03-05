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
tele_list = []
recr_list = []
callr_list = []
for item in calls:
    callr_list.append(item[0])
    recr_list.append(item[1])
for item in callr_list:
    if item not in recr_list and item not in tele_list:
        tele_list.append(item)
tele_list.sort()
print("These numbers could be telemarketers: ")
print(*tele_list,sep='\n')
