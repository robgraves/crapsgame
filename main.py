#!/usr/bin/env python3
#
# Matthew Page 07/02/2019, 12/26/2022
#
# main.py	-	My first attempt at making a command line
#				craps game.
#
#				12/28/2022 - First fully playable version
#				of the game with only Pass/Don't Pass
#				betting options.
#
##########################################################



############################################
#
#
# Importing stuff and other setup
#
#
############################################
import sys
import os
import math
import random
import pickle
import data.graphics.graphics
from data.graphics import graphics


#path for files used
userdata 		= "data/save/userdata.p"
dicesound 		= "data/sounds/diceroll.mp3"
awwsound		= "data/sounds/aww.mp3"
#applausesound	= "data/sounds/applause.wav"
applausesound	= "data/sounds/claps.mp3"
winsound		= "data/sounds/chips.mp3"
gruntsound 		= "data/sounds/grunt.mp3"

#Initializing the user database and loading if it exists,
#forcing creation of file if it doesn't exist to solve
#some issues encountered later
users_dict = {}
if os.path.exists(userdata):
	users_dict = pickle.load(open(userdata,"rb"))
else:
	os.system("mkdir -p data/save")
	users_dict = {"dealer":1000000}
pickle.dump(users_dict, open(userdata,"wb"))


############################################
#
#
#  Function definitions
#
#
#############################################

#Function that rolls two dice
def dice():
	if point == 0:
		print("Point is not set.")
	else:
		print("Point is : ", point)
	print("Rolling the dice...")
	rng = random.SystemRandom()
	die1 		= rng.randint(1,6)
	die2 		= rng.randint(1,6)
	diceresult 	= die1 + die2

    #Play dice rolling sound
	os.system("mplayer " + dicesound + " > /dev/null 2>&1")

	#Display proper ASCII art for each dieface for die 1
	if die1 == 1:
		graphics.dieface1()
	elif die1 == 2:
		graphics.dieface2()
	elif die1 == 3:
		graphics.dieface3()
	elif die1 == 4:
		graphics.dieface4()
	elif die1 == 5:
		graphics.dieface5()
	elif die1 == 6:
		graphics.dieface6()
	#Display proper ASCII art for each dieface for die 2
	if die2 == 1:
		graphics.dieface1()
	elif die2 == 2:
		graphics.dieface2()
	elif die2 == 3:
		graphics.dieface3()
	elif die2 == 4:
		graphics.dieface4()
	elif die2 == 5:
		graphics.dieface5()
	elif die2 == 6:
		graphics.dieface6()
	print(str(die1) + " " + str(die2))
	print("You rolled : ", diceresult)
	return diceresult


#Function for creating or loading user and their bankroll
def player():
	choice = "0"
	saveduser = None
	global bankroll
	while choice not in ("1","2"):
		print("Are you a new or returning player?")
		print("1 - New Player")
		print("2 - Returning Player")
		choice = input()
		if choice not in ("1","2"):
			print("ERROR: Bad choice! Invalid entry!")
	#Create new player
	if choice == "1":
		print("Please enter your name:")
		username = input()
		try:
			saveduser = pickle.load(open(userdata,"rb"))
			bankroll = saveduser.get(username)
			#if former player who busted, rebankroll
			if bankroll == 0 or bankroll == None:
				bankroll = 1000
				return username
			else:
				choice2 = "0"
				#Preventing overwriting of existing player
				while choice2 not in ("Y","y","N","n"):
					print("This player already exists.") 
					print("Would you like to overwrite the existing player?")
					choice2 = input("Y/N?")
					if choice2 == "N" or choice2 == "n":
						choice3 = "0"
						#If player exist, give option to load player
						while choice3 not in ("Y","y","N","n"):
							print("Would you like to load this player?")
							choice3 = input("Y/N?")
							#Quits out of game if player doesn't want to load
							#existing player, sending 1 signal to gameover()
							#doesn't save in the gameover() function
							if choice3 == "N" or choice3 == "n":
								gameover(1)
							elif choice3 == "Y" or choice3 == "y":
								return username
							if choice3 not in ("Y","y","N","n"):
								print("ERROR: Bad choice! Invalid entry!")
						return username
					#Allows user to overwrite existing player for whatever reason
					elif choice2 == "Y" or choice2 == "y":
						bankroll = 1000
						return username
					if choice2 not in ("Y","y","N","n"):
						print("ERROR: Bad choice! Invalid entry!")
		except FileNotFoundError:
			print("Error: File does not exist. Please create a New Player.")
		#Allows you to play with no name but warns you that you won't
		#be able to load the player in future gaming sessions
		if username == "" or None:
			print("WARNING: By not entering a name,")
			print("you may not be able to load your")
			print("saved game in the future.")
			input()
		bankroll = 1000
		return username
	#Loading existing user and their bankroll
	if choice == "2":
		print("Please enter your name:")
		username = input()
		try:
			saveduser = pickle.load(open(userdata,"rb"))
			bankroll = saveduser.get(username)
		except FileNotFoundError:
			print("Error: File does not exist. Please create a New Player.")
		while saveduser.get(username) == None:
			print("This user doesn't exist.")
			print("Please select New Player.")
			input()
			username = player()
			return username
	return username


