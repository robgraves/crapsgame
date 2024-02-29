#!/usr/bin/env python3
#
# Matthew Page  07/02/2019, 12/26/2022, 07/11/2023
#				02/28/2024
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
import platform
import time
import math
import random
import pickle
import data.graphics.graphics
from data.graphics import graphics


#Ansi codes set up for colors
class ansifmt:
	LGREEN		= '\033[38;5;119m'
	HIGREEN		= '\033[1;92m'
	GREEN		= '\033[0;32m'
	HIYELLOW	= '\033[1;93m'
	YELLOW		= '\033[0;33m'
	HIRED		= '\033[1;91m'
	HIWHITE		= '\033[1;97m'
	HIBLUE		= '\033[1;94m'
	HIBLACK		= '\033[1;90m'
	LRED		= '\033[38;5;203m'
	BOLD		= '\033[1m'
	RESET		= '\033[0m'


#Check for OS type
operating = platform.system()
#print(operating)
#input()



############################################
#
#
# Default settings menu initializations
#
#
############################################
#color on or off, 1 for on, 0 for off
global colorized
colorized = 1

#sound effects on or off
global soundfx 
soundfx = 1 

#mature content is off by default
global mature
mature = 0
############################################


#path for files used
if operating == "Linux":
	userdata             = "data/save/userdata.p"
	config				= "data/save/config.p"
	dicesound           = "data/sounds/diceroll.wav"
	awwsound          = "data/sounds/aww.wav"
	applausesound   = "data/sounds/claps.wav"
	winsound           = "data/sounds/chips.wav"
	gruntsound        = "data/sounds/grunt.wav"
elif operating == "Windows":
	userdata           = "data\\save\\userdata.p"
	config				= "data\\save\\config.p"
	dicesound         = "data\\sounds\\diceroll.wav"
	awwsound         = "data\\sounds\\aww.wav"
	applausesound  = "data\\sounds\\claps.wav"
	winsound          = "data\\sounds\\chips.wav"
	gruntsound       = "data\\sounds\\grunt.wav"
elif operating == "Darwin":
	userdata             = "data/save/userdata.p"
	config				= "data/save/config.p"
	dicesound           = "data/sounds/diceroll.wav"
	awwsound          = "data/sounds/aww.wav"
	applausesound   = "data/sounds/claps.wav"
	winsound           = "data/sounds/chips.wav"
	gruntsound        = "data/sounds/grunt.wav"
else:
	print("ERROR: Unrecognized Operating System!")	


#########################################################
#
# Initializing the user database and loading if it exists,
# forcing creation of file if it doesn't exist to solve
# some issues encountered later
#
#########################################################
users_dict = {}
if os.path.exists(userdata):
	users_dict = pickle.load(open(userdata,"rb"))
else:
	if operating == "Linux":
		os.system("mkdir -p data/save")
	elif operating == "Windows":
		os.system("mkdir data\\save")
	elif operating == "Darwin":
		os.system("mkdir -p data/save")
	else:
		print("ERROR: Unknown Operating System!")
	users_dict = {"dealer":1000000000}
pickle.dump(users_dict, open(userdata,"wb"))



################################################
#
#     Loading config file if it exists, forcing
# creation of file if it doesn't exist
# config_dump is a list variable with 3 single
# digit numbers in it, being either a 0 for off
# or a 1 for on. [colorized,soundfx,mature]
#     For example: [1,1,0] is laid out to have 
# colorization on, sound effects on, and mature
# content off.
#
################################################
global config_dump
config_dump = [1,1,0]
if os.path.exists(config):
	config_dump = pickle.load(open(config,"rb"))
else:
	if operating == "Linux":
		os.system("mkdir -p data/save")
	elif operating == "Windows":
		os.system("mkdir data\\save")
	elif operating == "Darwin":
		os.system("mkdir -p data/save")
	else:
		print("ERROR: Unknown Operating System!")
	config_dump = [1,1,0]
pickle.dump(config_dump, open(config,"wb"))
#print(config_dump)
#input()
#config_dump[2] = 0
#print(config_dump)
#input()
#pickle.dump(config_dump, open(config,"wb"))



############################################
#
#
#  Function definitions
#
#
#############################################


#Function for animating dice rolling
def animatedice():
	global colorized
	i = 0
	rng = random.SystemRandom()
	while i < 5:
		table()
		animatedie1 		= rng.randint(1,6)
		animatedie2 		= rng.randint(1,6)

		if colorized == 0:
			#GREYSCALE
			#Display proper ASCII art for each dieface for die 1
			if animatedie1 == 1:
				graphics.die1face1()
			elif animatedie1 == 2:
				graphics.die1face2()
			elif animatedie1 == 3:
				graphics.die1face3()
			elif animatedie1 == 4:
				graphics.die1face4()
			elif animatedie1 == 5:
				graphics.die1face5()
			elif animatedie1 == 6:
				graphics.die1face6()
			#Display proper ASCII art for each dieface for die 2
			if animatedie2 == 1:
				graphics.die2face1()
			elif animatedie2 == 2:
				graphics.die2face2()
			elif animatedie2 == 3:
				graphics.die2face3()
			elif animatedie2 == 4:
				graphics.die2face4()
			elif animatedie2 == 5:
				graphics.die2face5()
			elif animatedie2 == 6:
				graphics.die2face6()
		else:
			#COLORIZED
			#Display proper ASCII art for each dieface for die 1
			if animatedie1 == 1:
				graphics.color_die1face1()
			elif animatedie1 == 2:
				graphics.color_die1face2()
			elif animatedie1 == 3:
				graphics.color_die1face3()
			elif animatedie1 == 4:
				graphics.color_die1face4()
			elif animatedie1 == 5:
				graphics.color_die1face5()
			elif animatedie1 == 6:
				graphics.color_die1face6()
			#Display proper ASCII art for each dieface for die 2
			if animatedie2 == 1:
				graphics.color_die2face1()
			elif animatedie2 == 2:
				graphics.color_die2face2()
			elif animatedie2 == 3:
				graphics.color_die2face3()
			elif animatedie2 == 4:
				graphics.color_die2face4()
			elif animatedie2 == 5:
				graphics.color_die2face5()
			elif animatedie2 == 6:
				graphics.color_die2face6()

		time.sleep(0.2)
		graphics.die1blank()
		graphics.die2blank()
		i=i+1	

#Function that rolls two dice
def dice():
	global coloried
	#setup for hardway check
	global hardway
	hardway = 0

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
	if soundfx == 1:
		if operating == "Linux":
			os.system("aplay -q " + dicesound + " > /dev/null 2>&1 &")
		elif operating == "Windows":
			os.system("powershell -c (New-Object Media.SoundPlayer 'data\\sounds\\diceroll.wav').PlaySync();")
		elif operating == "Darwin":
			os.system("afplay " + dicesound + " > /dev/null 2>&1 &")
		else:
			print("ERROR: Unknown Operating System!")

	#Play dice animation in Linux and MacOS
	#This works but is jerky in Windows, not sure why yet.
	if operating == "Linux":
		animatedice()
		table()
	elif operating == "Windows":
		table()
	elif operating == "Darwin":
		animateddice()
		table()
	else:
		print("ERROR: Unknown Operating System!")

	#animatedice()
	#table()

	if colorized == 0:
		#GRAYSCALE
		#Display proper ASCII art for each dieface for die 1
		if die1 == 1:
			graphics.die1face1()
		elif die1 == 2:
			graphics.die1face2()
		elif die1 == 3:
			graphics.die1face3()
		elif die1 == 4:
			graphics.die1face4()
		elif die1 == 5:
			graphics.die1face5()
		elif die1 == 6:
			graphics.die1face6()
		#Display proper ASCII art for each dieface for die 2
		if die2 == 1:
			graphics.die2face1()
		elif die2 == 2:
			graphics.die2face2()
		elif die2 == 3:
			graphics.die2face3()
		elif die2 == 4:
			graphics.die2face4()
		elif die2 == 5:
			graphics.die2face5()
		elif die2 == 6:
			graphics.die2face6()
	else:
		#COLORIZED
		#Display proper ASCII art for each dieface for die 1
		if die1 == 1:
			graphics.color_die1face1()
		elif die1 == 2:
			graphics.color_die1face2()
		elif die1 == 3:
			graphics.color_die1face3()
		elif die1 == 4:
			graphics.color_die1face4()
		elif die1 == 5:
			graphics.color_die1face5()
		elif die1 == 6:
			graphics.color_die1face6()
		#Display proper ASCII art for each dieface for die 2
		if die2 == 1:
			graphics.color_die2face1()
		elif die2 == 2:
			graphics.color_die2face2()
		elif die2 == 3:
			graphics.color_die2face3()
		elif die2 == 4:
			graphics.color_die2face4()
		elif die2 == 5:
			graphics.color_die2face5()
		elif die2 == 6:
			graphics.color_die2face6()

	print(str(die1) + " " + str(die2))
	print("You rolled : ", diceresult)
	
	#checking for hardways
	if (die1 == 2) and (die2 == 2):
		hardway = 4
		print("Four! The Hard Way!")
	if (die1 == 3) and (die2 == 3):
		hardway = 6
		print("Six! The Hard Way!")
	if (die1 == 4) and (die2 == 4):
		hardway = 8
		print("Eight! The Hard Way!")
	if (die1 == 5) and (die2 == 5):
		hardway = 10
		print("Ten! The Hard Way!")

	return diceresult

def settings(username):
	global config_dump
	global colorized
	global soundfx
	global mature
	#username = player()
	return username


#Function for creating or loading user and their bankroll
def player(username):
	choice = "0"
	saveduser = None
	global bankroll
	global colorized
	

	while username == "dealer":
		if operating == "Linux":
			os.system("clear")
		elif operating == "Windows":
			os.system("cls")
		elif operating == "Darwin":
			os.system("clear")
		else:
			print("ERROR: Unknown Operating System!")
		#Intro screen
		if colorized == 0:
			graphics.intro()
		else:
			graphics.color_intro()
		while choice not in ("1","2","3","4"):
			print("Are you a new or returning player?")
			print("1 - New Player")
			print("2 - Returning Player")
			print("3 - Settings")
			print("4 - Quit")
			choice = input()
			if choice not in ("1","2","3","4"):
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
		if choice == "3":
			username = settings(username)
			choice = "0"
		if choice == "4":
			gameover(1)
	return username


#Saving player data
#Function to be used prior to quitting the game
#Also after every payout and loss, to prevent 
#quitting program to cheat.
def save(users_dict):
	global bankroll
	users_dict[username] = bankroll
	pickle.dump(users_dict, open(userdata,"wb"))


#Saving config settings
def save_config(config_dump):
	pickle.dump(config_dump, open(config,"wb"))


#Function to check if player wants mature content
def maturecheck(mature):
	choice = "0"
	while choice not in ("1","2",""):
		print("Do you want to play with G rated or Mature Content?")
		print("(Default is G-rated)")
		print("1 - G-rated")
		print("2 - Mature")
		choice = input()
		if choice not in ("1","2",""):
			print("ERROR: Bad choice! Invalid entry!")
	#If just hit enter, defaults to G-rated content
	if choice == "":
		mature = 0
		return mature
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
	
	if operating == "Linux":
		os.system("clear")
	elif operating == "Windows":
		os.system("cls")
	elif operating == "Darwin":
		os.system("clear")
	else:
		print("ERROR: Unknown Operating System!")


	if colorized == 0:
		print("Your current bankroll is: $" + str(bankroll)) 
	else:  
		#Code snippet added and modified by nullist to colorize the bankroll 
		bankrollcolor = ansifmt.LGREEN  if bankroll > 0 else ansifmt.LRED
		bankrollfmtstr = bankrollcolor + f'${str(bankroll)}' + ansifmt.RESET
		print(f'Your current bankroll is: {bankrollfmtstr}')
  
 
	if colorized == 0: 
		#GRAYSCALE
		if point == 0:
			graphics.crapstable()
		elif point == 4:
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
	else:
		#COLORIZED
		if point == 0:
			graphics.color_crapstable()
		elif point == 4:
			graphics.color_crapstable4()
		elif point == 5:
			graphics.color_crapstable5()
		elif point == 6:
			graphics.color_crapstable6()
		elif point == 8:
			graphics.color_crapstable8()
		elif point == 9:
			graphics.color_crapstable9()
		elif point == 10:
			graphics.color_crapstable10()


	#Display current Pass or Don't Pass bet
	if bet_location == "1":
		print("Pass: $" + str(bet_amount))
	if bet_location == "2":
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

	#Display come or don't come along with come points or don't come points
	if bets.get("come") != 0:
		print("Come: $" + str(bets.get("come")))
	if bets.get("dc") != 0:
		print("Don't Come: $" + str(bets.get("dc")))
	if bets.get("come4") != 0:
		print("Come Point 4: $" + str(bets.get("come4")))
	if bets.get("come5") != 0:
		print("Come Point 5: $" + str(bets.get("come5")))
	if bets.get("come6") != 0:
		print("Come Point 6: $" + str(bets.get("come6")))
	if bets.get("come8") != 0:
		print("Come Point 8: $" + str(bets.get("come8")))
	if bets.get("come9") != 0:
		print("Come Point 9: $" + str(bets.get("come9")))
	if bets.get("come10") != 0:
		print("Come Point 10: $" + str(bets.get("come10")))
	if bets.get("dc4") != 0:
		print("Don't Come Point 4: $" + str(bets.get("dc4")))
	if bets.get("dc5") != 0:
		print("Don't Come Point 5: $" + str(bets.get("dc5")))
	if bets.get("dc6") != 0:
		print("Don't Come Point 6: $" + str(bets.get("dc6")))
	if bets.get("dc8") != 0:
		print("Don't Come Point 8: $" + str(bets.get("dc8")))
	if bets.get("dc9") != 0:
		print("Don't Come Point 9: $" + str(bets.get("dc9")))
	if bets.get("dc10") != 0:
		print("Don't Come Point 10: $" + str(bets.get("dc10")))

	#Display Free odds bets on Come points or Don't Come points
	if bets.get("freeodds_come4") != 0:
		print("Odds on Come Point 4: $" + str(bets.get("freeodds_come4")))
	if bets.get("freeodds_come5") != 0:
		print("Odds on Come Point 5: $" + str(bets.get("freeodds_come5")))
	if bets.get("freeodds_come6") != 0:
		print("Odds on Come Point 6: $" + str(bets.get("freeodds_come6")))
	if bets.get("freeodds_come8") != 0:
		print("Odds on Come Point 8: $" + str(bets.get("freeodds_come8")))
	if bets.get("freeodds_come9") != 0:
		print("Odds on Come Point 9: $" + str(bets.get("freeodds_come9")))
	if bets.get("freeodds_come10") != 0:
		print("Odds on Come Point 10: $" + str(bets.get("freeodds_come10")))
	if bets.get("freeodds_dc4") != 0:
		print("Odds on Don't Come Point 4: $" + str(bets.get("freeodds_dc4")))
	if bets.get("freeodds_dc5") != 0:
		print("Odds on Don't Come Point 5: $" + str(bets.get("freeodds_dc5")))
	if bets.get("freeodds_dc6") != 0:
		print("Odds on Don't Come Point 6: $" + str(bets.get("freeodds_dc6")))
	if bets.get("freeodds_dc8") != 0:
		print("Odds on Don't Come Point 8: $" + str(bets.get("freeodds_dc8")))
	if bets.get("freeodds_dc9") != 0:
		print("Odds on Don't Come Point 9: $" + str(bets.get("freeodds_dc9")))
	if bets.get("freeodds_dc10") != 0:
		print("Odds on Don't Come Point 10: $" + str(bets.get("freeodds_dc10")))

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
		tentotal = bets.get("place10") + bets.get("buy10") +  bets.get("lay10")
		print("Ten: $" + str(tentotal))		

	#Display Hardways if you have money on them
	if (bets.get("hardway4") !=0):
		print("Hardway 4: $" + str(bets.get("hardway4")))
	if (bets.get("hardway6") !=0):
		print("Hardway 6: $" + str(bets.get("hardway6")))
	if (bets.get("hardway8") !=0):
		print("Hardway 8: $" + str(bets.get("hardway8")))
	if (bets.get("hardway10") !=0):
		print("Hardway 10: $" + str(bets.get("hardway10")))

	#Display Other Proposition bets if you have money on them	
	if (bets.get("two") !=0):
		print("Prop - Two: $" + str(bets.get("two")))
	if (bets.get("three") !=0):
		print("Prop - Three: $" + str(bets.get("three")))
	if (bets.get("eleven") !=0):
		print("Prop - Eleven: $" + str(bets.get("eleven")))
	if (bets.get("twelve") !=0):
		print("Prop - Twelve: $" + str(bets.get("twelve")))
	if (bets.get("anyseven") !=0):
		print("Prop - Any Seven: $" + str(bets.get("anyseven")))
	if (bets.get("anycraps") !=0):
		print("Prop - Any Craps: $" + str(bets.get("anycraps")))
	if (bets.get("C&E") !=0):
		print("Prop - Craps & Eleven: $" + str(bets.get("C&E")))
	if (bets.get("world") !=0):
		print("Prop - World: $" + str(bets.get("world") * 5))


