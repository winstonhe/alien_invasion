import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	''' a class to present a allien'''
	
	def __init__(self,ai_settings,screen):
		'''init allien and set its' starting position'''
		super(Alien,self).__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		
		#load allien image and set it's rect
		self.image=pygame.image.load("images/alien.bmp")
		self.rect=self.image.get_rect()
		
		#set the allien at the left up corner
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		
		#store the x postion of allien
		self.x=float(self.rect.x)
	
	def blitme(self):
		''' render the allien at the specified position'''
		self.screen.blit(self.image,self.rect)
		
	
	def update(self):	
		self.x +=self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction
		self.rect.x=self.x
	
	
	def check_edges(self):
		'''check if the alien is on edge'''
		
		screen_rect=self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left<=0:
			return True
		
		
	
	

