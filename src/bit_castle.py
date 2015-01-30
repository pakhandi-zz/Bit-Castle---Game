import pygame
import sys
import random

pygame.init()
pygame.display.init()

background_color = (255,255,255) #White
man_color = (0,0,0)
wall_color = (240,150,0)
red = (255,0,0)
green = (0, 155, 0)
gate_color = (255,0,0)
(width, height) = (200, 700)

wall_x = []
wall_y = []
wall_length = []
wall_width = []
WALLS = 22

death_x = []
death_y = []

recharge_x = []
recharge_y = []
initial_charge_array = [  700  ,  700  ,  700  ,  700  ,  400  ,  400  ,  400  ,  400  ,  300  ,  300  ]
clock_tick_array =     [  80   ,  70   ,  70   ,  50   ,  40   ,  40   ,  30   ,  30   ,  30   ,  30   ]
new_recharge_array =   [  140  ,  130  ,  100  ,  100  ,  120  ,  120  ,  130  ,  130  ,  150  ,  150  ]
max_deaths_array =     [  2    ,  3    ,  4    ,  4    ,  6    ,  6    ,  6    ,  6    ,  6    ,  6    ]
max_recharges_array =  [  6    ,  6    ,  6    ,  6    ,  6    ,  6    ,  5    ,  5    ,  4    ,  4    ]



global DEATHS
global RECHARGES

global gate_x
global gate_y
global reached_gate

global doexit
global isrunning

global curr_score
curr_score = 0

global INITIAL_CHARGE, NEW_RECHARGE, CLOCK_TICK

def start_Screen():
	screen = pygame.display.set_mode((width, height))
	font1 = pygame.font.SysFont('Arial', 20)
	font2 = pygame.font.SysFont('comicsansms', 30)
	pygame.display.set_caption("Bit Castle")
	screen.fill(background_color)
	screen.blit(font2.render("Bit Castle", True, green), (35,100))
	screen.blit(font1.render("Press P to Play",True, (0,0,0)), (45,200))
	pygame.display.flip()
	isrunning = True
	while isrunning:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					return
				if event.key == pygame.K_q:
					sys.exit(0)

def pause_Screen(curr_score):
	screen = pygame.display.set_mode((width, height))
	font1 = pygame.font.SysFont('Arial', 20)
	font2 = pygame.font.SysFont('comicsansms', 30)
	pygame.display.set_caption("Bit Castle")
	screen.fill(background_color)
	screen.blit(font2.render("Paused", True, green), (48,100))
	screen.blit(font1.render("Press Z to Resume",True, (0,0,0)), (30,200))
	coinpic = pygame.image.load('coin.png')
	screen.blit(coinpic, (60, 245))
	screen.blit(font1.render(str(curr_score), True, (0,0,0)), (80,240))
	
	pygame.display.flip()
	isrunning = True
	while isrunning:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p or event.key == pygame.K_z:
					return
				if event.key == pygame.K_q:
					sys.exit(0)

