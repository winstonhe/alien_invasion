import pygame

class Ship():	
	def __init__(self,ai_settings,screen):
		'''init ship and its' position'''
		self.screen=screen
		self.ai_settings=ai_settings
		
		
		'''load ship and get the outer rectangle'''
		self.image=pygame.image.load("images/ship.bmp")
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		
		'''put the ship in the center bottom of screen'''
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		
		self.center=float(self.rect.centerx)
		self.moving_right=False
		self.moving_left=False
				
	
	def blitme(self):
		'''draw the ship at specififed position'''
		self.screen.blit(self.image,self.rect)
	
	def update(self):
		'''adjust the ship position'''
		
		''' udpate ship center'''
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center+=self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left>0:
			self.center-=self.ai_settings.ship_speed_factor
		
		self.rect.centerx=self.center
		
	
	def center_ship(self):
		'''put the ship in the center bottom of screen'''
		self.center=self.screen_rect.centerx
		
