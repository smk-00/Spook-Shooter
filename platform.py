import pygame as pg


class Platform():
    def __init__(self, path, cords) -> None:
        self.path = path
        self.platform = None
        self.width = 120
        self.height = 40
        self.cords = cords
        self.hitbox = [cords[0], cords[1], self.width, self.height]

        self.loadPlatform()


    def loadPlatform(self):
        self.platform = pg.image.load(self.path)


    def draw(self, window):
        window.blit(self.platform, self.cords)
