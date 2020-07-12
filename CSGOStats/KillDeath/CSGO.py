import csv
import numpy as np

kills = []
deaths = []
difference = []

with open('CSGOStats\CSGO.csv', 'r') as datafile:
    csv_read = csv.reader(datafile)
    next(csv_read)
    for i in csv_read:
        kills.append(int(i[0]))
        deaths.append(int(i[1]))
        difference.append(int(i[0])-int(i[1]))

avg = sum(difference)/len(difference)
print(avg)

xlst = []
for i in range(0,10):
    xlst.append(i)
print(xlst)
print(np.median(xlst))