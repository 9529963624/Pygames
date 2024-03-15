import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

clock = pygame.time.Clock()

x = 10
y = 20
speed = pygame.Vector2(x,y)

position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dt = 0
r = 30
running = True

while running:
	screen.fill("black")
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	position += speed * dt

	circle = pygame.draw.circle(screen,  (int(position[0]%256), int(position[1]% 256), int(position[0] + position[1])% 256) , position, r)

	if position[0] > screen.get_width() - r:
		speed[0] = -x
	elif position[1] > screen.get_height() - r:
		speed[1] = -y
	elif position[0] < r:
		speed[0] = x
	elif position[1] < r:
		speed[1] = y
	pygame.display.flip()



	dt = clock.tick(60) / 100