#Function for implementing Mike's idea for ways to make
#money if you go broke, only works if you chose M-rated
#at the start of game.
def shady():
	global colorized
	if operating == "Linux":
		os.system("clear")
	elif operating == "Windows":
		os.system("cls")
	elif operating == "Darwin":
		os.system("clear")
	else:
		print("ERROR: Unknown Operating System!")
	if colorized == 0:
		print("A shady looking middle-aged man approaches")
		print('you and he says, "I notice you are broke."')
		print("                                          ")
		print("You are a little unsure if you can trust  ")
		print("him. But you let him continue.            ")
		print("                                          ")
		print('He goes on, "...I have a way for you to   ')
		print('make some money if you follow me          ')
		print('out back."                                ')
	else:
		print(f"{ansifmt.HIWHITE}A shady looking middle-aged man approaches{ansifmt.RESET}")
		print(f'{ansifmt.HIWHITE}you and he says, "I notice you are broke."{ansifmt.RESET}')
		print("                                          ")
		print(f"{ansifmt.HIWHITE}You are a little unsure if you can trust  {ansifmt.RESET}")
		print(f"{ansifmt.HIWHITE}him. But you let him continue.            {ansifmt.RESET}")
		print("                                          ")
		print(f'{ansifmt.HIWHITE}He goes on, "...I have a way for you to   {ansifmt.RESET}')
		print(f'{ansifmt.HIWHITE}make some money if you follow me          {ansifmt.RESET}')
		print(f'{ansifmt.HIWHITE}out back."                                {ansifmt.RESET}')
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
		if colorized == 0:
			print("The man has you go behind the dumpster")
			print("with him and he drops his pants...    ")
		else:
			print(f"{ansifmt.HIWHITE}The man has you go behind the dumpster{ansifmt.RESET}")
			print(f"{ansifmt.HIWHITE}with him and he drops his pants...    {ansifmt.RESET}")
		if soundfx == 1:
			if operating == "Linux":
				os.system("aplay -q " + gruntsound + " > /dev/null 2>&1")
			elif operating == "Windows":
				os.system("powershell -c (New-Object Media.SoundPlayer 'data\\sounds\\grunt.wav').PlaySync();")
			elif operating == "Darwin":
				os.system("afplay " + gruntsound + " > /dev/null 2>&1")
			else:
				print("ERROR: Unknown Operating System!")
		input()
		if colorized == 0:
			print("...15 minutes later")
			print("You have made 20 dollars")
		else:
			print(f"{ansifmt.HIWHITE}...15 minutes later{ansifmt.RESET}")
			print(f"{ansifmt.HIWHITE}You have made 20 dollars{ansifmt.RESET}")
		bankroll = 20
		input()
		if operating == "Linux":
			os.system("clear")
		elif operating == "Windows":
			os.system("cls")
		elif operating == "Darwin":
			os.system("clear")
		else:
			print("ERROR: Unknown Operating System!")
		return bankroll
	if choice == "2":
		if colorized == 0:
			print("You decide not to follow the man.")
		else:
			print(f"{ansifmt.HIWHITE}You decide not to follow the man.{ansifmt.RESET}")
	return bankroll


#Function for endgame/gameover if bankroll hits 0
#0 to save, 1 to not save as input to function
def gameover(int):
	global config_dump
	global colorized
	if operating == "Linux":
		os.system("clear")
	elif operating == "Windows":
		os.system("cls")
	elif operating == "Darwin":
		os.system("clear")
	else:
		print("ERROR: Unknown Operating System!")
	if colorized == 0:
		print("******************************\n\n")
	else:
		print(f"{ansifmt.HIYELLOW}******************************\n\n{ansifmt.RESET}")
	if bankroll == 0:
		if colorized == 0:
			print("       You are broke!\n\n")
		else:
			print(f"{ansifmt.HIWHITE}       You are broke!\n\n{ansifmt.RESET}")
	else:
		if colorized == 0:
			print("      Come back soon!!\n\n")
		else:
			print(f"{ansifmt.HIWHITE}      Come back soon!!\n\n{ansifmt.RESET}")
	if bankroll == 0:
		if colorized == 0:
			print("******************************\n")
			print("     G A M E  O V E R!!!\n\n")
			print("******************************\n\n")
		else:
			print(f"{ansifmt.HIYELLOW}******************************\n{ansifmt.RESET}")
			print(f"{ansifmt.HIBLUE}     G A M E  O V E R!!!\n\n{ansifmt.RESET}")
			print(f"{ansifmt.HIYELLOW}******************************\n\n{ansifmt.RESET}")
	else:
		if colorized == 0:
			graphics.cactus()
		else:
			graphics.color_cactus()
	if colorized == 0:
		print("**** Terminal Craps Game ****")
		print("** written by Matthew Page **")
		print("**** me@matthewjpage.com ****\n\n")
		print("******************************\n")
	else:
		print(f"{ansifmt.HIYELLOW}**** {ansifmt.RESET}" + f"{ansifmt.HIBLUE}Terminal Craps Game {ansifmt.RESET}" + f"{ansifmt.HIYELLOW}****{ansifmt.RESET}")
		print(f"{ansifmt.HIYELLOW}** {ansifmt.RESET}" + f"{ansifmt.HIBLUE}written by Matthew Page {ansifmt.RESET}" + f"{ansifmt.HIYELLOW}**{ansifmt.RESET}")
		print(f"{ansifmt.HIBLUE}" + f"{ansifmt.HIYELLOW}**** {ansifmt.HIBLUE}me@matthewjpage.com {ansifmt.RESET}" + f"{ansifmt.HIYELLOW}****\n\n{ansifmt.RESET}")
		print(f"{ansifmt.HIYELLOW}******************************\n{ansifmt.RESET}")
	if bankroll == 0:
		if colorized == 0:
			print("To play again, choose New User")
			print("and use the same name to reset")
			print("your bankroll.                \n")
		else:
			print(f"{ansifmt.HIWHITE}To play again, choose New User{ansifmt.RESET}")
			print(f"{ansifmt.HIWHITE}and use the same name to reset{ansifmt.RESET}")
			print(f"{ansifmt.HIWHITE}your bankroll.                \n{ansifmt.RESET}")
	else:
		if colorized == 0:
			print("To play again, choose Returning")
			print("User and use the same name to  ")
			print("use your saved bankroll.       \n")
		else:
			print(f"{ansifmt.HIWHITE}To play again, choose Returning{ansifmt.RESET}")
			print(f"{ansifmt.HIWHITE}User and use the same name to  {ansifmt.RESET}")
			print(f"{ansifmt.HIWHITE}use your saved bankroll.       \n{ansifmt.RESET}")
	if int == 0:
		save(users_dict)
		save_config(config_dump)
	input()
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
	"come":0,				#acts like pass line, pays 1 to 1
	"come4":0,				#come point 4, pays 1 to 1
	"come5":0,				#come point 5, pays 1 to 1
	"come6":0,				#come point 6, pays 1 to 1
	"come8":0,				#come point 8, pays 1 to 1
	"come9":0,				#come point 9, pays 1 to 1
	"come10":0,				#come point 10, pays 1 to 1
	"dc":0,					#acts like don't pass, pays 1 to 1
	"dc4":0,				#don't come point 4, pays 1 to 1
	"dc5":0,				#don't come point 5, pays 1 to 1
	"dc6":0,				#don't come point 6, pays 1 to 1
	"dc8":0,				#don't come point 8, pays 1 to 1
	"dc9":0,				#don't come point 9, pays 1 to 1
	"dc10":0,				#don't come point 10, pays 1 to 1
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
	"horn":0,				#odds same as next 4 bets/this never is actually used
	"eleven":0,				#odds 15 to 1 YO-leven!!!
	"twelve":0,				#odds 30 to 1
	"three":0,				#odds 15 to 1
	"two":0,				#odds 30 to 1
    "big6":0,               #some craps tables have these, odds 1 to 1
    "big8":0,               #some craps tables have these, odds 1 to 1
    "world":0,              #horn plus any seven
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
	global bet_location
	global bet_amount
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
		#Reject if no money on Pass or Don't Pass
		if bet_location == "3":
			print("You cannot take odds on Pass or Don't Pass")
			print("if you didn't bet on Pass or Don't Pass on")
			print("the come out roll.")
			input()
			table()
			return(bets)
		#Odds on Pass Line wager
		if bet_location == "1":
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
			while not int(oddsbet) in range(1, (bet_amount*5)+1):
				if oddsbet > (bet_amount * 5):
					print("You cannot take more than 5x odds")
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
			if operating == "Linux":
				os.system("clear")
			elif operating == "Windows":
				os.system("cls")
			elif operating == "Darwin":
				os.system("clear")
			else:
				print("ERROR: Unknown Operating System!")
			print("Your current bankroll is: $" + str(bankroll))
			#save(users_dict)
			#print(bets)   					##FOR TESTING
			#input()						##FOR TESTING

		#Odds on Don't Pass wager
		if bet_location == "2":
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
			while not int(oddsbet) in range(1, (bet_amount*5)+1):
				if oddsbet > (bet_amount * 5):
					print("You cannot take more than 5x odds")
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
			if operating == "Linux":
				os.system("clear")
			elif operating == "Windows":
				os.system("cls")
			elif operating == "Darwin":
				os.system("clear")
			else:
				print("ERROR: Unknown Operating System!")
			print("Your current bankroll is: $" + str(bankroll))
			#save(users_dict)
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
	if operating == "Linux":
		os.system("clear")
	elif operating == "Windows":
		os.system("cls")
	elif operating == "Darwin":
		os.system("clear")
	else:
		print("ERROR: Unknown Operating System!")
	print("Your current bankroll is: $" + str(bankroll))
	#save(users_dict)
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
	#not contract bets (bets you are stuck with once you make them (Pass and Come bets))
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
				print("4  - Take down Place 4 bet")
			if bets.get("place5") != 0:
				print("5  - Take down Place 5 bet")
			if bets.get("place6") != 0:
				print("6  - Take down Place 6 bet")
			if bets.get("place8") != 0:
				print("8  - Take down Place 8 bet")
			if bets.get("place9") != 0:
				print("9  - Take down Place 9 bet")
			if bets.get("place10") != 0:
				print("10 - Take down Place 10 bet")
			print("B - Back")
			#Take user input and takedown relevant bet
			takedownbet = input()
			if (takedownbet == "B") or (takedownbet == "b"):
				return(bets)
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
		if operating == "Linux":
			os.system("clear")
		elif operating == "Windows":
			os.system("cls")
		elif operating == "Darwin":
			os.system("clear")
		else:
			print("ERROR: Unknown Operating System!")
		print("Your current bankroll is: $" + str(bankroll))
		#save(users_dict)
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
	global bankroll
	#Check for out of money and return if so
	if bankroll == 0:
		print("You have no more money available to bet.")
		input()
		table()
		return(bets)
	global buyselect
	print("Your current bankroll is: $" + str(bankroll))
	buybet_location = "0"
	#The only way to get out of the Buy bet submenu is to type B or b for Back as
	#many players will bet on multiple numbers here allowing you to place every number
	#desired and then go back to main bet menu when finished.
	#Also includes a Takedown option as a seven will wipe all these bets and they are
	#not contract bets (bets you are stuck with once you make them (Pass and Come bets))
	#so players can choose to takedown or turn off these bets at any point to protect it
	#from the inevitable shooter Sevening Out
	while buybet_location != "B" or buybet_location != "b":
		while buybet_location not in ("Q","q","B","b","T","t","4","5","6","8","9","10"):
			print("Choose where to place your bet: ")
			print("4  - Buy 4")
			print("5  - Buy 5")
			print("6  - Buy 6")
			print("8  - Buy 8")
			print("9  - Buy 9")
			print("10 - Buy 10")
			print("T  - Take down a bet")
			print("B  - Back")
			print("Q  - Quit Game")
			print("PLEASE NOTE: There is a 5% commission")
			print("on Buy bets paid from winnings.")
			buybet_location = input()
			if buybet_location in ("Q","q","B","b","T","t","4","5","6","8","9","10"):
				break
			else:
				print("Invalid entry!")
		print("You chose " + buybet_location)

		#Allow for quitting game at every menu but warning player that there are still
		#live bets on the table and quitting now would surrender those bets to the house
		if buybet_location == "Q" or buybet_location == "q":
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
		if buybet_location == "B" or buybet_location == "b":
			table()
			return(bets)

		#Takedown bets submenu
		if buybet_location == "T" or buybet_location == "t":
			print("Which bet do you want to take down?")
			if bets.get("buy4") != 0:
				print("4  - Take down Buy 4 bet")
			if bets.get("buy5") != 0:
				print("5  - Take down Buy 5 bet")
			if bets.get("buy6") != 0:
				print("6  - Take down Buy 6 bet")
			if bets.get("buy8") != 0:
				print("8  - Take down Buy 8 bet")
			if bets.get("buy9") != 0:
				print("9  - Take down Buy 9 bet")
			if bets.get("buy10") != 0:
				print("10 - Take down Buy 10 bet")
			print("B - Back")
			#Take user input and takedown relevant bet
			takedownbet = input()
			if (takedownbet == "B") or (takedownbet == "b"):
				return(bets)
			if takedownbet == "4":
				bankroll = bankroll + bets.get("buy4")
				bets.update({"buy4":0})
			if takedownbet == "5":
				bankroll = bankroll + bets.get("buy5")
				bets.update({"buy5":0})
			if takedownbet == "6":
				bankroll = bankroll + bets.get("buy6")
				bets.update({"buy6":0})
			if takedownbet == "8":
				bankroll = bankroll + bets.get("buy8")
				bets.update({"buy8":0})
			if takedownbet == "9":
				bankroll = bankroll + bets.get("buy9")
				bets.update({"buy9":0})
			if takedownbet == "10":
				bankroll = bankroll + bets.get("buy10")
				bets.update({"buy10":0})
			print("Your current bankroll is: $" + str(bankroll))
			break
		#Get bet amount
		print("Enter bet amount: ")
		placebet = 0
		while not int(buybet) in range(1, bankroll+1):
			if buybet > bankroll:
				print("You do not have that much.")
				print("Your current bankroll is: $" + str(bankroll))
				print("Enter a bet amount: ")
			try:
				buybet = int(input())
			except ValueError:
				print("Error: Invalid entry. Please enter a number.")
				continue
		print("You chose " + str(buybet))
		#Take buy bet and based on number chosen update betting dictionary
		#for that number
		bankroll = bankroll - buybet
		if operating == "Linux":
			os.system("clear")
		elif operating == "Windows":
			os.system("cls")
		elif operating == "Darwin":
			os.system("clear")
		else:
			print("ERROR: Unknown Operating System!")
		print("Your current bankroll is: $" + str(bankroll))
		#save(users_dict)
		if buybet_location == "4":
			buyselect[0] = 4	
			bets.update({"buy4":(buybet + bets.get("buy4"))})
			buybet_location = "0"
		if buybet_location == "5":
			buyselect[1] = 5	
			bets.update({"buy5":(buybet + bets.get("buy5"))})
			buybet_location = "0"
		if buybet_location == "6":
			buyselect[2] = 6	
			bets.update({"buy6":(buybet + bets.get("buy6"))})
			buybet_location = "0"
		if buybet_location == "8":
			buyselect[3] = 8	
			bets.update({"buy8":(buybet + bets.get("buy8"))})
			buybet_location = "0"
		if buybet_location == "9":
			buyselect[4] = 9	
			bets.update({"buy9":(buybet + bets.get("buy9"))})
			buybet_location = "0"
		if buybet_location == "10":
			buyselect[5] = 10	
			bets.update({"buy10":(buybet + bets.get("buy10"))})
			buybet_location = "0"
		table()
	print("You chose " + buybet_location)
	table()
	return bets


