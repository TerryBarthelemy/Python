# ram = space on harddrive
# proc = processor 

import csv

ram = []
proc = []


with open("Z:/test.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        proc.append(row[2])
        if(row[3] == "08"):
            ram.append(row[3])

print("There are",len(ram),"computers with 8GB of RAM")
print("There are",len(proc),"computers in total")