#Saving player data
#Function to be used prior to quitting the game
#Also after every payout and loss, to prevent 
#quitting program to cheat.
def save(users_dict):
	global bankroll
	users_dict[username] = bankroll
	pickle.dump(users_dict, open(userdata,"wb"))


#Function to check if player wants mature content
def maturecheck(mature):
	choice = "0"
	while choice not in ("1","2"):
		print("Do you want to play with G rated or Mature Content?")
		print("1 - G-rated")
		print("2 - Mature")
		choice = input()
		if choice not in ("1","2"):
			print("ERROR: Bad choice! Invalid entry!")
	if choice == "1":
		mature = 0
		return mature
	if choice == "2":
		mature = 1
	return mature


#Function to display craps table, depending on come-out
#roll or what the established point is
def table():
	global bankroll
	global bet_location
	global bet_amount
	global point
	freeoddsbet = 0
	os.system("clear")
	print("Your current bankroll is: $" + str(bankroll))
	if point == 4:
		graphics.crapstable4()
	elif point == 5:
		graphics.crapstable5()
	elif point == 6:
		graphics.crapstable6()
	elif point == 8:
		graphics.crapstable8()
	elif point == 9:
		graphics.crapstable9()
	elif point == 10:
		graphics.crapstable10()
	#Display current Pass or Don't Pass bet
	if bet_location == 1:
		print("Pass: $" + str(bet_amount))
	if bet_location == 2:
		print("DP: $" + str(bet_amount))
	#Display current Odds bet if there is one
	if (bets.get('freeodds_pass4o10') != 0) or (bets.get('freeodds_pass5o9') != 0) or (bets.get('freeodds_pass6o8') != 0) or (bets.get('freeodds_dp4o10') != 0) or (bets.get('freeodds_dp5o9') !=0) or (bets.get('freeodds_dp6o8') != 0):
		if (point == 4) or (point == 10):
			freeoddsbet = (bets.get('freeodds_pass4o10') + bets.get('freeodds_dp4o10'))
		if (point == 5) or (point == 9):
			freeoddsbet = (bets.get('freeodds_pass5o9') + bets.get('freeodds_dp5o9'))
		if (point == 6) or (point == 8):
			freeoddsbet = (bets.get('freeodds_pass6o8') + bets.get('freeodds_dp6o8'))
		print("Odds: $" + str(freeoddsbet))
	#Display current Field bet if there is one
	if bets.get("field") != 0:
		print("Field: $" + str(bets.get("field")))
	#Display numbers you have money on and their 
	#respective amount of bets 
	#Not doing these individually because typically
	#people only play place, buy, or lay, not any combination
	#of those types of bets, e.g. if betting place, may have multiple place numbers
	#but no buy or lays bets 
	if  (bets.get("place4") != 0) or (bets.get("buy4") != 0) or (bets.get("lay4") != 0):
		fourtotal = bets.get("place4") + bets.get("buy4") +  bets.get("lay4")
		print("Four: $" + str(fourtotal))		
	if  (bets.get("place5") != 0) or (bets.get("buy5") != 0) or (bets.get("lay5") != 0):
		fivetotal = bets.get("place5") + bets.get("buy5") +  bets.get("lay5")
		print("Five: $" + str(fivetotal))		
	if  (bets.get("place6") != 0) or (bets.get("buy6") != 0) or (bets.get("lay6") != 0):
		sixtotal = bets.get("place6") + bets.get("buy6") +  bets.get("lay6")
		print("Six: $" + str(sixtotal))		
	if  (bets.get("place8") != 0) or (bets.get("buy8") != 0) or (bets.get("lay8") != 0):
		eighttotal = bets.get("place8") + bets.get("buy8") +  bets.get("lay8")
		print("Eight: $" + str(eighttotal))		
	if  (bets.get("place9") != 0) or (bets.get("buy9") != 0) or (bets.get("lay9") != 0):
		ninetotal = bets.get("place9") + bets.get("buy9") +  bets.get("lay9")
		print("Nine: $" + str(ninetotal))		
	if  (bets.get("place10") != 0) or (bets.get("buy10") != 0) or (bets.get("lay10") != 0):
		tentotal = bets.get("place4") + bets.get("buy4") +  bets.get("lay4")
		print("Ten: $" + str(tentotal))		


