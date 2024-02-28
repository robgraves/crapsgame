#!/usr/bin/env python3
#
# Matthew Page 01/03/2023
#
# graphics.py  - 	A library I made to move
#					all the ASCII art for the
# 					game into a seperate file.
#
##############################################


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


##############################################
#
#
# Functions definitions for ASCII art
#
#
##############################################



def intro():
	'''Function that displays Intro screen'''
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
	print("         robgraves  2024         ")
	print("       me@matthewjpage.com       ")
	print("                                 ")


def color_intro():
	'''Function that displays Color Intro screen'''
	print(f"{ansifmt.HIYELLOW}Welcome to Terminal Craps Game!!!{ansifmt.RESET}")
	print(f"{ansifmt.HIRED}       .-------.    ______       {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}      /{ansifmt.RESET}" + f"{ansifmt.HIWHITE}   o{ansifmt.RESET}" + f"{ansifmt.HIRED}   /|   /\     \      {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}     /_______/{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}|  /{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o {ansifmt.RESET}" + f"{ansifmt.HIRED}\  {ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}  \     {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}     | {ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}     | | /   {ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}\_____\    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}     |   {ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}   |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}/ \{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}   /{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" f"{ansifmt.HIRED}    /    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}     |     {ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED} |/   \ {ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}/  {ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}  /     {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}     '-------'     \/____{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}/      {ansifmt.RESET}")
	print("                                 ")
	print(f"{ansifmt.HIBLUE}   Created by Matthew J. Page    {ansifmt.RESET}")
	print(f"{ansifmt.HIBLUE}         robgraves  2024         {ansifmt.RESET}")
	print(f"{ansifmt.HIBLUE}       me@matthewjpage.com       {ansifmt.RESET}")
	print("                                 ")


def crapstable():
	'''Function that draws the craps table in ASCII art, come-out roll'''
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
	print("|e |       don't pass  bar 12| |eleven | twelve|   ")
	print("|t  \_________PASS_LINE______| +===============+   ")
	print("|s                           | |  any    craps |   ")
	print(" \________No Call Bets_______| |    7 to 1     |   ")
	print("                               +---------------+   ")


def crapstable4():
	'''Function that draws the craps table in ASCII art, point is 4'''
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
	print("|e |       don't pass  bar 12| |eleven | twelve|   ")
	print("|t  \_________PASS_LINE______| +===============+   ")
	print("|s                           | |  any    craps |   ")
	print(" \________No Call Bets_______| |    7 to 1     |   ")
	print("                               +---------------+   ")


def crapstable5():
	'''Function that draws the craps table in ASCII art, point is 5'''
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
	print("|e |       don't pass  bar 12| |eleven | twelve|   ")
	print("|t  \_________PASS_LINE______| +===============+   ")
	print("|s                           | |  any    craps |   ")
	print(" \________No Call Bets_______| |    7 to 1     |   ")
	print("                               +---------------+   ")


def crapstable6():
	'''Function that draws the craps table in ASCII art, point is 6'''
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
	print("|e |       don't pass  bar 12| |eleven | twelve|   ")
	print("|t  \_________PASS_LINE______| +===============+   ")
	print("|s                           | |  any    craps |   ")
	print(" \________No Call Bets_______| |    7 to 1     |   ")
	print("                               +---------------+   ")


def crapstable8():
	'''Function that draws the craps table in ASCII art, point is 8'''
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
	print("|e |       don't pass  bar 12| |eleven | twelve|   ")
	print("|t  \_________PASS_LINE______| +===============+   ")
	print("|s                           | |  any    craps |   ")
	print(" \________No Call Bets_______| |    7 to 1     |   ")
	print("                               +---------------+   ")


def crapstable9():
	'''Function that draws the craps table in ASCII art, point is 9'''
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
	print("|e |       don't pass  bar 12| |eleven | twelve|   ")
	print("|t  \_________PASS_LINE______| +===============+   ")
	print("|s                           | |  any    craps |   ")
	print(" \________No Call Bets_______| |    7 to 1     |   ")
	print("                               +---------------+   ")


def crapstable10():
	'''Function that draws the craps table in ASCII art, point is 10'''
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
	print("|e |       don't pass  bar 12| |eleven | twelve|   ")
	print("|t  \_________PASS_LINE______| +===============+   ")
	print("|s                           | |  any    craps |   ")
	print(" \________No Call Bets_______| |    7 to 1     |   ")
	print("                               +---------------+   ")


