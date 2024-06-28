from Background import *
from Obstacle import *
import os 
import random

GR = pygame.image.load(os.path.join("Assets/Jungle/Background", "Ground.png"))

ROCK = [pygame.image.load(os.path.join("Assets/Jungle/Object", "Rock.png"))]

EF = [pygame.image.load(os.path.join("Assets/Jungle/Object", "Eating_flower.png"))]

BUSH = [pygame.image.load(os.path.join("Assets/Jungle/Object", "bush.png"))]

SPIKE = [pygame.image.load(os.path.join("Assets/Jungle/Object", "spike.png"))]


class Rock(Obstacle):
    def __init__(self):
        super().__init__(ROCK, 0)
        self.rect.y = 325
    

class Eating_flower(Obstacle):
    def __init__(self):
        super().__init__(EF, 0)
        self.rect.y = 280
    
class Bush(Obstacle):
    def __init__(self, x):
        super().__init__(BUSH, 0)
        self.rect.x = x
        self.rect.y = 305
        self.mask.clear()
        self.get_point = True

    def update(self):
        super().update()

class Spike_Bush(Obstacle):
    def __init__(self, x):
        super().__init__(SPIKE, 0)
        self.rect.x = x
        self.rect.y = 305

    def update(self):
        super().update()

def ob_spawn_jungle(index):
    if index == 0:
        rock = Rock()
        obstacles.add(rock)
        all_sprites.add(rock)

    elif index == 1:
        eatingFlower = Eating_flower()
        obstacles.add(eatingFlower)
        all_sprites.add(eatingFlower)

    elif index == 2:
        pos = 1100
        for i in range(0, 5): 
            bush = Bush(pos + i * 100)
            all_sprites.add(bush)
            obstacles.add(bush)
        spike = Spike_Bush(pos + random.randint(0, 4) * 100)
        all_sprites.add(spike)
        obstacles.add(spike)