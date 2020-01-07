import pygame
from pygame.sprite import Sprite

class Allien(Sprite):
	''' a class to present a allien'''
	
	def __init__(self,ai_settings,screen):
		'''init allien and set its' starting position'''
		super(Allien,self).__init__()
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

