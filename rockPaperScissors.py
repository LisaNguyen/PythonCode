import random

###ASK FIRST USER TO ENTER THEIR CHOICE###
firstChoice =  raw_input("Rock, paper, or scissors: ")

###GENERATES A RANDOM ANSWER FOR INT FOR THE SECOND USER###
secondChoice = random.randint(0,3);

"""
COMPARES THE RANDOM INT USING CONDITIONAL STATEMENTS
DEPENDING ON THE RANDOM INT GENERATED, DECLARE AND INITIALISE A VALUE TO HOLD A STRING 
"""
if(secondChoice == 0):
	secondChoice_ = "Rock"

elif(secondChoice == 1):
	secondChoice_ = "Paper"

else:
	secondChoice_ = "Scissors"
	

###COMPARES THE TWO VALUES, CHECKS WHO THE WINNER IS AND PRINTS THE RESULT TO SCREEN ###
def compare(first, second):
	if((first.lower() == "rock") and (second.lower() == "scissors")):
		print "First user wins"

	elif((first.lower() == "scissors") and (second.lower() == "paper")):
		print "First user wins"

	elif((first.lower() == "paper") and (second.lower() == "rock")):
		print "First user wins"

	elif(first.lower() == second.lower()):
		print "It's a tie"

	else:
		print "Second user wins"

###CALLS THE COMPARE FUNCTION AND ENTER THE TWO USERS' CHOICES AS PARAMETERS###
compare(firstChoice, secondChoice_)
print "First user's choice: " + firstChoice
print "Second user's choice: " + secondChoice_
