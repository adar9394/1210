from subprocess import call
size = input("How big do you want the Board: ")
world = [0 for x in range(int(size) + 1)]
for x in range(0,int(size)):
	world[x] = "_"

def printBoard():
	for x in range(0,int(size)):
		print(world[x], end=' ')
	print("\n")
printBoard()
location = 0
player = 1
while(world[int(size)-1] == "_"):
	tile = input("Player 1, how many tile do you want to put down: ")
	call(["clear"])
	for x in range(0,int(tile)):
		world[location] = "1"
		location += 1
	printBoard()
	player = 1
	if(world[int(size)-1] != "_"):
		break
	tile = input("Player 2, how many tile do you want to put down: ")
	call(["clear"])
	for x in range(0,int(tile)):
		world[location] = "2"
		location += 1
	printBoard()
	player = 2
print("Player " + str(player)+ " wins")# 1210
