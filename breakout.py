
from collections import namedtuple as nt
import pygame as pg
import sys
import time

W = 804
H = 600
RED = 200, 0, 0
WHITE = 200, 200, 200
GOLD = 205, 145, 0

ball = Rect((W/2, H/2), (30, 30))
Direction = nt('Direction', 'x y')
ball_dir = Direction(5, -5)

bat = Rect((W/2, H/2), (30, 30))

class Block(Rect):
	
	def __init__(self, colour, rect):
		Rect.__init__(self, rect)
		self.colour = colour
		
blocks = []
for n_block in range(24):
	block = Block(GOLD, ((((n_block % 8)* 100) + 2, ((n_block // 8) * 25) + 2), (96, 23)))
	blocks.append(block)
	
def draw_blocks():
	for block in blocks:
		screen.draw.filled_rect(block, block.colour)
		
def draw():
	screen.clear()
	screen.draw.filled_rect(ball, WHITE)
	screen.draw.filled_rect(bat, RECD)
