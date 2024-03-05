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

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
callers_dict = {}
for record in calls:
    for i in range(2):
        if record[i] in callers_dict:
            callers_dict[record[i]]=int(record[3]) + callers_dict[record[i]]
        else:
            callers_dict[record[i]] = int(record[3])
max_v = 0
for k, v in callers_dict.items():
    if v>max_v:
        max_v = v
        max_k = k
print(f"{max_k} spent the longest time, {max_v:,} seconds, on the phone during September 2016.")

