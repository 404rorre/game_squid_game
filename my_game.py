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
		#Flags
		self.exit_game = False

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_event()
			self.villain.update()
			self._draw_screen()
				


	def _check_event(self):
		"""Checking for input"""
		for event in pygame.event.get():
			self._check_key_down_events(event)
			self._check_key_up_events(event)
			self._check_close_game(event)


	def _check_close_game(self, event):
		if event.type == pygame.QUIT:
			self.exit_game = True		
		if self.exit_game:
			sys.exit()

	def _check_key_down_events(self, event):
		"""Checking for KEYDOWN-Events"""
		if event.type == pygame.KEYDOWN:
			#Move object to the right.
			if event.key == pygame.K_RIGHT:
				self.villain.right = True
			#Move object to the left.
			if event.key == pygame.K_LEFT:
				self.villain.left = True
			#Move the object up.
			if event.key == pygame.K_UP:
				self.villain.up = True
			#Move the object down.
			if event.key == pygame.K_DOWN:
				self.villain.down = True
			#Close the game.
			if event.key == pygame.K_q:
				self.exit_game = True

	def _check_key_up_events(self, event):
		"""Checking for KEYUP-Events"""
		if event.type == pygame.KEYUP:
			#Move object to the right.
			if event.key == pygame.K_RIGHT:
				self.villain.right = False
			#Move object to the left.
			if event.key == pygame.K_LEFT:
				self.villain.left = False
			#Move the object up.
			if event.key == pygame.K_UP:
				self.villain.up = False
			#Move the object down.
			if event.key == pygame.K_DOWN:
				self.villain.down = False

	def _draw_screen(self):
		"""Drawing screen every cycle."""
		self.screen.fill(self.settings.bg_color)
		self.villain.blitme()
		pygame.display.flip()

if __name__ == "__main__":
	#Create instance and run game.
	game = Game()
	game.run_game()
