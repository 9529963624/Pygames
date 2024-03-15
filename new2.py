
import pygame

stat = pygame.init()

# print(stat)

window_1 = pygame.display.set_mode((500,500))

#apne game mein time ki bachodi na ho isliye...
clock_bahi = pygame.time.Clock()

#tuime passed between two frames..
dt = 0
speed = pygame.Vector2(70 , 100)

#window khuli rakhne ke liye...
running = True

col = "white"

player_pos = pygame.Vector2(window_1.get_width()/2, window_1.get_height()/2)

while running:

	window_1.fill("black")

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	player_pos += speed * dt
	gola = pygame.draw.circle(window_1,col,player_pos,50)

	
	if player_pos.y >= window_1.get_height() -50 :
		speed.y *= -1
		col = "Green"
	elif player_pos.y <= 50 :
		speed.y *= -1
		col = "Blue"
	elif player_pos.x >= window_1.get_height() -50 :
		speed.x *= -1
		col = "red"
	elif player_pos.x <= 50 :
		speed.x *= -1
		col = "yellow"

	# keys = pygame.key.get_pressed()
	# if keys[pygame.K_w]:
	# 	player_pos.y -= 300 * dt
	# if keys[pygame.K_s]:
	# 	player_pos.y += 300 * dt
	# if keys[pygame.K_a]: 
	# 	player_pos.x -= 300*dt
	# if keys[pygame.K_d]:
	# 	player_pos.x += 300*dt


	if player_pos.x >= (window_1.get_width() + (50)):
		player_pos.x = 0 - 50
	

	# if keys[pygame.K_q]:
	# 	# quit()
	# 	running = False # or we can do  this


	#flip the screen ...
	pygame.display.flip()

	dt = clock_bahi.tick(60)/1000
	print(dt)
	
pygame.quit()