#!/usr/bin/env python3
#
# Matthew Page 07/02/2019  12/26/2022
#
# craps.py	-	My first attempt at making a command line
#				craps game.
#


#Importing stuff
import os
import random
import pickle


#Initializing the user database and loading if it exists
users_dict = {}
if os.path.exists("userdata.p"):
	users_dict = pickle.load(open("userdata.p","rb"))


#Function that rolls two dice
def dice():
	if point == 0:
		print("Point is not set.")
	else:
		print("Point is : ", point)
	print("Rolling the dice...")
	die1 		= random.randint(1,6)
	die2 		= random.randint(1,6)
	diceresult 	= die1 + die2 	
	print(str(die1) + " " + str(die2))
	print("You rolled : ", diceresult)
	return diceresult


#Function that displays Intro screen
def intro():
	print("Welcome to Matt's Craps Game!!!")
	print("       .-------.    ______     ")
	print("      /   o   /|   /\     \    ")
	print("     /_______/o|  /o \  o  \   ")
	print("     | o     | | /   o\_____\  ")
	print("     |   o   |o/ \o   /o    /  ")
	print("     |     o |/   \ o/  o  /   ")
	print("     '-------'     \/____o/    ")
	print("                               ")
	print("   Created by Matthew J. Page  ")
	print("         robgraves  2022       ")
	print("       me@matthewjpage.com     ")
	print("                               ")


#Function that draws the craps table in ASCII art
def crapstable():
	print(" __ ___  ____________________                      ")
	print("|N |  d||DC| 4| 5| 6| 8| 9|10| +---------------+   ")
	print("|o |P o||__|__|__|__|__|__|__| |any seven   4-1|   ")
	print("|  |A n| ____________________  +===============+   ")
	print("|C |S t||     C O M E        | |hard 4 | hard 6|   ")
	print("|a |S p||____________________| |-------+-------|   ")
	print("|l |L a| ____________________  |hard 10| hard 8|   ")
	print("|l |I s||2  3 4  9  10 11  12| +===============+   ")
	print("|  |N s||_______FIELD________| |two    |  three|   ")
	print("|B |E  |_____________________  |-----HORN------|   ")
	print("|e |       don't pass bar    | |eleven | twelve|   ")
	print("|t  \_________PASS_LINE______| +===============+   ")
	print("|s                           | |  any    craps |   ")
	print(" \________No Call Bets_______| |    7 to 1     |   ")
	print("                               +---------------+   ")


#Function that draws the craps table in ASCII art
def crapstable4():
	print(" __ ___  ____________________                      ")
	print("|N |  d||DC| 4| 5| 6| 8| 9|10| +---------------+   ")
	print("|o |P o||__|ON|__|__|__|__|__| |any seven   4-1|   ")
	print("|  |A n| ____________________  +===============+   ")
	print("|C |S t||     C O M E        | |hard 4 | hard 6|   ")
	print("|a |S p||____________________| |-------+-------|   ")
	print("|l |L a| ____________________  |hard 10| hard 8|   ")
	print("|l |I s||2  3 4  9  10 11  12| +===============+   ")
	print("|  |N s||_______FIELD________| |two    |  three|   ")
	print("|B |E  |_____________________  |-----HORN------|   ")
	print("|e |       don't pass bar    | |eleven | twelve|   ")
	print("|t  \_________PASS_LINE______| +===============+   ")
	print("|s                           | |  any    craps |   ")
	print(" \________No Call Bets_______| |    7 to 1     |   ")
	print("                               +---------------+   ")


#Function that draws the craps table in ASCII art
def crapstable5():
	print(" __ ___  ____________________                      ")
	print("|N |  d||DC| 4| 5| 6| 8| 9|10| +---------------+   ")
	print("|o |P o||__|__|ON|__|__|__|__| |any seven   4-1|   ")
	print("|  |A n| ____________________  +===============+   ")
	print("|C |S t||     C O M E        | |hard 4 | hard 6|   ")
	print("|a |S p||____________________| |-------+-------|   ")
	print("|l |L a| ____________________  |hard 10| hard 8|   ")
	print("|l |I s||2  3 4  9  10 11  12| +===============+   ")
	print("|  |N s||_______FIELD________| |two    |  three|   ")
	print("|B |E  |_____________________  |-----HORN------|   ")
	print("|e |       don't pass bar    | |eleven | twelve|   ")
	print("|t  \_________PASS_LINE______| +===============+   ")
	print("|s                           | |  any    craps |   ")
	print(" \________No Call Bets_______| |    7 to 1     |   ")
	print("                               +---------------+   ")


