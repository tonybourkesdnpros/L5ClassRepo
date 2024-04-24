import csv

with open('vlans.csv', 'r') as file:
    raw_csv = csv.DictReader(file)
    data = [row for row in raw_csv]
print(data)


