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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
diff_nums = []
for record in texts:
    for i in range(2):
        if record[i] not in diff_nums:
            diff_nums.append(record[i])

for record in calls:
    for i in range(2):
        if record[i] not in diff_nums:
            diff_nums.append(record[i])
print(f"There are {len(diff_nums)} different telephone numbers in the records")