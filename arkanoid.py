import pygame

# Class
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        transparent = (0,0,0)
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(transparent)
        self.image.set_colorkey(transparent)
 
        pygame.draw.rect(self.image, color, [0, 0, width, height])
 
        self.rect = self.image.get_rect()
 
    def moveLeft(self, position):
        self.rect.x -= position
        if self.rect.x <= 0:
          self.rect.x = 0
 
    def moveRight(self, position):
        self.rect.x += position
        if self.rect.x >= 400:
          self.rect.x = 400

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

# All sprite group
all_enemy_list = pygame.sprite.Group()

# Block
block = Block(light_grey, 100, 15)
block.rect.x = screen_width / 2 - 40
block.rect.y = 900

# FPS
clock = pygame.time.Clock()

# Adding block to list
all_enemy_list.add(block)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        block.moveLeft(4)
    if keys[pygame.K_RIGHT]:
        block.moveRight(4)

    # Screen visualizer
    screen.fill(bg_color)
    pygame.draw.line(screen, light_grey, [0, 38], [800, 38], 2)

    # Block Visualizer
    all_enemy_list.draw(screen)

    # Updating
    pygame.display.flip()
    clock.tick(60)