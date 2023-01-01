#!/usr/bin/env python3
#
# Matthew Page 07/02/2019, 12/26/2022
#
# craps.py	-	My first attempt at making a command line
#				craps game.
#
#				12/28/2022 - First fully playable version
#				of the game with only Pass/Don't Pass
#				betting options.
#


#Importing stuff
import sys
import os
import math
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
	rng = random.SystemRandom()	
	#die1 		= random.randint(1,6)
	#die2 		= random.randint(1,6)
	die1 		= rng.randint(1,6)
	die2 		= rng.randint(1,6)
	diceresult 	= die1 + die2 	
	#Display proper ASCII art for each dieface for die 1
	if die1 == 1:
		dieface1()
	elif die1 == 2:
		dieface2()
	elif die1 == 3:
		dieface3()
	elif die1 == 4:
		dieface4()
	elif die1 == 5:
		dieface5()
	elif die1 == 6:
		dieface6()
	#Display proper ASCII art for each dieface for die 2
	if die2 == 1:
		dieface1()
	elif die2 == 2:
		dieface2()
	elif die2 == 3:
		dieface3()
	elif die2 == 4:
		dieface4()
	elif die2 == 5:
		dieface5()
	elif die2 == 6:
		dieface6()
	print(str(die1) + " " + str(die2))
	print("You rolled : ", diceresult)
	return diceresult


#Function that displays Intro screen
def intro():
	print("Welcome to Terminal Craps Game!!!")
	print("       .-------.    ______       ")
	print("      /   o   /|   /\     \      ")
	print("     /_______/o|  /o \  o  \     ")
	print("     | o     | | /   o\_____\    ")
	print("     |   o   |o/ \o   /o    /    ")
	print("     |     o |/   \ o/  o  /     ")
	print("     '-------'     \/____o/      ")
	print("                                 ")
	print("   Created by Matthew J. Page    ")
	print("         robgraves  2022         ")
	print("       me@matthewjpage.com       ")
	print("                                 ")


#Function that draws the craps table in ASCII art, come-out roll
def crapstable():
	print(" __ ___  ____________________  (OFF)               ")
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


#Function that draws the craps table in ASCII art, point is 4
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


#Function that draws the craps table in ASCII art, point is 5
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


#Function that draws the craps table in ASCII art, point is 6
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


#Function that draws the craps table in ASCII art, point is 8
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


#Function that draws the craps table in ASCII art, point is 9
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


#Function that draws the craps table in ASCII art, point is 10
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


#Function for implementing Mike's idea for ways to make
#money if you go broke
def shady():
	os.system("clear")
	print("A shady looking middle-aged man approaches")	
	print('you and he says, "I notice you are broke."')
	print("                                          ")
	print("You are a little unsure if you can trust  ")
	print("him. But you let him continue.            ")
	print("                                          ")
	print('He goes on, "...I have a way for you to   ')
	print('make some money if you follow me          ')
	print('out back."                                ')
	choice = "0"
	global bankroll
	while choice not in ("1","2"):
		print("Do you follow the shady man out back?     ")	
		print("1 - Yes")
		print("2 - No")
		choice = input()
		if choice not in ("1","2"):
			print("ERROR: Bad choice! Invalid entry!")
	if choice == "1":
		print("The man has you go behind the dumpster")
		print("with him and he drops his pants...    ")
		input()
		os.system("clear")
		print("...15 minutes later")
		print("You have made 20 dollars")
		bankroll = 20
		return bankroll	
	if choice == "2":
		print("You decide not to follow the man.")
	return bankroll


