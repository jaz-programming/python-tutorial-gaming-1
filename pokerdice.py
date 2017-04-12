#!/usr/bin/python2.7

#pokerdice.py

import random
from itertools import groupby

nine = 1
ten = 2
jack = 3
queen = 4
king = 5
ace = 6

names = { nine: "9", ten: "10", jack: "J", queen : "Q", king = "K", ace = "A" }

player_score = 0
computer_score = 0

def start():
	print "Let's play a game of Poker Dice."
	while game():
		pass
	scores()
	
def game():
	print "The computer will help you throw your five dice."
	throws()
	return play_again()
	
def throws():
	roll_number = 5
	dice = roll(roll_number)
	dice.sort()
	for i in range(len(dice)):
		print "Dice ", i + 1, ": ", names[dice[i]]
		
	result = hand(dice)
	print "You currently have", result
	
	while True:
		rerolls = raw_input("How many dice do you want to throw again?")
		try:
			if rerolls in (1, 2, 3, 4, 5):
				break
		except ValueError:
			pass
		print "That wasn't a valid answer. Please enter 1, 2, 3, 4 or 5."
	if rerolls == 0:
		print "You finish with ", result
	else:
		roll_number = rerolls
		dice_rerolls = roll(roll_number)
		dice_changes = range(rerolls)
		print "Enter the number of a dice to reroll: "
		
		
		iterations = 0
		while iterations < rerolls:
			iterations += 1
			while True:
				selection = raw_input("")
				try:
					if selection in (1, 2, 3, 4, 5):
						break
				except ValueError:
					pass
				print "That wasn't a valid answer. Please enter 1, 2, 3, 4 or 5."
			dice_changes[iterations-1] = selection-1
			print "You have changed dice ", selection
			
		iterations = 0
		while iterations < rerolls:
			iterations += 1
			replacement = dice 
			
		
	
	
