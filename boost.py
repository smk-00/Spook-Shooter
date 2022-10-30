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
        self.candy = pg.transform.scale(self.candy, (40,40))
        self.n_taken = True 

    def draw(self,win, C_PLAYER):
        win.blit(self.candy, (self.x, self.y))
        if self.y+20 <= 640:
            self.y += 5

        if (self.x > C_PLAYER.hitbox[0] and self.x < C_PLAYER.hitbox[0]+C_PLAYER.hitbox[2]) and (self.y > C_PLAYER.hitbox[1] and self.y > C_PLAYER.hitbox[1]-C_PLAYER.hitbox[3]):
            if(C_PLAYER.y > 450):
                self.n_taken = False
                if(C_PLAYER.life < 10):
                    C_PLAYER.life += self.boost