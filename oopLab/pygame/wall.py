import pygame
from pygame.locals import *

class Wall(object):
	def __init__(self, pos, color):
		(self.x,self.y) = pos
		self.color = color
	
	def render(self, surface):
		pygame.draw.line(surface, self.color, (self.x,self.y), (self.x,self.y+400), 2)
