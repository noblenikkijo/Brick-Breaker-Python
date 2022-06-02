import pygame as pg

class Overlay(pg.sprite.Sprite): #inherit from sprite
 
    def __init__(self):
        super().__init__()
   
        self.__score__ = 0;
        self.__lives__ = 3;
        self.image = pg.Surface([100, 50])
        font = pg.font.Font(None, 34)
        text = font.render("Score: " + str(self.__score__), 1, (0,0,0))
        
        text = font.render("Lives: " + str(self.__lives__), 1, (0,0,0))

    def getScore(self):
        return self.__score__

    def getLives(self):
        return self.__lives__

    def update(self, screen) -> None:
        font = pg.font.Font(None, 34)
        text = font.render("Score: " + str(self.__score__), 1, (0,0,0))
        screen.blit(text, (20,10))
        text = font.render("Lives: " + str(self.__lives__), 1, (0,0,0))
        screen.blit(text, (650,10))