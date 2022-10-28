import pygame as pg
import random

from environment import Environment
from player import Player
from enemy import Enemy

# pygame init
pg.init()

font = pg.font.SysFont('comicsans', 30, True)

screen_w = 1366
screen_h = 720

FPS = 30
clock = pg.time.Clock()

WINDOW = pg.display.set_mode((screen_w,screen_h))
pg.display.set_caption("Soppky Shooter")

# Game instance
ENVIRONMENT = Environment(
                            musicPath="./assets/environment/bg_music.mp3",
                            level=2,
                            width=screen_w,
                            height=screen_h
                        )

C_PLAYER = Player(height=100, width=50, speed=10, font=font)
E_PLAYER_M = Enemy(x=random.randint(100, 800), y=-15, life=10, speed=3, e_type='zombie', height=100, width=60,
                   images=['./assets/enemy/zombie_m/1.png','./assets/enemy/zombie_m/2.png','./assets/enemy/zombie_m/3.png','./assets/enemy/zombie_m/4.png','./assets/enemy/zombie_m/5.png','./assets/enemy/zombie_m/6.png'])

E_PLAYER_F = Enemy(x=random.randint(100, 800), y=-15, life=5, speed=6, e_type='zombie', height=100, width=60,
                   images=['./assets/enemy/zombie_f/1.png','./assets/enemy/zombie_f/2.png','./assets/enemy/zombie_f/3.png','./assets/enemy/zombie_f/4.png','./assets/enemy/zombie_f/5.png','./assets/enemy/zombie_f/6.png'])

RUN = True

while True:
    if not RUN:
        break
    
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUN = False

    C_PLAYER.move(ENVIRONMENT)
    E_PLAYER_M.move(ENVIRONMENT, C_PLAYER)
    E_PLAYER_F.move(ENVIRONMENT, C_PLAYER)

    ENVIRONMENT.draw(WINDOW)
    C_PLAYER.draw(WINDOW)
    E_PLAYER_M.draw(WINDOW)
    E_PLAYER_F.draw(WINDOW)
    

    pg.display.update() 

pg.quit()