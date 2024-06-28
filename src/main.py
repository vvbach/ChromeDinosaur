from MainGame import *
from Intro import *
from GameOver import *

scene = INTRO
while True:
    if scene == INTRO:
        scene = intro()
    if scene == GAME_RUNNING:
        scene = game()
    if scene == GAME_OVER:
        scene = game_over()