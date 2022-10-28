import pygame as pg
from environment import Environment
from player import Player


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
                            platformCords=[[130, 420], [256, 390], [1000, 200], [500, 300], [800, 200]],
                            width=screen_w,
                            height=screen_h
                        )

C_PLAYER = Player(x=0, y=0, life=0, scr=0, jump=True, height=100, width=50, speed=25)


RUN = True

while True:
    if not RUN:
        break
    
    pg.time.delay(200)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUN = False

    C_PLAYER.move()

    ENVIRONMENT.draw(WINDOW)
    C_PLAYER.draw(WINDOW)

    pg.display.update() 

pg.quit()