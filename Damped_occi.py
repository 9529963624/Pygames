import pygame

# Initialize Pygame
pygame.init()

# Set up the window
window_size = (500, 500)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Damped Oscillation")

# Set up clock
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball properties
ball_radius = 25
ball_pos = [window_size[0] // 2, window_size[1] // 2]
ball_speed = [0, 0]  # Initial speed
gravity = 0.5
damping_factor = 0.99

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Apply gravity
    ball_speed[1] += gravity

    # Update ball position
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Check boundaries
    if ball_pos[1] >= window_size[1] - ball_radius:
        # Reverse vertical speed and apply damping
        ball_speed[1] *= -damping_factor
        print(ball_speed[1])
        

    

    # Fill background
    window.fill(BLACK)

    # Draw ball
    pygame.draw.circle(window, WHITE, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
