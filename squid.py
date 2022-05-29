import pygame
import random
from pygame.sprite import Sprite

class Squid(Sprite):
	"""
	Simple class to hold all squid related variables and methods to update
	movement and position.
	"""
	def __init__(self, game):
		"""Initialize squid variables."""
		#Initialize superclass Sprite
		super().__init__()
		#Initialize game variables
		self.screen = game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = game.settings
		#Intialize image variables
		self.image = pygame.image.load("images/squid.bmp")
		self.rect = self.image.get_rect()
		#position storage
		self.rect_old_y = None
		#Initialize movement variables
		self.x = int(self.rect.x)
		self.y = int(self.rect.y)
		#Unique movement attributes
		self.speed_y_unique= 0
		self.border_unique =0
		self.direction_unique = 1

	def update(self):
		"""Updates squid position."""
		self.y += int(self.speed_y_unique
					* self.direction_unique)
		self.rect.y = self.y

	def check_edge_y(self):
		"""Checks for individual border to change direction."""
		rng_border = random.uniform(1, 2)
		print(self.rect_old_y , " ", self.rect.y)
		if (self.rect_old_y >= (self.rect.y + self.settings.squid_border) or
			self.rect_old_y <= (self.rect.y - self.settings.squid_border)or 
			self.rect.top <= self.screen_rect.top or 
			self.rect.bottom >= self.screen_rect.bottom):

			self.rect_old_y = self.rect.y 
			self.border_unique *= rng_border
			return True
			

