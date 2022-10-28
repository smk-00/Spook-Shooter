import pygame as pg
from environment import Environment


# pygame init
pg.init()

screen_w = 1240
screen_h = 680

WINDOW = pg.display.set_mode((screen_w,screen_h))
pg.display.set_caption("Soppky Shooter")

# Game instance

ENVIRONMENT = Environment(floorPath="./assets/environment/floor.png", musicPath="./assets/environment/bg_music.mp3")



def mainGame():
    while True:
        ENVIRONMENT.draw()



pg.quit()