#Function for implementing Mike's idea for ways to make
#money if you go broke, only works if you chose M-rated
#at the start of game.
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
		os.system("mplayer " + gruntsound + " > /dev/null 2>&1")
		input()
		print("...15 minutes later")
		print("You have made 20 dollars")
		bankroll = 20
		input()
		os.system("clear")
		return bankroll
	if choice == "2":
		print("You decide not to follow the man.")
	return bankroll


#Function for endgame/gameover if bankroll hits 0
#0 to save, 1 to not save as input to function
def gameover(int):
	os.system("clear")
	print("******************************\n\n")
	if bankroll == 0:
		print("       You are broke!\n\n")
	else:
		print("      Come back soon!!\n\n")
	if bankroll == 0:
		print("******************************\n")
		print("     G A M E  O V E R!!!\n\n")
		print("******************************\n\n")
	else:
		graphics.cactus()
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
	if int == 0:
		save(users_dict)
	sys.exit()
	quitflag = True
	return quitflag


#Function to initialize bets dictionary
def bets_init():
	bets = {
    #########################################################################
    #
    # Bets Dictionary holds all bets except for Pass/Don't Pass wagers
    #
    #########################################################################
    #     Odds are x to y where y is bet and payoff is ((y * x) + y)
    #in the case of division resulting in fractional results, the payout is
    #round`ed down (math.floor) for the house advantage.
    #     Come and Don't Come behaves like a Pass/Don't Pass mid game creating
    #come points,  your bet will move to the come point (4,5,6,8,9,10) if next
    #roll isn't a 7,11 (win on come bet) or 2,3,12 (loss on come bet),
    #also a roll of 12 on don't pass or don't come bets is a push (BAR 12),
    #at this point any come points win if they are hit before a 7 comes out
    #again, don't come wins if shooter Sevens Out.
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
	"come":0,				#acts like pass line, but bet turns into buy bet sort of
	"dc":0,					#acts like don't pass line, but bet turns into lay bet sort of
	"field":0,				#roll 2 is 2 to 1, roll 12 is 3 to 1, everything else is 1 to 1
    "place4":0,             #hit 4 before shooter loses, odds 9 to 5
    "place5":0,             #hit 5 before shooter loses, odds 7 to 5
    "place6":0,             #hit 6 before shooter loses, odds 7 to 6
    "place8":0,             #hit 8 before shooter loses, odds 7 to 6
    "place9":0,             #hit 9 before shooter loses, odds 7 to 5
    "place10":0,            #hit 10 before shooter loses, odds 9 to 5
	"buy4":0,				#odds 2 to 1 buy bets pay 5% commission from winnings
	"lay4":0,				#odds 1 to 2 lay bets pay 5% commission when betting
	"buy5":0,				#odds 3 to 2 buy bets pay 5% commission from winnings
	"lay5":0,				#odds 2 to 3 lay bets pay 5% commission when betting
	"buy6":0,				#odds 6 to 5 buy bets pay 5% commission from winnings
	"lay6":0,				#odds 5 to 6 lay bets pay 5% commission when betting
	"buy8":0,				#odds 6 to 5 buy bets pay 5% commission from winnings
	"lay8":0,				#odds 5 to 6 lay bets pay 5% commission when betting
	"buy9":0,				#odds 3 to 2 buy bets pay 5% commission from winnings
	"lay9":0,				#odds 2 to 3 lay bets pay 5% commission when betting
	"buy10":0,				#odds 2 to 1 buy bets pay 5% commission from winnings
	"lay10":0,				#odds 1 to 2 lay bets pay 5% commission when betting
	"hardway6":0,			#odds 9 to 1
	"hardway8":0,			#odds 9 to 1
	"hardway4":0,			#odds 7 to 1
	"hardway10":0,			#odds 7 to 1
	"anyseven":0,			#odds 4 to 1
	"anycraps":0,			#odds 7 to 1
	"horn11":0,				#odds 15 to 1 YO-leven!!!
	"horn12":0,				#odds 30 to 1
	"horn3":0,				#odds 15 to 1
	"horn2":0,				#odds 30 to 1
    "big6":0,               #some craps tables have these, odds 1 to 1
    "big8":0,               #some craps tables have these, odds 1 to 1
    "C&E":0                 #craps-eleven, same as any craps plus 11, pays same as
	}                       #the individual bets, any craps (7 to 1) & YO11 (15 to 1)
	return bets


#Function to clear out mid game betting
def clearbets(bets):
	bets.clear()
	bets = bets_init()
	return bets

