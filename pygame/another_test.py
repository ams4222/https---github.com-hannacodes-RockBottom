import pygame, sys
from pygame.locals import *
from settings import *
from tiles import Tile
from level import Level

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Another Test")
mainClock = pygame.time.Clock()

level = Level(level_map, screen)
test_tile = pygame.sprite.Group(Tile((100, 100), 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    level.run()
    pygame.display.update()
    mainClock.tick(60)