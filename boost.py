import pygame as pg
import random

class Boost:
    def __init__(self) -> None:
        self.paths = ["purple", "teal", "yellow"]
        self.candy = None
        self.boost = 0
        self.x = random.randint(10, 1366)
        self.y = -20
    
        self.loadCandy()

    def loadCandy(self):
        path = random.randrange(3)
        if path=="purple":
            self.boost = 5
        else:
            self.boost = 2

        self.candy = pg.image.load(f"./assets/boosts/{self.paths[path]}.png")
        self.candy = pg.transform.scale(self.candy, (30,30))

    def draw(self,win):
        win.blit(self.candy, (self.x, self.y))
        if self.y+20 <= 640:
            self.y += 5