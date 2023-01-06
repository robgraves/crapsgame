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
import data.graphics
from data import graphics


#path for userdata.p file
userdata = "data/userdata.p"
musicfile = "data/diceroll.mp3"


#Initializing the user database and loading if it exists,
#forcing creation of file if it doesn't exist to solve
#some issues encountered later
users_dict = {}
if os.path.exists(userdata):
	users_dict = pickle.load(open(userdata,"rb"))
else:
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
	#die1 		= random.randint(1,6)
	#die2 		= random.randint(1,6)
	die1 		= rng.randint(1,6)
	die2 		= rng.randint(1,6)
	diceresult 	= die1 + die2

    #Play dice rolling sound
	os.system("mpg123 -q " + musicfile + " > /dev/null 2>&1")
	#os.system("mplayer " + musicfile + " > /dev/null 2>&1")

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
	if choice == "1":
		print("Please enter your name:")
		username = input()
		if username == "" or None:
			print("WARNING: By not entering a name,")
			print("you may not be able to load your")
			print("saved game in the future.")
			input()
		bankroll = 1000
		return username
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


#Function to be used prior to quitting the game
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
def gameover():
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


#Function for handling free odds bets on Pass Line or Don't Pass
def freeodds_passdp(bets):
	global bankroll
	if point == 0:
		print("You cannot take free odds bets on a come out roll.")
		input()
		return(bets)
	elif bankroll == 0:
		print("You have no more money available to bet.")
		input()
		return(bets)
	else:
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


#Function for handling the Field Bet (a one roll bet)
#pays 2 to 1 for roll of 2, pays 3 to 1 for roll of 12
#pays 1 to 1 for rolls of 3, 4, 9, 10, and 11
#anything else is a loss.
def fieldbet(bets):
	global bankroll
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
	bankroll = bankroll - fieldbet
	bets.update({"field":(fieldbet + bets.get("field"))})
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
		print("6 - Place, Buy, and Lay Bets")
		print("7 - Hardway & Horn Bets")
		print("8 - Miscellaneous Bets")
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
	for key in bets:
		if bets[key] != 0:
			activebet = bets[key]
	if (bets.get('freeodds_pass4o10') != 0) or (bets.get('freeodds_pass5o9') != 0) or (bets.get('freeodds_pass6o8') != 0) or (bets.get('freeodds_dp4o10') != 0) or (bets.get('freeodds_dp5o9') !=0) or (bets.get('freeodds_dp6o8') != 0):
		freeoddsbet = activebet
		print("Free odds bets on table: $" + str(freeoddsbet))
	midbet_location = int(midbet_location)
	if midbet_location == 1:
		print("Shooter has the dice! No more bets!")
		input()
	if midbet_location == 2:
		bets = freeodds_passdp(bets)
	if midbet_location == 3:
		bets = fieldbet(bets)
	#if midbet_location == 4:
		#Come and Don't Come
	#if midbet_location == 5:
		#Free Odds on Come/Don't Come
	#if midbet_location == 6:
		#Place/Buy/Lay
	#if midbet_location == 7:
		#Hardway and Horn
	#if midbet_location == 8:
		#Miscellaneous Bets
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
mature = 0    #mature content is off by default

global point
point = 0
global bankroll
bankroll = 0
global bet_location
bet_location = "0"

bets = bets_init()
mature = maturecheck(mature)
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
		gameover()
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
		graphics.crapstable()
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
        #on 2 or 3, pushes if rolls 12 (BAR 12)
		elif result == 2 or result == 3 or result == 12:
			print("Shooter Craps Out!")
			print("bet location is : ", bet_location)
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
			input()
			os.system("clear")

		#Subsequent rolls if not a Come-Out roll
		while iscomeout == False:
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
			print("You rolled " + str(result))
			bets = midgamebet(bets)
			os.system("clear")
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
			print("Press any key to roll again.")
			input()
			result = dice()

			#Field bet payouts
			if result in (2,3,4,9,10,11,12):
				if (bets.get("field") != 0):
					print("Field bet Winner!!!")
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

			#Payoff for if shooter Sevens Out
			elif result == 7:
				print("Big Red!!! Shooter sevens out!")
				print("Pay the Don't Pass.")
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

##############################################
#
#
# End of File
#
#
##############################################
