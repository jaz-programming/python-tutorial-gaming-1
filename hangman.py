#!/usr/bin/python2.7

#First we import some modules
from random import *
import sys

#Then we create the score variables
player_score = 0
computer_score = 0

#Then we create the functions

def hangedman(hangman):
	graphic = [
	"""
	    +-----+
	    |	  
	    |	  
	    |	  
	    |
	    |
	==============
	"""
	,
	"""
	    +-----+
	    |     |
	    |     O	
	    |	   
	    |
	    |
        ==============
	"""
	,
	"""
	    +-----+
	    |     |	
	    |     O	
	    |    -|- 
	    |
	    |
	==============
	"""
	,
	"""
	    +-----+
	    |     |	
	    |     O	
	    |    -|- 
	    |    / \\
	    |
        ==============
	"""]
	print graphic[hangman]
	return
	


def start():
	print "Let's play a game of Linux Hangman!"
	'''while game():
		pass'''
	try:
		game()
	except KeyboardInterrupt:
		print
		print
		sys.exit("Goodbye!")
	scores()	

def game():
	dictionary = ["gnu", "kernel", "linux", "compile", "terminal", "ubuntu"]
	word = choice(dictionary) 
	word_length = len(word)
	clue = word_length * ["_"]
	tries = 3
	letters_tried = ""
	guesses = 0
	letters_right = 0
	letters_wrong = 0
	global computer_score, player_score
	
	while (letters_wrong != tries) and ("".join(clue) != word):
		letter = guess_letter()
		if len(letter) == 1 and letter.isalpha():
			if letters_tried.find(letter) != -1:
				print "You've already picked ", letter
			else:
				letters_tried = letters_tried + letter
				first_index = word.find(letter)
				if first_index == -1:
					letters_wrong += 1
					print "Sorry, ", letter, "isn't one of the letters."
				else:
					print "Well done! ", letter, "is correct!"
					for i in range(word_length):
						if letter == word[i]:
							clue[i] = letter
							
		else:
			print "Choose another."
			
			
		hangedman(letters_wrong)
		print " ".join(clue)
		print "Guesses: ", letters_tried
		
		if letters_wrong == tries:
			print "Game Over."
			print "The word was:", word
			computer_score += 1
			break
		if "".join(clue) == word:
			print "You Win!"
			print "The word was: ", word
			player_score += 1
			break
	return play_again()
	
def guess_letter():
	print
	letter = raw_input("Take a guess at the word:")
	letter.strip()
	letter.lower()
	print
	return letter
	
def play_again():
	answer = raw_input("Would you like to play again? y/n: ")
	if answer in ("y", "Y", "yes", "Yes"):
		return answer
	else:
		print "Thanks for playing my game. See you next time!"
		
def scores():
	global player_score, computer_score
	print
	print "SCORES"
	print
	print "Player: ", player_score
	print "Computer: ", computer_score
	print
	
if __name__ == "__main__":
	start()