#Function that draws the craps table in ASCII art
def crapstable6():
	print(" __ ___  ____________________                      ")
	print("|N |  d||DC| 4| 5| 6| 8| 9|10| +---------------+   ")
	print("|o |P o||__|__|__|ON|__|__|__| |any seven   4-1|   ")
	print("|  |A n| ____________________  +===============+   ")
	print("|C |S t||     C O M E        | |hard 4 | hard 6|   ")
	print("|a |S p||____________________| |-------+-------|   ")
	print("|l |L a| ____________________  |hard 10| hard 8|   ")
	print("|l |I s||2  3 4  9  10 11  12| +===============+   ")
	print("|  |N s||_______FIELD________| |two    |  three|   ")
	print("|B |E  |_____________________  |-----HORN------|   ")
	print("|e |       don't pass bar    | |eleven | twelve|   ")
	print("|t  \_________PASS_LINE______| +===============+   ")
	print("|s                           | |  any    craps |   ")
	print(" \________No Call Bets_______| |    7 to 1     |   ")
	print("                               +---------------+   ")


#Function that draws the craps table in ASCII art
def crapstable8():
	print(" __ ___  ____________________                      ")
	print("|N |  d||DC| 4| 5| 6| 8| 9|10| +---------------+   ")
	print("|o |P o||__|__|__|__|ON|__|__| |any seven   4-1|   ")
	print("|  |A n| ____________________  +===============+   ")
	print("|C |S t||     C O M E        | |hard 4 | hard 6|   ")
	print("|a |S p||____________________| |-------+-------|   ")
	print("|l |L a| ____________________  |hard 10| hard 8|   ")
	print("|l |I s||2  3 4  9  10 11  12| +===============+   ")
	print("|  |N s||_______FIELD________| |two    |  three|   ")
	print("|B |E  |_____________________  |-----HORN------|   ")
	print("|e |       don't pass bar    | |eleven | twelve|   ")
	print("|t  \_________PASS_LINE______| +===============+   ")
	print("|s                           | |  any    craps |   ")
	print(" \________No Call Bets_______| |    7 to 1     |   ")
	print("                               +---------------+   ")


#Function that draws the craps table in ASCII art
def crapstable9():
	print(" __ ___  ____________________                      ")
	print("|N |  d||DC| 4| 5| 6| 8| 9|10| +---------------+   ")
	print("|o |P o||__|__|__|__|__|ON|__| |any seven   4-1|   ")
	print("|  |A n| ____________________  +===============+   ")
	print("|C |S t||     C O M E        | |hard 4 | hard 6|   ")
	print("|a |S p||____________________| |-------+-------|   ")
	print("|l |L a| ____________________  |hard 10| hard 8|   ")
	print("|l |I s||2  3 4  9  10 11  12| +===============+   ")
	print("|  |N s||_______FIELD________| |two    |  three|   ")
	print("|B |E  |_____________________  |-----HORN------|   ")
	print("|e |       don't pass bar    | |eleven | twelve|   ")
	print("|t  \_________PASS_LINE______| +===============+   ")
	print("|s                           | |  any    craps |   ")
	print(" \________No Call Bets_______| |    7 to 1     |   ")
	print("                               +---------------+   ")


#Function that draws the craps table in ASCII art
def crapstable10():
	print(" __ ___  ____________________                      ")
	print("|N |  d||DC| 4| 5| 6| 8| 9|10| +---------------+   ")
	print("|o |P o||__|__|__|__|__|__|ON| |any seven   4-1|   ")
	print("|  |A n| ____________________  +===============+   ")
	print("|C |S t||     C O M E        | |hard 4 | hard 6|   ")
	print("|a |S p||____________________| |-------+-------|   ")
	print("|l |L a| ____________________  |hard 10| hard 8|   ")
	print("|l |I s||2  3 4  9  10 11  12| +===============+   ")
	print("|  |N s||_______FIELD________| |two    |  three|   ")
	print("|B |E  |_____________________  |-----HORN------|   ")
	print("|e |       don't pass bar    | |eleven | twelve|   ")
	print("|t  \_________PASS_LINE______| +===============+   ")
	print("|s                           | |  any    craps |   ")
	print(" \________No Call Bets_______| |    7 to 1     |   ")
	print("                               +---------------+   ")


#Function to display a one on a die in ASCII
def dieface1():
	print("     ___     ")
	print("    |   |    ")
	print("    | o |    ")
	print("    |___|    ")
	print("             ")

#Function to display a two on a die in ASCII
def dieface2():
	print("     ___     ")
	print("    |o  |    ")
	print("    |   |    ")
	print("    |__o|    ")
	print("             ")


#Function to display a three on a die in ASCII
def dieface3():
	print("     ___     ")
	print("    |o  |    ")
	print("    | o |    ")
	print("    |__o|    ")
	print("             ")


#Function to display a four on a die in ASCII
def dieface4():
	print("     ___     ")
	print("    |o o|    ")
	print("    |   |    ")
	print("    |o_o|    ")
	print("             ")


#Function to display a five on a die in ASCII
def dieface5():
	print("     ___     ")
	print("    |o o|    ")
	print("    | o |    ")
	print("    |o_o|    ")
	print("             ")


#Function to display a six on a die in ASCII
def dieface6():
	print("     ___     ")
	print("    |o o|    ")
	print("    |o o|    ")
	print("    |o_o|    ")
	print("             ")


