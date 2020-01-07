import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStates
import game_functions as gf
from pygame.sprite import Group

def run_game():
#初始化游戏并创建一个屏幕对象
	pygame.init()
	
	'''load game settings'''
	ai_settings=Settings()
	
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption(ai_settings.caption)
	
	'''create a ship'''
	ship=Ship(ai_settings,screen)
	
	'''init a allien group'''
	aliens=Group()
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	'''create a group to store all bullets'''
	bullets=Group()
	
	#init a stats object
	stats=GameStates(ai_settings)
	
		
	#开始游戏的主循环
	while True:
		#监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,ship,bullets)
		
		if stats.game_active:
			gf.update_ship(ship)
			
			gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
			
			print(len(bullets))		
			gf.update_screen(ai_settings,screen,ship,aliens,bullets)		
		 
run_game()
