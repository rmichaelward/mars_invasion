import pygame
from pygame.locals import *
import os
import random
import player_ship

pygame.init()

W, H = 256, 500
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Mars Invasion')

bg = pygame.image.load(os.path.join('images', "desert-backgorund-looped.png")).convert()
bgY = 0
bgY2 = bg.get_height() * -1

clock = pygame.time.Clock()

def redrawWindow():
    largeFont = pygame.font.SysFont('comicsans', 30)
    win.blit(bg, (0, bgY))
    win.blit(bg, (0, bgY2))
    player_ship.draw(win)
    # add later text = largeFont.render('Score: ' + str(score), 1, (255,255,255))

    # add later win.blit(text, (700, 10))
    pygame.display.update()

player_ship = player_ship.player(128, 490, 74, 56)
speed = 60


score = 0

run = True

pause = 0

while run:
    redrawWindow()
    bgY += 1.4
    bgY2 += 1.4
    if bgY > bg.get_height() :
        bgY = bg.get_height() * -1
    if bgY2 > bg.get_height() :
        bgY2 = bg.get_height() * -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

    if pause > 0:
        pause += 1
        if pause > fallSpeed * 2:
            endScreen()

    score = speed//10 - 3
    clock.tick(speed)

