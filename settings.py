class Settings():
	"""A class to store all game settings."""
	def __init__(self):
		"""Initializing game settings."""
		#screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0, 0, 0)
		#object settings
		self.soldier_limit = 3
		#bullet settings
		self.bullet_height = 3
		self.bullet_width = 15
		self.bullet_color = (255, 255, 255)
		self.bullet_limit = 3
		#squid settings
		self.squid_border = 200
		self.squid_direction = 1
		#Dynamic settings
		self.scaleup_lvl = 1.1
		#Init functions
		self._initialize_dynamic_settings()

	def _initialize_dynamic_settings(self):
		"""Initializing settings which increase with a level up."""
		#movement settings
		self.obj_speed = 2
		self.bullet_speed = 1.0
		self.squid_speed_x = 30
		self.squid_speed_y = 1
		#scoring settings
		self.squid_points = 50

	def increase_lvl(self):
		"""Initialize increase of settings."""
		self.obj_speed *= self.scaleup_lvl
		self.bullet_speed *= self.scaleup_lvl
		self.squid_speed_x *= self.scaleup_lvl
		self.squid_speed_y *= self.scaleup_lvl
		#scoring settings
		self.squid_points = int(self.squid_points * self.scaleup_lvl)

