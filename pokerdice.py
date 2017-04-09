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
			if rerolls in (1, 2, 3, 4, 5)
	
	
