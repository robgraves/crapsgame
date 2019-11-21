#!/usr/bin/env python3
#
# Matthew Page 07/02/2019
#
# craps.py	-	my first attempt at making a command line
#				craps game.
#

import os
import random
import pickle

##Testing save and load function	
#users_dict = {"Dan":250, "Thomas":1500}
#pickle.dump(users_dict, open("userdata.p","wb"))

users_dict = {}
if os.path.exists("userdata.p"):
	users_dict = pickle.load(open("userdata.p","rb"))

def dice():
	print("Rolling the dice...")
	die1 		= random.randint(1,6)
	die2 		= random.randint(1,6)
	diceresult 	= die1 + die2 	
	print(str(die1) + " " + str(die2))
	return diceresult

def intro():
	print("Welcome to Matt's Craps Game!!!")
	print("       .-------.    ______     ")
	print("      /   o   /|   /\     \    ")
	print("     /_______/o|  /o \  o  \   ")
	print("     | o     | | /   o\_____\  ")
	print("     |   o   |o/ \o   /o    /  ")
	print("     |     o |/   \ o/  o  /   ")
	print("     '-------'     \/____o/    ")

def crapstable():
	print(" ___  ____________________                      ")
	print("|  d||DC| 4| 5| 6| 8| 9|10| +---------------+   ")
	print("|P o||__|__|__|__|__|__|__| |any seven   4-1|   ")
	print("|A n| ____________________  +===============+   ")
	print("|S t||     C O M E        | |hard 4 | hard 6|   ")
	print("|S p||____________________| |-------+-------|   ")
	print("|L a| ____________________  |hard 10| hard 8|   ")
	print("|I s||2  3 4  9  10 11  12| +===============+   ")
	print("|N s||_______FIELD________| |two    |  three|   ")
	print("|E  |_____________________  |-----HORN------|   ")
	print("|       don't pass bar    | |eleven | twelve|   ")
	print(" \_________PASS_LINE______| +===============+   ")
	print("                           |  any    craps |    ")
	print("                           +---------------+    ")


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

##I think this function is dead now, probably will delete
#def bet_pass(bankroll):
#	print("Enter a bet location: ")
#	print("1 - Pass Line (Bet with the shooter)")
#	print("2 - Don't Pass Line (Bet with the house)")
#	bet_location = input()
#	print("Enter a bet amount: ")
#	bet_amount = input()


#Script starts here
intro()
bankroll = 0
username = player()
print("Welcome " + username + "!!!")
print("Your bankroll is: " + str(bankroll))
save(users_dict)

##testing craps table output
#print("Press any key to show the craps table.")
#input()
#crapstable()

##Pre Come-Out roll bet
print("Your current bankroll is: " + str(bankroll))

##Get bet location
#print("Enter a bet location: ")
#print("1 - Pass Line (Bet with the shooter)")
#print("2 - Don't Pass Line (Bet with the house)")
bet_location = "0"
#while not int(bet_location) in range(1,3):
while bet_location not in ("1","2"):
	print("Enter a bet location: ")
	print("1 - Pass Line (Bet with the shooter)")
	print("2 - Don't Pass Line (Bet with the house)")
	bet_location = input()
	if bet_location in ("1","2"):
		break
	else:
		print("Invalid entry!")
	#try:
	#	bet_location = int(input())
	#except ValueError:
	#	print("Error: Invalid entry.  Enter 1 or 2")
	#if bet_location > 2:
	#	print("Error: Invalid entry.  Enter 1 or 2")
	#	continue
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
print("Your current bankroll is: " + str(bankroll))
save(users_dict)

##Actual come-out roll
iscomeout = True
while iscomeout == True:
	print("Press any key to roll.")
	input()
	result = dice()
	#If 7 or 11 Pass bettors win, Don't Pass loses
	if result == 7 or result == 11:
		print("Shooter Wins!!!")
		iscomeout = True
	elif result == 2 or result == 3 or result == 12:
		print("Shooter Craps Out!")
		iscomeout = True
	else:
		point = result
		print("The point is now " + str(result))
		iscomeout = False

	#If 2, 3, or 12 Pass bettors lose, Don't Pass wins
	#Anything else becomes the point (4, 5, 6, 8, 9, 10)
	#If point is established we change come-out roll state

	#iscomeout = False
	while iscomeout == False:
		print("Press any key to roll again.")
		input()
		result = dice()
		if result == point:
			print("Shooter hits the point!!!")
			print("Pass Line Wins!!!")
			iscomeout = True
		elif result == 7:
			print("Seven!!! Shooter loses!")
			print("Pass Line loses.")
			iscomeout = True
		else:
			continue

##Random roll for no reason
#print("Press any key to roll the dice.")
#input()
#result = dice()
#print("Result: " + str(result))


