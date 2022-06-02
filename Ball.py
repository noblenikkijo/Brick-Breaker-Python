# Ball: inherit form sprite (when hit x and y swap)
# State) Image, rectangle, x, y, 
# Methods:
# - Draw
# - Update (override -> check collisions,changes direction, moves ball, etc)

#The ball class inherits from sprite


import pygame as pg
from random import randint
 
class Ball(pg.sprite.Sprite): #by passing sprite as the paramater we are using Pythonic inheritace
    
    def __init__(self):
        super().__init__()

        __width__ = 10
        __height__ = 10
        
        self.image = pg.Surface([__width__, __height__])
        pg.draw.circle(self.image, (0, 0, 0), [0, 0], 10)
        
        self.velocity = [5,5]

        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = -self.velocity[1]

    