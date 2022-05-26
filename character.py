import pygame
from settings import Settings

class Soldier:
	"""Intitialize villain character of SquidGame."""
	def __init__(self, game):
		"""Initialize game character."""
		self.screen = game.screen
		self.screen_rect = self.screen.get_rect()
		#Initialize settings
		self.settings = Settings()
		#load image of game character
		self.image = pygame.image.load("images/squid_game.bmp")
		self.rect = self.image.get_rect()
		#Start the game character at the midleft of the screen
		self.rect.midbottom = self.screen_rect.midbottom
		#Movement flag
		self.right = False
		self.left = False
		self.up = False
		self.down = False	
	
	def update(self):
		"""Update the objects positions bases on the movement flag."""
		#Move to the rigth.
		if self.rect.right <= self.screen_rect.right:
			if self.right:
				self.rect.x += float(self.settings.obj_speed)
		#Move to the left.
		if self.rect.left >= 0 :
			if self.left:
				self.rect.x -= float(self.settings.obj_speed)
		#Move up.
		if self.rect.top >= 0 :
			if self.up:
				self.rect.y -= float(self.settings.obj_speed)
		#Move down.
		if self.rect.bottom <= self.screen_rect.bottom:
			if self.down:
				self.rect.y += float(self.settings.obj_speed)

	def blitme(self):
		"""Draw character on screen."""
		self.screen.blit(self.image, self.rect)
