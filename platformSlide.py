import pygame as pg


class PlatformSlide():
    def __init__(self, path, cords) -> None:
        self.path = path
        self.platformSlide = None
        self.width = 120
        self.height = 40
        self.cords = cords
        self.hitbox = [cords[0], cords[1], self.width, self.height]

        self.loadPlatformSlide()


    def loadPlatformSlide(self):
        self.platformSlide = pg.image.load(self.path)


    def draw(self, window):
        window.blit(self.platformSlide, self.cords)
        pg.display.update()
