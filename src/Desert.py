from Background import *
from Obstacle import *
import os 
import random


SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Desert/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Desert/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Desert/Cactus", "SmallCactus3.png"))]
                
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Desert/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Desert/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Desert/Cactus", "LargeCactus3.png"))]

ME = [pygame.image.load(os.path.join("Assets/Meteor", "Meteor_1.png")),
      pygame.image.load(os.path.join("Assets/Meteor", "Meteor_2.png")),
      pygame.image.load(os.path.join("Assets/Meteor", "Meteor_R1.png")),
      pygame.image.load(os.path.join("Assets/Meteor", "Meteor_R2.png")),
      pygame.image.load(os.path.join("Assets/Meteor", "Boom.png")),
      pygame.image.load(os.path.join("Assets/Meteor", "Rock.png"))]

BIRD = [pygame.image.load(os.path.join("Assets/Desert/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Desert/Bird", "Bird2.png"))]
        




class SmallCactus(Obstacle):
    def __init__(self):
        self.index = random.randint(0, 2)
        super().__init__(SMALL_CACTUS, self.index)
        self.rect.y = 310


class LargeCactus(Obstacle):
    def __init__(self):
        self.index = random.randint(0, 2)
        super().__init__(LARGE_CACTUS, self.index)
        self.rect.y = 285


class Bird(Obstacle):
    def __init__(self):
        self.index = 0
        super().__init__(BIRD, self.index)
        self.rect.y = 250
        

    def update(self):
        super().update()
        if self.index >= 9:
            self.index = 0
        self.image = BIRD[self.index // 5]
        self.index += 1

class Meteor(Obstacle):
    def __init__(self):
        self.index = 0
        super().__init__(ME, self.index)
        self.on_air = True
        self.rect.x = 100
        self.rect.y = -100

        self.vec_x = 65
        self.vec_y = 30

        self.boom_fade = 255
    

    def boom(self, i):
        boom_img = ME[4]
        boom_img.convert()
        boom_img.set_alpha(i)
        if i > 0: screen.blit(boom_img, (self.rect.x - 100, self.rect.y - 120))
        pygame.display.update()
            
    def update(self):
        self.rect.x += self.vec_x
        self.rect.y += self.vec_y

        if self.index >= 9:
            self.index = 0
        self.image = ME[self.index // 5]
        self.index += 1

        if self.rect.y >= 285:
            self.boom(self.boom_fade)
            self.boom_fade -= 10
            self.vec_x = 0
            self.vec_y = 0
            self.image = ME[5]
            super().update()

class Meteor_To_The_Face(Meteor):
    def __init__(self):
        super().__init__()
        self.positions = [(1000, -130), [1000, -30]]
        i = random.randint(0, 1)
        (self.rect.x ,self.rect.y) = self.positions[i]

        self.vec_x = -26
        self.vec_y = 10


    def update(self):
        self.rect.x += self.vec_x
        self.rect.y += self.vec_y

        if self.index >= 9:
            self.index = 0
        self.image = ME[self.index // 5 + 2]
        self.index += 1
        
        if self.rect.y >= 285:
            self.boom(self.boom_fade)
            self.boom_fade -= 10
            self.vec_x = 0
            self.vec_y = 0
            self.image = ME[5]
            super().update()

def ob_spawn_desert(index):
    if index == 0:
        sc = SmallCactus()
        all_sprites.add(sc)
        obstacles.add(sc)
                
    elif index == 1:
        lc = LargeCactus()
        all_sprites.add(lc)
        obstacles.add(lc)
                 
    elif index == 2:
        bird = Bird()
        all_sprites.add(bird)
        obstacles.add(bird)

    elif index == 3:
        meteor = Meteor()
        all_sprites.add(meteor)
        obstacles.add(meteor)

    elif index == 4:
        meteor_2 = Meteor_To_The_Face()
        all_sprites.add(meteor_2)
        obstacles.add(meteor_2)

    elif index == 5:
        ob_spawn_desert(3)
        ob_spawn_desert(4)
        