####################################################
#
#    Function for handling free odds bets on
# Pass Line or Don't Pass. These are paid at
# true odds with no commission.  This is actually
# the bet with the  lowest house advantage bet
# in the entire casino.
#
####################################################
def freeodds_passdp(bets):
	global bankroll
	#this scenario (point == 0) never happens in the game's current 
	#state as this function is never called in a come-out roll
	#but is there for future proofing if ever make it so players
	#have all bets available as choices at all times in the game
	if point == 0:
		print("You cannot take free odds bets on a come out roll.")
		input()
		return(bets)
	#Check for out of money
	elif bankroll == 0:
		print("You have no more money available to bet.")
		input()
		table()
		return(bets)
	else:
		#Odds on Pass Line wager
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
			#Placing Freeodds bet and putting on relevant number
			#I combined the keys for 4 and 10, 5 and 9, and 8 and 6, as they have the same
			#odds and payouts
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

		#Odds on Don't Pass wager
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
			#Placing Freeodds bet and putting on relevant number
			#I combined the keys for 4 and 10, 5 and 9, and 8 and 6, as they have the same
			#odds and payouts
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
	table()
	return bets


#######################################################
#
# Function for handling the Field Bet (a one roll bet)
# pays 2 to 1 for roll of 2, pays 3 to 1 for roll of 12
# pays 1 to 1 for rolls of 3, 4, 9, 10, and 11
# anything else is a loss.
#
#######################################################
def fieldbet(bets):
	global bankroll
	#Check for out of money and return if so
	if bankroll == 0:
		print("You have no more money available to bet.")
		input()
		table()
		return(bets)
	print("Your current bankroll is: $" + str(bankroll))
	#Get bet amount
	print("Enter amount to bet on the Field: ")
	fieldbet = 0
	while not int(fieldbet) in range(1, bankroll+1):
		if fieldbet > bankroll:
			print("You do not have that much.")
			print("Your current bankroll is: $" + str(bankroll))
			print("Enter a bet amount: ")
		try:
			fieldbet = int(input())
		except ValueError:
			print("Error: Invalid entry. Please enter a number.")
			continue
	print("You chose " + str(fieldbet))
	#Take field bet from bankroll and updating the bet dictionary
	bankroll = bankroll - fieldbet
	bets.update({"field":(fieldbet + bets.get("field"))})
	os.system("clear")
	print("Your current bankroll is: $" + str(bankroll))
	save(users_dict)
	#print(bets)   					##FOR TESTING
	#input()						##FOR TESTING
	table()
	return bets


