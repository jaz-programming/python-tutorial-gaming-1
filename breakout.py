
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
Direction = nt('Direction')
