class Settings():
	"""A class to store all game settings."""
	def __init__(self):
		"""Initializing game settings."""
		#screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0, 0, 0)
		#ship settings
		self.obj_speed = 1.5
		#bullet settings
		self.bullet_height = 3
		self.bullet_width = 15
		self.bullet_speed = 1.0
		self.bullet_color = (255, 255, 255)
		self.bullet_limit = 3
		#squid settings
		self.squid_speed_x = 10
		self.squid_speed_y = 1
		self.squid_border = 100
		self.squid_direction = 1

