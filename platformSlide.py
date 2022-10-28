import pygame as pg


class PlatformSlide():
    def __init__(self, path, cords) -> None:
        self.path = path
        self.platformSlide = None
        self.width = 220
        self.height = 70
        self.cords = cords
        self.hitbox = [cords[0], cords[1], self.width, self.height]

        self.loadPlatformSlide()


    def loadPlatformSlide(self):
        self.platformSlide = pg.image.load(self.path)
        self.platformSlide = pg.transform.scale(self.platformSlide, (self.width, self.height))


    def draw(self, window):
        window.blit(self.platformSlide, self.cords)