def color_crapstable():
	'''Function that draws the craps table in ASCII art, come-out roll'''
	print(f"{ansifmt.GREEN} __ ___  ____________________  {ansifmt.RESET}" + f"{ansifmt.HIBLACK}(OFF)               {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}N{ansifmt.RESET}" + f"{ansifmt.GREEN} |  {ansifmt.RESET}" + f"{ansifmt.HIBLACK}d{ansifmt.RESET}" + f"{ansifmt.GREEN}||{ansifmt.RESET}" + f"{ansifmt.HIBLACK}DC{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 4{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 5{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 6{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 8{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 9{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}10{ansifmt.RESET}" + f"{ansifmt.GREEN}| +---------------+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}o{ansifmt.RESET}" + f"{ansifmt.GREEN} |{ansifmt.RESET}" + f"{ansifmt.LGREEN}P {ansifmt.RESET}" + f"{ansifmt.HIBLACK}o{ansifmt.RESET}" + f"{ansifmt.GREEN}||__|__|__|__|__|__|__| |{ansifmt.RESET}" + f"{ansifmt.LRED}any seven   {ansifmt.RESET}" + f"{ansifmt.HIWHITE}4-1{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|  |{ansifmt.RESET}" + f"{ansifmt.LGREEN}A {ansifmt.RESET}" + f"{ansifmt.HIBLACK}n{ansifmt.RESET}" + f"{ansifmt.GREEN}| ____________________  +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}C {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}S {ansifmt.RESET}" + f"{ansifmt.HIBLACK}t{ansifmt.RESET}" + f"{ansifmt.GREEN}||     {ansifmt.RESET}" + f"{ansifmt.LRED}C O M E        {ansifmt.RESET}" + f"{ansifmt.GREEN}| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 4 {ansifmt.RESET}" + f"{ansifmt.GREEN}| {ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 6{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}a {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}S {ansifmt.RESET}" + f"{ansifmt.HIBLACK}p{ansifmt.RESET}" + f"{ansifmt.GREEN}||____________________| |-------+-------|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}l {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}L {ansifmt.RESET}" + f"{ansifmt.HIBLACK}a{ansifmt.RESET}" + f"{ansifmt.GREEN}| ____________________  |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 10{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIWHITE} hard 8{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}l {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}I {ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}||{ansifmt.RESET}" + f"{ansifmt.YELLOW}2  3 4  9  10 11  12{ansifmt.RESET}" + f"{ansifmt.GREEN}| +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|  |{ansifmt.RESET}" + f"{ansifmt.LGREEN}N {ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}||_______{ansifmt.RESET}" + f"{ansifmt.YELLOW}FIELD{ansifmt.RESET}" + f"{ansifmt.GREEN}________| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}two    {ansifmt.RESET}" + f"{ansifmt.GREEN}|  {ansifmt.RESET}" + f"{ansifmt.HIWHITE}three{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}B {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}E  {ansifmt.RESET}" + f"{ansifmt.GREEN}|_____________________  |-----{ansifmt.RESET}" + f"{ansifmt.LRED}HORN{ansifmt.RESET}" + f"{ansifmt.GREEN}------|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}e {ansifmt.RESET}" + f"{ansifmt.GREEN}|       {ansifmt.RESET}" + f"{ansifmt.HIBLACK}don't pass  bar {ansifmt.RESET}" + f"{ansifmt.LRED}12{ansifmt.RESET}" + f"{ansifmt.GREEN}| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}eleven {ansifmt.RESET}" + f"{ansifmt.GREEN}| {ansifmt.RESET}" + f"{ansifmt.HIWHITE}twelve{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}t  {ansifmt.RESET}" + f"{ansifmt.GREEN}\_________{ansifmt.RESET}" + f"{ansifmt.LGREEN}PASS_LINE{ansifmt.RESET}" + f"{ansifmt.GREEN}______| +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}                           | |  {ansifmt.RESET}" + f"{ansifmt.LRED}any    craps {ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN} \________{ansifmt.RESET}" + f"{ansifmt.HIBLACK}No Call Bets{ansifmt.RESET}" + f"{ansifmt.GREEN}_______| |    {ansifmt.RESET}" + f"{ansifmt.HIWHITE}7 to 1     {ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}                               +---------------+   {ansifmt.RESET}")


def color_crapstable4():
	'''Function that draws the craps table in ASCII art, come-out roll'''
	print(f"{ansifmt.GREEN} __ ___  ____________________  {ansifmt.RESET}" + f"{ansifmt.HIBLACK}(OFF)               {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}N{ansifmt.RESET}" + f"{ansifmt.GREEN} |  {ansifmt.RESET}" + f"{ansifmt.HIBLACK}d{ansifmt.RESET}" + f"{ansifmt.GREEN}||{ansifmt.RESET}" + f"{ansifmt.HIBLACK}DC{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 4{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 5{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 6{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 8{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 9{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}10{ansifmt.RESET}" + f"{ansifmt.GREEN}| +---------------+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}o{ansifmt.RESET}" + f"{ansifmt.GREEN} |{ansifmt.RESET}" + f"{ansifmt.LGREEN}P {ansifmt.RESET}" + f"{ansifmt.HIBLACK}o{ansifmt.RESET}" + f"{ansifmt.GREEN}||__|{ansifmt.RESET}" + f"{ansifmt.HIWHITE}ON{ansifmt.RESET}" + f"{ansifmt.GREEN}|__|__|__|__|__| |{ansifmt.RESET}" + f"{ansifmt.LRED}any seven   {ansifmt.RESET}" + f"{ansifmt.HIWHITE}4-1{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|  |{ansifmt.RESET}" + f"{ansifmt.LGREEN}A {ansifmt.RESET}" + f"{ansifmt.HIBLACK}n{ansifmt.RESET}" + f"{ansifmt.GREEN}| ____________________  +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}C {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}S {ansifmt.RESET}" + f"{ansifmt.HIBLACK}t{ansifmt.RESET}" + f"{ansifmt.GREEN}||     {ansifmt.RESET}" + f"{ansifmt.LRED}C O M E        {ansifmt.RESET}" + f"{ansifmt.GREEN}| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 4 {ansifmt.RESET}" + f"{ansifmt.GREEN}| {ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 6{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}a {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}S {ansifmt.RESET}" + f"{ansifmt.HIBLACK}p{ansifmt.RESET}" + f"{ansifmt.GREEN}||____________________| |-------+-------|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}l {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}L {ansifmt.RESET}" + f"{ansifmt.HIBLACK}a{ansifmt.RESET}" + f"{ansifmt.GREEN}| ____________________  |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 10{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIWHITE} hard 8{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}l {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}I {ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}||{ansifmt.RESET}" + f"{ansifmt.YELLOW}2  3 4  9  10 11  12{ansifmt.RESET}" + f"{ansifmt.GREEN}| +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|  |{ansifmt.RESET}" + f"{ansifmt.LGREEN}N {ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}||_______{ansifmt.RESET}" + f"{ansifmt.YELLOW}FIELD{ansifmt.RESET}" + f"{ansifmt.GREEN}________| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}two    {ansifmt.RESET}" + f"{ansifmt.GREEN}|  {ansifmt.RESET}" + f"{ansifmt.HIWHITE}three{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}B {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}E  {ansifmt.RESET}" + f"{ansifmt.GREEN}|_____________________  |-----{ansifmt.RESET}" + f"{ansifmt.LRED}HORN{ansifmt.RESET}" + f"{ansifmt.GREEN}------|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}e {ansifmt.RESET}" + f"{ansifmt.GREEN}|       {ansifmt.RESET}" + f"{ansifmt.HIBLACK}don't pass  bar {ansifmt.RESET}" + f"{ansifmt.LRED}12{ansifmt.RESET}" + f"{ansifmt.GREEN}| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}eleven {ansifmt.RESET}" + f"{ansifmt.GREEN}| {ansifmt.RESET}" + f"{ansifmt.HIWHITE}twelve{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}t  {ansifmt.RESET}" + f"{ansifmt.GREEN}\_________{ansifmt.RESET}" + f"{ansifmt.LGREEN}PASS_LINE{ansifmt.RESET}" + f"{ansifmt.GREEN}______| +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}                           | |  {ansifmt.RESET}" + f"{ansifmt.LRED}any    craps {ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN} \________{ansifmt.RESET}" + f"{ansifmt.HIBLACK}No Call Bets{ansifmt.RESET}" + f"{ansifmt.GREEN}_______| |    {ansifmt.RESET}" + f"{ansifmt.HIWHITE}7 to 1     {ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}                               +---------------+   {ansifmt.RESET}")


