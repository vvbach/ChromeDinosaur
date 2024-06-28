import pygame
import os
from setting import *

SOUND = [os.path.join("Assets/Music", "dino_die.mp3"),
         os.path.join("Assets/Music", "menu.mp3"),
         os.path.join("Assets/Music", "run.mp3"),
         os.path.join("Assets/Music", "tick.wav")]

class Text(pygame.sprite.Sprite):
    def __init__(self, text, x , y, font_size):
        pygame.sprite.Sprite.__init__(self) 
        self.font = pygame.font.SysFont('consolas', font_size)
        self.image = self.font.render(text, True, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update_text(self, text):
        self.image = self.font.render(text, True, (0, 0, 0))

class Score(Text):
    def __init__(self):
        self.score = 0
        self.text = "Score : " + str(self.score)
        Text.__init__(self, self.text, 60, 20, 20)

    def update_score(self):
        play_sound(SOUND[3])
        self.score += 1
        self.update_text("Score : " + str(self.score))

def play_music(music, play_times):
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(play_times)

def play_sound(sound):
    get_sound = pygame.mixer.Sound(sound)
    pygame.mixer.Sound.play(get_sound)