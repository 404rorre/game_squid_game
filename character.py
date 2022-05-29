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
		self.rect.midleft = self.screen_rect.midleft
		#Position parameters
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
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
				self.x  += float(self.settings.obj_speed)
		#Move to the left.
		if self.rect.left >= 0 :
			if self.left:
				self.x  -= float(self.settings.obj_speed)
		#Move up.
		if self.rect.top >= 0 :
			if self.up:
				self.y -= float(self.settings.obj_speed)
		#Move down.
		if self.rect.bottom <= self.screen_rect.bottom:
			if self.down:
				self.y += float(self.settings.obj_speed)

		self.rect.x = self.x 
		self.rect.y = self.y 

	def blitme(self):
		"""Draw character on screen."""
		self.screen.blit(self.image, self.rect)

	def reset_soldier(self):
		"""Resets Soldier to start position."""
		self.rect.midleft = self.screen_rect.midleft
		
		self.rect.x = self.x 
		self.rect.y = self.y
