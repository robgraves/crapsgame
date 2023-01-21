# crapsgame
Matthew Page

me@matthewjpage.com



INSTRUCTIONS:

-To play, using python 3, run from command line:

`python3 main.py`

-To have sound install mplayer package on your Linux distribution

if it isn't already on your system.



FILES:

main.py 	-  main game file

README.md   -  this file

data/save/userdata.p  -  user data is stored here

data/graphics/graphics.py - ASCII art for game

data/sounds/diceroll.mp3 - sound effect for dice rolls

data/sounds/aww.mp3 - sound effect for shooter losing

data/sounds/applause.wav - sound effect for shooter winning

data/sounds/claps.mp3 - sound effect for shooter winning

data/sounds/winsound.wav - sound effect for any other bet winning

data/sounds/chips.mp3 - sound effect for any other bet winning



01/20/2023

I may have found the hanging bug I had from the previous couple of 

commits.  My initial thought was that it had something to do with

my save function, which calls pickle as I had/have it saving multiple

times in a round of gameplay.  I also had read online that pickle was

slow and people were suggesting JSON, which I may still switch over to.

But it is currently my thought that it was my sound files that were

causing the bottleneck as I call a certain soundfile to be played anytime

a bet wins, but that could be multiple bets winning simultaneously which means

I could have a ton of system calls to play the same exact winning sound every

time, so I switched all those sound calls to just switching a variable from a 

0 to a 1, and then at the end of each stage checking that variable if it's 1 to

play the win sound.  Only further extensive testing will tell if I'm right, but

it appears to be fixed.



01/18/2023

Finished function for Come and Don't Come bets that mostly work

but there do seem to be some erroneous payouts, or rather not

paying out when it should and/or not taking the bet when it should.

Additionally I have a nasty bug that happens occasionally within the 

Come/Don't Come function that causes the game to hang for 10 to 20 

seconds.  

I think the solutions to both of these problems is some further 

reorganization and restructuring of the code as I have payouts

and bet losses all handled outside of a function that has repeated

sections of code, so I plan to move all the payouts/losses into 

function(s).  The other plan is to make all the functions take

and return multiple variables, which I didn't realize you could do

in Python, so I can eliminate all of my global variables, and then chop

up all my functions into seperate files, so that the main function ends up

being mostly just a series of function calls so I can scan through it

quicker to find bugs in the game flow.

That's the plan anyway.  Unsure the timespan to accomplish the above,

but starting that soon.



01/16/2023

Added the ability to NOT bet on Pass or Don't Pass on come out

roll.  Also limited Free Odds bets to 5x the pass/dp bet.

Also changed Field Bet payout for 12 from 3x to 2x to match the 2.



01/13/2023

Propositions bets appear to be working, this includes 2,3,11,12, 

also the hardways for 4,6,8,10, as well as any seven, and any craps

Added Big 6, Big 8, C&E, and World bets under Miscellaneous bets

Works but needs more rigorous testing to ensure accuracy.



01/09/2023

Place, Buy, and Lay bets completed and appears to be working.

Needs some thorough testing to make sure there are no hiccups

anywhere.



01/07/2023

Place bets with option to take down bets appears to be

fully functional.  Next on to Buy bets and Lay bets.

Also added more sounds.



01/03/2023

Free odds bets for Pass/Don't Pass are fully functional 

and reorganized code into a folder and a couple files

renamed craps.py to main.py

NOTE:	If you have an earlier pull of this like I do and want to keep your bankroll

then you will need to move your userdata.p into the new data folder



	
12/28/2022

Fully functional game with only the Pass/Don't Pass betting options, saving and loading works.

TO DO:

All other betting options:

DONE! 12/30/2022 - Free odds bets on Pass/DP

- Come bet/Don't Come Bets

- Free odds bets on Come/Don't Come

DONE! 01/03/2023 - Field Bets

DONE! 01/07/2023 - Place Bets/Buy Bets/Lay Bets

DONE! 01/13/2023 - Propostions bets,Hardway Bets/Any Craps/Any Seven

- Any other bets or features I might want to add:

DONE! 01/13/2023 - Big 6 and Big 8

DONE! 01/13/2023 - C&E Bet (Craps and Eleven)

DONE! 01/13/2023 - World Bet (C&E plus any seven)



12/26/2022

Toying with this command line craps game again hoping to make it functional.



11/15/2019 

After a hiatus from working on this I am trying to structure this is some way that I don't end up with a mess of spaghetti code.  Need to plan out all the functions and program control flow that I'm going to need for this game to 
function properly.



07/15/2019

This is just an experiment with me learning python again and trying to get back into coding after a hiatus.
So I'm just learning python while trying to write a command line Craps game because I love playing craps at the casinos.

I started working on this a few weeks ago but decided to make a repo for it so I don't lose my progress and feel more secure about making major changes.