#Function defining Lay Bets
def lay(bets):
	global bankroll
	#Check for out of money and return if so
	if bankroll == 0:
		print("You have no more money available to bet.")
		input()
		table()
		return(bets)
	global layselect
	print("Your current bankroll is: $" + str(bankroll))
	laybet_location = "0"
	#The only way to get out of the Lay bet submenu is to type B or b for Back as
	#many players will bet on multiple numbers here allowing you to place every number
	#desired and then go back to main bet menu when finished.
	#Also includes a Takedown option as a seven will wipe all these bets and they are
	#not contract bets (bets you are stuck with once you make them (Pass and Come bets))
	#so players can choose to takedown or turn off these bets at any point to protect it
	#from the inevitable shooter Sevening Out
	while laybet_location != "B" or laybet_location != "b":
		while laybet_location not in ("Q","q","B","b","T","t","4","5","6","8","9","10"):
			print("Choose where to place your bet: ")
			print("4  - Lay 4")
			print("5  - Lay 5")
			print("6  - Lay 6")
			print("8  - Lay 8")
			print("9  - Lay 9")
			print("10 - Lay 10")
			print("T  - Take down a bet")
			print("B  - Back")
			print("Q  - Quit Game")
			print("PLEASE NOTE: There is a 5% commission")
			print("on Lay bets paid up up front.")
			laybet_location = input()
			if laybet_location in ("Q","q","B","b","T","t","4","5","6","8","9","10"):
				break
			else:
				print("Invalid entry!")
		print("You chose " + laybet_location)

		#Allow for quitting game at every menu but warning player that there are still
		#live bets on the table and quitting now would surrender those bets to the house
		if laybet_location == "Q" or laybet_location == "q":
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
		if laybet_location == "B" or laybet_location == "b":
			table()
			return(bets)

		#Takedown bets submenu
		if laybet_location == "T" or laybet_location == "t":
			print("Which bet do you want to take down?")
			if bets.get("lay4") != 0:
				print("4  - Take down Lay 4 bet")
			if bets.get("lay5") != 0:
				print("5  - Take down Lay 5 bet")
			if bets.get("lay6") != 0:
				print("6  - Take down Lay 6 bet")
			if bets.get("lay8") != 0:
				print("8  - Take down Lay 8 bet")
			if bets.get("lay9") != 0:
				print("9  - Take down Lay 9 bet")
			if bets.get("lay10") != 0:
				print("10 - Take down Lay 10 bet")
			print("B - Back")
			#Take user input and takedown relevant bet
			takedownbet = input()
			if (takedownbet == "B") or (takedownbet == "b"):
				return(bets)
			if takedownbet == "4":
				bankroll = bankroll + bets.get("lay4")
				bets.update({"lay4":0})
			if takedownbet == "5":
				bankroll = bankroll + bets.get("lay5")
				bets.update({"lay5":0})
			if takedownbet == "6":
				bankroll = bankroll + bets.get("lay6")
				bets.update({"lay6":0})
			if takedownbet == "8":
				bankroll = bankroll + bets.get("lay8")
				bets.update({"lay8":0})
			if takedownbet == "9":
				bankroll = bankroll + bets.get("lay9")
				bets.update({"lay9":0})
			if takedownbet == "10":
				bankroll = bankroll + bets.get("lay10")
				bets.update({"lay10":0})
			print("Your current bankroll is: $" + str(bankroll))
			break
		#Get bet amount
		print("Enter bet amount: ")
		laybet = 0
		while not int(laybet) in range(1, bankroll+1):
			if laybet > bankroll:
				print("You do not have that much.")
				print("Your current bankroll is: $" + str(bankroll))
				print("Enter a bet amount: ")
			try:
				laybet = int(input())
			except ValueError:
				print("Error: Invalid entry. Please enter a number.")
				continue
		print("You chose " + str(laybet))
		#Initializing commission to zero for sanity
		commission = 0 
		#Take lay bet plus 5% commision on potential win, 
		#then update betting dictionary for that number
		if bets.get("lay4") != 0:
			commission = (math.ceil(math.ceil(laybet/2) * 0.05))
			bankroll = bankroll - (laybet + commission)
		elif bets.get("lay5") != 0:
			commission = (math.ceil(math.ceil(laybet*(2/3)) * 0.05))
			bankroll = bankroll - (laybet + commission)
		elif bets.get("lay6") != 0:
			commission = (math.ceil(math.ceil(laybet*(5/6)) * 0.05))
			bankroll = bankroll - (laybet + commission)
		elif bets.get("lay8") != 0:
			commission = (math.ceil(math.ceil(laybet*(5/6)) * 0.05))
			bankroll = bankroll - (laybet + commission)
		elif bets.get("lay9") != 0:
			commission = (math.ceil(math.ceil(laybet*(2/3)) * 0.05))
			bankroll = bankroll - (laybet + commission)
		elif bets.get("lay10") != 0:
			commission = (math.ceil(math.ceil(laybet/2) * 0.05))
			bankroll = bankroll - (laybet + commission)


		if operating == "Linux":
			os.system("clear")
		elif operating == "Windows":
			os.system("cls")
		elif operating == "Darwin":
			os.system("clear")
		else:
			print("ERROR: Unknown Operating System!")
			
		print("Your current bankroll is: $" + str(bankroll))
		#save(users_dict)
		if laybet_location == "4":
			layselect[0] = 4	
			bets.update({"lay4":(laybet + bets.get("lay4"))})
			laybet_location = "0"
		if laybet_location == "5":
			layselect[1] = 5	
			bets.update({"lay5":(laybet + bets.get("lay5"))})
			laybet_location = "0"
		if laybet_location == "6":
			layselect[2] = 6	
			bets.update({"lay6":(laybet + bets.get("lay6"))})
			laybet_location = "0"
		if laybet_location == "8":
			layselect[3] = 8	
			bets.update({"lay8":(laybet + bets.get("lay8"))})
			laybet_location = "0"
		if laybet_location == "9":
			layselect[4] = 9	
			bets.update({"lay9":(laybet + bets.get("lay9"))})
			laybet_location = "0"
		if laybet_location == "10":
			layselect[5] = 10	
			bets.update({"lay10":(laybet + bets.get("lay10"))})
			laybet_location = "0"
		table()
	print("You chose " + laybet_location)
	table()
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

#Function for Come and Don't Come bets
def comedc(bets):
	global bankroll
	comebet = 0

	#Check for come out roll, block if so
	if point == 0:
		print("You cannot bet on Come or Don't Come")
		print("on the Come Out roll.")
		input()
		table()
				
	#Check for out of money and return if so
	if bankroll == 0:
		print("You have no more money available to bet.")
		input()
		table()
		return(bets)

	print("Your current bankroll is: $" + str(bankroll))
	comebet_location = "0"
	#Come bet submenu
	#while comebet_location not in ("B","b","Q","q"):
	while comebet_location != "B" or comebet_location != "b": 
		while comebet_location not in ("Q","q","B","b","C","c","D","d"):
			print("Choose where to place your bet: ")
			print("C  - Come")
			print("D  - Don't Come (Bar 12)")
			print("B  - Back")
			print("Q  - Quit Game")
			comebet_location = input()
			if comebet_location in ("Q","q","B","b","C","c","D","d"):
				break
			else:
				print("Invalid entry!")
			#Return if player chooses Back
			#if comebet_location == "B" or comebet_location == "b":
			#	table()
				#print("we are in the comebet_loc check for B")
				#print(comebet_location)
				#input()
			#	break
				#pass
			#	return(bets)
		print("You chose " + comebet_location)

		#Return if player chooses Back
		if comebet_location == "B" or comebet_location == "b":
			table()
			#print("we are in the comebet_loc check for B")
			#print(comebet_location)
			#input()
			#break
			return(bets)

		#Allow for quitting game at every menu but warning player that there are still
		#live bets on the table and quitting now would surrender those bets to the house
		if comebet_location == "Q" or comebet_location == "q":
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


		#Get bet amount
		print("Enter bet amount: ")
		comebet = 0
		while not int(comebet) in range(1, bankroll+1):
			if comebet > bankroll:
				print("You do not have that much.")
				print("Your current bankroll is: $" + str(bankroll))
				print("Enter a bet amount: ")
			try:
				comebet = int(input())
			except ValueError:
				print("Error: Invalid entry. Please enter a number.")
				continue
		print("You chose " + str(comebet))
		#Take come bet or don't come bet and update betting dictionary
		bankroll = bankroll - comebet
		if comebet_location == "C" or comebet_location == "c":
			bets.update({"come":(bets.get("come") + comebet)})
			table()
			return(bets)
		if comebet_location == "D" or comebet_location == "d":
			bets.update({"dc":(bets.get("dc") + comebet)})
			table()
			return(bets)
		comebet = 0
		if operating == "Linux":
			os.system("clear")
		elif operating == "Windows":
			os.system("cls")
		elif operating == "Darwin":
			os.system("clear")
		else:
			print("ERROR: Unknown Operating System!")
	print("Your current bankroll is: $" + str(bankroll))

	#save(users_dict)
	table()
	return bets


