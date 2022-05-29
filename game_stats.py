class GameStats:
	"""Simple Class to track game statistics."""
	def __init__(self, game):
		"""Initialize game stastistics."""
		self.settings = game.settings
		self.reset_stats()

	def reset_stats(self):
		"""Resets soldiers."""
		self.soldiers_left = self.settings.soldier_limit
		#Start the game in an active state.
		self.game_active = True
