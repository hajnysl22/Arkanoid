import pygame
from random import randint
import random

# Classes
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

class Ball(pygame.sprite.Sprite): 
    def __init__(self, color, screen_width, screen_height):
        super().__init__()
        transparent = (0,0,0)

        self.image = pygame.Surface([screen_width, screen_height])
        self.image.fill(transparent)
        self.image.set_colorkey(transparent)
 
        pygame.draw.ellipse(self.image, color, [0, 0, screen_width, screen_height])
        
        self.speed = [7 * random.choice((1,-1)),7]

        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
          
    def bounce(self):
        self.speed[0] = -self.speed[0]
        self.speed[1] = random.choice((-7,7))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        transparent = (0,0,0)

        self.image = pygame.Surface([width, height])
        self.image.fill(transparent)
        self.image.set_colorkey(transparent)
 
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

# Setup
pygame.init()

# Game Colors
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)
row1_color = (88, 24, 69)
row2_color = (144, 12, 63)
row3_color = (199, 0 , 57)
row4_color = (255, 87, 51)
row5_color = (255, 195, 0)

# Game Variables
screen_width = 500
screen_height = 1000
game_active = True
score = 0
lives = 3

# Game Window
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Arkanoid")

# Game Font
font = pygame.font.Font('Pixeltype.ttf', 35)

# All sprite group
all_enemy_list = pygame.sprite.Group()

# Block
block = Block(light_grey, 100, 15)
block.rect.x = screen_width / 2 - 40
block.rect.y = 900

# Ball
ball = Ball(light_grey,20,20)
ball.rect.x = 250
ball.rect.y = 880

enemy_blocks = pygame.sprite.Group()
for i in range(5):
    enemy = Enemy(row1_color,85,15)
    enemy.rect.x = 13 + i* 95
    enemy.rect.y = 60
    all_enemy_list.add(enemy)
    enemy_blocks.add(enemy)
for i in range(5):
    enemy = Enemy(row2_color,85,15)
    enemy.rect.x = 13 + i* 95
    enemy.rect.y = 110
    all_enemy_list.add(enemy)
    enemy_blocks.add(enemy)
for i in range(5):
    enemy = Enemy(row3_color,85,15)
    enemy.rect.x = 13 + i* 95
    enemy.rect.y = 160
    all_enemy_list.add(enemy)
    enemy_blocks.add(enemy)
for i in range(5):
    enemy = Enemy(row4_color,85,15)
    enemy.rect.x = 13 + i* 95
    enemy.rect.y = 210
    all_enemy_list.add(enemy)
    enemy_blocks.add(enemy)
for i in range(5):
    enemy = Enemy(row5_color,85,15)
    enemy.rect.x = 13 + i* 95
    enemy.rect.y = 260
    all_enemy_list.add(enemy)
    enemy_blocks.add(enemy)


# FPS
clock = pygame.time.Clock()

# Adding block + ball to list
all_enemy_list.add(block)
all_enemy_list.add(ball)

# Game Loop
while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        block.moveLeft(4)
    if keys[pygame.K_RIGHT]:
        block.moveRight(4)

    # Game Logic 
    all_enemy_list.update()

    

    if ball.rect.x>=480:
        ball.speed[0] *= -1
    if ball.rect.x<=0:
        ball.speed[0] = -ball.speed[0]
    if ball.rect.y>screen_height:
        ball.speed[1] = -ball.speed[1]
        lives -= 1

        # Game Over
        if lives == 0:
            game_over_font = pygame.font.Font('Pixeltype.ttf', 100)
            text = game_over_font.render("GAME OVER", 1, light_grey)
            screen.blit(text, (100,500))
            pygame.display.flip()
            pygame.time.wait(3000)
            game_active = False
            
    if ball.rect.y<40:
        ball.speed[1] = -ball.speed[1]

    # Ball bounce
    if pygame.sprite.collide_mask(ball, block):
        ball.rect.x -= ball.speed[0]
        ball.rect.y -= ball.speed[1]
        ball.bounce()

    enemy_collision_list = pygame.sprite.spritecollide(ball,enemy_blocks,False)
    for enemy in enemy_collision_list:
      ball.bounce()
      score += 1
      enemy.kill()
      if len(enemy_blocks) == 0:
            victory_royale_font = pygame.font.Font('Pixeltype.ttf', 100)
            text = victory_royale_font.render("You Won!", 1, light_grey)
            screen.blit(text, (100,500))
            pygame.display.flip()
            pygame.time.wait(3000)
            game_active = False

    # Screen visualizer
    screen.fill(bg_color)
    pygame.draw.line(screen, light_grey, [0, 38], [800, 38], 2)

    # Score
    text = font.render("Score: " + str(score), 1, light_grey)
    screen.blit(text, (20,10))

    text = font.render("Lives: " + str(lives), 1, light_grey)
    screen.blit(text, (400,10))

    # Block + Ball Visualizer
    all_enemy_list.draw(screen)

    # Updating
    pygame.display.flip()
    clock.tick(60)
