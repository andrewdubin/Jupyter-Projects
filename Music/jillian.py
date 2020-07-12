import csv

info = []
with open('buff_baby.csv', 'r') as datafile:
    csv_reader = csv.reader(datafile)
    next(csv_reader)
    for i in csv_reader:
        info.append([i[1],i[2],i[3]])

print(info)