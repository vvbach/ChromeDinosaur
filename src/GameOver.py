import pygame
from UI import *
from setting import *
from MainGame import *

def game_over():
    play_music(SOUND[0], 1)
    gameOver = pygame.image.load(os.path.join("Assets/Others", "GameOver.png"))
    gameOverRect = gameOver.get_rect()
    gameOverRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)

    score_text = Text("Your score: " + str(getScore()),  SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20)

    text = Text("PRESS SPACE TO RESTART!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100, 20)

    all_sprites.add(text, score_text)
    
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
        screen.blit(gameOver, gameOverRect)

        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.update()
        clock.tick(60)

    return GAME_RUNNING