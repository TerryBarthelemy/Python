import csv

ipaddress = []

def results():
    if(firstO >= "128"):
        if(firstO <= "191"):
            print(ipaddress[row][0],ipaddress[row][1],ipaddress[row][2],ipaddress[row][3],"is a Class B IP address with a Subnet Mask of 255.255.0.0")

with open("z:/ipaddress.txt") as csvfile:
    file = csv.reader(csvfile)
    for record in file:
      ipaddress.append(record[0].split("."))

for row in range(0, len(ipaddress)):
    firstO = ipaddress[row][0]
    results()
    

