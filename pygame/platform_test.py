import pygame, sys

from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((600,600), 0, 32)
pygame.display.set_caption("Me desperately trying to get a platform to move")

platform_vel = 5
x = 100
y = 150
player_x = 180
player_y = 0
rect = Rect(x, y, 200, 50)
gravity = 8
player = Rect(player_x, player_y, 50, 50)

run = True

while run:
    clock.tick(60)
    pygame.draw.rect(screen, (255, 255, 255), player)
    if rect.left >= 300 or rect.left < 100:
        platform_vel *= -1
    collide = pygame.Rect.colliderect(rect, player)
    if collide:
        player.bottom = rect.top
        player.left += platform_vel
    rect.left += platform_vel
    player.top += gravity
    pygame.draw.rect(screen, (255, 0, 0), rect)
    pygame.display.update()
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
