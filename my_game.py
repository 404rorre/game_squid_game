import sys
import pygame
from pygame.sprite import Sprite
from random import uniform
from random import randint
from settings import Settings
from character import Soldier
from bullet import Bullet
from squid import Squid

class Game:
	"""Main class for running the game."""
	def __init__(self):
		"""Initializing the game and create game ressources."""
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode(
			(0,0),
			pygame.FULLSCREEN

			)
		self.screen_rect = self.screen.get_rect()
		self.settings.screen_width = self.screen_rect.width
		self.settings.screen_height = self.screen_rect.height
		pygame.display.set_caption("This is awesome!")
		#Initialize game variables
		self.soldier = Soldier(self)
		self.bullets = pygame.sprite.Group()
		self.squids = pygame.sprite.Group()
		self._create_x_squids(5)
		#Flags
		self.exit_game = False

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_event()
			self.soldier.update()
			self._bullet_update()
			self._squids_update()
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
				self.soldier.right = True
				print("right")
			#Move object to the left.
			if event.key == pygame.K_LEFT:
				self.soldier.left = True
				print("left")
			#Move the object up.
			if event.key == pygame.K_UP:
				self.soldier.up = True
				print("up")
			#Move the object down.
			if event.key == pygame.K_DOWN:
				self.soldier.down = True
				print("down")
			#Close the game.
			if event.key == pygame.K_q:
				self.exit_game = True
				print("q")
			#Shooting bullet
			if event.key == pygame.K_SPACE:
				self._fire_bullet()
				print("Space")

	def _check_key_up_events(self, event):
		"""Checking for KEYUP-Events"""
		if event.type == pygame.KEYUP:
			#Move object to the right.
			if event.key == pygame.K_RIGHT:
				self.soldier.right = False
			#Move object to the left.
			if event.key == pygame.K_LEFT:
				self.soldier.left = False
			#Move the object up.
			if event.key == pygame.K_UP:
				self.soldier.up = False
			#Move the object down.
			if event.key == pygame.K_DOWN:
				self.soldier.down = False

	def _fire_bullet(self):
		"""Firing one bullet."""
		if len(self.bullets) < self.settings.bullet_limit:
			#Creating Std bullet
			bullet_new = Bullet(self)			
		else:
			#Creating slow bullets because overheated
			bullet_new = Bullet(self, 0.3)	
		self.bullets.add(bullet_new)

	def _bullet_update(self):
		"""Update bullet Position and remove when off screen."""
		#Update position
		self.bullets.update()
		#Remove bullets which left the screen
		for bullet in self.bullets.copy():
			if bullet.rect.left > self.screen_rect.right:
				self.bullets.remove(bullet)
		#Check bullet-squid collision.
		self._check_bullet_squid_collision()


	def _draw_screen(self):
		"""Drawing screen every cycle."""
		self.screen.fill(self.settings.bg_color)
		self.soldier.blitme()
		self._bullet_draw()
		self.squids.draw(self.screen)
		pygame.display.flip()

	def _bullet_draw(self):
		"""Draw bullet on screen."""
		#go through sprite.Group and draw each bullet
		for bullet in self.bullets:
			bullet.draw()

	def _check_bullet_squid_collision(self):
		"""Checks bullet-squid collision."""
		#Remove any bullets and squids that collided.
		collisions = pygame.sprite.groupcollide(self.bullets, 
												self.squids, 
												True, True)
		if not self.squids:
			#Destroy any remaining bullet.
			self.bullets.empty()
			self._create_x_squids(5)

	def _create_x_squids(self, nr_squid):
		"""Function to add multiple squids on the field."""
		for nr in range(nr_squid):
			self._create_one_squid()

	def _create_one_squid(self):
		"""Simple function to add only one squid on the screen."""
		squid = Squid(self)
		squid_width, squid_height = squid.rect.size
		#random position generator for squids to shoot down
		rng_x = randint(self.soldier.rect.width + 3 * squid_width,
						self.settings.screen_width - squid_width)
		rng_y = randint(squid_height, 
						self.settings.screen_height - squid_height)
		#set squid position
		squid.x = rng_x
		squid.rect.x = rng_x
		squid.y = rng_y 
		squid.rect.y = squid.y
		#set unique movement
		rng_speed = uniform(1, 2.3)
		squid.speed_y_unique = self.settings.squid_speed_y * rng_speed
		#first storage for unique border
		squid.border_unique = self.settings.squid_border
		squid.rect_old_y = squid.rect.y
		self.squids.add(squid)

	def _squids_update(self):
		"""Updates squid position."""

		self.squids.update()
		self._squids_check_edge()

	def _squids_check_edge(self):
		"""
		Checkes in one squid touches edge and changes y movement.
		Full function inside the loop.
		"""
		for squid in self.squids.sprites():
			if squid.check_edge_y():
				squid.direction_unique *= -1
				squid.x -= self.settings.squid_speed_x
				squid.rect.x = squid.x
				squid.rect_old = squid.rect			


if __name__ == "__main__":
	#Create instance and run game.
	game = Game()
	game.run_game()
