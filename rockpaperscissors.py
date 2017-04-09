#!/usr/bin/python2.7

import random
import time
import os

rock = 1
paper = 2
scissors = 3

names = { rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = { rock: scissors, paper: rock, scissors: paper }

player_score = 0
computer_score = 0

def start():
	print("Let's play a game of Rock, Paper, Scissors...")
	while game():
		pass
	scores()

def game():
	player = move()
	computer = random.randint(1, 3)
	result(player, computer)
	return play_again()
	
def move():
	while True:
		print()
		player = raw_input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
		try:
			player = int(player)
			if player in (1, 2, 3):
				return player
		except ValueError:
			pass
		print("That wasn't a valid answer. Please enter 1, 2 or 3.")

def result(player, computer):
	print("1...")
	time.sleep(1)
	print("2...")
	time.sleep(1)
	print("3!")
	time.sleep(0.5)
	
	print("Computer threw {0}!").format(names[computer])
	global player_score, computer_score
	if player == computer:
		print("You tied!")
	else:
		if rules[player] == computer:
			print("You won!")
			player_score += 1
		else:
			print("You lost, better luck next time!")
			computer_score += 1
			
def play_again():
	answer = raw_input("Would you like to play again? y/n: ")
	if answer in ("y", "Y", "yes", "Yes"):
		return answer
	else:
		print("Thanks for playing my game. See you next time!")
		
def scores():
	global player_score, computer_score
	os.system("clear")
	print("SCORES:")
	print "Player: ", player_score
	print "Computer: ", computer_score
	time.sleep(4)
	
if __name__ == '__main__':
	start()