#Function defining Place Bets
def place(bets):
	global bankroll
	#Check for out of money and return if so
	if bankroll == 0:
		print("You have no more money available to bet.")
		input()
		table()
		return(bets)
	global placeselect
	print("Your current bankroll is: $" + str(bankroll))
	placebet_location = "0"
	#The only way to get out of the Place bet submenu is to type B or b for Back as
	#many players will bet on multiple numbers here allowing you to place every number
	#desired and then go back to main bet menu when finished.
	#Also includes a Takedown option as a seven will wipe all these bets and they are
	#not contract bets (bets you are stuck with once you make them (Pass and Come bets)
	#so players can choose to takedown or turn off these bets at any point to protect it
	#from the inevitable shooter Sevening Out
	while placebet_location != "B" or placebet_location != "b":
		while placebet_location not in ("Q","q","B","b","T","t","4","5","6","8","9","10"):
			print("Choose where to place your bet: ")
			print("4  - Place 4")
			print("5  - Place 5")
			print("6  - Place 6")
			print("8  - Place 8")
			print("9  - Place 9")
			print("10 - Place 10")
			print("T  - Take down a bet")
			print("B  - Back")
			print("Q  - Quit Game")
			placebet_location = input()
			if placebet_location in ("Q","q","B","b","T","t","4","5","6","8","9","10"):
				break
			else:
				print("Invalid entry!")
		print("You chose " + placebet_location)

		#Allow for quitting game at every menu but warning player that there are still
		#live bets on the table and quitting now would surrender those bets to the house
		if placebet_location == "Q" or placebet_location == "q":
			confirm = "0"
			while confirm not in ("Y","N","y","n"):
				print("Are you sure? (Y/N) All bets on the table will be lost.")
				confirm = input()
				if confirm in ("Y","N","y","n"):
					break
				else:
					 print("Invalid entry!")
			#sending gameover function the 0 signal
			#to ensure saving
			if confirm == "Y" or confirm == "y":
				gameover(0)
			elif confirm == "N" or confirm == "n":
				print("Returning to game")
				table()
				return(bets)

		#Return if player chooses Back
		if placebet_location == "B" or placebet_location == "b":
			table()
			return(bets)

		#Takedown bets submenu
		if placebet_location == "T" or placebet_location == "t":
			print("Which bet do you want to take down?")
			if bets.get("place4") != 0:
				print("4  - Take down bet on the 4")
			if bets.get("place5") != 0:
				print("5  - Take down bet on the 5")
			if bets.get("place6") != 0:
				print("6  - Take down bet on the 6")
			if bets.get("place8") != 0:
				print("8  - Take down bet on the 8")
			if bets.get("place9") != 0:
				print("9  - Take down bet on the 9")
			if bets.get("place10") != 0:
				print("10 - Take down bet on the 10")
			#Take user input and takedown relevant bet
			takedownbet = input()
			if takedownbet == "4":
				bankroll = bankroll + bets.get("place4")
				bets.update({"place4":0})
			if takedownbet == "5":
				bankroll = bankroll + bets.get("place5")
				bets.update({"place5":0})
			if takedownbet == "6":
				bankroll = bankroll + bets.get("place6")
				bets.update({"place6":0})
			if takedownbet == "8":
				bankroll = bankroll + bets.get("place8")
				bets.update({"place8":0})
			if takedownbet == "9":
				bankroll = bankroll + bets.get("place9")
				bets.update({"place9":0})
			if takedownbet == "10":
				bankroll = bankroll + bets.get("place10")
				bets.update({"place10":0})
			print("Your current bankroll is: $" + str(bankroll))
			break
		#Get bet amount
		print("Enter bet amount: ")
		placebet = 0
		while not int(placebet) in range(1, bankroll+1):
			if placebet > bankroll:
				print("You do not have that much.")
				print("Your current bankroll is: $" + str(bankroll))
				print("Enter a bet amount: ")
			try:
				placebet = int(input())
			except ValueError:
				print("Error: Invalid entry. Please enter a number.")
				continue
		print("You chose " + str(placebet))
		#Take place bet and based on number chosen update betting dictionary
		#for that number
		bankroll = bankroll - placebet
		os.system("clear")
		print("Your current bankroll is: $" + str(bankroll))
		save(users_dict)
		if placebet_location == "4":
			placeselect[0] = 4	
			bets.update({"place4":(placebet + bets.get("place4"))})
			placebet_location = "0"
		if placebet_location == "5":
			placeselect[1] = 5	
			bets.update({"place5":(placebet + bets.get("place5"))})
			placebet_location = "0"
		if placebet_location == "6":
			placeselect[2] = 6	
			bets.update({"place6":(placebet + bets.get("place6"))})
			placebet_location = "0"
		if placebet_location == "8":
			placeselect[3] = 8	
			bets.update({"place8":(placebet + bets.get("place8"))})
			placebet_location = "0"
		if placebet_location == "9":
			placeselect[4] = 9	
			bets.update({"place9":(placebet + bets.get("place9"))})
			placebet_location = "0"
		if placebet_location == "10":
			placeselect[5] = 10	
			bets.update({"place10":(placebet + bets.get("place10"))})
			placebet_location = "0"
		table()
	print("You chose " + placebet_location)
	table()
	return bets


#Function defining Buy Bets
def buy(bets):
	#BUY BET FUNCTION 
    return bets


#Function defining Lay Bets
def lay(bets):
	#LAY BET FUNCTION
    return bets


############################################################
#
#    Function for handling Place, Buy, and Lay Bets
# These are essentially betting that certain numbers
# will show up before a shooter Sevens Out (in the case
# of Place and Buy Bets) or that a shooter Sevens Out
# before said number is rolled (Lay Bets)
#
#    Place and Buy are essentially betting with the shooter
# whereas Lay is against the shooter.
# The Difference between Place and Buy is Buy gets true
# odds but has to pay a 5% commission on the winnings
# Place Bets behave the same with no commission but
# lower odds payouts.
#
#    Lay Bets behave like the opposite of Buy bets, where
# player pays a 5% commission, but it is payed up front
# Possible numbers for Place, Buy and Lay Bets are the
# point numbers: 4, 5, 6, 8, 9, and 10
#
#    These are all multi-roll bets, like Pass/DP and
# Come/DC, as they stay until either the shooter Sevens Out
# or the number hits, all other dice resuts don't affect
# these bets.
#
###########################################################
def placebuylay(bets):
	pblbet_location = "0"
	#Submenu to choose Place, Buy, or Lay bets
	while pblbet_location not in ("1","2","3","B","b","Q","q"):
		print("Choose one: ")
		print("1 - Place Bets")
		print("2 - Buy Bets")
		print("3 - Lay Bets")
		print("B - Back")
		print("Q - Quit Game")
		pblbet_location = input()
		if pblbet_location in ("1","2","3","B","b","Q","q"):
			break
		else:
			print("Invalid entry!")
	#Allow for quitting game at every menu but warning player that there are still
	#live bets on the table and quitting now would surrender those bets to the house
	if pblbet_location == "Q" or pblbet_location == "q":
		confirm = "0"
		while confirm not in ("Y","N","y","n"):
			print("Are you sure? (Y/N) All bets on the table will be lost.")
			confirm = input()
			if confirm in ("Y","N","y","n"):
				break
			else:
				 print("Invalid entry!")
		if confirm == "Y" or confirm == "y":
			gameover(0)
		elif confirm == "N" or confirm == "n":
			print("Returning to game")
			table()
			return(bets)
	#Depending on user input go to next submenu function
	#for place(), buy() and lay() bets
	if pblbet_location == "1":
		bets = place(bets)
		return(bets)
	if pblbet_location == "2":
		bets = buy(bets)
		return(bets)
	if pblbet_location == "3":
		bets = lay(bets)
		return(bets)
	#Allow user to back out without committing to any of
	#these bets
	if pblbet_location == "B" or pblbet_location == "b":
		table()
		return(bets)
	print("You chose " + pblbet_location)
	return bets