def color_crapstable5():
	'''Function that draws the craps table in ASCII art, come-out roll'''
	print(f"{ansifmt.GREEN} __ ___  ____________________  {ansifmt.RESET}" + f"{ansifmt.HIBLACK}(OFF)               {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}N{ansifmt.RESET}" + f"{ansifmt.GREEN} |  {ansifmt.RESET}" + f"{ansifmt.HIBLACK}d{ansifmt.RESET}" + f"{ansifmt.GREEN}||{ansifmt.RESET}" + f"{ansifmt.HIBLACK}DC{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 4{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 5{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 6{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 8{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 9{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}10{ansifmt.RESET}" + f"{ansifmt.GREEN}| +---------------+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}o{ansifmt.RESET}" + f"{ansifmt.GREEN} |{ansifmt.RESET}" + f"{ansifmt.LGREEN}P {ansifmt.RESET}" + f"{ansifmt.HIBLACK}o{ansifmt.RESET}" + f"{ansifmt.GREEN}||__|__|{ansifmt.RESET}" + f"{ansifmt.HIWHITE}ON{ansifmt.RESET}" + f"{ansifmt.GREEN}|__|__|__|__| |{ansifmt.RESET}" + f"{ansifmt.LRED}any seven   {ansifmt.RESET}" + f"{ansifmt.HIWHITE}4-1{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|  |{ansifmt.RESET}" + f"{ansifmt.LGREEN}A {ansifmt.RESET}" + f"{ansifmt.HIBLACK}n{ansifmt.RESET}" + f"{ansifmt.GREEN}| ____________________  +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}C {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}S {ansifmt.RESET}" + f"{ansifmt.HIBLACK}t{ansifmt.RESET}" + f"{ansifmt.GREEN}||     {ansifmt.RESET}" + f"{ansifmt.LRED}C O M E        {ansifmt.RESET}" + f"{ansifmt.GREEN}| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 4 {ansifmt.RESET}" + f"{ansifmt.GREEN}| {ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 6{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}a {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}S {ansifmt.RESET}" + f"{ansifmt.HIBLACK}p{ansifmt.RESET}" + f"{ansifmt.GREEN}||____________________| |-------+-------|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}l {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}L {ansifmt.RESET}" + f"{ansifmt.HIBLACK}a{ansifmt.RESET}" + f"{ansifmt.GREEN}| ____________________  |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 10{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIWHITE} hard 8{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}l {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}I {ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}||{ansifmt.RESET}" + f"{ansifmt.YELLOW}2  3 4  9  10 11  12{ansifmt.RESET}" + f"{ansifmt.GREEN}| +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|  |{ansifmt.RESET}" + f"{ansifmt.LGREEN}N {ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}||_______{ansifmt.RESET}" + f"{ansifmt.YELLOW}FIELD{ansifmt.RESET}" + f"{ansifmt.GREEN}________| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}two    {ansifmt.RESET}" + f"{ansifmt.GREEN}|  {ansifmt.RESET}" + f"{ansifmt.HIWHITE}three{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}B {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}E  {ansifmt.RESET}" + f"{ansifmt.GREEN}|_____________________  |-----{ansifmt.RESET}" + f"{ansifmt.LRED}HORN{ansifmt.RESET}" + f"{ansifmt.GREEN}------|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}e {ansifmt.RESET}" + f"{ansifmt.GREEN}|       {ansifmt.RESET}" + f"{ansifmt.HIBLACK}don't pass  bar {ansifmt.RESET}" + f"{ansifmt.LRED}12{ansifmt.RESET}" + f"{ansifmt.GREEN}| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}eleven {ansifmt.RESET}" + f"{ansifmt.GREEN}| {ansifmt.RESET}" + f"{ansifmt.HIWHITE}twelve{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}t  {ansifmt.RESET}" + f"{ansifmt.GREEN}\_________{ansifmt.RESET}" + f"{ansifmt.LGREEN}PASS_LINE{ansifmt.RESET}" + f"{ansifmt.GREEN}______| +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}                           | |  {ansifmt.RESET}" + f"{ansifmt.LRED}any    craps {ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN} \________{ansifmt.RESET}" + f"{ansifmt.HIBLACK}No Call Bets{ansifmt.RESET}" + f"{ansifmt.GREEN}_______| |    {ansifmt.RESET}" + f"{ansifmt.HIWHITE}7 to 1     {ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}                               +---------------+   {ansifmt.RESET}")


