import pygame
import os
from pygame.sprite import Sprite

class player(Sprite):
    image = [pygame.image.load(os.path.join('images', 'sprite_pack_1', 'PNG', 'playerShip1_red.png'))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))