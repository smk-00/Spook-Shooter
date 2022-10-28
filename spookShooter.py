from json import load
from tkinter import W
import pygame as pg
import random
import pickle

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


loadScreen = pg.image.load("./assets/start/bg.png")
loadScreen = pg.transform.scale(loadScreen, (screen_w, screen_h))
hiscores = pickle.load(open('highscore.txt',"rb"))


GAME_START = True
GAME_RUN = False


while GAME_START:
    WINDOW.blit(loadScreen, (0,0))
    pg.display.update()

    while GAME_RUN:
        clock.tick(FPS)
        
        if not GAME_RUN:
            break
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                GAME_RUN = False

        if C_PLAYER.life<=0:
            c_score = C_PLAYER.scr
            hiscores.sort()
            for score in hiscores:
                if c_score>score:
                    hiscores.append(score)
            hiscores.sort()
            pickle.dump(hiscores[:5],open('highscore.txt',"wb"))
            GAME_RUN = False

        C_PLAYER.move(ENVIRONMENT)

        ENVIRONMENT.draw(WINDOW)
        C_PLAYER.draw(WINDOW)
        E_PLAYER_M.draw(WINDOW)
        E_PLAYER_F.draw(WINDOW)


        pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            GAME_START = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            if (mouse_x<195 and mouse_x>94) and (mouse_y>595 and mouse_y<640):
                GAME_RUN = True
            if (mouse_x<1263 and mouse_x>1168) and (mouse_y>596 and mouse_y<720):
                GAME_START = False
            if (mouse_x<826 and mouse_x>535) and (mouse_y>595 and mouse_y<648):
                GAME_START = False
                WINDOW.fill((23,23,23))
                WINDOW.blit(font.render(("Highscores"),18,(255,255,255)), (600, 300))
                scrs = []
                for i, score in enumerate(hiscores):
                    WINDOW.blit(font.render((f"{i+1}. {score}"),18,(255,255,255)), (700, 400+(10*(i+1))))

                WINDOW.blit(font.render(("back"),18,(255,255,255)), (612, 520))
                if (mouse_x<680 and mouse_x>520) and (mouse_y>612 and mouse_y<540):
                    GAME_START = True

pg.quit()