def color_crapstable6():
	'''Function that draws the craps table in ASCII art, come-out roll'''
	print(f"{ansifmt.GREEN} __ ___  ____________________  {ansifmt.RESET}" + f"{ansifmt.HIBLACK}(OFF)               {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}N{ansifmt.RESET}" + f"{ansifmt.GREEN} |  {ansifmt.RESET}" + f"{ansifmt.HIBLACK}d{ansifmt.RESET}" + f"{ansifmt.GREEN}||{ansifmt.RESET}" + f"{ansifmt.HIBLACK}DC{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 4{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 5{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 6{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 8{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 9{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}10{ansifmt.RESET}" + f"{ansifmt.GREEN}| +---------------+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}o{ansifmt.RESET}" + f"{ansifmt.GREEN} |{ansifmt.RESET}" + f"{ansifmt.LGREEN}P {ansifmt.RESET}" + f"{ansifmt.HIBLACK}o{ansifmt.RESET}" + f"{ansifmt.GREEN}||__|__|__|{ansifmt.RESET}" + f"{ansifmt.HIWHITE}ON{ansifmt.RESET}" + f"{ansifmt.GREEN}|__|__|__| |{ansifmt.RESET}" + f"{ansifmt.LRED}any seven   {ansifmt.RESET}" + f"{ansifmt.HIWHITE}4-1{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|  |{ansifmt.RESET}" + f"{ansifmt.LGREEN}A {ansifmt.RESET}" + f"{ansifmt.HIBLACK}n{ansifmt.RESET}" + f"{ansifmt.GREEN}| ____________________  +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}C {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}S {ansifmt.RESET}" + f"{ansifmt.HIBLACK}t{ansifmt.RESET}" + f"{ansifmt.GREEN}||     {ansifmt.RESET}" + f"{ansifmt.LRED}C O M E        {ansifmt.RESET}" + f"{ansifmt.GREEN}| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 4 {ansifmt.RESET}" + f"{ansifmt.GREEN}| {ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 6{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}a {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}S {ansifmt.RESET}" + f"{ansifmt.HIBLACK}p{ansifmt.RESET}" + f"{ansifmt.GREEN}||____________________| |-------+-------|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}l {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}L {ansifmt.RESET}" + f"{ansifmt.HIBLACK}a{ansifmt.RESET}" + f"{ansifmt.GREEN}| ____________________  |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 10{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIWHITE} hard 8{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}l {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}I {ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}||{ansifmt.RESET}" + f"{ansifmt.YELLOW}2  3 4  9  10 11  12{ansifmt.RESET}" + f"{ansifmt.GREEN}| +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|  |{ansifmt.RESET}" + f"{ansifmt.LGREEN}N {ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}||_______{ansifmt.RESET}" + f"{ansifmt.YELLOW}FIELD{ansifmt.RESET}" + f"{ansifmt.GREEN}________| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}two    {ansifmt.RESET}" + f"{ansifmt.GREEN}|  {ansifmt.RESET}" + f"{ansifmt.HIWHITE}three{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}B {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}E  {ansifmt.RESET}" + f"{ansifmt.GREEN}|_____________________  |-----{ansifmt.RESET}" + f"{ansifmt.LRED}HORN{ansifmt.RESET}" + f"{ansifmt.GREEN}------|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}e {ansifmt.RESET}" + f"{ansifmt.GREEN}|       {ansifmt.RESET}" + f"{ansifmt.HIBLACK}don't pass  bar {ansifmt.RESET}" + f"{ansifmt.LRED}12{ansifmt.RESET}" + f"{ansifmt.GREEN}| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}eleven {ansifmt.RESET}" + f"{ansifmt.GREEN}| {ansifmt.RESET}" + f"{ansifmt.HIWHITE}twelve{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}t  {ansifmt.RESET}" + f"{ansifmt.GREEN}\_________{ansifmt.RESET}" + f"{ansifmt.LGREEN}PASS_LINE{ansifmt.RESET}" + f"{ansifmt.GREEN}______| +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}                           | |  {ansifmt.RESET}" + f"{ansifmt.LRED}any    craps {ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN} \________{ansifmt.RESET}" + f"{ansifmt.HIBLACK}No Call Bets{ansifmt.RESET}" + f"{ansifmt.GREEN}_______| |    {ansifmt.RESET}" + f"{ansifmt.HIWHITE}7 to 1     {ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}                               +---------------+   {ansifmt.RESET}")


