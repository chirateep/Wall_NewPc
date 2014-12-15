import pygame
from pygame.locals import *

import random
import gamelib
from arrow import Arrow
from wall import Wall

class WallGame(gamelib.SimpleGame):
	BLACK = pygame.Color('black')
	WHITE = pygame.Color('white')
	GREEN = pygame.Color('green')
	
	def __init__(self):
		super(WallGame, self).__init__('Wall', WallGame.BLACK)
		self.arrow = []
		for i in range(10):
			self.arrow.append(Arrow(key = random.randint(0,25), color = WallGame.WHITE , pos = (random.randint(800,1000), random.randint(50,350)), speed = 1))
		self.wall = Wall(pos = (200,0), color = WallGame.WHITE)
		self.score = 0
		self.count_speed_up = 0
		self.count_speed_down = 0
		self.dead = True
		
	def init(self):
		super(WallGame, self).init()
		self.render_score()

		
	def update(self):
		if self.dead is True:
			for i in self.arrow:
				i.move()
				if self.is_key_pressed(i.key_press(i.get_key())):
					i.remove()
					self.score += 1
					self.render_score()
					self.count_speed_up += 1
				if i.get_x() < 200:
					i.remove()
					self.score -= 5
					self.render_score()
					self.count_speed_down += 1
				if self.count_speed_up == 10:
					i.speed_up()
					self.count_speed_up = 0
				if self.count_speed_down == 100:
					i.speed_down()
					self.count_speed_down = 0
				if self.score < 0:
					self.is_dead()

	def is_dead(self):
		self.dead = False
		self.render_dead()
		self.score = 0
		self.render_score()

		
	def render_dead(self):
		self.dead_image = self.font.render("BooM Your Dead!!!", 0,WallGame.WHITE)
				
	def render_score(self):
		self.score_image = self.font.render("Score = %d" % self.score, 0, WallGame.WHITE)

	def render_key(self):
		for i in self.arrow:
			i.key_image = self.font.render("%c" % i.key_arrow(i.get_key()), 0, WallGame.WHITE)
		

	def render(self, surface):
		surface.blit(self.score_image, (10,10))
		if self.dead is False:
			surface.blit(self.dead_image,(300,150))
		self.render_key()
		for i in self.arrow:
			surface.blit(i.key_image, (i.get_x(),i.get_y()))
		self.wall.render(surface)
		
		

def main():
	game = WallGame()
	game.run()

if __name__ == '__main__':
	main()
