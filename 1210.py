from subprocess import call
call(["clear"])

select = input("C = Choose \n"
	+"N = Nah \n"+
	"Choose: ")
size = 10
if (select == "C"):
	size = input("How big do you want the Board: ")
world = [0 for x in range(int(size) + 1)]
def setup():
	for x in range(0,int(size)):
		world[x] = "_"

def printBoard():
	for x in range(0,int(size)):
		print(world[x], end=' ')
	print("\n")


def play1DSet():
	setup()
	printBoard()
	location = 0
	player = 1
	while(world[int(size)-1] == "_"):
		tile = input("Player 1, how many tile do you want to put down: ")
		while (int(tile) != 1 and int(tile) != 2):
			print("Please enter 1 or 2")
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
		while (int(tile) != 1 and int(tile) != 2):
			print("Please enter 1 or 2")
			tile = input("Player 2, how many tile do you want to put down: ")
		call(["clear"])
		for x in range(0,int(tile)):
			world[location] = "2"
			location += 1
		printBoard()
		player = 2
	print("Player " + str(player)+ " wins")

def play1DVari():
	setup()
	printBoard()
	location = 0
	player = 1
	while(world[int(size)-1] == "_"):
		tile = input("Player 1, how many tile do you want to put down: ")
		while (int(tile) != 1 and int(tile) != 2):
			print("Please enter 1 or 2")
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
		while (int(tile) != 1 and int(tile) != 2):
			print("Please enter 1 or 2")
			tile = input("Player 2, how many tile do you want to put down: ")
		call(["clear"])
		for x in range(0,int(tile)):
			world[location] = "2"
			location += 1
		printBoard()
		player = 2
	print("Player " + str(player)+ " wins")
if (select == "C"):
	play1DVari()
elif (select == "N"):
	play1DSet()
