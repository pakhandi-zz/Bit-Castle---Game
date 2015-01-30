import pygame
import sys
import random
from Tkinter import *

pygame.init()
pygame.display.init()

background_color = (255,255,255) #White
man_color = (0,0,0)
wall_color = (240,150,0)
red = (255,0,0)
green = (0, 155, 0)
gate_color = (255,0,0)
grey = (128,128,128)
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
initial_charge_array = [  700  ,  700  ,  700  ,  700  ,  400  ,  400  ,  400  ,  400  ,  300  ,  300  ,  100 ]
clock_tick_array =     [  80   ,  70   ,  70   ,  50   ,  50   ,  50   ,  50   ,  50   ,  50   ,  50   ,  50  ]
new_recharge_array =   [  140  ,  130  ,  100  ,  100  ,  120  ,  120  ,  130  ,  130  ,  150  ,  150  ,  100 ]
max_deaths_array =     [  2    ,  3    ,  4    ,  4    ,  6    ,  6    ,  6    ,  6    ,  6    ,  6    ,  10  ]
max_recharges_array =  [  6    ,  6    ,  6    ,  6    ,  6    ,  6    ,  5    ,  5    ,  4    ,  4    ,  4   ]
dead_time_array =      [  1800 ,  1500 ,  1500 ,  1200 ,  1200 ,  1100 ,  1100 ,  1000 ,  1000 ,  800  ,  800 ]

global DEATHS
global RECHARGES

global gate_x
global gate_y
global reached_gate

global doexit
global isrunning

global curr_score
curr_score = 0

global DELAY
DELAY = 300

global EXTRA_CHARGE
EXTRA_CHARGE = 0

global INITIAL_CHARGE, NEW_RECHARGE, CLOCK_TICK

def init_game():
	global DELAY, EXTRA_CHARGE, curr_score
	DELAY =300
	EXTRA_CHARGE = 0
	curr_score = 0
	return

def rules():
	screen1 = pygame.display.set_mode((width+800, height))
	font1 = pygame.font.SysFont('comicsansms', 18)
	font2 = pygame.font.SysFont('comicsansms', 30)
	font3 = pygame.font.SysFont('comicsansms', 20)
	pygame.display.set_caption("Bit Castle")
	screen1.fill(background_color)

	batterypic = pygame.image.load('battery.png')
	killpic = pygame.image.load('kill.png')
	gatepic = pygame.image.load('door.png')
	bigbatterypic = pygame.image.load('bigbattery.png')
	keypic = pygame.image.load('key.png')
	coinpic = pygame.image.load('coin.png')

	isrunning = True
	while isrunning:
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			sys.exit(0)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				isrunning = False
				return
		screen1.fill(background_color)
		screen1.blit(font2.render("Rules & Controls", True, green), (380,50))
		screen1.blit(font1.render("Press R to Return",True, (0,0,0)), (420,100))
		screen1.blit(font1.render("1>  Goal of the game is to reach the door in each level.", True, (0,0,0)), ( 10 , 140 ))
		screen1.blit(font1.render("2>  Each level is completed only when the player reaches the gate with the Key.", True, (0,0,0)), ( 10 , 170 ))
		screen1.blit(font1.render("3>  Without taking the key, the level won't be over.", True, (0,0,0)), ( 10 , 200 ))
		screen1.blit(font1.render("4>  You have got a torch, it'll make it possible for you to see the objects in a level.", True, (0,0,0)), ( 10 , 230 ))
		screen1.blit(font1.render("5>  The torch can be turned OFF or ON using Space-Bar.", True, (0,0,0)), ( 10 , 260 ))
		screen1.blit(font1.render("6>  When the torch is OFF, you can only see yourself and nothing else.", True, (0,0,0)), ( 10 , 290 ))
		screen1.blit(font1.render("7>  If the battery of the torch runs out, the torch is put-off automatically.", True, (0,0,0)), ( 10 , 320 ))
		screen1.blit(font1.render("8>  If you decide to put OFF the torch, the torch can be put back ON after a certain amout of time ONLY.", True, (0,0,0)), ( 10 , 350 ))
		screen1.blit(font1.render("9>  There are some 'red' colored crosses, touching them will kill you instantaneously.", True, (0,0,0)), ( 10 , 380 ))
		screen1.blit(font1.render("10>  There are some 'green' colored batteries, touching them will recharge your torch batteries a little.", True, (0,0,0)), ( 10 , 410 ))
		screen1.blit(font1.render("11>  You have to reach the gate in a certain amount of time, else the Game Is Over.", True, (0,0,0)), ( 10 , 440 ))
		screen1.blit(font1.render("12>  After every level, you can visit the store and buy some boosts to help you in coming levels.", True, (0,0,0)), ( 10 , 470 ))
		screen1.blit(font1.render("13>  The left-over battery charge will be converted to coins at the end of any level.", True, (0,0,0)), ( 10 , 500 ))
		screen1.blit(font1.render("14>  Press Z to PAUSE.", True, (0,0,0)), ( 10 , 530 ))
		screen1.blit(gatepic, (10, 570))
		screen1.blit(font1.render("The door", True, (0,0,0)), (30, 560))
		screen1.blit(killpic, (10, 590))
		screen1.blit(font1.render("Death", True, (0,0,0)), (30, 580))
		screen1.blit(batterypic, (10, 610))
		screen1.blit(font1.render("Recharge", True, (0,0,0)), (30, 600))
		pygame.display.update()
				
		