#Function for creating or loading user and their bankroll
def player():
	choice = "0"
	global bankroll
	while choice not in ("1","2"):
		print("Are you a new or returning player?")
		print("1 - New Player")
		print("2 - Returning Player")
		choice = input()
		if choice not in ("1","2"):
			print("ERROR: Bad choice! Invalid entry!")
	if choice == "1":
		print("Please enter your name:")
		username = input()
		bankroll = 1000
		return username		
	if choice == "2":
		print("Please enter your name:")
		username = input()
		saveduser = pickle.load(open("userdata.p","rb"))
		bankroll = saveduser.get(username)
	return username


#Function to be used prior to quitting the game
def save(users_dict):
	global bankroll
	users_dict[username] = bankroll
	pickle.dump(users_dict, open("userdata.p","wb"))


#Function for endgame/gameover if bankroll hits 0
def gameover():
	os.system("clear");
	print("******************************\n\n")
	print("       You are broke!\n\n")
	print("******************************\n")
	print("     G A M E  O V E R!!!\n\n")
	print("******************************\n\n")
	print("**** Terminal Craps Game ****")
	print("** written by Matthew Page **")
	print("**** me@matthewjpage.com ****\n\n")
	print("******************************\n")
	print("To play again, choose New User")
	print("and use the same name to reset")
	print("your bankroll.\n") 
	quitflag = True
	return quitflag


#Script starts here
os.system("clear")
intro()
global point
point = 0
global bankroll
bankroll = 0
username = player()
print("Welcome " + username + "!!!")
print("Your bankroll is: " + str(bankroll))
save(users_dict)
os.system("clear")


#Main Game Loop
quitflag = False
while quitflag == False:
	
	#Pre Come-Out roll bet
	print("Your current bankroll is: " + str(bankroll))

	#Get bet location
	bet_location = "0"
	crapstable()
	if bankroll == 0:
		quitflag = gameover()
		break
	while bet_location not in ("1","2","3"):
		print("Enter a bet location: ")
		print("1 - Pass Line (Bet with the shooter)")
		print("2 - Don't Pass Line (Bet with the house)")
		print("3 - Quit Game")
		bet_location = input()
		if bet_location in ("1","2","3"):
			break
		else:
			print("Invalid entry!")
	if bet_location == "3":
		quitflag = True
		break
	print("You chose " + bet_location)
	bet_location = int(bet_location)

	#Get bet amount
	print("Enter a bet amount: ")
	bet_amount = 0
	while not int(bet_amount) in range(1, bankroll+1):
		if bet_amount > bankroll:
			print("You do not have that much.")
			print("Your current bankroll is: " + str(bankroll))
			print("Enter a bet amount: ")
		try:
			bet_amount = int(input())
		except ValueError:
			print("Error: Invalid entry. Please enter a number.")
			continue
	print("You chose " + str(bet_amount))
	bankroll = bankroll - bet_amount
	os.system("clear")
	print("Your current bankroll is: " + str(bankroll))
	save(users_dict)

	#The Come-Out roll
	iscomeout = True
	while iscomeout == True:
		crapstable()
		print("Press any key to roll.")
		input()
		result = dice()
		#If 7 or 11 Pass bettors win, Don't Pass loses
		if result == 7 or result == 11:
			print("Shooter Wins!!!")
			print("bet location is : ", bet_location)
			if bet_location == 1:
				bankroll = (bankroll + (bet_amount * 2))
			save(users_dict)
			iscomeout = True
			point = 0
			input()
			os.system("clear")
			break
		#If 2, 3, or 12 Pass bettors lose, Don't Pass wins
		elif result == 2 or result == 3 or result == 12:
			print("Shooter Craps Out!")
			print("bet location is : ", bet_location)
			if bet_location == 2:
				bankroll = (bankroll + (bet_amount * 2))
			save(users_dict)
			iscomeout = True
			point = 0
			input()
			os.system("clear")
			break
		#Anything else becomes the point (4, 5, 6, 8, 9, 10)
		else:
			point = result
			print("The point is now " + str(point))
			#If point is established we change come-out roll state
			iscomeout = False
			save(users_dict)
			input()
			os.system("clear")

		#Subsequent rolls if not a Come-Out roll
		while iscomeout == False:
			os.system("clear")
			print("Your current bankroll is: " + str(bankroll))
			if point == 4:
				crapstable4()
			elif point == 5:
				crapstable5()
			elif point == 6:
				crapstable6()
			elif point == 8:
				crapstable8()
			elif point == 9:
				crapstable9()
			elif point == 10:
				crapstable10()
			print("You rolled " + str(result))
			print("Press any key to roll again.")
			input()
			result = dice()
			if result == point:
				print("Shooter hits the point!!!")
				print("Pass Line Wins!!!")
				print("bet location is : ", bet_location)
				if bet_location == 1:
					bankroll = (bankroll + (bet_amount * 2))
				save(users_dict)
				iscomeout = True
				point = 0
				input()
				os.system("clear")
				break
			elif result == 7:
				print("Seven!!! Shooter loses!")
				print("Pass Line loses.")
				print("bet location is : ", bet_location)
				if bet_location == 2:
					bankroll = (bankroll + (bet_amount * 2))
				save(users_dict)
				iscomeout = True
				point = 0
				input()
				os.system("clear")
				break
		break

#End of File
