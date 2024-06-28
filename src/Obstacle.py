import pygame
from setting import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type, index):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.image = self.type[index]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.speed = 16
        
        self.mask = pygame.mask.from_surface(self.image)

        self.get_point = False

    def update(self):
        self.rect.x -= self.speed 
        if self.rect.x < -200:
            all_sprites.remove(self)
            obstacles.remove(self)

