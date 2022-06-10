import pygame.font

class Button:
	"""Simple method to display buttons in game."""
	def __init__(self, game, msg):
		"""Initialize settings for button."""
		#Init game attributes
		self.game = game
		self.screen = game.screen 
		self.screen_rect = self.screen.get_rect()
		self.settings = game.settings 

		#Init Font settings
		self.width, self.height = 200, 50
		self.button_color = (250, 0, 0)
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		#Init Buttons rect object and set position
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		#Prep msg
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Turn msg into a rendered image and center on the button."""
		self.msg_image = self.font.render(msg, True,
							self.text_color, self.button_color)
		self.msg_rect = self.msg_image.get_rect()
		self.msg_rect.center = self.rect.center

	def blit_button(self):
		"""Display button on screen."""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_rect)