def color_crapstable8():
	'''Function that draws the craps table in ASCII art, come-out roll'''
	print(f"{ansifmt.GREEN} __ ___  ____________________  {ansifmt.RESET}" + f"{ansifmt.HIBLACK}(OFF)               {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}N{ansifmt.RESET}" + f"{ansifmt.GREEN} |  {ansifmt.RESET}" + f"{ansifmt.HIBLACK}d{ansifmt.RESET}" + f"{ansifmt.GREEN}||{ansifmt.RESET}" + f"{ansifmt.HIBLACK}DC{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 4{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 5{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 6{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 8{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 9{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}10{ansifmt.RESET}" + f"{ansifmt.GREEN}| +---------------+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}o{ansifmt.RESET}" + f"{ansifmt.GREEN} |{ansifmt.RESET}" + f"{ansifmt.LGREEN}P {ansifmt.RESET}" + f"{ansifmt.HIBLACK}o{ansifmt.RESET}" + f"{ansifmt.GREEN}||__|__|__|__|{ansifmt.RESET}" + f"{ansifmt.HIWHITE}ON{ansifmt.RESET}" + f"{ansifmt.GREEN}|__|__| |{ansifmt.RESET}" + f"{ansifmt.LRED}any seven   {ansifmt.RESET}" + f"{ansifmt.HIWHITE}4-1{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|  |{ansifmt.RESET}" + f"{ansifmt.LGREEN}A {ansifmt.RESET}" + f"{ansifmt.HIBLACK}n{ansifmt.RESET}" + f"{ansifmt.GREEN}| ____________________  +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}C {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}S {ansifmt.RESET}" + f"{ansifmt.HIBLACK}t{ansifmt.RESET}" + f"{ansifmt.GREEN}||     {ansifmt.RESET}" + f"{ansifmt.LRED}C O M E        {ansifmt.RESET}" + f"{ansifmt.GREEN}| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 4 {ansifmt.RESET}" + f"{ansifmt.GREEN}| {ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 6{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}a {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}S {ansifmt.RESET}" + f"{ansifmt.HIBLACK}p{ansifmt.RESET}" + f"{ansifmt.GREEN}||____________________| |-------+-------|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}l {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}L {ansifmt.RESET}" + f"{ansifmt.HIBLACK}a{ansifmt.RESET}" + f"{ansifmt.GREEN}| ____________________  |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 10{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIWHITE} hard 8{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}l {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}I {ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}||{ansifmt.RESET}" + f"{ansifmt.YELLOW}2  3 4  9  10 11  12{ansifmt.RESET}" + f"{ansifmt.GREEN}| +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|  |{ansifmt.RESET}" + f"{ansifmt.LGREEN}N {ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}||_______{ansifmt.RESET}" + f"{ansifmt.YELLOW}FIELD{ansifmt.RESET}" + f"{ansifmt.GREEN}________| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}two    {ansifmt.RESET}" + f"{ansifmt.GREEN}|  {ansifmt.RESET}" + f"{ansifmt.HIWHITE}three{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}B {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}E  {ansifmt.RESET}" + f"{ansifmt.GREEN}|_____________________  |-----{ansifmt.RESET}" + f"{ansifmt.LRED}HORN{ansifmt.RESET}" + f"{ansifmt.GREEN}------|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}e {ansifmt.RESET}" + f"{ansifmt.GREEN}|       {ansifmt.RESET}" + f"{ansifmt.HIBLACK}don't pass  bar {ansifmt.RESET}" + f"{ansifmt.LRED}12{ansifmt.RESET}" + f"{ansifmt.GREEN}| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}eleven {ansifmt.RESET}" + f"{ansifmt.GREEN}| {ansifmt.RESET}" + f"{ansifmt.HIWHITE}twelve{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}t  {ansifmt.RESET}" + f"{ansifmt.GREEN}\_________{ansifmt.RESET}" + f"{ansifmt.LGREEN}PASS_LINE{ansifmt.RESET}" + f"{ansifmt.GREEN}______| +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}                           | |  {ansifmt.RESET}" + f"{ansifmt.LRED}any    craps {ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN} \________{ansifmt.RESET}" + f"{ansifmt.HIBLACK}No Call Bets{ansifmt.RESET}" + f"{ansifmt.GREEN}_______| |    {ansifmt.RESET}" + f"{ansifmt.HIWHITE}7 to 1     {ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}                               +---------------+   {ansifmt.RESET}")


