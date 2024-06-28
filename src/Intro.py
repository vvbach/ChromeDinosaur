from dis import Instruction
import pygame
from UI import *
from setting import *

def intro():
    text = Text("PRESS SPACE TO START", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100, 22)    
    instruction = Text("UP ARROW - JUMP      DOWN ARROW - DUCK", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100, 20)
    credit = Text("A GAME MADE BY DREAMWALKERS", SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100, 14)
    
    all_sprites.add(text, instruction, credit)
    play_music(SOUND[1], -1)
    running = True
    while running:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                    pygame.mixer.music.stop()
                    all_sprites.empty()
                    running = False
        
        screen.fill((255, 255, 255))
        
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.update()
        clock.tick(60)

    return GAME_RUNNING