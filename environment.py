import pygame as pg
from pygame import mixer


class Environment:
    def __init__(self, floorPath, musicPath) -> None:
        self.floor = None
        self.floorPath = floorPath
        self.musicPath = musicPath
        self.loadAssets()


    def loadAssets(self):
        self.floor = pg.image.load(self.floorPath)
        mixer.music.load(self.musicPath)
        mixer.music.play(-1)



    def draw(self, window):
        window.blit(self.floor, (0, 0))