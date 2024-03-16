import pygame

stat = pygame.init()

# print(stat)

window_1 = pygame.display.set_mode((500, 500))

# apne game mein time ki bachodi na ho isliye...
clock_bahi = pygame.time.Clock()

# tuime passed between two frames..
dt = 0
speed = pygame.Vector2(0, 0)

# window khuli rakhne ke liye...
running = True

col = "white"

player_pos = pygame.Vector2(window_1.get_width() / 2, window_1.get_height() / 2)

gravity = pygame.Vector2(0 , 0.8)
damping_factor = 0.99

while running :

    window_1.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    gola = pygame.draw.circle(window_1, col, (int(player_pos.x), int(player_pos.y)), 50)

    speed.y += gravity.y
    

    player_pos += speed * dt

    if player_pos.y >= window_1.get_height() - 50:
        speed.y *= -1 * damping_factor
        
        

    # flip the screen ...
    pygame.display.flip()

    dt = clock_bahi.tick(60) / 1000
    print(dt)

pygame.quit()
