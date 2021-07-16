#whichrow - Which row to sit in
#whichseat - Which seat to sit in
#try another seat - request another seat

def wr():
    whichrow = int(input("what row would you like to sit in? "))
    return (whichrow)

def ws():
    whichseat = input("What seat would you like to sit in? ")
    return (whichseat)

def display_seat_map(aA, aB, aC, aD):    
    for r in range (1, 8):        
        print("   ", r,  " ", aA[r]," ", aB[r], "   ", aC[r], " ", aD[r])

def tas():
    try_another_seat = input("Would you like to try another seat Sir/Ma'am? ")
    return (try_another_seat)


aisleA = ["","A","A","A","A","A","A","A"]
aisleB = ["","B","B","B","B","B","B","B"]
aisleC = ["","C","C","C","C","C","C","C"]
aisleD = ["","D","D","D","D","D","D","D"]

try_another_s = "y"
while(try_another_s == "y"):
    whichrow = wr()
    whichseat = ws()
    if(aisleA[whichrow] == "A" and whichseat == "A"):
        aisleA[whichrow] = "X"
    elif(aisleB[whichrow] == "B" and whichseat == "B"):
        aisleB[whichrow] = "X"
    elif(aisleC[whichrow] == "C"and whichseat == "C"):
        aisleC[whichrow] = "X"
    elif(aisleD[whichrow] == "D" and whichseat == "D"):
        aisleD[whichrow] = "X"
    else:
        print('Sorry! This seat is already taken.')
    display_seat_map(aisleA, aisleB, aisleC, aisleD)
    try_another_s = tas()