#Function for Free Odds on Come/DC points
def freeodds_comedc(bets):
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
		#Reject if no money on Come or Don't Come points
		if bets.get("come4") == 0 and bets.get("come5") == 0 and bets.get("come6") == 0 and bets.get("come8") == 0 and bets.get("come9") == 0 and bets.get("come10") == 0 and bets.get("dc4") == 0 and bets.get("dc5") == 0 and bets.get("dc6") == 0 and bets.get("dc8") == 0 and bets.get("dc9") == 0 and bets.get("dc10") == 0:
			print("You cannot take odds on Come or Don't Come")
			print("points if you don't have any Come or Don't Come")
			print("point bets.")
			input()
			table()
			return(bets)
		else:
			oddsbet = 0
			oddsbet_location = "0" 
			while oddsbet_location != "B" or oddsbet_location != "b":
				while oddsbet_location not in ("B","b","C4","C5","C6","C8","C9","C10","c4","c5","c6","c8","c9","c10","D4","D5","D6","D8","D9","D10","d4","d5","d6","d8","d9","d10"):
					print("Choose where to take Come or Don't Come Odds: ")
					if bets.get("come4") != 0:
						print("C4  - Odds on Come 4")
					if bets.get("dc4") != 0:
						print("D4  - Odds on Don't Come 4")
					if bets.get("come5") != 0:
						print("C5  - Odds on Come 5")
					if bets.get("dc5") != 0:
						print("D5  - Odds on Don't Come 5")   
					if bets.get("come6") != 0:
						print("C6  - Odds on Come 6")
					if bets.get("dc6") != 0:
						print("D6  - Odds on Don't Come 6")   
					if bets.get("come8") != 0:
						print("C8  - Odds on Come 8")
					if bets.get("dc8") != 0:
						print("D8  - Odds on Don't Come 8")   
					if bets.get("come9") != 0:
						print("C9  - Odds on Come 9")
					if bets.get("dc9") != 0:
						print("D9  - Odds on Don't Come 9")   
					if bets.get("come10") != 0:
						print("C10  - Odds on Come 10")
					if bets.get("dc10") != 0:
						print("D10  - Odds on Don't Come 10")
					print("B - Back")   
					oddsbet_location = input()
					if (oddsbet_location == "B") or (oddsbet_location == "b"):
						return(bets)
					#Get bet amount
					print("Enter bet amount: ")
					oddsbet = 0
					while not int(oddsbet) in range(1,bankroll+1):
						if oddsbet > bankroll:
							print("You do not have that much.")
							print("Your current bankroll is: $" + str(bankroll))
							print("Enter bet amount: ")
						try:
							oddsbet = int(input())
						except ValueError:
							print("Error: Invalid entry.  Please enter a number.")
							continue
					while not int(oddsbet) in range(1, (bet_amount*5)+1):
						if oddsbet > (bet_amount * 5):
							print("You cannot take more than 5x odds")
							print("Enter a bet amount: ")
						try:
							oddsbet = int(input())
						except ValueError:
							print("Error: Invalid entry. Please enter a number.")
							continue
					#Put in 5x limit or 5-4-3 limit on odds bet for the future
					print("You chose " + str(oddsbet))
					#Take oddsbet and place it on come or don't come point chosen
					#and update the betting dictionary.
					bankroll = bankroll - oddsbet
					if operating == "Linux":
						os.system("clear")
					elif operating == "Windows":
						os.system("cls")
					elif operating == "Darwin":
						os.system("clear")
					else:
						print("ERROR: Unknown Operating System!")
					#table()
					
					if oddsbet_location == "C4" or oddsbet_location == "c4":
						if bets.get("come4") == 0:
							print("You have no bets here.")
							table()
							return(bets)
						bets.update({"freeodds_come4":(oddsbet + bets.get("freeodds_come4"))})
						table()
						return(bets)
					if oddsbet_location == "D4" or oddsbet_location == "d4":
						if bets.get("dc4") == 0:
							print("You have no bets here.")
							table()
							return(bets)
						bets.update({"freeodds_dc4":(oddsbet + bets.get("freeodds_dc4"))})
						table()
						return(bets)
					if oddsbet_location == "C5" or oddsbet_location == "c5":
						if bets.get("come5") == 0:
							print("You have no bets here.")
							table()
							return(bets)
						bets.update({"freeodds_come5":(oddsbet + bets.get("freeodds_come5"))})
						table()
						return(bets)
					if oddsbet_location == "D5" or oddsbet_location == "d5":
						if bets.get("dc5") == 0:
							print("You have no bets here.")
							table()
							return(bets)
						bets.update({"freeodds_dc5":(oddsbet + bets.get("freeodds_dc5"))})
						table()
						return(bets)
					if oddsbet_location == "C6" or oddsbet_location == "c6":
						if bets.get("come6") == 0:
							print("You have no bets here.")
							table()
							return(bets)
						bets.update({"freeodds_come6":(oddsbet + bets.get("freeodds_come6"))})
						table()
						return(bets)
					if oddsbet_location == "D6" or oddsbet_location == "d6":
						if bets.get("dc6") == 0:
							print("You have no bets here.")
							table()
							return(bets)
						bets.update({"freeodds_dc6":(oddsbet + bets.get("freeodds_dc6"))})
						table()
						return(bets)
					if oddsbet_location == "C8" or oddsbet_location == "c8":
						if bets.get("come8") == 0:
							print("You have no bets here.")
							table()
							return(bets)
						bets.update({"freeodds_come8":(oddsbet + bets.get("freeodds_come8"))})
						table()
						return(bets)
					if oddsbet_location == "D8" or oddsbet_location == "d8":
						if bets.get("dc8") == 0:
							print("You have no bets here.")
							table()
							return(bets)
						bets.update({"freeodds_dc8":(oddsbet + bets.get("freeodds_dc8"))})
						table()
						return(bets)
					if oddsbet_location == "C9" or oddsbet_location == "c9":
						if bets.get("come9") == 0:
							print("You have no bets here.")
							table()
							return(bets)
						bets.update({"freeodds_come9":(oddsbet + bets.get("freeodds_come9"))})
						table()
						return(bets)
					if oddsbet_location == "D9" or oddsbet_location == "d9":
						if bets.get("dc9") == 0:
							print("You have no bets here.")
							table()
							return(bets)
						bets.update({"freeodds_dc9":(oddsbet + bets.get("freeodds_dc9"))})
						table()
						return(bets)
					if oddsbet_location == "C10" or oddsbet_location == "c10":
						if bets.get("come10") == 0:
							print("You have no bets here.")
							table()
							return(bets)
						bets.update({"freeodds_come10":(oddsbet + bets.get("freeodds_come10"))})
						table()
						return(bets)
					if oddsbet_location == "D10" or oddsbet_location == "d10":
						if bets.get("dc10") == 0:
							print("You have no bets here.")
							table()
							return(bets)
						bets.update({"freeodds_dc10":(oddsbet + bets.get("freeodds_dc10"))})
						table()
						return(bets)

			#input()

	table()
	return bets


#Function for Hardway Bets
def hardwaybets(bets):
	global bankroll
	#Check for out of money and return if so
	if bankroll == 0:
		print("You have no more money available to bet.")
		input()
		table()
		return(bets)
	print("Your current bankroll is: $" + str(bankroll))
	hardwaybet_location = "0"
	#The only way to get out of the Hardway bet submenu is to type B or b for Back
	#Also includes a Takedown option as a seven will wipe all these bets and they are
	#not contract bets (bets you are stuck with once you make them (Pass and Come bets))
	#so players can choose to takedown or turn off these bets at any point to protect it
	#from the inevitable shooter Sevening Out
	while hardwaybet_location != "B" or hardwaybet_location != "b":
		while hardwaybet_location not in ("Q","q","B","b","T","t","4","6","8","10"):
			print("Choose where to place your bet: ")
			print("4  - 4 Hardway")
			print("6  - 6 Hardway")
			print("8  - 8 Hardway")
			print("10 - 10 Hardway")
			print("T  - Take down a bet")
			print("B  - Back")
			print("Q  - Quit Game")
			hardwaybet_location = input()
			if hardwaybet_location in ("Q","q","B","b","T","t","4","6","8","10"):
				break
			else:
				print("Invalid entry!")
		print("You chose " + hardwaybet_location)

		#Allow for quitting game at every menu but warning player that there are still
		#live bets on the table and quitting now would surrender those bets to the house
		if hardwaybet_location == "Q" or hardwaybet_location == "q":
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
		if hardwaybet_location == "B" or hardwaybet_location == "b":
			table()
			return(bets)

		#Takedown bets submenu
		if hardwaybet_location == "T" or hardwaybet_location == "t":
			print("Which bet do you want to take down?")
			if bets.get("hardway4") != 0:
				print("4  - Take down 4 Hardway bet")
			if bets.get("hardway6") != 0:
				print("6  - Take down 6 Hardway bet")
			if bets.get("hardway8") != 0:
				print("8  - Take down 8 Hardway bet")
			if bets.get("hardway10") != 0:
				print("10 - Take down 10 Hardway bet")
			print("B - Back")
			#Take user input and takedown relevant bet
			takedownbet = input()
			if (takedownbet == "B") or (takedownbet == "B"):
				return(bets)
			if takedownbet == "4":
				bankroll = bankroll + bets.get("hardway4")
				bets.update({"hardway4":0})
			if takedownbet == "6":
				bankroll = bankroll + bets.get("hardway6")
				bets.update({"hardway6":0})
			if takedownbet == "8":
				bankroll = bankroll + bets.get("hardway8")
				bets.update({"hardway8":0})
			if takedownbet == "10":
				bankroll = bankroll + bets.get("hardway10")
				bets.update({"hardway10":0})
			print("Your current bankroll is: $" + str(bankroll))
			break
		#Get bet amount
		print("Enter bet amount: ")
		hardwaybet = 0
		while not int(hardwaybet) in range(1, bankroll+1):
			if hardwaybet > bankroll:
				print("You do not have that much.")
				print("Your current bankroll is: $" + str(bankroll))
				print("Enter a bet amount: ")
			try:
				hardwaybet = int(input())
			except ValueError:
				print("Error: Invalid entry. Please enter a number.")
				continue
		print("You chose " + str(hardwaybet))
		#Take place bet and based on number chosen update betting dictionary
		#for that number
		bankroll = bankroll - hardwaybet
		if operating == "Linux":
			os.system("clear")
		elif operating == "Windows":
			os.system("cls")
		elif operating == "Darwin":
			os.system("clear")
		else:
			print("ERROR: Unknown Operating System!")
		print("Your current bankroll is: $" + str(bankroll))
		#save(users_dict)
		if hardwaybet_location == "4":
			bets.update({"hardway4":(hardwaybet + bets.get("hardway4"))})
			hardwaybet_location = "0"
		if hardwaybet_location == "6":
			bets.update({"hardway6":(hardwaybet + bets.get("hardway6"))})
			hardwaybet_location = "0"
		if hardwaybet_location == "8":
			bets.update({"hardway8":(hardwaybet + bets.get("hardway8"))})
			hardwaybet_location = "0"
		if hardwaybet_location == "10":
			bets.update({"hardway10":(hardwaybet + bets.get("hardway10"))})
			hardwaybet_location = "0"
		table()
	print("You chose " + hardwaybet_location)
	table()
	return bets


#Function for Proposition bets (Hardways, 2, 3, 12, 11, Horn, Any Craps, and Any Seven)
def proposition(bets):
	global bankroll
	if bankroll == 0:
		print("You have no more money available to bet.")
		input()
		table()
		return(bets)
	prop_location = "0"
	#Submenu to choose Proposition bets
	while prop_location not in ("1","2","3","11","12","6","7","C","c","B","b","Q","q"):
		print("Choose one: ")
		print("1  - Hardways")
		print("2  - Two           - 30 to 1")
		print("3  - Three         - 15 to 1")
		print("11 - Eleven        - 15 to 1")
		print("12 - Twelve        - 30 to 1")
		print("6  - Horn Bet (must be divisible by 4)")
		print("7  - Any Seven Bet - 4 to 1")
		print("C  - Any Craps Bet - 7 to 1")
		print("B  - Back")
		print("Q  - Quit Game")
		prop_location = input()
		if prop_location in ("1","2","3","11","12","6","7","C","c","B","b","Q","q"):
			break
		else:
			print("Invalid entry!")
	#Allow for quitting game at every menu but warning player that there are still
	#live bets on the table and quitting now would surrender those bets to the house
	if prop_location == "Q" or prop_location == "q":
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

	#Allow user to back out without committing to any of
	#these bets
	if prop_location == "B" or prop_location == "b":
		table()
		return(bets)

	#check for hardways submenu
	if prop_location == "1":
		bets = hardwaybets(bets)
		return(bets)

	#Get bet amount
	print("Enter bet amount: ")
	propbet = 0
	while not int(propbet) in range(1, bankroll+1):
		if propbet > bankroll:
			print("You do not have that much.")
			print("Your current bankroll is: $" + str(bankroll))
			print("Enter a bet amount: ")
		try:
			propbet = int(input())
		except ValueError:
			print("Error: Invalid entry. Please enter a number.")
			continue
	print("You chose " + str(propbet))

	#Depending on user input go to next submenu function
	#for hardway bets or take bets on other prop bets
	if operating == "Linux":
		os.system("clear")
	elif operating == "Windows":
		os.system("cls")
	elif operating == "Darwin":
		os.system("clear")
	else:
		print("ERROR: Unknown Operating System!")
	print("Your current bankroll is: $" + str(bankroll))
	#save(users_dict)
	if prop_location == "2":
		bets.update({"two":(propbet + bets.get("two"))})
		bankroll = bankroll - propbet
		propbet = 0
		prop_location = "0"
	if prop_location == "3":
		bets.update({"three":(propbet + bets.get("three"))})
		bankroll = bankroll - propbet
		propbet = 0
		prop_location = "0"
	if prop_location == "11":
		bets.update({"eleven":(propbet + bets.get("eleven"))})
		bankroll = bankroll - propbet
		propbet = 0
		prop_location = "0"
	if prop_location == "12":
		bets.update({"twelve":(propbet + bets.get("twelve"))})
		bankroll = bankroll - propbet
		propbet = 0
		prop_location = "0"
	if prop_location == "6":
		bankroll = bankroll - propbet
		propbet = math.floor(propbet/4)
		bets.update({"two":(propbet + bets.get("two"))})
		bets.update({"three":(propbet + bets.get("three"))})
		bets.update({"eleven":(propbet + bets.get("eleven"))})
		bets.update({"twelve":(propbet + bets.get("twelve"))})
		propbet = 0
		prop_location = "0"
	if prop_location == "7":
		bets.update({"anyseven":(propbet + bets.get("anyseven"))})
		bankroll = bankroll - propbet
		propbet = 0
		prop_location = "0"
	if prop_location == "C" or prop_location == "c":
		bets.update({"anycraps":(propbet + bets.get("anycraps"))})
		bankroll = bankroll - propbet
		propbet = 0
		prop_location = "0"
	table()

	print("You chose " + prop_location)
	table()
	return bets


