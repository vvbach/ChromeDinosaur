import random
import pygame
import os
from setting import *
from Obstacle import *

HOLE = [pygame.image.load(os.path.join("Assets/Lava", "hole.png"))]

class Hole(Obstacle):
    def __init__(self):
        super().__init__(HOLE, 0)
        self.rect.y = 378



def spawn_hole():
    hole = Hole()
    all_sprites.add(hole)
    obstacles.add(hole)

