import pygame
import sys

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

GAME_RUNNING = 0
GAME_OVER = 1
INTRO = 2

all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
ground_sprites = pygame.sprite.Group()



background_speed = 10

game_state = ["DESERT", "JUNGLE", "LAVA", "BOSS"]

