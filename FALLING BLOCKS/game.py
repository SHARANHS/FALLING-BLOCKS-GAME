
import pygame  
import random
import sys
pygame.init()  

width=800 
height=600 
orange=(255, 153, 0)
green=(9, 112, 84)
black=(0,0,0)
bg=(175,238,238)

player_size=60
player_pos =[width/2,height-2*player_size]


enemy_size=50

enemy_pos =[random.randint(0,width-enemy_size),0]
enemy_list=[enemy_pos]

speed=10
score =0

screen = pygame.display.set_mode((width,height)) #2
game_over=False

clock=pygame.time.Clock()

myFont=pygame.font.SysFont("monospace",35)

def set_level(score,speed):
	

	speed=score/5+5;
	return speed

def drop_enemies(enemy_list):
	delay=random.random()
	if len(enemy_list)<10 and delay<0.1:
		x_pos=random.randint(0,width-enemy_size)
		y_pos=0
		enemy_list.append([x_pos,y_pos])

		
def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen,green,(enemy_pos[0],enemy_pos[1],enemy_size,enemy_size))

def update_en_pos(enemy_list,score):
	for idx,enemy_pos in enumerate(enemy_list):
			if enemy_pos[1] >=0 and enemy_pos[1] < height:
				enemy_pos[1]+=speed
			else:
				enemy_list.pop(idx)
				score+=1
	return score

def col_check(enemy_list,player_pos):
	for enemy_pos in enemy_list:
		if detect_col(enemy_pos,player_pos):
			return True
	return False

def detect_col(player_pos,enemy_pos):
	px=player_pos[0]
	py=player_pos[1]

	ex=enemy_pos[0]
	ey=enemy_pos[1]

	if (ex>=px and ex<(px+player_size)) or (px>=ex and px<(ex+enemy_size)):
		if (ey>=py and ey<(py+player_size)) or (py>=ey and py<(ey+enemy_size)):
			return True
	return False

while not game_over: 
	for event in pygame.event.get():

		if event.type==pygame.QUIT:
			sys.exit()
		if event.type== pygame.KEYDOWN:
			
			x=player_pos[0] 
			y=player_pos[1]

			if event.key==pygame.K_LEFT:
				x-=player_size	

			elif event.key==pygame.K_RIGHT:
				x+=player_size

			player_pos=[x,y]

	screen.fill(bg)
	#updating pos of enemy
	

	

	drop_enemies(enemy_list)
	score=update_en_pos(enemy_list,score)

	speed=set_level(score,speed)
	text="Score:"+str(score)
	label=myFont.render(text,1,black)
	screen.blit(label,(width-200,height-40))


	if col_check(enemy_list,player_pos):
		game_over=True
		print('GAME OVER!! your score is')
		print(score)
		break

	draw_enemies(enemy_list)

	pygame.draw.rect(screen,orange,(player_pos[0],player_pos[1],player_size,player_size))
	
	clock.tick(30)

	pygame.display.update()