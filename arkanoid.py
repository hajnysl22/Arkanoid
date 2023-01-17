import pygame

# Setup
pygame.init()

screen_width = 500
screen_height = 1000

# Game Window
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Arkanoid")

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()