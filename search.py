# Search = what name you are looking for in search


import csv

firstname = []
lastname = []
phone_num = []
email = []
dep = []
pos = []

flag = -1

search = input("What name are you looking for? ")

with open("Z:/Lab4c.txt") as csvfile:
    lab4c = csv.reader(csvfile)
    for row in lab4c:
        firstname.append(row[0])
        lastname.append(row[1])
        phone_num.append(row[2])
        email.append(row[3])
        dep.append(row[4])
        pos.append(row[5])


for index in range (0,len(pos)):
    if(lastname[index] == search):
        flag = index


if(flag == -1):
    print("Not found!!!")
else:
    print("We have found","  ",firstname[flag],"  ",lastname[flag],"  ",phone_num[flag],"  ",email[flag],"  ",dep[flag],"  ",pos[flag])

