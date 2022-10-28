import pygame as pg
from pygame import mixer
from platformSlide import PlatformSlide


class Environment:
    def __init__(self, musicPath, level, width, height) -> None:
        self.bg = None
        self.bgPath = f"./assets/environment/level {level}/bg.png"
        self.musicPath = musicPath
        self.level = level
        self.width = width
        self.height = height
        self.platformCords = None
        self.platformSlides = []
        self.loadlevel()


    def loadlevel(self):
        self.bg = pg.image.load(self.bgPath)
        self.bg = pg.transform.scale(self.bg, (self.width, self.height))
        mixer.music.load(self.musicPath)
        mixer.music.play(-1)

        if self.level==1:
            self.platformCords=[[100, 460], [350, 320], [600, 200], [850, 320], [1100, 460]]
        
        if self.level==2:
            self.platformCords=[[100, 500], [350, 400], [100, 300], [350, 200], [100, 100]]

        if self.level==3:
            self.platformCords=[[100, 500], [350, 400], [600, 300], [850, 200], [1100, 100]]

        for i, platformCord in enumerate(self.platformCords):
            self.platformSlides.append(PlatformSlide(f"./assets/environment/level {self.level}/platform{i+1}.png", platformCord))



    def draw(self, window):
        window.blit(self.bg, (0, 0))
        for platformSlide in self.platformSlides:
            platformSlide.draw(window)