def color_crapstable9():
	'''Function that draws the craps table in ASCII art, come-out roll'''
	print(f"{ansifmt.GREEN} __ ___  ____________________  {ansifmt.RESET}" + f"{ansifmt.HIBLACK}(OFF)               {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}N{ansifmt.RESET}" + f"{ansifmt.GREEN} |  {ansifmt.RESET}" + f"{ansifmt.HIBLACK}d{ansifmt.RESET}" + f"{ansifmt.GREEN}||{ansifmt.RESET}" + f"{ansifmt.HIBLACK}DC{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 4{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 5{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 6{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 8{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 9{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}10{ansifmt.RESET}" + f"{ansifmt.GREEN}| +---------------+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}o{ansifmt.RESET}" + f"{ansifmt.GREEN} |{ansifmt.RESET}" + f"{ansifmt.LGREEN}P {ansifmt.RESET}" + f"{ansifmt.HIBLACK}o{ansifmt.RESET}" + f"{ansifmt.GREEN}||__|__|__|__|__|{ansifmt.RESET}" + f"{ansifmt.HIWHITE}ON{ansifmt.RESET}" + f"{ansifmt.GREEN}|__| |{ansifmt.RESET}" + f"{ansifmt.LRED}any seven   {ansifmt.RESET}" + f"{ansifmt.HIWHITE}4-1{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|  |{ansifmt.RESET}" + f"{ansifmt.LGREEN}A {ansifmt.RESET}" + f"{ansifmt.HIBLACK}n{ansifmt.RESET}" + f"{ansifmt.GREEN}| ____________________  +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}C {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}S {ansifmt.RESET}" + f"{ansifmt.HIBLACK}t{ansifmt.RESET}" + f"{ansifmt.GREEN}||     {ansifmt.RESET}" + f"{ansifmt.LRED}C O M E        {ansifmt.RESET}" + f"{ansifmt.GREEN}| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 4 {ansifmt.RESET}" + f"{ansifmt.GREEN}| {ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 6{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}a {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}S {ansifmt.RESET}" + f"{ansifmt.HIBLACK}p{ansifmt.RESET}" + f"{ansifmt.GREEN}||____________________| |-------+-------|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}l {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}L {ansifmt.RESET}" + f"{ansifmt.HIBLACK}a{ansifmt.RESET}" + f"{ansifmt.GREEN}| ____________________  |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 10{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIWHITE} hard 8{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}l {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}I {ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}||{ansifmt.RESET}" + f"{ansifmt.YELLOW}2  3 4  9  10 11  12{ansifmt.RESET}" + f"{ansifmt.GREEN}| +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|  |{ansifmt.RESET}" + f"{ansifmt.LGREEN}N {ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}||_______{ansifmt.RESET}" + f"{ansifmt.YELLOW}FIELD{ansifmt.RESET}" + f"{ansifmt.GREEN}________| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}two    {ansifmt.RESET}" + f"{ansifmt.GREEN}|  {ansifmt.RESET}" + f"{ansifmt.HIWHITE}three{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}B {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}E  {ansifmt.RESET}" + f"{ansifmt.GREEN}|_____________________  |-----{ansifmt.RESET}" + f"{ansifmt.LRED}HORN{ansifmt.RESET}" + f"{ansifmt.GREEN}------|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}e {ansifmt.RESET}" + f"{ansifmt.GREEN}|       {ansifmt.RESET}" + f"{ansifmt.HIBLACK}don't pass  bar {ansifmt.RESET}" + f"{ansifmt.LRED}12{ansifmt.RESET}" + f"{ansifmt.GREEN}| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}eleven {ansifmt.RESET}" + f"{ansifmt.GREEN}| {ansifmt.RESET}" + f"{ansifmt.HIWHITE}twelve{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}t  {ansifmt.RESET}" + f"{ansifmt.GREEN}\_________{ansifmt.RESET}" + f"{ansifmt.LGREEN}PASS_LINE{ansifmt.RESET}" + f"{ansifmt.GREEN}______| +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}                           | |  {ansifmt.RESET}" + f"{ansifmt.LRED}any    craps {ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN} \________{ansifmt.RESET}" + f"{ansifmt.HIBLACK}No Call Bets{ansifmt.RESET}" + f"{ansifmt.GREEN}_______| |    {ansifmt.RESET}" + f"{ansifmt.HIWHITE}7 to 1     {ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}                               +---------------+   {ansifmt.RESET}")


def color_crapstable10():
	'''Function that draws the craps table in ASCII art, come-out roll'''
	print(f"{ansifmt.GREEN} __ ___  ____________________  {ansifmt.RESET}" + f"{ansifmt.HIBLACK}(OFF)               {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}N{ansifmt.RESET}" + f"{ansifmt.GREEN} |  {ansifmt.RESET}" + f"{ansifmt.HIBLACK}d{ansifmt.RESET}" + f"{ansifmt.GREEN}||{ansifmt.RESET}" + f"{ansifmt.HIBLACK}DC{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 4{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 5{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 6{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 8{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN} 9{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}10{ansifmt.RESET}" + f"{ansifmt.GREEN}| +---------------+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}o{ansifmt.RESET}" + f"{ansifmt.GREEN} |{ansifmt.RESET}" + f"{ansifmt.LGREEN}P {ansifmt.RESET}" + f"{ansifmt.HIBLACK}o{ansifmt.RESET}" + f"{ansifmt.GREEN}||__|__|__|__|__|__|{ansifmt.RESET}" + f"{ansifmt.HIWHITE}ON{ansifmt.RESET}" + f"{ansifmt.GREEN}| |{ansifmt.RESET}" + f"{ansifmt.LRED}any seven   {ansifmt.RESET}" + f"{ansifmt.HIWHITE}4-1{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|  |{ansifmt.RESET}" + f"{ansifmt.LGREEN}A {ansifmt.RESET}" + f"{ansifmt.HIBLACK}n{ansifmt.RESET}" + f"{ansifmt.GREEN}| ____________________  +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}C {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}S {ansifmt.RESET}" + f"{ansifmt.HIBLACK}t{ansifmt.RESET}" + f"{ansifmt.GREEN}||     {ansifmt.RESET}" + f"{ansifmt.LRED}C O M E        {ansifmt.RESET}" + f"{ansifmt.GREEN}| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 4 {ansifmt.RESET}" + f"{ansifmt.GREEN}| {ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 6{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}a {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}S {ansifmt.RESET}" + f"{ansifmt.HIBLACK}p{ansifmt.RESET}" + f"{ansifmt.GREEN}||____________________| |-------+-------|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}l {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}L {ansifmt.RESET}" + f"{ansifmt.HIBLACK}a{ansifmt.RESET}" + f"{ansifmt.GREEN}| ____________________  |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}hard 10{ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIWHITE} hard 8{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}l {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}I {ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}||{ansifmt.RESET}" + f"{ansifmt.YELLOW}2  3 4  9  10 11  12{ansifmt.RESET}" + f"{ansifmt.GREEN}| +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|  |{ansifmt.RESET}" + f"{ansifmt.LGREEN}N {ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}||_______{ansifmt.RESET}" + f"{ansifmt.YELLOW}FIELD{ansifmt.RESET}" + f"{ansifmt.GREEN}________| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}two    {ansifmt.RESET}" + f"{ansifmt.GREEN}|  {ansifmt.RESET}" + f"{ansifmt.HIWHITE}three{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}B {ansifmt.RESET}" + f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.LGREEN}E  {ansifmt.RESET}" + f"{ansifmt.GREEN}|_____________________  |-----{ansifmt.RESET}" + f"{ansifmt.LRED}HORN{ansifmt.RESET}" + f"{ansifmt.GREEN}------|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}e {ansifmt.RESET}" + f"{ansifmt.GREEN}|       {ansifmt.RESET}" + f"{ansifmt.HIBLACK}don't pass  bar {ansifmt.RESET}" + f"{ansifmt.LRED}12{ansifmt.RESET}" + f"{ansifmt.GREEN}| |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}eleven {ansifmt.RESET}" + f"{ansifmt.GREEN}| {ansifmt.RESET}" + f"{ansifmt.HIWHITE}twelve{ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}t  {ansifmt.RESET}" + f"{ansifmt.GREEN}\_________{ansifmt.RESET}" + f"{ansifmt.LGREEN}PASS_LINE{ansifmt.RESET}" + f"{ansifmt.GREEN}______| +===============+   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}|{ansifmt.RESET}" + f"{ansifmt.HIBLACK}s{ansifmt.RESET}" + f"{ansifmt.GREEN}                           | |  {ansifmt.RESET}" + f"{ansifmt.LRED}any    craps {ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN} \________{ansifmt.RESET}" + f"{ansifmt.HIBLACK}No Call Bets{ansifmt.RESET}" + f"{ansifmt.GREEN}_______| |    {ansifmt.RESET}" + f"{ansifmt.HIWHITE}7 to 1     {ansifmt.RESET}" + f"{ansifmt.GREEN}|   {ansifmt.RESET}")
	print(f"{ansifmt.GREEN}                               +---------------+   {ansifmt.RESET}")


