import csv

lastname = []

def swap(n, t):
    temporary = n[t]
    n[t] = n[t + 1]
    n[t + 1] = temporary

with open("Z:/swap.txt") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        lastname.append(row[1])
    noe = len(lastname)

for b in range(0, noe - 1):
    for t in range(0, noe - 1):
        if(lastname[t] > lastname[t + 1]):
            swap(lastname, t)


for l in range(0, 5):
        print(lastname[l])

for l in range(noe - 5, noe):
        print(lastname[l])

