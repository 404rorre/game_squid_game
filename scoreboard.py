import pygame.font
from pygame.sprite import Group
from character import Soldier

class Scoreboard:
	"""Class to show scoreboard HUD of the game."""
	def __init__(self, game):
		"""Initializing attributes."""
		#Init game attributes
		self.game = game
		self.settings = game.settings
		self.stats = game.stats 
		self.screen = game.screen 
		self.screen_rect = self.screen.get_rect()

		#Font settings for scoring information.
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		#Prepare initial score images
		self.prep_score()
		self.prep_hs_score()
		self.prep_lvl()
		self.prep_soldiers_left()

	def prep_score(self):
		"""Initialize score image for the game."""
		rounded_score = round(self.stats.score, -1)
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True,
							self.text_color, self.settings.bg_color)
		
		#Display the score at the top right corner if the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right -20
		self.score_rect.top = 20

	def prep_hs_score(self):
		"""Initialize high score image for the game."""
		rounded_hs = round(self.stats.high_score, -1)
		hs_str = "{:,}".format(rounded_hs)
		self.hs_image = self.font.render(hs_str, True,
							self.text_color, self.settings.bg_color)

		#Display High Sore in the middle of the sceen.
		self.hs_rect = self.hs_image.get_rect()
		self.hs_rect.midtop = self.screen_rect.midtop
		self.hs_rect.top = self.score_rect.top

	def prep_lvl(self):
		"""Initialize level image for the game."""
		level_str = str(self.stats.level)
		self.lvl_image = self.font.render(level_str, True,
							self.text_color, self.settings.bg_color)

		#Display image below Score
		self.lvl_rect = self.lvl_image.get_rect()
		self.lvl_rect.right = self.score_rect.right
		self.lvl_rect.top = self.score_rect.bottom

	def prep_soldiers_left(self):
		"""Initialize life display of game character soldier."""
		self.soldiers = Group()
		for soldier_nr in range(self.stats.soldiers_left):
			soldier = Soldier(self.game)
			soldier.rect.top = self.score_rect.top
			soldier.rect.x = soldier.rect.width * soldier_nr + 10 
			self.soldiers.add(soldier)

	def update(self):
		"""Updates Scoreboard."""
		self.prep_score()
		self.prep_lvl()
		self.prep_soldiers_left()
		self.check_high_score()

	def check_high_score(self):
		"""Checks if the player reached a bigger high score."""
		if self.stats.high_score < self.stats.score:
			self.stats.high_score = self.stats.score
			self.prep_hs_score()
			print(self.stats.high_score)

	def show_score(self):
		"""Draws Scoreboard on screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.hs_image, self.hs_rect)
		self.screen.blit(self.lvl_image, self.lvl_rect)
		self.soldiers.draw(self.screen)

