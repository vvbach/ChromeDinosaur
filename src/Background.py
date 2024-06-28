import pygame
import os
from setting import *

BG_D = [pygame.image.load(os.path.join("Assets/Desert/Background", "Background_0.png")),
      pygame.image.load(os.path.join("Assets/Desert/Background", "Background_1.png")),
      pygame.image.load(os.path.join("Assets/Desert/Background", "Background_2.png")),
      pygame.image.load(os.path.join("Assets/Desert/Background", "Background_3.png")),
      pygame.image.load(os.path.join("Assets/Desert/Background", "Background_4.png")),
      pygame.image.load(os.path.join("Assets/Desert/Background", "Background_5.png"))]

BG_J = [pygame.image.load(os.path.join("Assets/Jungle/Background", "Background_0.png")),
      pygame.image.load(os.path.join("Assets/Jungle/Background", "Background_1.png")),
      pygame.image.load(os.path.join("Assets/Jungle/Background", "Background_2.png")),
      pygame.image.load(os.path.join("Assets/Jungle/Background", "Background_3.png")),
      pygame.image.load(os.path.join("Assets/Jungle/Background", "Background_4.png")),
      pygame.image.load(os.path.join("Assets/Jungle/Background", "Background_5.png"))]

BG_L = [pygame.image.load(os.path.join("Assets/Lava", "Background_0.png")),
      pygame.image.load(os.path.join("Assets/Lava", "Background_1.png")),
      pygame.image.load(os.path.join("Assets/Lava", "Background_2.png")),
      pygame.image.load(os.path.join("Assets/Lava", "Background_3.png")),
      pygame.image.load(os.path.join("Assets/Lava", "Background_4.png")),
      pygame.image.load(os.path.join("Assets/Lava", "Background_5.png"))]

BG_BOSS = [pygame.image.load(os.path.join("Assets/Boss/Background", "Background_0.png")),
           pygame.image.load(os.path.join("Assets/Boss/Background", "Background_1.png")),
           pygame.image.load(os.path.join("Assets/Boss/Background", "Background_2.png")),
           pygame.image.load(os.path.join("Assets/Boss/Background", "Background_3.png")),
           pygame.image.load(os.path.join("Assets/Boss/Background", "Background_4.png")),
           pygame.image.load(os.path.join("Assets/Boss/Background", "Background_5.png"))]

GR = pygame.image.load(os.path.join("Assets/Desert/Background", "Ground.png"))

class Background(pygame.sprite.Sprite):
    def __init__(self, x, index):
        pygame.sprite.Sprite.__init__(self)
        self.index = index
        self.biome = BG_D
        self.image = self.biome[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0

    def update(self):
        self.rect.x -= background_speed
        if self.rect.x < - self.image.get_width():
            self.rect.x = self.image.get_width() - 10
            self.index += 2
            self.image = self.biome[self.index % 6]


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = GR
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 380