#Function for any other miscellaneous bets
def otherbets(bets):
	global bankroll
	#Check for out of money and return if so
	if bankroll == 0:
		print("You have no more money available to bet.")
		input()
		table()
		return(bets)
	print("Your current bankroll is: $" + str(bankroll))
	otherbet_location = "0"
	#The only way to get out of the miscellaneous bet submenu is to type B or b for Back
	#Also includes a Takedown option as a seven will wipe all these bets and they are
	#not contract bets (bets you are stuck with once you make them (Pass and Come bets))
	#so players can choose to takedown or turn off these bets at any point to protect it
	#from the inevitable shooter Sevening Out
	while otherbet_location != "B" or otherbet_location != "b":
		while otherbet_location not in ("Q","q","B","b","T","t","C","c","6","8","W","w"):
			print("Choose where to place your bet: ")
			print("6  - Big 6")
			print("8  - Big 8")
			print("C  - C&E (Craps and Eleven")
			print("W  - World (must be divisible by 5)")
			print("T  - Take down a bet")
			print("B  - Back")
			print("Q  - Quit Game")
			otherbet_location = input()
			if otherbet_location in ("Q","q","B","b","T","t","C","c","6","8","W","w"):
				break
			else:
				print("Invalid entry!")
		print("You chose " + otherbet_location)

		#Allow for quitting game at every menu but warning player that there are still
		#live bets on the table and quitting now would surrender those bets to the house
		if otherbet_location == "Q" or otherbet_location == "q":
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
		if otherbet_location == "B" or otherbet_location == "b":
			table()
			return(bets)

		#Takedown bets submenu
		if otherbet_location == "T" or otherbet_location == "t":
			print("Which bet do you want to take down?")
			if bets.get("big6") != 0:
				print("6  - Take down Big 6 bet")
			if bets.get("big8") != 0:
				print("8  - Take down Big 8 bet")
			print("B - Back")
			#Take user input and takedown relevant bet
			takedownbet = input()
			if (takedownbet == "B") or (takedownbet == "B"):
				return(bets)
			if takedownbet == "6":
				bankroll = bankroll + bets.get("big6")
				bets.update({"big6":0})
			if takedownbet == "8":
				bankroll = bankroll + bets.get("big8")
				bets.update({"big8":0})
			print("Your current bankroll is: $" + str(bankroll))
			break
		#Get bet amount
		print("Enter bet amount: ")
		otherbet = 0
		while not int(otherbet) in range(1, bankroll+1):
			if otherbet > bankroll:
				print("You do not have that much.")
				print("Your current bankroll is: $" + str(bankroll))
				print("Enter a bet amount: ")
			try:
				otherbet = int(input())
			except ValueError:
				print("Error: Invalid entry. Please enter a number.")
				continue
		print("You chose " + str(otherbet))
		#Take place bet and based on number chosen update betting dictionary
		#for that number
		bankroll = bankroll - otherbet
		#if operating == "Linux":
		#	os.system("clear")
		#elif operating == "Windows":
		#	os.system("cls")
		#elif operating == "Darwin":
		#	os.system("clear")
		#else:
		#	print("ERROR: Unknown Operating System!")
		print("Your current bankroll is: $" + str(bankroll))
		#save(users_dict)
		if otherbet_location == "6":
			bets.update({"big6":(otherbet + bets.get("big6"))})
			otherbet_location = "0"
		if otherbet_location == "8":
			bets.update({"big8":(otherbet + bets.get("big8"))})
			otherbet_location = "0"
		if otherbet_location == "C" or otherbet_location == "c":
			bets.update({"C&E":(otherbet + bets.get("C&E"))})
			otherbet_location = "0"
		if otherbet_location == "W" or otherbet_location == "w":
			otherbet = math.floor(otherbet/5)
			bets.update({"world":(otherbet + bets.get("world"))})
			otherbet_location = "0"
		table()
	return bets


#Function for mid game betting
def midgamebet(bets):
	global bankroll
	midbet_location = "0"
	#print(bets)   					##FOR TESTING
	#input()						##FOR TESTING
	#Main Menu for mid-game betting (not the Come-Out roll)
	while midbet_location != "1":
		while midbet_location not in ("1","2","3","4","5","6","7","8","9",""):
			print("Your bankroll is: $" + str(bankroll))
			print("Enter a bet location: ")
			print("1 - No More Bets - Roll Dice")
			print("2 - Free Odds Bets on Pass or Don't Pass")
			print("3 - Field Bet")
			print("4 - Come or Don't Come Bets")
			print("5 - Free Odds Bets on Come or Don't Come")
			print("6 - Place, Buy, and Lay Bets")
			print("7 - Proposition Bets")
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
			bets = comedc(bets)
		#Choosing 5 allows player to bet Odds on Come points or
		#Don't Come points 
		if midbet_location == 5:
			#Free Odds on Come/Don't Come
			bets = freeodds_comedc(bets)
		#Choosing 6 allows player to bet on place numbers, buy numbers,
		#or lay numbers
		if midbet_location == 6:
			#Place/Buy/Lay
			bets = placebuylay(bets)
		#Choosing 7 allows player to bet on the Proposition Bets
		if midbet_location == 7:
			#Proposition Bets
			bets = proposition(bets)
		#Choosing 8 allows players to make other bets (Big6, Big8, C&E, World,
		#and anything else I come up with or think about)
		if midbet_location == 8:
			#Miscellaneous Bets
			bets = otherbets(bets)
	table()
	return bets


#############################################
#
#
#  Script starts here
#
#
#############################################

if operating == "Linux":
	os.system("clear")
elif operating == "Windows":
	os.system("cls")
elif operating == "Darwin":
	os.system("clear")
else:
	print("ERROR: Unknown Operating System!")


#color on or off, 1 for on, 0 for off
#global colorized
#colorized = 1
#Handled in settings now

#sound effects on or off
#global soundfx 
#soundfx = 1 
#Handled in settings now

#mature content is off by default
#mature = 0
#Handled in settings now

#Intro screen
#if colorized == 0:
#	graphics.intro()
#else:
#	graphics.color_intro()

#Result of two d6 dice being thrown
#global result
#result = 0

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

#Mid Game submenu selection
midbet_location = "0"

#Bet_amount variable is amount
#bet on Pass or Don't Pass on
#Come out roll.
bet_amount = 0

#Trying to control if a DC point is
#new or old to prevent clearing
#with newdcbet initialized to 0
newdcbet = 0

#Lists for Place, Buy, and Lay bets
#Need to check against results
global placeselect
placeselect =	[0,0,0,0,0,0]
global buyselect
buyselect   = 	[0,0,0,0,0,0]
global layselect
layselect   =	[0,0,0,0,0,0]

#Variable to track whether a hardway
#is thrown: 0 means no hardway
#other oprions are 4,6,8, and 10.
global hardway
hardway = 0

#Set up betting dictionary
bets = bets_init()

#Attempting to fix hanging game bug
#which I think is multiple winsounds
#being played simultaneously
#so alternate solution is if any win 
#occurs set winflag to 1 then later check
#winflag to play singular winsound
winflag = 0

#Check for mature content
#mature = maturecheck(mature)
#Handled in settings now

#Initializing username for settings loop in 
#player() function
username = "dealer"

#Set up user, whether new or loading old user
username = player(username)
print("Welcome " + username + "!!!")
print("Your bankroll is: $" + str(bankroll))

save(users_dict)
if operating == "Linux":
	os.system("clear")
elif operating == "Windows":
	os.system("cls")
elif operating == "Darwin":
	os.system("clear")
