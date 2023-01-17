import pygame

# Setup
pygame.init()

# Game Colors
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

# Game Variables
screen_width = 500
screen_height = 1000

# Game Window
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Arkanoid")

# FPS
clock = pygame.time.Clock()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Screen visualizer
    screen.fill(bg_color)
    pygame.draw.line(screen, light_grey, [0, 38], [800, 38], 2)

    # Updating
    pygame.display.flip()
    clock.tick(60)