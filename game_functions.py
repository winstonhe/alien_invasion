import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_event(event,ai_settings,screen,ship,bullets):
	''' keydown event'''
	if event.key == pygame.K_RIGHT:
		ship.moving_right=True
	elif event.key==pygame.K_LEFT:
		ship.moving_left=True
	
	elif event.key==pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	
	elif event.key==pygame.K_q:
		sys.exit()		
		

def fire_bullet(ai_settings,screen,ship, bullets):
	'''if threshold is not reached, fire a bullet'''
	
	#init  a new bullet and add it to group
	if len(bullets)<ai_settings.bullets_allowed:
			new_bullet=Bullet(ai_settings,screen,ship)
			bullets.add(new_bullet)
	

def check_keyup_event(event,ship):
	''' keyup event'''
	if event.key == pygame.K_RIGHT:
		ship.moving_right=False
	elif event.key==pygame.K_LEFT:
		ship.moving_left=False
	
def check_events(ai_settings,screen,ship,bullets):
	'''respond mouse and keyboard event'''
	
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type== pygame.KEYDOWN:
			check_keydown_event(event,ai_settings,screen,ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_event(event,ship)
			

def update_screen(ai_settings,screen,ship,aliens,bullets):
	'''refresh the screen'''
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	
	'''re-draw the bullet'''
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	aliens.draw(screen)
	
	'''let the latest screen visible'''
	pygame.display.flip()
	

def update_bullets(ai_settings,screen,ship,aliens,bullets):
	'''update the position of bullet, and erase the gone bullet'''
	#update bullet position
	bullets.update()
	
	# erase the gone bullet
	for bullet in bullets.copy():
		if bullet.rect.bottom <=0:
			bullets.remove(bullet)	
	
	check_bullet_alien_collision(ai_settings,screen,ship,aliens,bullets)

	

def check_bullet_alien_collision(ai_settings,screen,ship,aliens,bullets):
	'''respond the collision between bullet and alien'''
	#check if the bullet shoots the alien	
	collisions=pygame.sprite.groupcollide(aliens,bullets,True,True)		
	if len(aliens)==0:
		#delete current bullets group and re-create another aliens group
		bullets.empty()
		create_fleet(ai_settings,screen,ship,aliens)
	
	print(len(aliens))
			

def update_ship(ship):
	'''update ship'''
	ship.update()

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
	
	screen_rect = screen.get_rect()
	#erase the aliens if the alien reaches the screen bottom
	for alien in aliens.copy():
		if alien.rect.bottom >= screen_rect.bottom:
			aliens.remove(alien)
	
	#detect if the ship hit with aliens
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,stats,screen,ship,aliens,bullets)

def check_fleet_edges(ai_settings,aliens):	
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break

def change_fleet_direction(ai_settings,aliens):
	for alien in aliens.sprites():
		alien.rect.y+=ai_settings.fleet_drop_speed
	ai_settings.fleet_direction*=-1
		

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
	'''re-act once the ship was hit by alien'''
	
	#ship left minus 1
	if stats.ship_left>0:
		stats.ship_left-=1
		
		#clean all bullets and aliens
		bullets.empty()
		aliens.empty()
		
		#create a new alien fleet, and put the  ship in the middle
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()
		
		#pause 0.5 second
		sleep(0.5)
	
	else:
		stats.game_active=False
		print("GAME OVER")
		

def get_number_aliens_x(ai_settings, alien_width):
	''' calculate how many aliens it can have in each row'''
	
	available_space_x =ai_settings.screen_width - 2*alien_width
	number_aliens_x= int(available_space_x / (2* alien_width))
	return number_aliens_x
	

def get_number_aliens_y(ai_settings,ship_height,alien_height):
	'''calculate how may rows the screen can have'''
	available_space_y=ai_settings.screen_height - ship_height - 4*alien_height
	number_aliens_y= int (available_space_y / (2* alien_height))
	return number_aliens_y

def create_alien(ai_settings,screen,aliens,alien_number,alien_number_row):
	''' create a single alien at specified place: alien_number'''
	alien = Alien(ai_settings,screen)
	alien_width=alien.rect.width
	alien.x=alien_width + 2*alien_width*alien_number
	alien.rect.x=alien.x
	
	alien.rect.y=alien.rect.height + 2*alien.rect.height * alien_number_row
	
	aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
	'''create a alien group'''
	alien=Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
	number_aliens_rows= get_number_aliens_y(ai_settings,ship.rect.height, alien.rect.height)
	
	# create a row of aliens
	for row_number in range(number_aliens_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number,row_number)
	


		
	