def die1face1():
	'''Function to display a one on a die1 in ASCII'''
	print("     ___     ")
	print("    |   |    ")
	print("    | o |    ")
	print("    |___|    ")
	print("             ")

def die1face2():
	'''Function to display a two on a die1 in ASCII'''
	print("     ___     ")
	print("    |o  |    ")
	print("    |   |    ")
	print("    |__o|    ")
	print("             ")


def die1face3():
	'''Function to display a three on a die1 in ASCII'''
	print("     ___     ")
	print("    |o  |    ")
	print("    | o |    ")
	print("    |__o|    ")
	print("             ")


def die1face4():
	'''Function to display a four on a die1 in ASCII'''
	print("     ___     ")
	print("    |o o|    ")
	print("    |   |    ")
	print("    |o_o|    ")
	print("             ")


def die1face5():
	'''Function to display a five on a die1 in ASCII'''
	print("     ___     ")
	print("    |o o|    ")
	print("    | o |    ")
	print("    |o_o|    ")
	print("             ")


def die1face6():
	'''Function to display a six on a die1 in ASCII'''
	print("     ___     ")
	print("    |o o|    ")
	print("    |o o|    ")
	print("    |o_o|    ")
	print("             ")

 
def die1blank():
	'''Function to display a six on a die1 in ASCII'''
	print("             ")
	print("             ")
	print("             ")
	print("             ")
	print("             ")


def die2face1():
	'''Function to display a one on a die2 in ASCII'''
	print("           ___     ")
	print("          |   |    ")
	print("          | o |    ")
	print("          |___|    ")
	print("                   ")


def die2face2():
	'''Function to display a two on a die2 in ASCII'''
	print("           ___     ")
	print("          |o  |    ")
	print("          |   |    ")
	print("          |__o|    ")
	print("                   ")


def die2face3():
	'''Function to display a three on a die2 in ASCII'''
	print("           ___     ")
	print("          |o  |    ")
	print("          | o |    ")
	print("          |__o|    ")
	print("                   ")


def die2face4():
	'''Function to display a four on a die2 in ASCII'''
	print("           ___     ")
	print("          |o o|    ")
	print("          |   |    ")
	print("          |o_o|    ")
	print("                   ")


def die2face5():
	'''Function to display a five on a die2 in ASCII'''
	print("           ___     ")
	print("          |o o|    ")
	print("          | o |    ")
	print("          |o_o|    ")
	print("                   ")


def die2face6():
	'''Function to display a six on a die2 in ASCII'''
	print("           ___     ")
	print("          |o o|    ")
	print("          |o o|    ")
	print("          |o_o|    ")
	print("                   ")


def die2blank():
	'''Function to display a six on a die2 in ASCII'''
	print("                   ")
	print("                   ")
	print("                   ")
	print("                   ")
	print("                   ")


def color_die1face1():
	'''Function to display a one on a die1 in ASCII'''
	print(f"{ansifmt.HIRED}     ___     {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}    |   |    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}    | {ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED} |    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}    |___|    {ansifmt.RESET}")
	print("             ")

def color_die1face2():
	'''Function to display a two on a die1 in ASCII'''
	print(f"{ansifmt.HIRED}     ___     {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}    |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}  |    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}    |   |    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}    |__{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}|    {ansifmt.RESET}")
	print("             ")


