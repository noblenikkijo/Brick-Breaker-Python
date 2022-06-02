import pygame as pg
 
class Paddle(pg.sprite.Sprite): #inherits from pygame sprite.Sprite


    def __init__(self):
        #width is 100 height is 10. do these need to be local variables?
        __width__ = 125
        __height__ = 10

        super().__init__() 
       
        self.image = pg.Surface([__width__, __height__])
    
        pg.draw.rect(self.image, (100, 100, 100), [0, 0, __width__, __height__])
        
        self.rect = self.image.get_rect()
        
        #Move paddle methods
    
    def moveLeft(self):
        self.rect.x -= 8
        #prevents the paddle from moving off the screen
        if self.rect.x < 0:
          self.rect.x = 0
          
    def moveRight(self):
        self.rect.x += 8
        #prevents the paddle from moving off the screen
        if self.rect.x > 700:
          self.rect.x = 700
