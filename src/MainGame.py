import pygame
import random
from Boss import spawn_boss
from setting import *
from Background import *
from Desert import *
from Jungle import *
from Player import *
from UI import *
from Obstacle import *
from Lava import *



def getScore():
    return sco

def game():
    background_1 = Background(0, 0)
    background_2 = Background(1100, 1)
    all_sprites.add(background_1, background_2)

    ground_1 = Ground()
    all_sprites.add(ground_1)
    ground_sprites.add(ground_1)

    player = Player()
    all_sprites.add(player)

    score = Score()
    all_sprites.add(score)
    global sco
    sco = 0

    play_music(SOUND[2], -1)
    first_ob = True
    get_first_time = True

    current_state = game_state[0]
    new_state = game_state[0]

    time_spawn_hole = 115

    boss = 0

    vec_return = 5

    time_start_playing = pygame.time.get_ticks()

    last_choice = 0

    change = False

    num_of_hole = 10

    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            player.control(event, current_state)

        screen.fill((172, 170, 170))
        current_time = pygame.time.get_ticks()

        if first_ob:
            if get_first_time: 
                time_start = pygame.time.get_ticks()
                get_first_time = False
            time_end = pygame.time.get_ticks()
            if time_end - time_start >= 2000: 
                if current_state == "DESERT":
                    ob_spawn_desert(random.randint(0, 4))
                elif current_state == "JUNGLE":
                    ob_spawn_jungle(random.randint(0, 2))
                elif current_state == "BOSS":
                    boss = random.randint(1, 2)
                    spawn_boss(boss)
                first_ob = False

        elif len(obstacles) == 0:  
            if current_state == "DESERT":
                ob_spawn_desert(random.randint(0, 4))
            elif current_state == "JUNGLE":
                ob_spawn_jungle(random.randint(0, 2))

        

        for ob in obstacles:
            if current_state in ["DESERT", "JUNGLE", "LAVA"]:
                if not ob.get_point:
                    if player.rect.x  >= ob.rect.x + ob.image.get_width(): 
                        score.update_score()
                        sco = score.score
                        ob.get_point = True
                        change = True
                if ob.speed < 20: ob.speed += (current_time - time_start_playing) // 45000

            if current_state == "BOSS":
                if boss == 0: pass
                elif boss == 1:
                    if not ob.get_point:
                        if player.rect.x <= ob.rect.x + 70 and player.rect.x >= ob.rect.x + 20: 
                            score.update_score()
                            sco = score.score
                            ob.get_point = True
                            change = True
                elif boss == 2:
                    if ob.type == "rock":
                        if ob.rect.y >= 380: 
                            score.update_score()
                            sco = score.score
                            ob.get_point = True   
                            all_sprites.remove(ob)
                            obstacles.remove(ob) 
                            change = True 
                    if ob.type == "boss":
                        ob.drop_rock(player)

            if new_state != "BOSS": 
                ob.end = True
                boss = 0
            
        if sco % 10 == 0 and sco != 0: 
            if change:
                choices = [0, 1, 2, 3]
                choices.remove(last_choice)
                choice = random.choice(choices)
                new_state = game_state[choice] 
                last_choice = choice 
                change = False

        if new_state != current_state:
            if new_state == "DESERT":
                background_1.biome = BG_D
                background_2.biome = BG_D
                background_1.index = 0
                background_2.index = 1
                first_ob = True
                get_first_time = True
            elif new_state == "JUNGLE":
                background_1.biome = BG_J
                background_2.biome = BG_J
                background_1.index = 0
                background_2.index = 1
                first_ob = True
                get_first_time = True
            elif new_state == "LAVA":
                background_1.biome = BG_L
                background_2.biome = BG_L
                background_1.index = 0
                background_2.index = 1
            elif new_state == "BOSS":
                background_1.biome = BG_BOSS
                background_2.biome = BG_BOSS
                background_1.index = 0
                background_2.index = 1
                ground_1.rect.x = 0
                first_ob = True
                get_first_time = True
                time_spawn_hole = 115
                text = Text("PRESS LEFT OR RIGHT ARROW TO MOVE", SCREEN_WIDTH // 2, 450, 20)
                all_sprites.add(text)
                
        if current_state != "BOSS":
            if player.X_POS > 80: 
                player.X_POS -= vec_return 
                if player.X_POS < 80: player.X_POS = 80
                all_sprites.remove(text)
            elif player.X_POS < 80: 
                player.X_POS += vec_return 
                if player.X_POS > 80: player.X_POS = 80
                all_sprites.remove(text)
            
        if current_state == "LAVA": 
            if time_spawn_hole > 0: time_spawn_hole -= 1
            elif num_of_hole > 0: 
                spawn_hole()
                time_spawn_hole = 30
                num_of_hole -= 1
        else: num_of_hole = 10

        current_state = new_state 

        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.update()
        clock.tick(60)


        if player.lose: 
            pygame.mixer.music.stop()
            all_sprites.empty()
            obstacles.empty()
            ground_sprites.empty()
            running = False

    return GAME_OVER

