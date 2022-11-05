import pygame as pg
from pygame import mixer
from platformSlide import PlatformSlide


class Environment:
    def __init__(self, musicPath, level, width, height) -> None:
        self.bg = None
        self.bench = None
        self.musicPath = musicPath
        self.level = level
        self.width = width
        self.height = height
        self.platformCords = None
        self.platformSlides = []
        self.benchCords = None
        self.loadlevel()


    def loadlevel(self):
        self.bg = pg.image.load(f"./assets/environment/level {self.level}/bg.png")
        self.bg = pg.transform.scale(self.bg, (self.width, self.height))
                
        self.bench = pg.image.load(f"./assets/environment/level {self.level}/bench.png")
        self.platformCords = []
        mixer.music.load(self.musicPath)
        mixer.music.play(-1)

        if self.level==1:
            self.platformCords=[[100, 480], [350, 340], [600, 220], [850, 340], [1100, 480]]
            self.bench = pg.transform.scale(self.bench, (683, 10))
            self.benchCords = [341, 80]
        
        if self.level==2:
            self.platformCords=[[100, 500], [350, 400], [100, 300], [350, 200], [100, 100]]
            self.bench = pg.transform.scale(self.bench, (500, 10))
            self.benchCords = [800, 300]

        if self.level==3:
            self.platformCords=[[100, 500], [350, 400], [600, 300], [850, 200], [1100, 100]]
            self.bench = pg.transform.scale(self.bench, (500, 10))
            self.benchCords = [50, 200]

        for i, platformCord in enumerate(self.platformCords):
            self.platformSlides.append(PlatformSlide(f"./assets/environment/level {self.level}/platform{i+1}.png", platformCord))



    def draw(self, window):
        window.blit(self.bg, (0, 0))
        #window.blit(self.bench, self.benchCords)
        for platformSlide in self.platformSlides:
            platformSlide.draw(window)