#Function for mid game betting
def midgamebet(bets):
	midbet_location = "0"
	#print(bets)   					##FOR TESTING
	#input()						##FOR TESTING
	#Main Menu for mid-game betting (not the Come-Out roll)
	while midbet_location != "1":
		while midbet_location not in ("1","2","3","4","5","6","7","8","9",""):
			print("Enter a bet location: ")
			print("1 - No More Bets - Roll Dice")
			print("2 - Free Odds Bets on Pass or Don't Pass")
			print("3 - Field Bet")
			print("4 - Come or Don't Come Bets")
			print("5 - Free Odds Bets on Come or Don't Come")
			print("6 - Place, Buy, and Lay Bets")
			print("7 - Hardway & Horn Bets")
			print("8 - Miscellaneous Bets")
			print("9 - Quit Game")
			midbet_location = input()
			if midbet_location in ("1","2","3","4","5","6","7","8","9",""):
				break
			else:
				print("Invalid entry!")
		#Allow for quitting game at every menu but warning player that there are still
		#live bets on the table and quitting now would surrender those bets to the house
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
				gameover(0)
			elif confirm == "N" or confirm == "n":
				print("Returning to game")
				return(bets)
		#Checking if user just presses Enter to roll dice
		if midbet_location == "":
			print("Shooter has the dice! No more bets!")
			input()
			break
		print("You chose " + midbet_location)
		midbet_location = int(midbet_location)
		#Choosing 1 always continues the game to the next roll
		if midbet_location == 1:
			print("Shooter has the dice! No more bets!")
			input()
			break
		#Choosing 2 allows player to make an Odds bet
		if midbet_location == 2:
			#Free odds on Pass or Don't Pass
			bets = freeodds_passdp(bets)
		#Choosing 3 allows player to make the Field bet
		if midbet_location == 3:
			#Field Bet
			bets = fieldbet(bets)
		#Choosing 4 allows player to bet on Come or Don't Come
		if midbet_location == 4:
			#Come and Don't Come
			print("Come/Don't Come bets here") #Deleting when written
			#DOING LAST
			#bets = comedc(bets)
		#Choosing 5 allows player to bet Odds on Come points or
		#Don't Come points 
		if midbet_location == 5:
			#Free Odds on Come/Don't Come
			print("Free Odds onCome/Don't Come bets here") #Deleting when written
			#DOING LAST
			#bets = freeodds_comedc(bets)
		#Choosing 6 allows player to bet on place numbers, buy numbers,
		#or lay numbers
		if midbet_location == 6:
			#Place/Buy/Lay
			bets = placebuylay(bets)
		#Choosing 7 allows player to bet on the Hardways or Horn Bets
		if midbet_location == 7:
			#Hardway and Horn
			print("Hardway and Horn bets here") #Deleting when written
			#bets = hardwayhorn(bets)
		#Choosing 8 allows players to make other bets (Big6, Big8, C&E, World,
		#and anything else I come up with or think about)
		if midbet_location == 8:
			#Miscellaneous Bets
			print("Other bets here") #Deleting when written
			#bets = otherbets(bets)
	return bets


#############################################
#
#
#  Script starts here
#
#
#############################################

os.system("clear")
graphics.intro()

#mature content is off by default
mature = 0

#Established point if there is one
#Can be 4, 5, 6, 8, 9 or 10
global point
point = 0
#Player's bankroll
global bankroll
bankroll = 0
#bet_location is Pass/Don't Pass bet
#1 for Pass, 2 for Don't Pass
global bet_location
bet_location = "0"
#List for Place bets
#Need to check against results
global placeselect
placeselect = [0,0,0,0,0,0]

