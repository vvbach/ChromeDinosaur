import pygame
import os
from pygame.sprite import collide_mask
from Background import *
from setting import *



RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        self.move_left = False
        self.move_right = False

        self.lose = False
        self.X_POS = 80
        self.Y_POS = 310
        self.Y_POS_DUCK = 340
        self.JUMP_VEL = 8.5

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.gravity = 0.8
        self.image = self.run_img[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

        self.mask = pygame.mask.from_surface(self.image)

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index += 1
        
        self.gravity = 0.8

    def jump(self):
        self.image = self.jump_img
        self.rect.x = self.X_POS
        if self.dino_jump:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= self.gravity
        if self.jump_vel < - self.JUMP_VEL or self.rect.y > self.Y_POS:
            self.dino_jump = False
            self.dino_run = True
            self.jump_vel = self.JUMP_VEL

    def control(self, event, state):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not self.dino_jump:
                self.dino_duck = False
                self.dino_run = False
                self.dino_jump = True
            if event.key == pygame.K_DOWN and not self.dino_jump:
                self.dino_duck = True
                self.dino_run = False
                self.dino_jump = False
            if event.key == pygame.K_DOWN and self.dino_jump:
                if self.jump_vel > 0:
                    self.jump_vel = 0
                self.gravity = 2.5
            if state == "BOSS":
                if event.key == pygame.K_RIGHT:
                    self.move_right = True
                if event.key == pygame.K_LEFT:
                    self.move_left = True
            
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT: self.move_left = False
            if event.key == pygame.K_RIGHT: self.move_right = False    
            if not self.dino_jump:
                self.dino_duck = False
                self.dino_run = True
                self.dino_jump = False
            

    def update(self):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.move_left:
            if self.X_POS > 0: self.X_POS += -6
        if self.move_right:
            if self.X_POS < 1000 :self.X_POS += 6

        if self.step_index >= 10:
            self.step_index = 0
        for obstacle in obstacles:
            if collide_mask(self, obstacle): 
                self.lose = True

        hit_ground = pygame.sprite.spritecollide(self, ground_sprites, False)
        for hit in hit_ground:
            self.rect.bottom = hit.rect.top 