#Function for endgame/gameover if bankroll hits 0
def gameover():
	os.system("clear")
	print("******************************\n\n")
	if bankroll == 0:
		print("       You are broke!\n\n")
	else:
		print("                     \n\n")
	print("******************************\n")
	print("     G A M E  O V E R!!!\n\n")
	print("******************************\n\n")
	print("**** Terminal Craps Game ****")
	print("** written by Matthew Page **")
	print("**** me@matthewjpage.com ****\n\n")
	print("******************************\n")
	if bankroll == 0:
		print("To play again, choose New User")
		print("and use the same name to reset")
		print("your bankroll.                \n") 
	else:
		print("To play again, choose Returning")
		print("User and use the same name to  ")
		print("use your saved bankroll.       \n") 
	save(users_dict)
	sys.exit()
	quitflag = True
	return quitflag


#Function to initialize bets dictionary
def bets_init():
	bets = {
	"freeodds_pass4o10":0,	#can be made after point established, odds 2 to 1
	"freeodds_pass5o9":0,	#can be made after point established, odds 3 to 2
	"freeodds_pass6o8":0,	#can be made after point established, odds 6 to 5
	"freeodds_dp4o10":0,	#can be made after point established, odds 1 to 2
	"freeodds_dp5o9":0, 	#can be made after point established, odds 2 to 3
	"freeodds_dp6o8":0, 	#can be made after point established, odds 5 to 6
	"freeodds_come4":0,		#can be made after point established, odds 2 to 1
	"freeodds_come5":0,		#can be made after point established, odds 3 to 2
	"freeodds_come6":0,		#can be made after point established, odds 6 to 5
	"freeodds_come8":0,		#can be made after point established, odds 6 to 5
	"freeodds_come9":0,		#can be made after point established, odds 3 to 2
	"freeodds_come10":0,	#can be made after point established, odds 2 to 1
	"freeodds_dc4":0,		#can be made after point established, odds 1 to 2 
	"freeodds_dc5":0,		#can be made after point established, odds 2 to 3
	"freeodds_dc6":0,		#can be made after point established, odds 5 to 6
	"freeodds_dc8":0,		#can be made after point established, odds 5 to 6
	"freeodds_dc9":0,		#can be made after point established, odds 2 to 3
	"freeodds_dc10":0,		#can be made after point established, odds 1 to 2
	"come":0,				#acts like pass line, but bet turns into next roll buy bet
	"dc":0,					#acts like don't pass line, but bet turns into next roll lay bet
	"field":0,				#roll 2 is 2 to 1, roll 12 is 3 to 1, everything else is 1 to 1
	"buy4":0,				#odds 2 to 1
	"lay4":0,				#odds 1 to 2
	"buy5":0,				#odds 3 to 2
	"lay5":0,				#odds 2 to 3
	"buy6":0,				#odds 6 to 5
	"lay6":0,				#odds 5 to 6
	"buy8":0,				#odds 6 to 5
	"lay8":0,				#odds 5 to 6
	"buy9":0,				#odds 3 to 2
	"lay9":0,				#odds 2 to 3
	"buy10":0,				#odds 2 to 1
	"lay10":0,				#odds 1 to 2
	"hardway6":0,			#odds 9 to 1
	"hardway8":0,			#odds 9 to 1
	"hardway4":0,			#odds 7 to 1
	"hardway10":0,			#odds 7 to 1
	"anyseven":0,			#odds 4 to 1
	"anycraps":0,			#odds 7 to 1
	"horn11":0,				#odds 15 to 1 YO-leven!!!
	"horn12":0,				#odds 30 to 1
	"horn3":0,				#odds 15 to 1
	"horn2":0				#odds 30 to 1
	}
	return bets


#Function to clear out mid game betting 
def clearbets(bets):
	bets.clear()
	bets = bets_init()
	return bets


