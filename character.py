import pygame

class Squid:
	"""Intitialize villain character of SquidGame."""
	def __init__(self, game):
		"""Initialize game character."""
		self.screen = game.screen
		self.screen_rect = self.screen.get_rect()
		#load image of game character
		self.image = pygame.image.load("/images/squid_game.bmp")
		self.rect = self.image.get_rect()
		#Start the game character at the midleft of the screen
		self.rect.midleft = self.screen_rect.midleft

	def blitme(self):
		"""Draw character on screen."""
		self.image.blit(self.image, self.rect)
