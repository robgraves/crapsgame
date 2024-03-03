#!/usr/bin/env python3

############################
#
# Testing dice distribution
# for fun.
#
############################

import random

i=10000000
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
	rng = random.SystemRandom()
	die1 = rng.randint(1,6)
	die2 = rng.randint(1,6)
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