def start_Screen():
	init_game()
	
	isrunning = True
	while isrunning:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					screen.fill(background_color)
					return
				if event.key == pygame.K_r:
					rules()
		screen = pygame.display.set_mode((width, height))
		font1 = pygame.font.SysFont('comicsansms', 15)
		font2 = pygame.font.SysFont('comicsansms', 30)
		pygame.display.set_caption("Bit Castle V-1.0.0")
		screen.fill(background_color)
		screen.blit(font2.render( "Bit Castle", True, green), (35,100) )
		screen.blit(font1.render( "Press P to Play",True, (0,0,0)), (50,200))
		screen.blit(font1.render( "Press R for Rules & Controls",True, (0,0,0)), (2,250))
		screen.blit(font1.render( "By -- Asim Krishna Prasad",True, (0,0,0)), (10,320))
		pygame.display.flip()

def pause_Screen(curr_score):
	screen = pygame.display.set_mode((width, height))
	font1 = pygame.font.SysFont('comicsansms', 15)
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

global PLAYER,  entry2, input2


def get_log_var(w1):
	global PLAYER
	PLAYER = entry2.get()
	#print PLAYER
	#destroyit(w1)
	#w1.destroy()
	return

def get_log_var2(event):
	global w1
	global PLAYER
	PLAYER = entry2.get()
	#print PLAYER
	#destroyit(w1)
	w1.destroy()
	return

def getusername():
	global w1
	w1 = Tk()

	w1.title("Bit Castle")
	w1.geometry("300x100+350+120")

	global entry2
	global input2

	label2 = Label(w1,text="Enter your Name : ", height=2)
	label2.grid(row=4, column=4)

	input2 = StringVar()
	entry2 = Entry(w1, textvariable = input2)
	btndec = Button(w1, text="Submit", command=lambda : get_log_var(w1))
	
	#btndec['get_log_var(w1)'] = w1.destroy()
	entry2.grid(row=4, column=7 )
	btndec.grid(row=5, column=5)
	entry2.bind("<Return>", get_log_var2)
	entry2.focus_set()
	w1.mainloop()

