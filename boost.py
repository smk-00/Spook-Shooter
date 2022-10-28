import pygame as pg
import random

class Boost:
    def __init__(self) -> None:
        self.paths = ["purple", "teal", "yellow"]
        self.candy = None
        self.boost = 0
    
    def loadCandy(self):
        path = random.randrange(4)
        if path=="purple":
            self.boost = 25
        else:
            self.boost = 10

        self.candy = pg.image.load(f"./assets/boosts/{path}.png")

    def draw(self):