else:
	print("ERROR: Unknown Operating System!")

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
	#graphics.crapstable()
	table()
	#checking for easter egg if user chose mature content at start
	if bankroll == 0:
		if mature == 1:
			shady()
			print("Your current bankroll is: $" + str(bankroll))
			if colorized == 0:
				graphics.crapstable()
			else:
				graphics.color_crapstable()
	if bankroll == 0:
		gameover(0)
		break
	while bet_location not in ("1","2","3","4","Q","q",""):
		print("Enter a bet location: ")
		print("1 - Pass Line (Bet with the shooter)")
		print("2 - Don't Pass Line (The Dark Side)")
		print("3 - Done betting/Skip Betting")
		print("4 - Other bets")
		print("Q - Quit Game")
		#This variable bet_location only refers to Pass and Don't Pass
		bet_location = input()
		if bet_location == "4":
			bets = midgamebet(bets)	
		if bet_location in ("1","2","3","Q","q",""):
			break
		else:
			print("Invalid entry!")
	if bet_location == "Q" or bet_location == "q":
		quitflag = True
		gameover(0)
		break

		
	print("You chose " + bet_location)
	#bet_location = int(bet_location)

	if bet_location == "1" or bet_location == "2":
		#Get bet amount
		print("Enter a bet amount: ")
		#This variable bet_amount only refers to Pass or Don't Pass bet
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
	if operating == "Linux":
		os.system("clear")
	elif operating == "Windows":
		os.system("cls")
	elif operating == "Darwin":
		os.system("clear")
	else:
		print("ERROR: Unknown Operating System!")
	print("Your current bankroll is: $" + str(bankroll))
	save(users_dict)

    #########################################
    #
	# The Come-Out roll
    #
    #########################################
	iscomeout = True
	while iscomeout == True:
		#graphics.crapstable()
		table()
		print("Press Enter to roll.")
		input()
		result = dice()
		#If 7 or 11 Pass bettors win, Don't Pass loses
		if result == 7 or result == 11:
			print("Shooter Wins!!!")
			if soundfx == 1:
				if operating == "Linux":
					os.system("aplay -q " + applausesound + " > /dev/null 2>&1")
				elif operating == "Windows":
					os.system("powershell -c (New-Object Media.SoundPlayer 'data\\sounds\\claps.wav').PlaySync();")
				elif operating == "Darwin":
					os.system("afplay " + applausesound + " > /dev/null 2>&1")
				else:
					print("ERROR: Unknown Operating System!")
			if bet_location == "1":
				bankroll = (bankroll + (bet_amount * 2))
				winflag = 1

			#Lay bet payouts on come-out rolls, pays on 7
			if result == 7:
				if bets.get("lay4") != 0:
					bankroll = (bankroll + math.floor(bets.get("lay4")/2) + bets.get("lay4"))
					winflag = 1
					bets.update({"lay4":0})
				if bets.get("lay5") != 0:
					bankroll = (bankroll + math.floor((bets.get("lay5") * 2)/3) + bets.get("lay5"))
					winflag = 1
					bets.update({"lay5":0})
				if bets.get("lay6") != 0:
					bankroll = (bankroll + math.floor((bets.get("lay6") * 5)/6) + bets.get("lay6"))
					winflag = 1
					bets.update({"lay6":0})
				if bets.get("lay8") != 0:
					bankroll = (bankroll + math.floor((bets.get("lay8") * 5)/6) + bets.get("lay8"))
					winflag = 1
					bets.update({"lay8":0})
				if bets.get("lay9") != 0:
					bankroll = (bankroll + math.floor((bets.get("lay9") * 2)/3) + bets.get("lay9"))
					winflag = 1
					bets.update({"lay9":0})
				if bets.get("lay10") != 0:
					bankroll = (bankroll + math.floor(bets.get("lay10")/2) + bets.get("lay10"))
					winflag = 1
					bets.update({"lay10":0})
				save(users_dict)


			#Clearing out come points on 7 on come out roll
			if result == 7:
				#Payouts for Don't Come on Seven Out	
				#Losses for come points
				if bets.get("dc4") != 0:
					winflag = 1
					bankroll = bankroll + (bets.get("dc4") * 2)
					bets.update({"dc4":0})
					bets.update({"come4":0})
				if bets.get("dc5") != 0:
					winflag = 1
					bankroll = bankroll + (bets.get("dc5") * 2)
					bets.update({"dc5":0})
					bets.update({"come5":0})
				if bets.get("dc6") != 0:
					winflag = 1
					bankroll = bankroll + (bets.get("dc6") * 2)
					bets.update({"dc6":0})
					bets.update({"come6":0})
				if bets.get("dc8") != 0:
					winflag = 1
					bankroll = bankroll + (bets.get("dc8") * 2)
					bets.update({"dc8":0})
					bets.update({"come8":0})
				if bets.get("dc9") != 0:
					winflag = 1
					bankroll = bankroll + (bets.get("dc9") * 2)
					bets.update({"dc9":0})
					bets.update({"come9":0})
				if bets.get("dc10") != 0:
					winflag = 1
					bankroll = bankroll + (bets.get("dc10") * 2)
					bets.update({"dc10":0})
					bets.update({"come10":0})
				#Payouts for Don't Come Odds on Seven Out	
				#Losses for come point odds
				if bets.get("freeodds_dc4") != 0:
					winflag = 1
					bankroll = bankroll + math.floor(((bets.get("freeodds_dc4") * 1)/2) + bets.get("freeodds_dc4"))
					bets.update({"freeodds_dc4":0})
					bets.update({"freeodds_come4":0})
				if bets.get("freeodds_dc5") != 0:
					winflag = 1
					bankroll = bankroll + math.floor(((bets.get("freeodds_dc5") * 2)/3) + bets.get("freeodds_dc5"))
					bets.update({"freeodds_dc5":0})
					bets.update({"freeodds_come5":0})
				if bets.get("freeodds_dc6") != 0:
					winflag = 1
					bankroll = bankroll + math.floor(((bets.get("freeodds_dc6") * 5)/6) + bets.get("freeodds_dc6"))
					bets.update({"freeodds_dc6":0})
					bets.update({"freeodds_come6":0})
				if bets.get("freeodds_dc8") != 0:
					winflag = 1
					bankroll = bankroll + math.floor(((bets.get("freeodds_dc8") * 5)/6) + bets.get("freeodds_dc8"))
					bets.update({"freeodds_dc8":0})
					bets.update({"freeodds_come8":0})
				if bets.get("freeodds_dc9") != 0:
					winflag = 1
					bankroll = bankroll + math.floor(((bets.get("freeodds_dc9") * 2)/3) + bets.get("freeodds_dc9"))
					bets.update({"freeodds_dc9":0})
					bets.update({"freeodds_come9":0})
				if bets.get("freeodds_dc10") != 0:
					winflag = 1
					bankroll = bankroll + math.floor(((bets.get("freeodds_dc10") * 1)/2) + bets.get("freeodds_dc10"))
					bets.update({"freeodds_dc10":0})
					bets.update({"freeodds_come10":0})

				bets.update({"come4":0})
				bets.update({"come5":0})
				bets.update({"come6":0})
				bets.update({"come8":0})
				bets.update({"come9":0})
				bets.update({"come10":0})
				bets.update({"freeodds_come4":0})
				bets.update({"freeodds_come5":0})
				bets.update({"freeodds_come6":0})
				bets.update({"freeodds_come8":0})
				bets.update({"freeodds_come9":0})
				bets.update({"freeodds_come10":0})

			if winflag == 1:
				if soundfx == 1:
					if operating == "Linux":
						os.system("aplay -q " + winsound + " > /dev/null 2>&1")
					elif operating == "Windows":
						os.system("powershell -c (New-Object Media.SoundPlayer 'data\\sounds\\chips.wav').PlaySync();")
					elif operating == "Darwin":
						os.system("afplay " + winsound + " > /dev/null 2>&1")
					else:
						print("ERROR: Unknown Operating System!")
				winflag = 0	

			save(users_dict)

			iscomeout = True
			point = 0
			input()
			if operating == "Linux":
				os.system("clear")
			elif operating == "Windows":
				os.system("cls")
			elif operating == "Darwin":
				os.system("clear")
			else:
				print("ERROR: Unknown Operating System!")
			break
		#If 2, 3, or 12 Pass bettors lose, Don't Pass wins
        #on 2 or 3, pushes if rolls 12 (BAR 12)
		elif result == 2 or result == 3 or result == 12:
			print("Shooter Craps Out!")
			if soundfx == 1:
				if operating == "Linux":
					os.system("aplay -q " + awwsound + " > /dev/null 2>&1")
				elif operating == "Windows":
					os.system("powershell -c (New-Object Media.SoundPlayer 'data\\sounds\\aww.wav').PlaySync();")
				elif operating == "Darwin":
					os.system("afplay " + awwsound + " > /dev/null 2>&1")
				else:
					print("ERROR: Unknown Operating System!")
			#print("bet location is : ", bet_location)
			if bet_location == "2":
				if result == 2 or result == 3:
					bankroll = (bankroll + (bet_amount * 2))
					winflag = 1
				if result == 12:
					bankroll = (bankroll + bet_amount)

			if winflag == 1:
				if soundfx == 1:
					if operating == "Linux":
						os.system("aplay -q " + winsound + " > /dev/null 2>&1")
					elif operating == "Windows":
						os.system("powershell -c (New-Object Media.SoundPlayer 'data\\sounds\\chips.wav').PlaySync();")
					elif operating == "Darwin":
						os.system("afplay " + winsound + " > /dev/null 2>&1")
					else:
						print("ERROR: Unknown Operating System!")
				winflag = 0	

			save(users_dict)
			iscomeout = True
			point = 0
			input()
			if operating == "Linux":
				os.system("clear")
			elif operating == "Windows":
				os.system("cls")
			elif operating == "Darwin":
				os.system("clear")
			else:
				print("ERROR: Unknown Operating System!")
			break
		#####################################################
		#
		# Anything else becomes the point (4, 5, 6, 8, 9, 10)
		#
		#####################################################
		else:
			point = result
			print("The point is now " + str(point))
			#If point is established we change come-out roll state
			iscomeout = False
			save(users_dict)

			#Handling Existing Come Bet
			if bets.get("come") != 0:
				#Come bet wins on 7 or 11
				if result == 7 or result == 11:
					print("Come Bet Winner!!!")
					winflag = 1
					comebet = bets.get("come")
					bets.update({"come":0})
					bankroll = bankroll + (comebet * 2)		
					comebet = 0
				if result == 2 or result == 3 or result == 12:
					bets.update({"come":0})
				if result == 4:
					bets.update({"come4":(bets.get("come"))})
					bets.update({"come":0})
				if result == 5:
					bets.update({"come5":(bets.get("come"))})
					bets.update({"come":0})
				if result == 6:
					bets.update({"come6":(bets.get("come"))})
					bets.update({"come":0})
				if result == 8:
					bets.update({"come8":(bets.get("come"))})
					bets.update({"come":0})
				if result == 9:
					bets.update({"come9":(bets.get("come"))})
					bets.update({"come":0})
				if result == 10:
					bets.update({"come10":(bets.get("come"))})
					bets.update({"come":0})
			#Handling Exisitng Don't Come Bet
			if bets.get("dc") != 0:
				#Don't Come bet wins on 2 or 3
				if result == 2 or result == 3:
					print("Pay the Don't Come!!!")
					winflag = 1
					comebet = bets.get("dc")
					bets.update({"dc":0})
					bankroll = bankroll + (comebet * 2)		
					comebet = 0
				#Loss on 7 or 11
				elif result == 7 or result == 11:
					bets.update({"dc":0})
				#Push if roll is 12
				elif result == 12:
					comebet = bets.get("dc")
					bets.update({"dc":0})
					bankroll = bankroll + comebet
					comebet = 0
				else:
					if result == 4:
						bets.update({"dc4":(bets.get("dc"))})
						bets.update({"dc":0})
						newdcbet = 1
					if result == 5:
						bets.update({"dc5":(bets.get("dc"))})
						bets.update({"dc":0})
						newdcbet = 1
					if result == 6:
						bets.update({"dc6":(bets.get("dc"))})
						bets.update({"dc":0})
						newdcbet = 1
					if result == 8:
						bets.update({"dc8":(bets.get("dc"))})
						bets.update({"dc":0})
						newdcbet = 1
					if result == 9:
						bets.update({"dc9":(bets.get("dc"))})
						bets.update({"dc":0})
						newdcbet = 1
					if result == 10:
						bets.update({"dc10":(bets.get("dc"))})
						bets.update({"dc":0})
						newdcbet = 1
			

			#Payouts if dice result matches come point	
			#Losses for don't come points
			if bets.get("come4") != 0 and result == 4:
				winflag = 1
				bankroll = bankroll + (bets.get("come4") * 2)
				bets.update({"come4":0})
			if bets.get("come5") != 0 and result == 5:
				winflag = 1
				bankroll = bankroll + (bets.get("come5") * 2)
				bets.update({"come5":0})
			if bets.get("come6") != 0 and result == 6:
				winflag = 1
				bankroll = bankroll + (bets.get("come6") * 2)
				bets.update({"come6":0})
			if bets.get("come8") != 0 and result == 8:
				winflag = 1
				bankroll = bankroll + (bets.get("come8") * 2)
				bets.update({"come8":0})
			if bets.get("come9") != 0 and result == 9:
				winflag = 1
				bankroll = bankroll + (bets.get("come9") * 2)
				bets.update({"come9":0})
			if bets.get("come10") != 0 and result == 10:
				winflag = 1
				bankroll = bankroll + (bets.get("come10") * 2)
				bets.update({"come10":0})
			save(users_dict)
			if newdcbet == 0:
				if bets.get("dc4") != 0 and result == 4:
					bets.update({"dc4":0})
				if bets.get("dc5") != 0 and result == 5:
					bets.update({"dc5":0})
				if bets.get("dc6") != 0 and result == 6:
					bets.update({"dc6":0})
				if bets.get("dc8") != 0 and result == 8:
					bets.update({"dc8":0})
				if bets.get("dc9") != 0 and result == 9:
					bets.update({"dc9":0})
				if bets.get("dc10") != 0 and result == 10:
					bets.update({"dc10":0})
				save(users_dict)
			newdcbet = 0
			#Payouts for odds if dice result matches come point	
			#Losses for odds on don't come points
			if bets.get("freeodds_come4") != 0 and result == 4:
				winflag = 1
				bankroll = bankroll + math.floor((bets.get("freeodds_come4") * 2)/1)
				bets.update({"freeodds_come4":0})
				bets.update({"freeodds_dc4":0})
			if bets.get("freeodds_come5") != 0 and result == 5:
				winflag = 1
				bankroll = bankroll + math.floor((bets.get("freeodds_come5") * 3)/2)
				bets.update({"freeodds_come5":0})
				bets.update({"freeodds_dc5":0})
			if bets.get("freeodds_come6") != 0 and result == 6:
				winflag = 1
				bankroll = bankroll + math.floor((bets.get("freeodds_come6") * 6)/5)
				bets.update({"freeodds_come6":0})
				bets.update({"freeodds_dc6":0})
			if bets.get("freeodds_come8") != 0 and result == 8:
				winflag = 1
				bankroll = bankroll + math.floor((bets.get("freeodds_come8") * 6)/5)
				bets.update({"freeodds_come8":0})
				bets.update({"freeodds_dc8":0})
			if bets.get("freeodds_come9") != 0 and result == 9:
				winflag = 1
				bankroll = bankroll + math.floor((bets.get("freeodds_come9") * 3)/2)
				bets.update({"freeodds_come9":0})
				bets.update({"freeodds_dc9":0})
			if bets.get("freeodds_come10") != 0 and result == 10:
				winflag = 1
				bankroll = bankroll + math.floor((bets.get("freeodds_come10") * 2)/1)
				bets.update({"freeodds_come10":0})
				bets.update({"freeodds_dc10":0})
			save(users_dict)
			if newdcbet == 0:
				if bets.get("freeodds_dc4") != 0 and result == 4:
					bets.update({"freeodds_dc4":0})
				if bets.get("freeodds_dc5") != 0 and result == 5:
					bets.update({"freeodds_dc5":0})
				if bets.get("freeodds_dc6") != 0 and result == 6:
					bets.update({"freeodds_dc6":0})
				if bets.get("freeodds_dc8") != 0 and result == 8:
					bets.update({"freeodds_dc8":0})
				if bets.get("freeodds_dc9") != 0 and result == 9:
					bets.update({"freeodds_dc9":0})
				if bets.get("freeodds_dc10") != 0 and result == 10:
					bets.update({"freeodds_dc10":0})
				save(users_dict)
			newdcbet = 0

			#Lay bets lose if their number rolls
			#before a 7
			if (bets.get("lay4") != 0) and (result == 4):
				bets.update({"lay4":0})
			if (bets.get("lay5") != 0) and (result == 5):
				bets.update({"lay5":0})
			if (bets.get("lay6") != 0) and (result == 6):
				bets.update({"lay6":0})
			if (bets.get("lay8") != 0) and (result == 8):
				bets.update({"lay8":0})
			if (bets.get("lay9") != 0) and (result == 9):
				bets.update({"lay9":0})
			if (bets.get("lay10") != 0) and (result == 10):
				bets.update({"lay10":0})
			save(users_dict)

			#Field bet payouts
			if result in (2,3,4,9,10,11,12):
				if (bets.get("field") != 0):
					print("Field bet Winner!!!")
					winflag = 1
					if result == 2:
						bankroll = (bankroll + (bets.get("field") * 3))
						bets.update({"field":0})
					elif result == 12:
						#pay triple on 12 or just double ??? Not sure yet
						#bankroll = (bankroll + (bets.get("field") * 4))
						bankroll = (bankroll + (bets.get("field") * 3))
						bets.update({"field":0})
					elif result in (3,4,9,10,11):
						bankroll = (bankroll + (bets.get("field") * 2))
						bets.update({"field":0})
					else:
						bets.update({"field":0})
			else:
				bets.update({"field":0})
			save(users_dict)

		
			#Non-hardway proposition bet payouts
			#Payouts for Miscellaneous bets, C&E and World bets
			if result == 2:
				print("Snake Eyes!")
				if (bets.get("two") != 0):
					bankroll = (bankroll + (bets.get("two") * 30)) 			
					winflag = 1
					bets.update({"two":0})
				if (bets.get("anycraps") != 0):
					bankroll = (bankroll + (bets.get("anycraps") * 7)) 			
					winflag = 1
					bets.update({"two":0})
				if (bets.get("C&E") != 0):
					bankroll = (bankroll + math.floor(bets.get("C&E") * 7)) 			
					winflag = 1
					bets.update({"C&E":0})
				if (bets.get("world") != 0):
					bankroll = (bankroll + math.floor((bets.get("world") * 26)/5)) 			
					winflag = 1
					bets.update({"world":0})
			if result == 3:
				print("Pay the Three!")
				if (bets.get("three") != 0):
					bankroll = (bankroll + (bets.get("three") * 15)) 			
					winflag = 1
					bets.update({"three":0})
				if (bets.get("anycraps") != 0):
					bankroll = (bankroll + (bets.get("anycraps") * 7)) 			
					winflag = 1
					bets.update({"three":0})
				if (bets.get("C&E") != 0):
					bankroll = (bankroll + math.floor(bets.get("C&E") * 7)) 			
					winflag = 1
					bets.update({"C&E":0})
				if (bets.get("world") != 0):
					bankroll = (bankroll + math.floor((bets.get("world") * 11)/5)) 			
					winflag = 1
					bets.update({"world":0})
			if result == 11:
				print("YO-Eleven!!!")
				if (bets.get("eleven") != 0):
					bankroll = (bankroll + (bets.get("eleven") * 15)) 			
					winflag = 1
					bets.update({"eleven":0})
				if (bets.get("C&E") != 0):
					bankroll = (bankroll + math.floor(bets.get("C&E") * 15)) 			
					winflag = 1
					bets.update({"C&E":0})
				if (bets.get("world") != 0):
					bankroll = (bankroll + math.floor((bets.get("world") * 11)/5)) 			
					winflag = 1
					bets.update({"world":0})
			if result == 12:
				print("Box Cars!")
				if (bets.get("twelve") != 0):
					bankroll = (bankroll + (bets.get("twelve") * 30)) 			
					winflag = 1
					bets.update({"twelve":0})
				if (bets.get("anycraps") != 0):
					bankroll = (bankroll + (bets.get("anycraps") * 7)) 			
					winflag = 1
					bets.update({"twelve":0})
				if (bets.get("C&E") != 0):
					bankroll = (bankroll + math.floor(bets.get("C&E") * 7)) 			
					winflag = 1
					bets.update({"C&E":0})
				if (bets.get("world") != 0):
					bankroll = (bankroll + math.floor((bets.get("world") * 26)/5)) 			
					winflag = 1
					bets.update({"world":0})
			if result == 7:
				if (bets.get("anyseven") != 0):
					bankroll = (bankroll + (bets.get("anyseven") * 4)) 			
					print("Big Red!!!")
					winflag = 1
			#Resetting Propositions bets (minus Hardways) afer payouts or if loss
			bets.update({"two":0})
			bets.update({"three":0})
			bets.update({"eleven":0})
			bets.update({"twelve":0})
			bets.update({"anyseven":0})
			bets.update({"anycraps":0})
			save(users_dict)
			#Clearing Miscellaneous bets
			bets.update({"C&E":0})	
			bets.update({"world":0})	

			if winflag == 1:
				if soundfx == 1:
					if operating == "Linux":
						os.system("aplay -q " + winsound + " > /dev/null 2>&1")
					elif operating == "Windows":
						os.system("powershell -c (New-Object Media.SoundPlayer 'data\\sounds\\chips.wav').PlaySync();")
					elif operating == "Darwin":
						os.system("afplay " + winsound + " > /dev/null 2>&1")
					else:
						print("ERROR: Unknown Operating System!")
				winflag = 0	

			save(users_dict)

			input()
			if operating == "Linux":
				os.system("clear")
			elif operating == "Windows":
				os.system("cls")
			elif operating == "Darwin":
				os.system("clear")
			else:
				print("ERROR: Unknown Operating System!")

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
			#THAT EXTRA PAUSE IN THE GAME, next 2 lines
			#print("Press Enter to roll again.")
			#input()
			result = dice()

			#Payouts if dice result matches come point	
			#Losses for don't come points
			if bets.get("come4") != 0 and result == 4:
				winflag = 1
				bankroll = bankroll + (bets.get("come4") * 2)
				bets.update({"come4":0})
				bets.update({"dc4":0})
			if bets.get("come5") != 0 and result == 5:
				winflag = 1
				bankroll = bankroll + (bets.get("come5") * 2)
				bets.update({"come5":0})
				bets.update({"dc5":0})
			if bets.get("come6") != 0 and result == 6:
				winflag = 1
				bankroll = bankroll + (bets.get("come6") * 2)
				bets.update({"come6":0})
				bets.update({"dc6":0})
			if bets.get("come8") != 0 and result == 8:
				winflag = 1
				bankroll = bankroll + (bets.get("come8") * 2)
				bets.update({"come8":0})
				bets.update({"dc8":0})
			if bets.get("come9") != 0 and result == 9:
				winflag = 1
				bankroll = bankroll + (bets.get("come9") * 2)
				bets.update({"come9":0})
				bets.update({"dc9":0})
			if bets.get("come10") != 0 and result == 10:
				winflag = 1
				bankroll = bankroll + (bets.get("come10") * 2)
				bets.update({"come10":0})
				bets.update({"dc10":0})
		
			if bets.get("dc4") != 0 and result == 4:
				bets.update({"dc4":0})
			if bets.get("dc5") != 0 and result == 5:
				bets.update({"dc5":0})
			if bets.get("dc6") != 0 and result == 6:
				bets.update({"dc6":0})
			if bets.get("dc8") != 0 and result == 8:
				bets.update({"dc8":0})
			if bets.get("dc9") != 0 and result == 9:
				bets.update({"dc9":0})
			if bets.get("dc10") != 0 and result == 10:
				bets.update({"dc10":0})
			#Payouts for odds if dice result matches come point	
			#Losses for odds on don't come points
			if bets.get("freeodds_come4") != 0 and result == 4:
				winflag = 1
				bankroll = bankroll + math.floor((bets.get("freeodds_come4") * 2)/1)
				bets.update({"freeodds_come4":0})
				bets.update({"freeodds_dc4":0})
			if bets.get("freeodds_come5") != 0 and result == 5:
				winflag = 1
				bankroll = bankroll + math.floor((bets.get("freeodds_come5") * 3)/2)
				bets.update({"freeodds_come5":0})
				bets.update({"freeodds_dc5":0})
			if bets.get("freeodds_come6") != 0 and result == 6:
				winflag = 1
				bankroll = bankroll + math.floor((bets.get("freeodds_come6") * 6)/5)
				bets.update({"freeodds_come6":0})
				bets.update({"freeodds_dc6":0})
			if bets.get("freeodds_come8") != 0 and result == 8:
				winflag = 1
				bankroll = bankroll + math.floor((bets.get("freeodds_come8") * 6)/5)
				bets.update({"freeodds_come8":0})
				bets.update({"freeodds_dc8":0})
			if bets.get("freeodds_come9") != 0 and result == 9:
				winflag = 1
				bankroll = bankroll + math.floor((bets.get("freeodds_come9") * 3)/2)
				bets.update({"freeodds_come9":0})
				bets.update({"freeodds_dc9":0})
			if bets.get("freeodds_come10") != 0 and result == 10:
				winflag = 1
				bankroll = bankroll + math.floor((bets.get("freeodds_come10") * 2)/1)
				bets.update({"freeodds_come10":0})
				bets.update({"freeodds_dc10":0})
			if result == 7:
				bets.update({"freeodds_come4":0})
				bets.update({"freeodds_come5":0})
				bets.update({"freeodds_come6":0})
				bets.update({"freeodds_come8":0})
				bets.update({"freeodds_come9":0})
				bets.update({"freeodds_come10":0})
			save(users_dict)
			if newdcbet == 0:
				if bets.get("freeodds_dc4") != 0 and result == 4:
					bets.update({"freeodds_dc4":0})
				if bets.get("freeodds_dc5") != 0 and result == 5:
					bets.update({"freeodds_dc5":0})
				if bets.get("freeodds_dc6") != 0 and result == 6:
					bets.update({"freeodds_dc6":0})
				if bets.get("freeodds_dc8") != 0 and result == 8:
					bets.update({"freeodds_dc8":0})
				if bets.get("freeodds_dc9") != 0 and result == 9:
					bets.update({"freeodds_dc9":0})
				if bets.get("freeodds_dc10") != 0 and result == 10:
					bets.update({"freeodds_dc10":0})
				save(users_dict)
			newdcbet = 0


					

			#Handling Existing Come Bet
			if bets.get("come") != 0:
				#Come bet wins on 7 or 11
				if result == 7 or result == 11:
					print("Come Bet Winner!!!")
					winflag = 1
					comebet = bets.get("come")
					bets.update({"come":0})
					bankroll = bankroll + (comebet * 2)		
					comebet = 0
				if result == 2 or result == 3 or result == 12:
					bets.update({"come":0})
				if result == 4:
					bets.update({"come4":(bets.get("come"))})
					bets.update({"come":0})
				if result == 5:
					bets.update({"come5":(bets.get("come"))})
					bets.update({"come":0})
				if result == 6:
					bets.update({"come6":(bets.get("come"))})
					bets.update({"come":0})
				if result == 8:
					bets.update({"come8":(bets.get("come"))})
					bets.update({"come":0})
				if result == 9:
					bets.update({"come9":(bets.get("come"))})
					bets.update({"come":0})
				if result == 10:
					bets.update({"come10":(bets.get("come"))})
					bets.update({"come":0})

			#Handling Exisitng Don't Come Bet
			if bets.get("dc") != 0:
				#Don't Come bet wins on 2 or 3
				if result == 2 or result == 3:
					print("Pay the Don't Come!!!")
					winflag = 1
					comebet = bets.get("dc")
					bets.update({"dc":0})
					bankroll = bankroll + (comebet * 2)		
					comebet = 0
				#Loss on 7 or 11
				elif result == 7 or result == 11:
					bets.update({"dc":0})
				#Push if roll is 12
				elif result == 12:
					comebet = bets.get("dc")
					bets.update({"dc":0})
					bankroll = bankroll + comebet
					comebet = 0
				else:
					if result == 4:
						bets.update({"dc4":(bets.get("dc"))})
						bets.update({"dc":0})
						newdcbet = 1
					if result == 5:
						bets.update({"dc5":(bets.get("dc"))})
						bets.update({"dc":0})
						newdcbet = 1
					if result == 6:
						bets.update({"dc6":(bets.get("dc"))})
						bets.update({"dc":0})
						newdcbet = 1
					if result == 8:
						bets.update({"dc8":(bets.get("dc"))})
						bets.update({"dc":0})
						newdcbet = 1
					if result == 9:
						bets.update({"dc9":(bets.get("dc"))})
						bets.update({"dc":0})
						newdcbet = 1
					if result == 10:
						bets.update({"dc10":(bets.get("dc"))})
						bets.update({"dc":0})
						newdcbet = 1
			


			#Place bet payouts on non come-out rolls, bets are off on come-out rolls
			if bets.get("place4") != 0:
				if placeselect[0] == result:
					bankroll = (bankroll + math.floor((bets.get("place4") * 9)/5) + bets.get("place4"))
					winflag = 1
					bets.update({"place4":0})
			if bets.get("place5") != 0:
				if placeselect[1] == result:
					bankroll = (bankroll + math.floor((bets.get("place5") * 7)/5) + bets.get("place5"))
					winflag = 1
					bets.update({"place5":0})
			if bets.get("place6") != 0:
				if placeselect[2] == result:
					bankroll = (bankroll + math.floor((bets.get("place6") * 7)/6) + bets.get("place6"))
					winflag = 1
					bets.update({"place6":0})
			if bets.get("place8") != 0:
				if placeselect[3] == result:
					bankroll = (bankroll + math.floor((bets.get("place8") * 7)/6) + bets.get("place8"))
					winflag = 1
					bets.update({"place8":0})
			if bets.get("place9") != 0:
				if placeselect[4] == result:
					bankroll = (bankroll + math.floor((bets.get("place9") * 7)/5) + bets.get("place9"))
					winflag = 1
					bets.update({"place9":0})
			if bets.get("place10") != 0:
				if placeselect[5] == result:
					bankroll = (bankroll + math.floor((bets.get("place10") * 9)/5) + bets.get("place10"))
					winflag = 1
					bets.update({"place10":0})


			#Hardway bet payouts
			if (bets.get("hardway4") != 0) and (hardway == 4):
				bankroll = (bankroll + (bets.get("hardway4") * 7) + bets.get("hardway4"))
				winflag = 1
				bets.update({"hardway4":0})
				hardway = 0
			if (bets.get("hardway6") != 0) and (hardway == 6):
				bankroll = (bankroll + (bets.get("hardway6") * 9) + bets.get("hardway6"))
				winflag = 1
				bets.update({"hardway6":0})
				hardway = 0
			if bets.get("hardway8") != 0 and (hardway == 8):
				bankroll = (bankroll + (bets.get("hardway8") * 9) + bets.get("hardway8"))
				winflag = 1
				bets.update({"hardway8":0})
				hardway = 0
			if bets.get("hardway10") != 0 and (hardway == 10):
				bankroll = (bankroll + (bets.get("hardway10") * 7) + bets.get("hardway10"))
				winflag = 1
				bets.update({"hardway10":0})
				hardway = 0


			#Miscellaneous bet payouts on non come-out rolls, bets are off on come-out rolls
			#Big 6 and Big 8 only
			if bets.get("big6") != 0:
				bankroll = (bankroll + bets.get("big6") * 2)
				winflag = 1
				bets.update({"big6":0})
			if bets.get("big8") != 0:
				bankroll = (bankroll + bets.get("big8") * 2)
				winflag = 1
				bets.update({"big8":0})

			#Buy bet payouts on non come-out rolls, bets are off on come-out rolls
			#Initializing commission to zero for sanity
			commission = 0
			if bets.get("buy4") != 0:
				if buyselect[0] == result:
					commission = (math.ceil(bets.get("buy4") * 0.05))
					bankroll = (bankroll + math.floor(math.floor(bets.get("buy4") * 2) - commission) + bets.get("buy4"))
					winflag = 1
					bets.update({"buy4":0})
			if bets.get("buy5") != 0:
				if buyselect[1] == result:
					commission = (math.ceil(bets.get("buy5") * 0.05))
					bankroll = (bankroll + math.floor(math.floor((bets.get("buy5") * 3)/2) - commission) + bets.get("buy5"))
					winflag = 1
					bets.update({"buy5":0})
			if bets.get("buy6") != 0:
				if buyselect[2] == result:
					commission = (math.ceil(bets.get("buy6") * 0.05))
					bankroll = (bankroll + math.floor(math.floor((bets.get("buy6") * 6)/5) - commission) + bets.get("buy6"))
					winflag = 1
					bets.update({"buy6":0})
			if bets.get("buy8") != 0:
				if buyselect[3] == result:
					commission = (math.ceil(bets.get("buy8") * 0.05))
					bankroll = (bankroll + math.floor(math.floor((bets.get("buy8") * 6)/5) - commission) + bets.get("buy8"))
					winflag = 1
					bets.update({"buy8":0})
			if bets.get("buy9") != 0:
				if buyselect[4] == result:
					commission = (math.ceil(bets.get("buy9") * 0.05))
					bankroll = (bankroll + math.floor(math.floor((bets.get("buy9") * 3)/2) - commission) + bets.get("buy9"))
					winflag = 1
					bets.update({"buy9":0})
			if bets.get("buy10") != 0:
				if buyselect[5] == result:
					commission = (math.ceil(bets.get("buy10") * 0.05))
					bankroll = (bankroll + math.floor(math.floor(bets.get("buy10") * 2) - commission) + bets.get("buy10"))
					winflag = 1
					bets.update({"buy10":0})


			#Lay bet payouts on non come-out rolls
			#Pays on a Seven Out
			if result == 7:
				if bets.get("lay4") != 0:
					if layselect[0] != result:
						bankroll = (bankroll + math.floor(bets.get("lay4")/2) + bets.get("lay4"))
						winflag = 1
						bets.update({"lay4":0})
				if bets.get("lay5") != 0:
					if layselect[1] != result:
						bankroll = (bankroll + math.floor((bets.get("lay5") * 2)/3) + bets.get("lay5"))
						winflag = 1
						bets.update({"lay5":0})
				if bets.get("lay6") != 0:
					if layselect[2] != result:
						bankroll = (bankroll + math.floor((bets.get("lay6") * 5)/6) + bets.get("lay6"))
						winflag = 1
						bets.update({"lay6":0})
				if bets.get("lay8") != 0:
					if layselect[3] != result:
						bankroll = (bankroll + math.floor((bets.get("lay8") * 5)/6) + bets.get("lay8"))
						winflag = 1
						bets.update({"lay8":0})
				if bets.get("lay9") != 0:
					if layselect[4] != result:
						bankroll = (bankroll + math.floor((bets.get("lay9") * 2)/3) + bets.get("lay9"))
						winflag = 1
						bets.update({"lay9":0})
				if bets.get("lay10") != 0:
					if layselect[5] != result:
						bankroll = (bankroll + math.floor(bets.get("lay10")/2) + bets.get("lay10"))
						winflag = 1
						bets.update({"lay10":0})



			#Field bet payouts
			if result in (2,3,4,9,10,11,12):
				if (bets.get("field") != 0):
					print("Field bet Winner!!!")
					winflag = 1
					if result == 2:
						bankroll = (bankroll + (bets.get("field") * 3))
						bets.update({"field":0})
					elif result == 12:
						#pay triple on 12 or just double ??? Not sure yet
						#bankroll = (bankroll + (bets.get("field") * 4))
						bankroll = (bankroll + (bets.get("field") * 3))
						bets.update({"field":0})
					elif result in (3,4,9,10,11):
						bankroll = (bankroll + (bets.get("field") * 2))
						bets.update({"field":0})
					else:
						bets.update({"field":0})
			else:
				bets.update({"field":0})
			input()
			

			#Non-hardway proposition bet payouts
			#Payouts for Miscellaneous bets, C&E and World bets
			if result == 2:
				print("Snake Eyes!")
				if (bets.get("two") != 0):
					bankroll = (bankroll + (bets.get("two") * 30)) 			
					winflag = 1
					bets.update({"two":0})
				if (bets.get("anycraps") != 0):
					bankroll = (bankroll + (bets.get("anycraps") * 7)) 			
					winflag = 1
					bets.update({"two":0})
				if (bets.get("C&E") != 0):
					bankroll = (bankroll + math.floor(bets.get("C&E") * 7)) 			
					winflag = 1
					bets.update({"C&E":0})
				if (bets.get("world") != 0):
					bankroll = (bankroll + math.floor((bets.get("world") * 26)/5)) 			
					winflag = 1
					bets.update({"world":0})
			if result == 3:
				print("Pay the Three!")
				if (bets.get("three") != 0):
					bankroll = (bankroll + (bets.get("three") * 15)) 			
					winflag = 1
					bets.update({"three":0})
				if (bets.get("anycraps") != 0):
					bankroll = (bankroll + (bets.get("anycraps") * 7)) 			
					winflag = 1
					bets.update({"three":0})
				if (bets.get("C&E") != 0):
					bankroll = (bankroll + math.floor(bets.get("C&E") * 7)) 			
					winflag = 1
					bets.update({"C&E":0})
				if (bets.get("world") != 0):
					bankroll = (bankroll + math.floor((bets.get("world") * 11)/5)) 			
					winflag = 1
					bets.update({"world":0})
			if result == 11:
				print("YO-Eleven!!!")
				if (bets.get("eleven") != 0):
					bankroll = (bankroll + (bets.get("eleven") * 15)) 			
					winflag = 1
					bets.update({"eleven":0})
				if (bets.get("C&E") != 0):
					bankroll = (bankroll + math.floor(bets.get("C&E") * 15)) 			
					winflag = 1
					bets.update({"C&E":0})
				if (bets.get("world") != 0):
					bankroll = (bankroll + math.floor((bets.get("world") * 11)/5)) 			
					winflag = 1
					bets.update({"world":0})
			if result == 12:
				print("Box Cars!")
				if (bets.get("twelve") != 0):
					bankroll = (bankroll + (bets.get("twelve") * 30)) 			
					winflag = 1
					bets.update({"twelve":0})
				if (bets.get("anycraps") != 0):
					bankroll = (bankroll + (bets.get("anycraps") * 7)) 			
					winflag = 1
					bets.update({"twelve":0})
				if (bets.get("C&E") != 0):
					bankroll = (bankroll + math.floor(bets.get("C&E") * 7)) 			
					winflag = 1
					bets.update({"C&E":0})
				if (bets.get("world") != 0):
					bankroll = (bankroll + math.floor((bets.get("world") * 26)/5)) 			
					winflag = 1
					bets.update({"world":0})
			if result == 7:
				if (bets.get("anyseven") != 0):
					bankroll = (bankroll + (bets.get("anyseven") * 4)) 			
					print("Big Red!!!")
					winflag = 1
					bets.update({"anyseven":0})
					bets.update({"anycraps":0})
					bets.update({"two":0})
					bets.update({"three":0})
					bets.update({"eleven":0})
					bets.update({"twelve":0})
				if (bets.get("world") != 0):
					#Push
					bankroll = (bankroll + (bets.get("world"))) 			
					winflag = 1
					bets.update({"world":0})
			#Resetting Propositions bets (minus Hardways) afer payouts or if loss
			bets.update({"two":0})
			bets.update({"three":0})
			bets.update({"eleven":0})
			bets.update({"twelve":0})
			bets.update({"anyseven":0})
			bets.update({"anycraps":0})
			#Clearing Miscellaneous bets
			bets.update({"C&E":0})	
			bets.update({"world":0})	

			
			#Clearing hardway bets if number rolls soft (not same number)
			if (bets.get("hardway4") != 0) and (result == 4) and (hardway == 0):
				bets.update({"hardway4":0})
			if (bets.get("hardway6") != 0) and (result == 6) and (hardway == 0):
				bets.update({"hardway6":0})
			if (bets.get("hardway8") != 0) and (result == 8) and (hardway == 0):
				bets.update({"hardway8":0})
			if (bets.get("hardway10") != 0) and (result == 10) and (hardway == 0):
				bets.update({"hardway10":0})


			#Lay bets lose if their number rolls
			#before a 7
			if (bets.get("lay4") != 0) and (result == 4):
				bets.update({"lay4":0})
			if (bets.get("lay5") != 0) and (result == 5):
				bets.update({"lay5":0})
			if (bets.get("lay6") != 0) and (result == 6):
				bets.update({"lay6":0})
			if (bets.get("lay8") != 0) and (result == 8):
				bets.update({"lay8":0})
			if (bets.get("lay9") != 0) and (result == 9):
				bets.update({"lay9":0})
			if (bets.get("lay10") != 0) and (result == 10):
				bets.update({"lay10":0})

			if winflag == 1:
				if soundfx == 1:
					if operating == "Linux":
						os.system("aplay -q " + winsound + " > /dev/null 2>&1")
					elif operating == "Windows":
						os.system("powershell -c (New-Object Media.SoundPlayer 'data\\sounds\\chips.wav').PlaySync();")
					elif operating == "Darwin":
						os.system("afplay " + winsound + " > /dev/null 2>&1")
					else:
						print("ERROR: Unknown Operating System!")
				winflag = 0	
			
			save(users_dict)

			#############################################
			#
			# Payoff for shooter hitting the point
			#
			#############################################
			if result == point:
				print("Shooter hits the point!!!")
				print("Front Line Winner!!!")
				if soundfx == 1:
					if operating == "Linux":
						os.system("aplay -q " + applausesound + " > /dev/null 2>&1")
					elif operating == "Windows":
						os.system("powershell -c (New-Object Media.SoundPlayer 'data\\sounds\\claps.wav').PlaySync();")
					elif operating == "Darwin":
						os.system("afplay " + applausesound + " > /dev/null 2>&1")
					else:
						print("ERROR: Unknown Operating System!")
				#print("bet location is : ", bet_location)
				if bet_location == "1":
					bankroll = (bankroll + (bet_amount * 2))
					winflag = 1
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
				#Handling Existing Come Bet
				if bets.get("come") != 0:
					#Come bet wins on 7 or 11
					if result == 7 or result == 11:
						print("Come Bet Winner!!!")
						winflag = 1
						comebet = bets.get("come")
						bets.update({"come":0})
						bankroll = bankroll + (comebet * 2)		
						comebet = 0
					if result == 2 or result == 3 or result == 12:
						bets.update({"come":0})
					if result == 4:
						bets.update({"come4":(bets.get("come"))})
						bets.update({"come":0})
					if result == 5:
						bets.update({"come5":(bets.get("come"))})
						bets.update({"come":0})
					if result == 6:
						bets.update({"come6":(bets.get("come"))})
						bets.update({"come":0})
					if result == 8:
						bets.update({"come8":(bets.get("come"))})
						bets.update({"come":0})
					if result == 9:
						bets.update({"come9":(bets.get("come"))})
						bets.update({"come":0})
					if result == 10:
						bets.update({"come10":(bets.get("come"))})
						bets.update({"come":0})

				#Handling Exisitng Don't Come Bet
				if bets.get("dc") != 0:
					#Don't Come bet wins on 2 or 3
					if result == 2 or result == 3:
						print("Pay the Don't Come!!!")
						winflag = 1
						comebet = bets.get("dc")
						bets.update({"dc":0})
						bankroll = bankroll + (comebet * 2)		
						comebet = 0
					#Loss on 7 or 11
					elif result == 7 or result == 11:
						bets.update({"dc":0})
					#Push if roll is 12
					elif result == 12:
						comebet = bets.get("dc")
						bets.update({"dc":0})
						bankroll = bankroll + comebet
						comebet = 0
					else:
						if result == 4:
							bets.update({"dc4":(bets.get("dc"))})
							bets.update({"dc":0})
							newdcbet = 1
						if result == 5:
							bets.update({"dc5":(bets.get("dc"))})
							bets.update({"dc":0})
							newdcbet = 1
						if result == 6:
							bets.update({"dc6":(bets.get("dc"))})
							bets.update({"dc":0})
							newdcbet = 1
						if result == 8:
							bets.update({"dc8":(bets.get("dc"))})
							bets.update({"dc":0})
							newdcbet = 1
						if result == 9:
							bets.update({"dc9":(bets.get("dc"))})
							bets.update({"dc":0})
							newdcbet = 1
						if result == 10:
							bets.update({"dc10":(bets.get("dc"))})
							bets.update({"dc":0})
							newdcbet = 1

				#Losses for Don't Come on hitting 	
				#don't come point
				if newdcbet == 0:
					if bets.get("dc4") != 0 and result == 4:
						bets.update({"dc4":0})
					if bets.get("dc5") != 0 and result == 5:
						bets.update({"dc5":0})
					if bets.get("dc6") != 0 and result == 6:
						bets.update({"dc6":0})
					if bets.get("dc8") != 0 and result == 8:
						bets.update({"dc8":0})
					if bets.get("dc9") != 0 and result == 9:
						bets.update({"dc9":0})
					if bets.get("dc10") != 0 and result == 10:
						bets.update({"dc10":0})
				newdcbet = 0
				if newdcbet == 0:
					if bets.get("freeodds_dc4") != 0 and result == 4:
						bets.update({"freeodds_dc4":0})
					if bets.get("freeodds_dc5") != 0 and result == 5:
						bets.update({"freeodds_dc5":0})
					if bets.get("freeodds_dc6") != 0 and result == 6:
						bets.update({"freeodds_dc6":0})
					if bets.get("freeodds_dc8") != 0 and result == 8:
						bets.update({"freeodds_dc8":0})
					if bets.get("freeodds_dc9") != 0 and result == 9:
						bets.update({"freeodds_dc9":0})
					if bets.get("freeodds_dc10") != 0 and result == 10:
						bets.update({"freeodds_dc10":0})
				newdcbet = 0
				
				if winflag == 1:
					if soundfx == 1:
						if operating == "Linux":
							os.system("aplay -q " + winsound + " > /dev/null 2>&1")
						elif operating == "Windows":
							os.system("powershell -c (New-Object Media.SoundPlayer 'data\\sounds\\chips.wav').PlaySync();")
						elif operating == "Darwin":
							os.system("afplay " + winsound + " > /dev/null 2>&1")
						else:
							print("ERROR: Unknown Operating System!")
					winflag = 0	

				save(users_dict)

				iscomeout = True
				point = 0
				input()
				if operating == "Linux":
					os.system("clear")
				elif operating == "Windows":
					os.system("cls")
				elif operating == "Darwin":
					os.system("clear")
				else:
					print("ERROR: Unknown Operating System!")
				break
			###########################################
			#
			# Payoff for if shooter Sevens Out
			#
			###########################################
			elif result == 7:
				print("Big Red!!! Shooter sevens out!")
				print("Pay the Don't Pass.")
				if soundfx == 1:
					if operating == "Linux":
						os.system("aplay -q " + awwsound + " > /dev/null 2>&1")
					elif operating == "Windows":
						os.system("powershell -c (New-Object Media.SoundPlayer 'data\\sounds\\aww.wav').PlaySync();")
					elif operating == "Darwin":
						os.system("afplay " + awwsound + " > /dev/null 2>&1")
					else:
						print("ERROR: Unknown Operating System!")
				#print("bet location is : ", bet_location)
				if bet_location == "2":
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

				#Payouts for Don't Come on Seven Out	
				#Losses for come points
				if bets.get("dc4") != 0:
					winflag = 1
					bankroll = bankroll + (bets.get("dc4") * 2)
					bets.update({"dc4":0})
					bets.update({"come4":0})
				if bets.get("dc5") != 0:
					winflag = 1
					bankroll = bankroll + (bets.get("dc5") * 2)
					bets.update({"dc5":0})
					bets.update({"come5":0})
				if bets.get("dc6") != 0:
					winflag = 1
					bankroll = bankroll + (bets.get("dc6") * 2)
					bets.update({"dc6":0})
					bets.update({"come6":0})
				if bets.get("dc8") != 0:
					winflag = 1
					bankroll = bankroll + (bets.get("dc8") * 2)
					bets.update({"dc8":0})
					bets.update({"come8":0})
				if bets.get("dc9") != 0:
					winflag = 1
					bankroll = bankroll + (bets.get("dc9") * 2)
					bets.update({"dc9":0})
					bets.update({"come9":0})
				if bets.get("dc10") != 0:
					winflag = 1
					bankroll = bankroll + (bets.get("dc10") * 2)
					bets.update({"dc10":0})
					bets.update({"come10":0})
				#Payouts for Don't Come Odds on Seven Out	
				#Losses for come point odds
				if bets.get("freeodds_dc4") != 0:
					winflag = 1
					bankroll = bankroll + math.floor(((bets.get("freeodds_dc4") * 1)/2) + bets.get("freeodds_dc4"))
					bets.update({"freeodds_dc4":0})
					bets.update({"freeodds_come4":0})
				if bets.get("freeodds_dc5") != 0:
					winflag = 1
					bankroll = bankroll + math.floor(((bets.get("freeodds_dc5") * 2)/3) + bets.get("freeodds_dc5"))
					bets.update({"freeodds_dc5":0})
					bets.update({"freeodds_come5":0})
				if bets.get("freeodds_dc6") != 0:
					winflag = 1
					bankroll = bankroll + math.floor(((bets.get("freeodds_dc6") * 5)/6) + bets.get("freeodds_dc6"))
					bets.update({"freeodds_dc6":0})
					bets.update({"freeodds_come6":0})
				if bets.get("freeodds_dc8") != 0:
					winflag = 1
					bankroll = bankroll + math.floor(((bets.get("freeodds_dc8") * 5)/6) + bets.get("freeodds_dc8"))
					bets.update({"freeodds_dc8":0})
					bets.update({"freeodds_come8":0})
				if bets.get("freeodds_dc9") != 0:
					winflag = 1
					bankroll = bankroll + math.floor(((bets.get("freeodds_dc9") * 2)/3) + bets.get("freeodds_dc9"))
					bets.update({"freeodds_dc9":0})
					bets.update({"freeodds_come9":0})
				if bets.get("freeodds_dc10") != 0:
					winflag = 1
					bankroll = bankroll + math.floor(((bets.get("freeodds_dc10") * 1)/2) + bets.get("freeodds_dc10"))
					bets.update({"freeodds_dc10":0})
					bets.update({"freeodds_come10":0})

				#Clearing out come points on Seven Out
				bets.update({"come4":0})
				bets.update({"come5":0})
				bets.update({"come6":0})
				bets.update({"come8":0})
				bets.update({"come9":0})
				bets.update({"come10":0})
				#Clearing out come points odds on Seven Out
				bets.update({"freeodds_come4":0})
				bets.update({"freeodds_come5":0})
				bets.update({"freeodds_come6":0})
				bets.update({"freeodds_come8":0})
				bets.update({"freeodds_come9":0})
				bets.update({"freeodds_come10":0})

				#Clearing place bets on Seven Out
				bets.update({"place4":0})
				bets.update({"place5":0})
				bets.update({"place6":0})
				bets.update({"place8":0})
				bets.update({"place9":0})
				bets.update({"place10":0})

				#Clearing Big 6 and Big 8 on Seven Out
				bets.update({"big6":0})
				bets.update({"big8":0})

				#Clearing hardway bets on Seven Out
				bets.update({"hardway4":0})
				bets.update({"hardway6":0})
				bets.update({"hardway8":0})
				bets.update({"hardway10":0})

				if winflag == 1:
					if soundfx == 1:
						if operating == "Linux":
							os.system("aplay -q " + winsound + " > /dev/null 2>&1")
						elif operating == "Windows":
							os.system("powershell -c (New-Object Media.SoundPlayer 'data\\sounds\\chips.wav').PlaySync();")
						elif operating == "Darwin":
							os.system("afplay " + winsound + " > /dev/null 2>&1")
						else:
							print("ERROR: Unknown Operating System!")
					winflag = 0	
				
				save(users_dict)

				iscomeout = True
				point = 0
				input()
				if operating == "Linux":
					os.system("clear")
				elif operating == "Windows":
					os.system("cls")
				elif operating == "Darwin":
					os.system("clear")
				else:
					print("ERROR: Unknown Operating System!")
				break
		break

##############################################
#
#
# End of File
#
#
##############################################