bets = bets_init()
mature = maturecheck(mature)
username = player()
print("Welcome " + username + "!!!")
print("Your bankroll is: $" + str(bankroll))
save(users_dict)
os.system("clear")

#############################################
#
#
# Main Game Loop
#
#
#############################################
quitflag = False
while quitflag == False:

	#Pre Come-Out roll bet
	print("Your current bankroll is: $" + str(bankroll))

	if bankroll == None:
		break
	#Get bet location
	bet_location = "0"
	graphics.crapstable()
	#checking for easter egg if user chose mature content at start
	if bankroll == 0:
		if mature == 1:
			shady()
			print("Your current bankroll is: $" + str(bankroll))
			graphics.crapstable()
	if bankroll == 0:
		gameover(0)
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
		gameover(0)
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

    #########################################
    #
	# The Come-Out roll
    #
    #########################################
	iscomeout = True
	while iscomeout == True:
		graphics.crapstable()
		print("Press any key to roll.")
		input()
		result = dice()
		#If 7 or 11 Pass bettors win, Don't Pass loses
		if result == 7 or result == 11:
			print("Shooter Wins!!!")
			os.system("mplayer " + applausesound + " > /dev/null 2>&1")
			os.system("mplayer " + winsound + " > /dev/null 2>&1")
			#print("bet location is : ", bet_location)
			if bet_location == 1:
				bankroll = (bankroll + (bet_amount * 2))
			save(users_dict)
			iscomeout = True
			point = 0
			input()
			os.system("clear")
			break
		#If 2, 3, or 12 Pass bettors lose, Don't Pass wins
        #on 2 or 3, pushes if rolls 12 (BAR 12)
		elif result == 2 or result == 3 or result == 12:
			print("Shooter Craps Out!")
			os.system("mplayer " + awwsound + " > /dev/null 2>&1 &")
			#print("bet location is : ", bet_location)
			if bet_location == 2:
				if result == 2 or result == 3:
					bankroll = (bankroll + (bet_amount * 2))
				if result == 12:
					bankroll = (bankroll + bet_amount)
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

			#Place bet payouts on come-out roll, for previous place bets
			if bets.get("place4") != 0:
				if placeselect[0] == result:
					bankroll = (bankroll + math.floor((bets.get("place4") * 9)/5) + bets.get("place4"))
					bets.update({"place4":0})
			if bets.get("place5") != 0:
				if placeselect[1] == result:
					bankroll = (bankroll + math.floor((bets.get("place5") * 7)/5) + bets.get("place5"))
					bets.update({"place5":0})
			if bets.get("place6") != 0:
				if placeselect[2] == result:
					bankroll = (bankroll + math.floor((bets.get("place6") * 7)/6) + bets.get("place6"))
					bets.update({"place6":0})
			if bets.get("place8") != 0:
				if placeselect[3] == result:
					bankroll = (bankroll + math.floor((bets.get("place8") * 7)/6) + bets.get("place8"))
					bets.update({"place8":0})
			if bets.get("place9") != 0:
				if placeselect[4] == result:
					bankroll = (bankroll + math.floor((bets.get("place9") * 7)/5) + bets.get("place9"))
					bets.update({"place9":0})
			if bets.get("place10") != 0:
				if placeselect[5] == result:
					bankroll = (bankroll + math.floor((bets.get("place10") * 9)/5) + bets.get("place10"))
					bets.update({"place10":0})
			save(users_dict)

			input()
			os.system("clear")

        #########################################
        #
		# Subsequent rolls if not a Come-Out roll
        #
        #########################################
		while iscomeout == False:
			table()
			print("You rolled " + str(result))
			bets = midgamebet(bets)
			table()
			print("Press any key to roll again.")
			input()
			result = dice()


			#Place bet payouts on non come-out rolls, maybe I'll make this a function
			if bets.get("place4") != 0:
				if placeselect[0] == result:
					bankroll = (bankroll + math.floor((bets.get("place4") * 9)/5) + bets.get("place4"))
					os.system("mplayer " + winsound + " > /dev/null 2>&1 &")
					bets.update({"place4":0})
			if bets.get("place5") != 0:
				if placeselect[1] == result:
					bankroll = (bankroll + math.floor((bets.get("place5") * 7)/5) + bets.get("place5"))
					os.system("mplayer " + winsound + " > /dev/null 2>&1 &")
					bets.update({"place5":0})
			if bets.get("place6") != 0:
				if placeselect[2] == result:
					bankroll = (bankroll + math.floor((bets.get("place6") * 7)/6) + bets.get("place6"))
					os.system("mplayer " + winsound + " > /dev/null 2>&1 &")
					bets.update({"place6":0})
			if bets.get("place8") != 0:
				if placeselect[3] == result:
					bankroll = (bankroll + math.floor((bets.get("place8") * 7)/6) + bets.get("place8"))
					os.system("mplayer " + winsound + " > /dev/null 2>&1 &")
					bets.update({"place8":0})
			if bets.get("place9") != 0:
				if placeselect[4] == result:
					bankroll = (bankroll + math.floor((bets.get("place9") * 7)/5) + bets.get("place9"))
					os.system("mplayer " + winsound + " > /dev/null 2>&1 &")
					bets.update({"place9":0})
			if bets.get("place10") != 0:
				if placeselect[5] == result:
					bankroll = (bankroll + math.floor((bets.get("place10") * 9)/5) + bets.get("place10"))
					os.system("mplayer " + winsound + " > /dev/null 2>&1 &")
					bets.update({"place10":0})
			save(users_dict)

			#Field bet payouts
			if result in (2,3,4,9,10,11,12):
				if (bets.get("field") != 0):
					print("Field bet Winner!!!")
					os.system("mplayer " + winsound + " > /dev/null 2>&1 &")
					if result == 2:
						bankroll = (bankroll + (bets.get("field") * 3))
						bets.update({"field":0})
					elif result == 12:
						bankroll = (bankroll + (bets.get("field") * 4))
						bets.update({"field":0})
					elif result in (3,4,9,10,11):
						bankroll = (bankroll + (bets.get("field") * 2))
						bets.update({"field":0})
					else:
						bets.update({"field":0})
			else:
				bets.update({"field":0})
			input()

			#Payoff for shooter hitting the point
			if result == point:
				print("Shooter hits the point!!!")
				print("Front Line Winner!!!")
				os.system("mplayer " + applausesound + " > /dev/null 2>&1")
				os.system("mplayer " + winsound + " > /dev/null 2>&1")
				#print("bet location is : ", bet_location)
				if bet_location == 1:
					bankroll = (bankroll + (bet_amount * 2))
					#Checking for free odds bets on passline points and payouts
					if bets.get("freeodds_pass4o10") != 0:
						bankroll = (bankroll + math.floor((bets.get("freeodds_pass4o10") * 2)/1) + bets.get("freeodds_pass4o10"))
						bets.update({"freeodds_pass4o10":0})
					if bets.get("freeodds_pass5o9") != 0:
						bankroll = (bankroll + math.floor((bets.get("freeodds_pass5o9") * 3)/2) + bets.get("freeodds_pass5o9"))
						bets.update({"freeodds_pass5o9":0})
					if bets.get("freeodds_pass6o8") != 0:
						bankroll = (bankroll + math.floor((bets.get("freeodds_pass6o8") * 6)/5) + bets.get("freeodds_pass6o8"))
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

			#Payoff for if shooter Sevens Out
			elif result == 7:
				print("Big Red!!! Shooter sevens out!")
				print("Pay the Don't Pass.")
				os.system("mplayer " + awwsound + " > /dev/null 2>&1 &")
				#print("bet location is : ", bet_location)
				if bet_location == 2:
					bankroll = (bankroll + (bet_amount * 2))
					#Checking for free odds bets on don't pass points and payouts
					if bets.get("freeodds_dp4o10") != 0:
						bankroll = (bankroll + math.floor((bets.get("freeodds_dp4o10") * 1)/2) + bets.get("freeodds_dp4o10"))
						bets.update({"freeodds_dp4o10":0})
					if bets.get("freeodds_dp5o9") != 0:
						bankroll = (bankroll + math.floor((bets.get("freeodds_dp5o9") * 2)/3) + bets.get("freeodds_dp5o9"))
						bets.update({"freeodds_dp5o9":0})
					if bets.get("freeodds_dp6o8") != 0:
						bankroll = (bankroll + math.floor((bets.get("freeodds_dp6o8") * 5)/6) + bets.get("freeodds_dp6o8"))
						bets.update({"freeodds_dp6o8":0})

				#Clearing free odds bets for passline losses
				bets.update({"freeodds_pass4o10":0})
				bets.update({"freeodds_pass5o9":0})
				bets.update({"freeodds_pass6o8":0})
				save(users_dict)

				#Clearing place bets on Seven Out
				bets.update({"place4":0})
				bets.update({"place5":0})
				bets.update({"place6":0})
				bets.update({"place8":0})
				bets.update({"place9":0})
				bets.update({"place10":0})
				save(users_dict)

				iscomeout = True
				point = 0
				input()
				os.system("clear")
				break
		break

##############################################
#
#
# End of File
#
#
##############################################
