import pygame
from pygame.cursors import ball
import math

pygame.init()

width , height = 500, 400

screen = pygame.display.set_mode((width,height))

pygame.display.set_caption("Slingshot ball")

#colors
white = (255 , 255 ,255)
black = (0 , 0 ,0)
red = (255 , 0 , 0)


#const
FPS = 60
GRAVITY = 0.5

# SLING PROPERTIES
Slingshot_pos = (200 , height - 200)
Slingshot_redius = 20
Slingshot_length = 100

#ball properyies
ball_radius = 15
ball_color = red
ball_pos = Slingshot_pos

#sling mechaniscs veriablles
is_pulling_back=False
pull_back_distace = 0
angle = 0
pull_back_length = 100

clock = pygame.time.Clock()
running = True 

#jab mouse button reslease hoga tab


while running :
	screen.fill(white)

	#event handling 
	for event in pygame.event.get():
		if event.type== pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button ==1:
				is_pulling_back = True
		elif event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				is_pulling_back = False
				ball_speed = min(pull_back_distace , pull_back_length)
				angle_radians = math.radians(angle)
				ball_speed = (ball_speed * math.cos(angle_radians) , -ball_speed * math.sin(angle_radians))
				


	pygame.display.flip()
	clock.tick()

pygame.quit()

