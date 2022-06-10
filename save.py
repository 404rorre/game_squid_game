
class Save:
	"""Simple class to save highscore."""
	def __init__(self, game):
		"""Initialize class Save for highscore stats."""
		#Init game attributes.
		self.game = game
		self.stats = self.game.stats
		#Init save settings
		self.path_hs = "saves/highscore.txt"

	def hs_load(self):
		"""Loads high score after starting the game."""
		try:
			with open(self.path_hs, "r", encoding = "utf-8") as f:
				content = f.read().strip()
			self.stats.high_score = int(content)
			self.game.sb.prep_hs_score()
		except FileNotFoundError:
			pass

	def hs_save(self):
		"""Saves high score after closing the game."""
		with open(self.path_hs, "w", encoding = "utf-8") as f:
			f.write(f"{self.stats.high_score}\n")

