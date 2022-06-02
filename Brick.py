import pygame as pg
 
class Brick(pg.sprite.Sprite): #inherit from sprite
 
    def __init__(self, color):
        super().__init__()
        width = 80
        height = 30

        self.image = pg.Surface([width, height])
   

        pg.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    # def update(self):
    #     self.image = pg.Surface([80, 30])
    #     self.image.fill((0,0,0))
    #     self.image.set_colorkey((0,0,0))
      
    def draw(self, screen):
	    screen.blit(self.image, self.rect);
