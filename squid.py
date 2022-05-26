import pygame
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
		self.rect_old = None
		#Initialize movement variables
		self.x = int(self.rect.x)
		self.y = int(self.rect.y)
		#Unique movement speed
		self.speed_y_unique= 0

	def update(self):
		"""Updates squid position."""
		self.y += int(self.settings.squid_speed_y 
					* self.settings.squid_direction)
		self.rect.y = self.y

	def check_edges(self):
		"""Checks for individual border to change direction."""
		if (self.rect_old >= (self.rect_old + self.settings.squid_border) or
			self.rect_old <= (self.rect_old - self.settings.squid_border)):
			return True