def gameover_Screen():
	global curr_score
	global DELAY
	global EXTRA_CHARGE
	global PLAYER

	length = len(PLAYER)
	length = length * 13
	spaces = 400 - length
	start_x = spaces/2

	screen = pygame.display.set_mode((width+200, height))
	font1 = pygame.font.SysFont('comicsansms', 15)
	font2 = pygame.font.SysFont('comicsansms', 30)
	font3 = pygame.font.SysFont('comicsansms', 20)
	pygame.display.set_caption("Bit Castle")
	screen.fill(background_color)
	
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
		screen.fill(background_color)
		screen.blit(font2.render("Bit Castle", True, green), (148,100))
		screen.blit(font2.render("Congrats", True, (37,14,182)), (150, 150))
		screen.blit(font2.render(PLAYER, True, green), (start_x, 200))
		coinpic = pygame.image.load('coin.png')
		screen.blit(coinpic, (190, 265))
		screen.blit(font1.render(str(curr_score), True, (0,0,0)), (210,260))
		
		screen.blit(font1.render("Take a snapshot and share it on fb.com/bugecode", True, (0,0,0)), (25, 300))
		screen.blit(font1.render("Press Z to Start Again", True, (0,0,0)), (140, 350))
		pygame.display.update()


def start_level(nlevel):

	if nlevel >= 10:
		ind = 10
	else:
		ind = nlevel
	#sound = pygame.mixer.Sound("c.wav")
	#doclaps = pygame.mixer.Sound("claps.wav")

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
	global EXTRA_CHARGE

	INITIAL_CHARGE = initial_charge_array[ind]
	INITIAL_CHARGE += EXTRA_CHARGE
	battery = INITIAL_CHARGE

	isdead = False

	CLOCK_TICK = clock_tick_array[ind]
	NEW_RECHARGE = new_recharge_array[ind]

	MAX_DEATHS = max_deaths_array[ind]
	MAX_RECHARGES = max_recharges_array[ind]
	
	global DELAY

	font1 = pygame.font.SysFont('comicsansms', 15)


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
	#print key_x
	#print key_y

	global curr_score

	


	global DEATHS
	DEATHS = 0
	global RECHARGES
	RECHARGES = 0

	curr_x = 90
	curr_y = 570
	last_x = 90
	last_y = 590
	dir_x_change = 0
	dir_y_change = 0

	touched_wall_lower = False
	touched_wall_upper = False
	touched_wall_right = False
	touched_wall_left = False

	clock = pygame.time.Clock()

	batterypic = pygame.image.load('battery.png')
	killpic = pygame.image.load('kill.png')
	gatepic = pygame.image.load('door.png')
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
			if nlevel > 9 and DEATHS < MAX_DEATHS:
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
						target_time = curr_time + DELAY
					elif curr_time > target_time:
						torch = True
					#print curr_time
					#print target_time
					#print ""


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
			#getusername()
			#gameover_Screen()
			#channel = doclaps.play()
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


		#sound.set_volume(0.2)
		for i in range(WALLS):
			if ( (curr_x < wall_x[i]+wall_length[i] and curr_x >= wall_x[i]) or (curr_x+10 < wall_x[i]+wall_length[i] and curr_x+10 > wall_x[i]) ) and curr_y <= wall_y[i]+10 and curr_y>=wall_y[i]:
				touched_wall_lower = True
				#channel = sound.play()
				#sound.set_volume(0.2)

			if ( (curr_x < wall_x[i]+wall_length[i] and curr_x >= wall_x[i]) or (curr_x+10 < wall_x[i]+wall_length[i] and curr_x+10 > wall_x[i]) ) and curr_y+10 <= wall_y[i]+10 and curr_y+10 >=wall_y[i]:
				touched_wall_upper = True
				#channel = sound.play()
				#sound.set_volume(0.2)

			if curr_x >= wall_x[i] and curr_x <= wall_x[i]+wall_length[i] and ( (curr_y >= wall_y[i] and curr_y < wall_y[i]+wall_width[i]) or (curr_y+10 > wall_y[i] and curr_y+10 <= wall_y[i]+wall_width[i])):
				touched_wall_right = True
				#channel = sound.play()
				#sound.set_volume(0.2)

			if curr_x+10 >= wall_x[i] and curr_x+10 <= wall_x[i]+wall_length[i] and ( (curr_y >= wall_y[i] and curr_y < wall_y[i]+wall_width[i]) or (curr_y+10 > wall_y[i] and curr_y+10 <= wall_y[i]+wall_width[i])):
				touched_wall_left = True
				#channel = sound.play()
				#sound.set_volume(0.2)

		if curr_x <= 0:
			touched_wall_right = True
		if curr_x+10 >= width:
			touched_wall_left = True
		if curr_y <= 0:
			touched_wall_lower = True
		if curr_y+10 > 580:
			touched_wall_upper = True

		if curr_x >= width or curr_x < 0 or curr_y < 0 or curr_y >= height:
			doexit = True

		if curr_time > dead_time_array[ind]:
			isdead = True

		if isdead:
			getusername()
			gameover_Screen()
			main()
			#start_Screen()

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
		screen.blit(coinpic, (20, 645))
		screen.blit(font1.render(str(curr_score), True, (255,255,255)), (40, 640))
		if not got_key:
			screen.blit(font1.render("Key??",True, (255,255,255)), (80,580))
		else:
			screen.blit(font1.render("Get to the Door",True, (255,255,255)), (80,580))
		if curr_time<=target_time:
			screen.blit(font1.render("Torch will be back in : "+str(target_time - curr_time),True, (255,255,255)), (10,615))
		else:
			screen.blit(font1.render("Torch ready",True, (255,255,255)), (10,615))
		screen.blit(font1.render("Time Left : "+str(dead_time_array[ind] - curr_time), True, (255,255,255)), (30, 660))
		screen.blit(bigbatterypic, (8,580))
		pygame.display.update()

		clock.tick(CLOCK_TICK)
	
