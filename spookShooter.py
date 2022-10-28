import pygame as pg
from environment import Environment


# pygame init
pg.init()

screen_w = 1366
screen_h = 720

FPS = 60
clock = pg.time.Clock()

WINDOW = pg.display.set_mode((screen_w,screen_h))
pg.display.set_caption("Soppky Shooter")

# Game instance

ENVIRONMENT = Environment(
                            musicPath="./assets/environment/bg_music.mp3",
                            level=3,
                            width=screen_w,
                            height=screen_h
                        )


RUN = True

while True:
    if not RUN:
        break
    
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUN = False

    ENVIRONMENT.draw(WINDOW)


pg.quit()