def freeodds_passdp(bets):
	if point == 0:
		print("You cannot take free odds bets on a come out roll.")
		input()
		return(bets)
	else:
		global bankroll
		if bet_location == 1:
			print("Your current bankroll is: $" + str(bankroll))
			print("point is " + str(point))
			print("Take odds on Pass Line wager.")
			#Get bet amount
			print("Enter odds bet: ")
			oddsbet = 0
			while not int(oddsbet) in range(1, bankroll+1):
				if oddsbet > bankroll:
					print("You do not have that much.")
					print("Your current bankroll is: $" + str(bankroll))
					print("Enter a bet amount: ")
				try:
					oddsbet = int(input())
				except ValueError:
					print("Error: Invalid entry. Please enter a number.")
					continue
			print("You chose " + str(oddsbet))
			bankroll = bankroll - oddsbet
			if point == 4 or point == 10:
				bets.update({"freeodds_pass4o10":(oddsbet + bets.get("freeodds_pass4o10"))})
			if point == 5 or point == 9:
				bets.update({"freeodds_pass5o9":(oddsbet + bets.get("freeodds_pass5o9"))})
			if point == 6 or point == 8:
				bets.update({"freeodds_pass6o8":(oddsbet + bets.get("freeodds_pass6o8"))})
			os.system("clear")
			print("Your current bankroll is: $" + str(bankroll))
			save(users_dict)
			#print(bets)   					##FOR TESTING
			#input()						##FOR TESTING
		if bet_location == 2:
			print("Your current bankroll is: $" + str(bankroll))
			print("point is " + str(point)) 
			print("Take odds on Don't Pass wager.")
			#Get bet amount
			print("Enter odds bet: ")
			oddsbet = 0
			while not int(oddsbet) in range(1, bankroll+1):
				if oddsbet > bankroll:
					print("You do not have that much.")
					print("Your current bankroll is: $" + str(bankroll))
					print("Enter a bet amount: ")
				try:
					oddsbet = int(input())
				except ValueError:
					print("Error: Invalid entry. Please enter a number.")
					continue
			print("You chose " + str(oddsbet))
			bankroll = bankroll - oddsbet
			if point == 4 or point == 10:
				bets.update({"freeodds_dp4o10":(oddsbet + bets.get("freeodds_dp4o10"))})
			if point == 5 or point == 9:
				bets.update({"freeodds_dp5o9":(oddsbet + bets.get("freeodds_dp5o9"))})
			if point == 6 or point == 8:
				bets.update({"freeodds_dp6o8":(oddsbet + bets.get("freeodds_dp6o8"))})
			os.system("clear")
			print("Your current bankroll is: $" + str(bankroll))
			save(users_dict)
			#print(bets)   					##FOR TESTING
			#input()						##FOR TESTING
	return bets


#Function for mid game betting
def midgamebet(bets):
	midbet_location = "0"
	while midbet_location not in ("1","2","3","4","5","6","7","8","9"):
		print("Enter a bet location: ")
		print("1 - No More Bets - Roll Dice")
		print("2 - Free Odds Bets on Pass or Don't Pass")
		print("3 - Field Bet")
		print("4 - Come or Don't Come Bets")
		print("5 - Free Odds Bets on Come or Don't Come")
		print("6 - Buy Bets")
		print("7 - Lay Bets")
		print("8 - Hardway & Horn Bets")
		print("9 - Quit Game")
		midbet_location = input()
		if midbet_location in ("1","2","3","4","5","6","7","8","9"):
			break
		else:
			print("Invalid entry!")
	if midbet_location == "9":
		confirm = "0"
		while confirm not in ("Y","N","y","n"):
			print("Are you sure? (Y/N) All bets on the table will be lost.")
			confirm = input()
			if confirm in ("Y","N","y","n"):
				break
			else:
				 print("Invalid entry!")	
		if confirm == "Y" or confirm == "y":
			gameover()
		elif confirm == "N" or confirm == "n":
			print("Returning to game")
			return(bets)
	print("You chose " + midbet_location)
	for key in bets:												# These three lines won't work once I add
		if bets[key] != 0:											# more bets to game.  I may need to make
			print("Free odds bets on table: " + str(bets[key]))		# this loop more complicated.
	midbet_location = int(midbet_location)
	if midbet_location == 1:
		print("Shooter has the dice! No more bets!")
		input()
	if midbet_location == 2:
		bets = freeodds_passdp(bets)
	return bets


