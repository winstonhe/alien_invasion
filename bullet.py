import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
	'''a class for bullet'''
	def __init__(self,ai_settings,screen,ship):
		''' init a bullet object as ship position'''
		super(Bullet,self).__init__()
		self.screen=screen
		
		'''create a bullet rec at (0,0), then correct the positon'''
		self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
		self.rect.centerx=ship.rect.centerx
		self.rect.top=ship.rect.top
		
		'''store the buttet position with float'''
		self.y=float(self.rect.y)
		
		self.color=ai_settings.bullet_color
		self.speed_factor=ai_settings.bullet_speed_factor
		
	
	def update(self):
		'''move the bullet up'''
		
		'''update the bullet position'''
		self.y-= self.speed_factor
		
		'''update the bullect rect'''
		self.rect.y=self.y
		
	
	def draw_bullet(self):
		'''draw the bullet on screen'''
		pygame.draw.rect(self.screen,self.color,self.rect)
		
