class Settings():
	''' to save all settings of alian invasion'''
	
	def __init__(self):
		'''settings for screen'''
		self.screen_width=1200
		self.screen_height=800
		self.bg_color=(230,230,230)
		self.caption="Alien Invasion"
		
		'''settings for ship'''
		self.ship_speed_factor=1.5
		self.ship_limit=2
		
		'''settings for bullets'''
		self.bullet_color=(60,60,60)
		self.bullet_width=3;
		self.bullet_height=15
		self.bullet_speed_factor=20
		self.bullets_allowed=10
		
		'''settings for alien'''
		self.alien_speed_factor=1
		self.fleet_drop_speed=30
		self.fleet_direction=1
		
