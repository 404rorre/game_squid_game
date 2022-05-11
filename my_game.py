import sys
import pygame
from settings import Settings
from character import Squid

class Game:
	"""Main class for running the game."""
	def __init__(self):
		"""Initializing the game and create game ressources."""
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((
					self.settings.screen_width,
					self.settings.screen_height
					))
		pygame.display.set_caption("This is awesome!")
		self.villain = Squid(self)

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			#checking for input
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			#draw screen with background
			self.screen.fill(self.settings.bg_color)
			self.villain.blitme()
			#Redraw every cycle
			pygame.display.flip()

if __name__ == "__main__":
	#Create instance and run game.
	game = Game()
	game.run_game()
