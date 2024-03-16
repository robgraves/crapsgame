#!/usr/bin/env python3

############################
#
# Testing dice distribution
# for fun.
#
############################

import random
#import os
import math
import datetime
#import time

diceresult = 0

print("Enter name: ")
name = input()
nameint = 0
for n in name:
	nameint = ord(n)
print("Your name is: " + name)
print("Enter bankroll: ")
bankroll = input()
print("Your bankroll is: " + str(bankroll))
dateint = math.floor(datetime.datetime.now().timestamp())
#dateint = os.system('date +%s\n')
print("Date Integer is: " + str(dateint))
print("Enter number of times to roll the dice: ")
i = input()
print("You chose " + i)
i = int(i)

seedcomposite = int(nameint) + int(bankroll) + int(dateint) + int(diceresult)
print("Seed Composite: ", str(seedcomposite))
seedcomposite = int(seedcomposite)
input()


#i=10000000
x = i

two = 0
three = 0
four= 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
eleven = 0
twelve = 0

while i > 0:
	###ORIGINAL DICE RANDOMNESS METHOD
	### Works
	#rng = random.SystemRandom()
	#die1 = rng.randint(1,6)
	#die2 = rng.randint(1,6)

	###NEW DICE RANDOMNESS METHOD
	### Always results in all rolls
	### being same number BROKEN
	
	rng = random.SystemRandom()
	rng_num = rng.randint(1,10000)

	#time.sleep(0.2)
	dateint = math.floor(datetime.datetime.now().timestamp())
	seedcomposite = int(nameint) + int(bankroll) + int(dateint) + int(diceresult) + rng_num
	seedcomposite = int(seedcomposite)
	#
	# TESTS
	#print(nameint)
	#print(bankroll)
	#print(dateint)
	#print(diceresult)
	#print(seedcomposite)
	#input()
	#
	random.seed(seedcomposite)
	die1 = random.randint(1,6)
	die2 = random.randint(1,6)
	
	diceresult = die1 + die2
	print(diceresult)
	if diceresult == 2:
		two = two + 1
	elif diceresult == 3:
		three = three + 1
	elif diceresult == 4:
		four = four + 1
	elif diceresult == 5:
		five = five + 1
	elif diceresult == 6:
		six = six + 1
	elif diceresult == 7:
		seven = seven + 1
	elif diceresult == 8:
		eight = eight + 1
	elif diceresult == 9:
		nine = nine + 1
	elif diceresult == 10:
		ten = ten + 1
	elif diceresult == 11:
		eleven = eleven + 1
	elif diceresult == 12:
		twelve = twelve + 1
	else:
		print("ERROR: Something broke!!!")
	i = i - 1

print("Distribution of dice rolls over " + str(x) + " rolls: ")
print("Two : " + str(two))
print("Three : " + str(three))
print("Four : " + str(four))
print("Five : " + str(five))
print("Six : " + str(six))
print("Seven : " + str(seven))
print("Eight : " + str(eight))
print("Nine : " + str(nine))
print("Ten : " + str(ten))
print("Eleven : " + str(eleven))
print("Twelve : " + str(twelve))