def start_level(nlevel):

	sound = pygame.mixer.Sound("c.wav")
	doclaps = pygame.mixer.Sound("claps.wav")

	del wall_x[:]
	del wall_y[:]
	del wall_length[:]
	del wall_width[:]
	del death_x[:]
	del death_y[:]
	del recharge_x[:]
	del recharge_y[:]

	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Bit Castle")
	screen.fill(background_color)
	pygame.display.flip()

	global INITIAL_CHARGE
	global CLOCK_TICK, NEW_RECHARGE

	INITIAL_CHARGE = initial_charge_array[nlevel]
	battery = INITIAL_CHARGE

	isdead = False

	CLOCK_TICK = clock_tick_array[nlevel]
	NEW_RECHARGE = new_recharge_array[nlevel]

	MAX_DEATHS = max_deaths_array[nlevel]
	MAX_RECHARGES = max_recharges_array[nlevel]



	font1 = pygame.font.SysFont('Arial', 20)

	global isrunning
	isrunning = True

	global doexit
	doexit = False

	global WALLS
	global gate_x
	gate_x = 100
	global gate_y
	gate_y = 0
	global reached_gate
	reached_gate = False

	global key_x
	global key_y
	global got_key
	got_key = False
	key_y = random.randint(260,280)
	key_x = random.randint(10,180)
	print key_x
	print key_y

	global curr_score


	global DEATHS
	DEATHS = 0
	global RECHARGES
	RECHARGES = 0

	curr_x = 90
	curr_y = 590
	last_x = 90
	last_y = 590
	dir_x_change = 0
	dir_y_change = 0

	touched_wall_lower = False
	touched_wall_upper = False
	touched_wall_right = False
	touched_wall_left = False

	clock = pygame.time.Clock()

	img = pygame.image.load('snakeHead.png')
	batterypic = pygame.image.load('battery.png')
	killpic = pygame.image.load('kill.png')
	gatepic = pygame.image.load('door.png')
	brickpic = pygame.image.load('brick.png')
	bigbatterypic = pygame.image.load('bigbattery.png')
	keypic = pygame.image.load('key.png')
	coinpic = pygame.image.load('coin.png')

	for i in range(600):
		if i%100==0 and DEATHS<MAX_DEATHS:
			curr_death_x = random.randint(10,40)
			curr_death_y = i+curr_death_x
			curr_death_x = random.randint(0,190)
			death_x.append(curr_death_x)
			death_y.append(curr_death_y)
			DEATHS = DEATHS + 1
		if i%100==0 and RECHARGES<MAX_RECHARGES:
			curr_recharge_x = random.randint(10,40)
			curr_recharge_y = i+curr_recharge_x
			curr_recharge_x = random.randint(0,190)
			recharge_x.append(curr_recharge_x)
			recharge_y.append(curr_recharge_y)
			RECHARGES = RECHARGES + 1
			#print c
		
		if i==0:
			continue
		
		if i%50!=0:
			i = i-1
			continue
		temp = 0
		for j in range(2):
			curr_wall_width = 10
			curr_wall_length = random.randint(40,60)
			curr_wall_y = i
			
			if j==1:
				curr_wall_x = random.randint(temp+30,200-curr_wall_length)
			else:
				curr_wall_x = random.randint(0,100-curr_wall_length)

			wall_x.append(curr_wall_x)
			wall_y.append(curr_wall_y)
			wall_length.append(curr_wall_length)
			wall_width.append(curr_wall_width)
			temp = curr_wall_x + curr_wall_length

			
	curr_time = 0
	pygame.display.update()
	torch = False

	
	target_time = 0

	while isrunning:
		curr_time+=1
		reached_gate = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				isrunning = False
				sys.exit(0)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_z:
					pause_Screen(curr_score)
				if event.key == pygame.K_LEFT:
					dir_x_change = -1
					dir_y_change = 0
				elif event.key == pygame.K_RIGHT:
					dir_x_change = 1
					dir_y_change = 0
				elif event.key == pygame.K_UP:
					dir_y_change = -1
					dir_x_change = 0
				elif event.key == pygame.K_DOWN:
					dir_y_change = 1
					dir_x_change = 0
				elif event.key == pygame.K_SPACE:
					if battery <=0 :
						torch = False
					elif torch:
						torch = False
						target_time = curr_time + 300
					elif curr_time > target_time:
						torch = True
					print curr_time
					print target_time
					print ""


		if curr_x >= key_x and curr_x <= key_x+10 and curr_y >= key_y and curr_y<=key_y+10:
			got_key = True
		if curr_x+10 >= key_x and curr_x+10 <= key_x+10 and curr_y >= key_y and curr_y<=key_y+10:
			got_key = True
		if curr_x+10 >= key_x and curr_x+10 <= key_x+10 and curr_y+10 >= key_y and curr_y+10 <= key_y+10:
			got_key = True
		if curr_x >= key_x and curr_x <= key_x+10 and curr_y+10 >= key_y and curr_y+10 <= key_y+10:
			got_key = True

		if curr_x >= gate_x and curr_x <= gate_x+10 and curr_y >= gate_y and curr_y<=gate_y+10:
			reached_gate = True
		if curr_x+10 >= gate_x and curr_x+10 <= gate_x+10 and curr_y >= gate_y and curr_y<=gate_y+10:
			reached_gate = True
		if curr_x+10 >= gate_x and curr_x+10 <= gate_x+10 and curr_y+10 >= gate_y and curr_y+10 <= gate_y+10:
			reached_gate = True
		if curr_x >= gate_x and curr_x <= gate_x+10 and curr_y+10 >= gate_y and curr_y+10 <= gate_y+10:
			reached_gate = True



		if reached_gate and got_key:
			curr_score+=battery
			channel = doclaps.play()
			return

		for i in range(DEATHS):
			if curr_x >= death_x[i] and curr_x <= death_x[i]+10 and curr_y >= death_y[i] and curr_y<=death_y[i]+10:
				isdead = True
			if curr_x+10 >= death_x[i] and curr_x+10 <= death_x[i]+10 and curr_y >= death_y[i] and curr_y<=death_y[i]+10:
				isdead = True
			if curr_x+10 >= death_x[i] and curr_x+10 <= death_x[i]+10 and curr_y+10 >= death_y[i] and curr_y+10 <= death_y[i]+10:
				isdead = True
			if curr_x >= death_x[i] and curr_x <= death_x[i]+10 and curr_y+10 >= death_y[i] and curr_y+10 <= death_y[i]+10:
				isdead = True

		for i in range(RECHARGES):
			if curr_x >= recharge_x[i] and curr_x <= recharge_x[i]+10 and curr_y >= recharge_y[i] and curr_y<=recharge_y[i]+10:
				battery += NEW_RECHARGE
				recharge_x.remove(recharge_x[i])
				recharge_y.remove(recharge_y[i])
				RECHARGES-=1
				break;
			if curr_x+10 >= recharge_x[i] and curr_x+10 <= recharge_x[i]+10 and curr_y >= recharge_y[i] and curr_y<=recharge_y[i]+10:
				battery += NEW_RECHARGE
				recharge_x.remove(recharge_x[i])
				recharge_y.remove(recharge_y[i])
				RECHARGES-=1
				break;
			if curr_x+10 >= recharge_x[i] and curr_x+10 <= recharge_x[i]+10 and curr_y+10 >= recharge_y[i] and curr_y+10 <= recharge_y[i]+10:
				battery += NEW_RECHARGE
				recharge_x.remove(recharge_x[i])
				recharge_y.remove(recharge_y[i])
				RECHARGES-=1
				break;
			if curr_x >= recharge_x[i] and curr_x <= recharge_x[i]+10 and curr_y+10 >= recharge_y[i] and curr_y+10 <= recharge_y[i]+10:
				battery += NEW_RECHARGE
				recharge_x.remove(recharge_x[i])
				recharge_y.remove(recharge_y[i])
				RECHARGES-=1
				break;


		sound.set_volume(0.2)
		for i in range(WALLS):
			if ( (curr_x < wall_x[i]+wall_length[i] and curr_x >= wall_x[i]) or (curr_x+10 < wall_x[i]+wall_length[i] and curr_x+10 > wall_x[i]) ) and curr_y <= wall_y[i]+10 and curr_y>=wall_y[i]:
				touched_wall_lower = True
				channel = sound.play()
				sound.set_volume(0.2)

			if ( (curr_x < wall_x[i]+wall_length[i] and curr_x >= wall_x[i]) or (curr_x+10 < wall_x[i]+wall_length[i] and curr_x+10 > wall_x[i]) ) and curr_y+10 <= wall_y[i]+10 and curr_y+10 >=wall_y[i]:
				touched_wall_upper = True
				channel = sound.play()
				sound.set_volume(0.2)

			if curr_x >= wall_x[i] and curr_x <= wall_x[i]+wall_length[i] and ( (curr_y >= wall_y[i] and curr_y < wall_y[i]+wall_width[i]) or (curr_y+10 > wall_y[i] and curr_y+10 <= wall_y[i]+wall_width[i])):
				touched_wall_right = True
				channel = sound.play()
				sound.set_volume(0.2)

			if curr_x+10 >= wall_x[i] and curr_x+10 <= wall_x[i]+wall_length[i] and ( (curr_y >= wall_y[i] and curr_y < wall_y[i]+wall_width[i]) or (curr_y+10 > wall_y[i] and curr_y+10 <= wall_y[i]+wall_width[i])):
				touched_wall_left = True
				channel = sound.play()
				sound.set_volume(0.2)

		if curr_x <= 0:
			touched_wall_right = True
		if curr_x+10 >= width:
			touched_wall_left = True
		if curr_y <= 0:
			touched_wall_lower = True
		if curr_y+10 > height:
			touched_wall_upper = True

		if curr_x >= width or curr_x < 0 or curr_y < 0 or curr_y >= height:
			doexit = True

		if isdead:
			sys.exit(0)

		if touched_wall_upper and dir_y_change>0:
			curr_y = curr_y
		elif touched_wall_upper and dir_y_change<=0:
			curr_y += dir_y_change
		elif touched_wall_lower and dir_y_change<=0:
			curr_y = curr_y
		elif touched_wall_lower and dir_y_change>0:
			curr_y += dir_y_change
		if not touched_wall_upper and not touched_wall_lower:
			curr_y += dir_y_change

		if touched_wall_left and dir_x_change>0:
			curr_x = curr_x
		elif touched_wall_left and dir_x_change<=0:
			curr_x += dir_x_change
		elif touched_wall_right and dir_x_change<=0:
			curr_x = curr_x
		elif touched_wall_right and dir_x_change>0:
			curr_x += dir_x_change
		if not touched_wall_right and not touched_wall_left:
			curr_x += dir_x_change

		last_x = curr_x
		last_y = curr_y

		touched_wall_lower = False
		touched_wall_upper = False
		touched_wall_left = False
		touched_wall_right = False
 

		if not torch or battery<=0:
			screen.fill((0,0,0))
			pygame.draw.rect( screen, (255,255,255), [curr_x,curr_y,10,10] )
			
			#pygame.display.update()
			
		else:
			battery=battery-1
			screen.fill(background_color)

			for i in range(WALLS):
				pygame.draw.rect( screen, red, [wall_x[i],wall_y[i],wall_length[i],10] )

			for i in range(DEATHS):
				screen.blit(killpic, (death_x[i], death_y[i]))

			for i in range(RECHARGES):
				screen.blit(batterypic, (recharge_x[i], recharge_y[i]))
			
			if not got_key:
				screen.blit(keypic, (key_x, key_y))

			if not reached_gate:
				gate_color = red
			else:
				gate_color = green

			screen.blit(gatepic, (gate_x, gate_y))
			pygame.draw.rect( screen, man_color, [curr_x,curr_y,10,10] )
			#pygame.display.update()

		pygame.draw.rect( screen, (0,0,0), (0,580,200,120))
		screen.blit(font1.render(str(battery),True, (255,255,255)), (30,580))
		screen.blit(font1.render("Level : "+str(nlevel+1),True, (255,255,255)), (55,680))
		screen.blit(coinpic, (20, 650))
		screen.blit(font1.render(str(curr_score), True, (255,255,255)), (40, 645))
		if not got_key:
			screen.blit(font1.render("Key??",True, (255,255,255)), (80,580))
		else:
			screen.blit(font1.render("Get to the Door",True, (255,255,255)), (80,580))
		if curr_time<=target_time:
			screen.blit(font1.render("Torch will be back in : "+str(target_time - curr_time),True, (255,255,255)), (10,615))
		else:
			screen.blit(font1.render("Torch ready",True, (255,255,255)), (10,615))
		screen.blit(bigbatterypic, (8,580))
		pygame.display.update()

		clock.tick(CLOCK_TICK)
	


def main():
	start_Screen()
	for i in range(10):
		start_level(i)

if __name__ == "__main__":
	main()