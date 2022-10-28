import pygame as pg
from pygame import mixer
from platformSlide import PlatformSlide


class Environment:
    def __init__(self, bgPath, musicPath, level, platformCords) -> None:
        self.bg = None
        self.bgPath = bgPath
        self.musicPath = musicPath
        self.level = level
        self.platformCords = platformCords
        self.platformSlides = []
        self.loadlevel()


    def loadlevel(self):
        self.bg = pg.image.load(self.bgPath)
        mixer.music.load(self.musicPath)
        mixer.music.play(-1)

        for i, platformCord in enumerate(self.platformCords):
            self.platformSlides.append(PlatformSlide(f"./assets/environment/level {self.level}/platform{i+1}.png", platformCord))



    def draw(self, window):
        window.blit(self.bg, (0, 0))
        for platformSlide in self.platformSlides:
            platformSlide.draw(window)