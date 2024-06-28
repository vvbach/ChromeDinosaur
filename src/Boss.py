import pygame
import os
from setting import *


RUNNING_DINO_BOSS_LEFT = [pygame.image.load(os.path.join("Assets/Boss/Boss_1", "boss1_1.png")),
                          pygame.image.load(os.path.join("Assets/Boss/Boss_1", "boss1_2.png"))]

RUNNING_DINO_BOSS_RIGHT = [pygame.image.load(os.path.join("Assets/Boss/Boss_1", "boss1_3.png")),
                           pygame.image.load(os.path.join("Assets/Boss/Boss_1", "boss1_4.png"))]

TIRED_DINO_BOSS_LEFT = [pygame.image.load(os.path.join("Assets/Boss/Boss_1", "Boss_Tired_1.png")),
                        pygame.image.load(os.path.join("Assets/Boss/Boss_1", "Boss_Tired_2.png"))]

TIRED_DINO_BOSS_RIGHT = [pygame.image.load(os.path.join("Assets/Boss/Boss_1", "Boss_Tired_3.png")),
                        pygame.image.load(os.path.join("Assets/Boss/Boss_1", "Boss_Tired_4.png"))]

FLYING_DINO_BOSS_LEFT = pygame.image.load(os.path.join("Assets/Boss/Boss_2", "boss2_1.png"))

FLYING_DINO_BOSS_RIGHT = pygame.image.load(os.path.join("Assets/Boss/Boss_2", "boss2_2.png"))

DROPPED_ROCK = pygame.image.load(os.path.join("Assets/Boss/Boss_2", "dropped_rock.png"))


class RunningDinoBoss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.state = "left"
        self.end = False
        self.index = 0
        self.vec = 14
        self.speed = self.vec
        self.get_point = False

        self.image = RUNNING_DINO_BOSS_LEFT[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = 240

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.state == "left": 
            self.speed = -self.vec
            self.image = RUNNING_DINO_BOSS_LEFT[self.index // 5]
            
        elif self.state == "right": 
            self.speed = self.vec
            self.image = RUNNING_DINO_BOSS_RIGHT[self.index // 5]

        self.index += 1
        if self.index >= 10: self.index = 0

        if self.rect.x < -120: 
            self.state = "right"
            self.get_point = False
        elif self.rect.x > 1320: 
            if self.speed < 17: self.vec += 1
            self.state = "left"
            self.get_point = False

        if self.end:  
            self.rect.x -= 20

            if self.state == "left": self.image = TIRED_DINO_BOSS_LEFT[self.index // 5]
            else: self.image = TIRED_DINO_BOSS_RIGHT[self.index // 5]

            self.mask.clear()
            obstacles.remove(self)

            if self.rect.x <= -120:
                all_sprites.remove(self)
                
        else: self.rect.x += self.speed

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = DROPPED_ROCK
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 114
        self.type = "rock"
        self.get_point = True

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += 10
        
            

class FlyingBoss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.state = "left"
        self.end = False
        self.index = 0
        self.speed = 20

        self.image = FLYING_DINO_BOSS_LEFT
        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = 10

        self.type = "boss"
        self.time = 50

        self.mask = pygame.mask.from_surface(self.image)

    def drop_rock(self, player):
        if self.time > 0: self.time -= 1
        elif player.rect.x >= self.rect.x and player.rect.x + 94 <= self.rect.x + 208:
            bullet = Bullet(player.rect.x + player.image.get_width() / 2)
            all_sprites.add(bullet)
            obstacles.add(bullet)
            self.time = 50
        

    def update(self):
        if self.state == "left": 
            self.speed = -20
            self.image = FLYING_DINO_BOSS_LEFT
            
        elif self.state == "right": 
            self.speed = 20
            self.image = FLYING_DINO_BOSS_RIGHT

        if self.rect.x < 0: 
            self.state = "right"
            self.get_point = False
        elif self.rect.x > 1000: 
            self.state = "left"
            self.get_point = False

        if self.end:  
            self.rect.x -= 20

            self.mask.clear()
            obstacles.remove(self)

            if self.rect.x <= -120:
                all_sprites.remove(self)

        else: self.rect.x += self.speed

        
def spawn_boss(x):
    if x == 1:
        boss = RunningDinoBoss()
        all_sprites.add(boss)
        obstacles.add(boss)
    elif x == 2:
        boss = FlyingBoss()
        all_sprites.add(boss)
        obstacles.add(boss)

    