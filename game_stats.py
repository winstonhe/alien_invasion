import pygame

class GameStates():
	'''track the game statistics information'''
	
	#init function
	def __init__(self, ai_settings):
		self.ai_settings=ai_settings
		self.game_active=True
		self.reset_stats()
		
	
	def reset_stats(self):
		self.ship_left=self.ai_settings.ship_limit