#Script starts here
os.system("clear")
intro()
global point
point = 0
global bankroll
bankroll = 0
global bet_location
bet_location = "0"
bets = bets_init()
username = player()
print("Welcome " + username + "!!!")
print("Your bankroll is: $" + str(bankroll))
save(users_dict)
os.system("clear")


#Main Game Loop
quitflag = False
while quitflag == False:
	
	#Pre Come-Out roll bet
	print("Your current bankroll is: $" + str(bankroll))

	#Get bet location
	bet_location = "0"
	crapstable()
	#insert function call here for mikes idea function if broke
	if bankroll == 0:
		shady()		
	if bankroll == 0:
		gameover()
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
			print("Your current bankroll is: $" + str(bankroll))
			print("Enter a bet amount: ")
		try:
			bet_amount = int(input())
		except ValueError:
			print("Error: Invalid entry. Please enter a number.")
			continue
	print("You chose " + str(bet_amount))
	bankroll = bankroll - bet_amount
	os.system("clear")
	print("Your current bankroll is: $" + str(bankroll))
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
			print("Your current bankroll is: $" + str(bankroll))
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
			bets = midgamebet(bets)
			os.system("clear")
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
			print("Press any key to roll again.")
			input()
			result = dice()
			input()
			if result == point:
				print("Shooter hits the point!!!")
				print("Pass Line Wins!!!")
				print("bet location is : ", bet_location)
				if bet_location == 1:
					bankroll = (bankroll + (bet_amount * 2))
					#Checking for free odds bets on passline points and payouts
					if bets.get("freeodds_pass4o10") != 0: 
						bankroll = (bankroll + math.floor((bets.get("freeodds_pass4o10") * 1)/2) + bets.get("freeodds_pass4o10"))
						bets.update({"freeodds_pass4o10":0})
					if bets.get("freeodds_pass5o9") != 0: 
						bankroll = (bankroll + math.floor((bets.get("freeodds_pass5o9") * 2)/3) + bets.get("freeodds_pass5o9"))
						bets.update({"freeodds_pass5o9":0})
					if bets.get("freeodds_pass6o8") != 0: 
						bankroll = (bankroll + math.floor((bets.get("freeodds_pass6o8") * 5)/6) + bets.get("freeodds_pass6o8"))
						bets.update({"freeodds_pass6o8":0})
				#Clearing free odds bets for don't pass losses
				bets.update({"freeodds_dp4o10":0})
				bets.update({"freeodds_dp5o9":0})
				bets.update({"freeodds_dp6o8":0})
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
					#Checking for free odds bets on don't pass points and payouts
					if bets.get("freeodds_dp4o10") != 0: 
						bankroll = (bankroll + math.floor((bets.get("freeodds_dp4o10") * 2)/1) + bets.get("freeodds_dp4o10"))
						bets.update({"freeodds_dp4o10":0})
					if bets.get("freeodds_dp5o9") != 0: 
						bankroll = (bankroll + math.floor((bets.get("freeodds_dp5o9") * 3)/2) + bets.get("freeodds_dp5o9"))
						bets.update({"freeodds_dp5o9":0})
					if bets.get("freeodds_dp6o8") != 0: 
						bankroll = (bankroll + math.floor((bets.get("freeodds_dp6o8") * 6)/5) + bets.get("freeodds_dp6o8"))
						bets.update({"freeodds_dp6o8":0})
				#Clearing free odds bets for passline losses
				bets.update({"freeodds_pass4o10":0})
				bets.update({"freeodds_pass5o9":0})
				bets.update({"freeodds_pass6o8":0})
				save(users_dict)
				iscomeout = True
				point = 0
				input()
				os.system("clear")
				break
		break

#End of File