def store():
	global curr_score
	global DELAY
	global EXTRA_CHARGE

	screen = pygame.display.set_mode((width+200, height))
	font1 = pygame.font.SysFont('comicsansms', 20)
	font2 = pygame.font.SysFont('comicsansms', 30)
	font3 = pygame.font.SysFont('comicsansms', 20)
	font4 = pygame.font.SysFont('comicsansms', 15)
	pygame.display.set_caption("Bit Castle")
	screen.fill(background_color)
	
	
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
				if curr_score >= 1200:
					if event.key == pygame.K_1:
						curr_score-=1200
						DELAY -= 20
				if curr_score >= 800:
					if event.key == pygame.K_2:
						curr_score -= 800
						EXTRA_CHARGE += 25
				if curr_score >= 1200:
					if event.key == pygame.K_3:
						curr_score -= 1200
						EXTRA_CHARGE += 50
		screen.fill(background_color)
		screen.blit(font4.render("You have extra charge of : "+str(EXTRA_CHARGE), True, green), (10,40))
		screen.blit(font4.render("You have reduced delay by : "+str(300-DELAY), True, green), (10,60))
		screen.blit(font2.render("STORE", True, green), (148,100))
		screen.blit(font1.render("Press Z to Resume",True, (0,0,0)), (130,200))
		coinpic = pygame.image.load('coin.png')
		screen.blit(coinpic, (160, 245))
		screen.blit(font1.render(str(curr_score), True, (0,0,0)), (180,240))

		if curr_score < 1200:
			screen.blit(font3.render("1> Reduce Torch Lag by 20", True, grey), (10, 280) )
		else:
			screen.blit(font3.render("1> Reduce Torch Lag by 20", True, green), (10, 280) )

		screen.blit(coinpic, (330, 288))
		screen.blit(font1.render("1200", True, (0,0,0)), (350, 282))

		if curr_score < 800:
			screen.blit(font3.render("2> Increase initial battery by 25", True, grey), (10, 310) )
		else:
			screen.blit(font3.render("2> Increase initial battery by 25", True, green), (10, 310) )

		screen.blit(coinpic, (330, 318))
		screen.blit(font1.render("800", True, (0,0,0)), (350, 312))

		if curr_score < 1200:
			screen.blit(font3.render("3> Increase initial battery by 50", True, grey), (10, 340) )
		else:
			screen.blit(font3.render("3> Increase initial battery by 50", True, green), (10, 340) )

		screen.blit(coinpic, (330, 348))
		screen.blit(font1.render("1200", True, (0,0,0)), (350, 342))

		pygame.display.update()


def main():
	#getusername()
	#gameover_Screen()
	start_Screen()
	for i in range(100):
		start_level(i)
		store()

if __name__ == "__main__":
	main()