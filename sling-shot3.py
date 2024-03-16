import pygame
import math

from pygame.draw import circle

pygame.init()

width, height = 500, 400

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Slingshot ball")

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


# const
FPS = 60
GRAVITY = 0.5

# SLING PROPERTIES
Slingshot_pos = (200, height - 200)
Slingshot_redius = 20
Slingshot_length = 100

# ball properyies
ball_radius = 15
ball_color = red
ball_pos = Slingshot_pos

# sling mechaniscs veriablles
is_pulling_back = False
pull_back_distace = 0
angle = 0
pull_back_length = 100

clock = pygame.time.Clock()
running = True

ball_velocity = (0, 0)

# jab mouse button reslease hoga tab

while running:
    screen.fill(white)

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                is_pulling_back = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                is_pulling_back = False
                ball_speed = -min(pull_back_distace, pull_back_length)
                angle_radians = math.radians(angle)
                ball_velocity = (
                    ball_speed * math.cos(angle_radians),
                    -ball_speed * math.sin(angle_radians),
                )
                ball_velocity =(
                    Slingshot_pos[0]
                    + pull_back_distace
                    * math.cos(math.radians(angle)),
                    Slingshot_pos[1]
                    + pull_back_distace
                    * math.sin(math.radians(angle)),
                )
                pull_back_distace=0
    

        if is_pulling_back:
            mouse_pos = pygame.mouse.get_pos()
            pull_back_distace = min(
                (
                    math.sqrt(
                        (mouse_pos[0] - Slingshot_pos[0]) ** 2
                        + (mouse_pos[1] - Slingshot_pos[1]) ** 2
                    )
                ),
                pull_back_length,
            )
            angle = math.degrees(
                math.atan2(
                    Slingshot_pos[1] - mouse_pos[1],
                    Slingshot_pos[0] - mouse_pos[0],
                )
            )

    pygame.draw.circle(screen, black, Slingshot_pos, Slingshot_redius)
    pygame.draw.line(
        screen,
        black,
        Slingshot_pos,
        (
            Slingshot_pos[0]
            + pull_back_distace
            * math.cos(math.radians(angle)),
            Slingshot_pos[1]
            + pull_back_distace
            * math.sin(math.radians(angle)),
        ),
        2,
    )

    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

    try:
        ball_pos = (
            ball_pos[0] + ball_velocity[0],
            ball_pos[1] + ball_velocity[1],
        )
        ball_velocity = (
            ball_velocity[0],
            ball_velocity[1] + GRAVITY,
        )
    except UnboundLocalError:
        pass

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
