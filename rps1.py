# faith buford
# Rock paper scissors game 

#_________________________________________________________

# break into pieces 
# welcome screen, w/ name netry
# score screen with computer, player (name), ties
# options for game r, p, s, q
# game will loop until q is entered 
# each loop will get a random choice from the computer
# A choice from the player, compare the two, and update score 
# when the game is over, (q is entered), final score is displayed

# welcome page
# prompt for the player name 
# Welcome message 

#_________________________________________________________

# imports 
import random

# variables // keep them all in one place
playerScore = 0
computerScore = 0
ties = 0 
# make a list
cChoices = ["r", "p", "s"]

print("welcome to Rock paper scissors")
name = input("Enter your name: ")
# main loop
while True:
	# print score
	print("score: ")
	print("Computer: " + str(computerScore))
	print(name + ": " + str(playerScore))
	print("Ties: " + str(ties))
	choice = input("Enter 'r' for Rock, 'p' for Paper, 's' for scissors or 'q' to quit: ")
	computerChoice = random.choice(cChoices)
	print(computerChoice)
	if choice == "q": 
		break

	if choice == "r":
		print(name + " picked rock ")
		if computerChoice == "r": # tie
			print("computer picked rock")
			print("this is a tie")
			ties = ties + 1
		elif computerChoice == "p":
			print("computer picked paper")
			print("paper beats rock")
			computerScore += 1
		elif computerChoice == "s":
			print("computer picked scissors")
			print("rock beats scissors")
			playerScore += 1 
	
	elif choice == "p":
		print(name + " picked paper")
		if computerChoice == "r":
			print("computer picked rock")
			print("paper beats rock")
			playerScore += 1
		elif computerChoice == "p":
			print("computer picked paper")
			print("this is a tie")
			ties = ties + 1
		elif computerChoice == "s":
			print("computer picked scissors")
			print("scissors beats paper")
			computerScore += 1
	
	elif choice == "s":
		print(name + "picekd scissors")
		if computerChoice == "r":
			print("computer picked rock")
			print("rock beats scissors")
			computerScore += 1 
		elif computerChoice == "p":
			print("computer picked paper")
			print("scissors beats paper")
			playerScore += 1
		elif computerChoice == "s":
			print("computer picked scissors")
			print("this is a tie")
			ties = ties + 1
	else: # type something not on the list
		pass





