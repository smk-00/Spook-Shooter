import pygame as pg
import random

from environment import Environment
from player import Player
from enemy import Enemy

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
                            level=1,
                            width=screen_w,
                            height=screen_h
                        )

C_PLAYER = Player(height=100, width=50, speed=10)
E_PLAYER = Enemy(x=random.randint(100, 800), y=-15, life=10, speed=15, e_type='zombie', height=100, width=60,
                   images=['./assets/enemy/zombie_m/1.png','./assets/enemy/zombie_m/2.png','./assets/enemy/zombie_m/3.png','./assets/enemy/zombie_m/4.png','./assets/enemy/zombie_m/5.png','./assets/enemy/zombie_m/6.png'])

RUN = True

while True:
    if not RUN:
        break
    
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUN = False

    C_PLAYER.move(ENVIRONMENT)

    ENVIRONMENT.draw(WINDOW)
    C_PLAYER.draw(WINDOW)
    E_PLAYER.draw(WINDOW)

    pg.display.update() 

pg.quit()