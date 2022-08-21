import pygame, sys
from settings import *
from level import Level

pygame.init()

# setting up the game window
WIN = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Super Mario')


level = Level(level_map, WIN)

clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
            
    WIN.fill('black')
    level.run()
    pygame.display.update()

    clock.tick(60)