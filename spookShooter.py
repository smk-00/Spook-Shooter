import pygame as pg
from environment import Environment


# pygame init
pg.init()

screen_w = 1240
screen_h = 680

WINDOW = pg.display.set_mode((screen_w,screen_h))
pg.display.set_caption("Soppky Shooter")

# Game instance

ENVIRONMENT = Environment(
                            bgPath="./assets/environment/level 1/bg.png",
                            musicPath="./assets/environment/bg_music.mp3",
                            level=1,
                            platformCords=[[130, 420], [256, 390], [1000, 200], [500, 300], [800, 200]]
                        )



def mainGame():
    while True:
        ENVIRONMENT.draw(WINDOW)


mainGame()

pg.quit()