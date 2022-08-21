import csv
import itertools

f1 = open('3.csv')
f2 = open('17.csv')

"""
people = set()
for row in itertools.chain(csv.reader(f1), csv.reader(f2)):
    if "@" in row[4]:
        if row[4] not in people:
            people.add(row[4])
        else:
            print(row[0], row[1], row[6], row[7], row[9])
"""
successful = set()
for row in itertools.chain(csv.reader(f1), csv.reader(f2)):
    if "@" in row[4]:
        if row[9] != "-" and int(row[9][:-3]) >= 6:
            successful.add(row[4])
        else:
            if row[4] not in successful:
                print(row[9], row[6], row[7])
