import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""Simple class to shoot bullets."""
	def __init__(self, game, bullet_speed=None):
		super().__init__()
		self.screen = game.screen
		self.settings = game.settings
		self.color = game.settings.bullet_color
		if bullet_speed:
			self.bullet_speed = bullet_speed
		else:
			self.bullet_speed = self.settings.bullet_speed

		#Create a bullet at (0, 0) and set the correct position
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
					self.settings.bullet_height)
		self.rect.midright = game.soldier.rect.midright
		#create y coordinate of self.rect with float
		self.x = float(self.rect.x)

	def update(self):
		"""Updating y position of bullets on screen."""
		#update decimal position of the bullet
		self.x += self.bullet_speed
		#update the rect position
		self.rect.x = self.x

	def draw(self):
		"""Drawing bullet on screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)