def color_die1face3():
	'''Function to display a three on a die1 in ASCII'''
	print(f"{ansifmt.HIRED}     ___     {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}    |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}  |    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}    | {ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED} |    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}    |__{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}|    {ansifmt.RESET}")
	print("             ")


def color_die1face4():
	'''Function to display a four on a die1 in ASCII'''
	print(f"{ansifmt.HIRED}     ___     {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}    |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o o{ansifmt.RESET}" + f"{ansifmt.HIRED}|    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}    |   |    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}    |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}_{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}|    {ansifmt.RESET}")
	print("             ")


def color_die1face5():
	'''Function to display a five on a die1 in ASCII'''
	print(f"{ansifmt.HIRED}     ___     {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}    |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o o{ansifmt.RESET}" + f"{ansifmt.HIRED}|    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}    | {ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED} |    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}    |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}_{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}|    {ansifmt.RESET}")
	print("             ")


def color_die1face6():
	'''Function to display a six on a die1 in ASCII'''
	print(f"{ansifmt.HIRED}     ___     {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}    |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o o{ansifmt.RESET}" + f"{ansifmt.HIRED}|    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}    |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o o{ansifmt.RESET}" + f"{ansifmt.HIRED}|    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}    |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}_{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}|    {ansifmt.RESET}")
	print("             ")


def color_die2face1():
	'''Function to display a one on a die1 in ASCII'''
	print(f"{ansifmt.HIRED}           ___     {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}          |   |    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}          | {ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED} |    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}          |___|    {ansifmt.RESET}")
	print("                   ")

def color_die2face2():
	'''Function to display a two on a die1 in ASCII'''
	print(f"{ansifmt.HIRED}           ___     {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}          |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}  |    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}          |   |    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}          |__{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}|    {ansifmt.RESET}")
	print("                   ")


def color_die2face3():
	'''Function to display a three on a die1 in ASCII'''
	print(f"{ansifmt.HIRED}           ___     {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}          |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}  |    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}          | {ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED} |    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}          |__{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}|    {ansifmt.RESET}")
	print("                   ")


def color_die2face4():
	'''Function to display a four on a die1 in ASCII'''
	print(f"{ansifmt.HIRED}           ___     {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}          |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o o{ansifmt.RESET}" + f"{ansifmt.HIRED}|    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}          |   |    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}          |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}_{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}|    {ansifmt.RESET}")
	print("                   ")


def color_die2face5():
	'''Function to display a five on a die1 in ASCII'''
	print(f"{ansifmt.HIRED}           ___     {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}          |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o o{ansifmt.RESET}" + f"{ansifmt.HIRED}|    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}          | {ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED} |    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}          |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}_{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}|    {ansifmt.RESET}")
	print("                   ")


def color_die2face6():
	'''Function to display a six on a die1 in ASCII'''
	print(f"{ansifmt.HIRED}           ___     {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}          |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o o{ansifmt.RESET}" + f"{ansifmt.HIRED}|    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}          |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o o{ansifmt.RESET}" + f"{ansifmt.HIRED}|    {ansifmt.RESET}")
	print(f"{ansifmt.HIRED}          |{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}_{ansifmt.RESET}" + f"{ansifmt.HIWHITE}o{ansifmt.RESET}" + f"{ansifmt.HIRED}|    {ansifmt.RESET}")
	print("                   ")


def cactus():
	'''Function to display a cactus'''
	print("                              ")
	print("             /|\              ")
	print("            |||||             ")
	print("            |||||             ")
	print("        /\  |||||             ")
	print("       |||| |||||             ")
	print("       |||| |||||  /\         ")
	print("       |||| ||||| ||||        ")
	print("        \|`-'|||| ||||        ")
	print("         \__ |||| ||||        ")
	print("            ||||`-'|||        ")
	print("            |||| ___/         ")
	print("            |||||             ")
	print("            |||||             ")
	print("                              ")


def color_cactus():
	'''Function to display a green cactus'''
	print(f"{ansifmt.HIGREEN}                               {ansifmt.RESET}")
	print(f"{ansifmt.HIGREEN}              /|\              {ansifmt.RESET}")
	print(f"{ansifmt.HIGREEN}             |||||             {ansifmt.RESET}")
	print(f"{ansifmt.HIGREEN}             |||||             {ansifmt.RESET}")
	print(f"{ansifmt.HIGREEN}         /\  |||||             {ansifmt.RESET}")
	print(f"{ansifmt.HIGREEN}        |||| |||||             {ansifmt.RESET}")
	print(f"{ansifmt.HIGREEN}        |||| |||||  /\         {ansifmt.RESET}")
	print(f"{ansifmt.HIGREEN}        |||| ||||| ||||        {ansifmt.RESET}")
	print(f"{ansifmt.HIGREEN}         \|`-'|||| ||||        {ansifmt.RESET}")
	print(f"{ansifmt.HIGREEN}          \__ |||| ||||        {ansifmt.RESET}")
	print(f"{ansifmt.HIGREEN}             ||||`-'|||        {ansifmt.RESET}")
	print(f"{ansifmt.HIGREEN}             |||| ___/         {ansifmt.RESET}")
	print(f"{ansifmt.HIGREEN}             |||||             {ansifmt.RESET}")
	print(f"{ansifmt.HIGREEN}             |||||             {ansifmt.RESET}")
	print(f"{ansifmt.HIGREEN}                               {ansifmt.RESET}")

############################################
#
#
# End of File
#
#
############################################
