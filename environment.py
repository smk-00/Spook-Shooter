import pygame as pg
from pygame import mixer
from platform import Platform

class Environment:
    def __init__(self, bgPath, musicPath, platformsPaths, platformCords) -> None:
        self.bg = None
        self.bgPath = bgPath
        self.musicPath = musicPath
        self.level = 1
        self.platformsPaths = platformsPaths
        self.platformCords = platformCords
        self.platforms = []
        self.loadlevel()


    def loadlevel(self):
        self.bg = pg.image.load(self.bgPath)
        mixer.music.load(self.musicPath)
        mixer.music.play(-1)

        for platformPath, platformCord in zip(self.platformsPaths,self.platformCords):
            self.platforms.append(Platform(platformPath, platformCord))



    def draw(self, window):
        window.blit(self.bg, (0, 0))
        for platform in self.platforms:
            platform.draw(window)