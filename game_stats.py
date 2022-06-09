class GameStats:
	"""Simple Class to track game statistics."""
	def __init__(self, game):
		"""Initialize game stastistics."""
		self.settings = game.settings
		self.high_score = 0
		#Init auto functions
		self.reset_stats()


	def reset_stats(self):
		"""Resets soldiers."""
		#Starts the game with initial attributes
		self.soldiers_left = self.settings.soldier_limit
		self.score = 0
		self.level = 1

		#Start the game in an active state.
		self.game_active = True

	