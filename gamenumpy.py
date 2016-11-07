import numpy as np
from subprocess import call
call(["clear"])
size = input("How big do you want the Board: ")
call(["clear"])
boards= input("How many boards do you want: ")
call(["clear"])
world = np.empty((int(size),int(boards)), dtype=object)
p1score=0
p2score=0
winner=0
tie = False
for y in range(0,int(boards)):
        for x in range(0, int(size)):
             world[x][y] = "_"   
def placeTiles(tile, row, player):
        for x in range(0,int(size)):
                if(world[x][int(row)-1]=="_"):
                        world[x][int(row)-1] = str(player)
                        tile=int(tile)-1
                if(int(tile)==0):
                        break

def printBoards():
        for y in range(0,int(boards)):
                for x in range(0, int(size)):
                        print(world[x][y], end=' ')
                print("\n")
printBoards()
location = 0
player = 1
def checkBoards():
        for y in range(0, int(boards)):
                if(world[int(size)-1][y]=="_"):
                        return 1
        return 0
while(winner==0):
        tile = input("Player "+ str(player) +", how many tile do you want to put down: ")
        while (int(tile) != 1 and int(tile) != 2 ):
            tile = input("Please input 1 or 2: ")
        row = input("Player "+ str(player) +", what row do you want to change: ")
        while(int(row)>int(boards) or world[int(size)-1][int(row)-1]!="_"):
            row =input("Please enter a valid row.")
#        while(world[int(size)-1][int(row)-1]!="_"):
#            row = input("Please enter an available row: ")
            
        call(["clear"])
        placeTiles(tile, row, player)
        
        for y in range(0,int(boards)):
                if(world[int(size)-1][y] == "1"):
                        p1score=p1score+1
                        world[int(size)-1][y]="P1win"
                if(world[int(size)-1][y] == "2"):
                        p2score=p2score+1
                        world[int(size)-1][y]="P2win"
        if((p1score)>(float(boards)/2)):
            winner=1
        if((p2score)>(float(boards)/2)):
            winner=2
        printBoards()
        if(player==1):
                player=2
        else:
                player=1
        if (checkBoards() == 0 and (p1score == p2score)):
            tie = True
            winner = 4


if (tie == True):
    print("There is a tie!")
else:
    print("Player " + str(winner)+ " wins")
