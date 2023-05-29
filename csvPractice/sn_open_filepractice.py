import csv

with open('practice.csv', 'r') as f:
    reader = csv.reader(f)
    for r in reader:
        print(r)