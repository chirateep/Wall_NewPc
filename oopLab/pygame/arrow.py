import pygame
from pygame.locals import *
import gamelib
import random
class Arrow(object):

	def __init__(self, key, color, pos, speed):
		(self.x, self.y) = pos
		self.vx = speed
		self.key = key
		self.color = color

	def key_arrow(self, key):
		self.alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ' ]
		return self.alphabet[self.key]

	def key_press(self, key):
		self.press = 		[K_a,K_b,K_c,K_d,K_e,K_f,K_g,K_h,K_i,K_j,K_k,K_l,K_m,K_n,K_o,K_p,K_q,K_r,K_s,K_t,K_u,K_v,K_w,K_x,K_y,K_z,K_UP]
		return self.press[self.key]

	def move(self):
		self.x -= self.vx

	def remove(self):
		self.x = 800
		self.key = random.randint(0,25)

	def speed_up(self):
		self.vx += 1

	def speed_down(self):
		self.vx -= 0.1
		if self.vx <= 1:
			self.vx = 1
				

	def render(self, surface):
		pass

	def get_key(self):
		return self.key

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y
			

		
