from json import load
from tkinter import CURRENT, W
import pygame as pg
import random
import pickle

from environment import Environment
from player import Player
from boost import Boost
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
                            level=1,
                            width=screen_w,
                            height=screen_h
                        )

C_PLAYER = Player(height=100, width=50, speed=10, font=font)

ENEMYS = []
BOOSTS = []

for i in range(6):
    BOOSTS.append(Boost())
    if(i%2):
        E_PLAYER_M = Enemy(x=random.randint(100, 800), y=-15, life=10, speed=random.randint(2, 7), e_type='zombie', height=180, width=60,
                   images=['./assets/enemy/zombie_m/1.png','./assets/enemy/zombie_m/2.png','./assets/enemy/zombie_m/3.png','./assets/enemy/zombie_m/4.png','./assets/enemy/zombie_m/5.png','./assets/enemy/zombie_m/6.png'])
        ENEMYS.append(E_PLAYER_M)
    else:
        E_PLAYER_F = Enemy(x=random.randint(100, 800), y=-15, life=10, speed=random.randint(2, 7), e_type='zombie', height=100, width=60,
                   images=['./assets/enemy/zombie_f/1.png','./assets/enemy/zombie_f/2.png','./assets/enemy/zombie_f/3.png','./assets/enemy/zombie_f/4.png','./assets/enemy/zombie_f/5.png','./assets/enemy/zombie_f/6.png'])
        ENEMYS.append(E_PLAYER_F)

loadScreen = pg.image.load("./assets/start/bg.png")
loadScreen = pg.transform.scale(loadScreen, (screen_w, screen_h))

hiscores = pickle.load(open('highscore',"rb"))
hiscores = list(hiscores)
print(hiscores)
for i, score in enumerate(hiscores):
    hiscores[i] = int(score)

game_over_music = pg.mixer.Sound("./assets/game_over.wav")

GAME_START = True
GAME_RUN = False
highscorePage = False

while GAME_START:
    WINDOW.blit(loadScreen, (0,0))
    pg.display.update()

    while highscorePage:
        WINDOW.fill((23,23,23))
        WINDOW.blit(font.render(("Highscores"),36,(255,255,255)), (600, 200))
        scrs = []
        for i, score in enumerate(hiscores):
            if i < 5:
                WINDOW.blit(font.render((f"{i+1}. {score}"),18,(255,255,255)), (700, 250+(25*(i+1))))


        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                highscorePage = False


    while GAME_RUN:
        clock.tick(FPS)
        
        if not GAME_RUN:
            break
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                GAME_RUN = False

        if(len(BOOSTS) <= 1):
            BOOSTS.append(Boost())
            BOOSTS.append(Boost())

        for h in BOOSTS:
            if(h.n_taken):
                h.draw(WINDOW, C_PLAYER)
            else:
                BOOSTS.remove(h)
            pg.display.update()

        if C_PLAYER.life_count<=0:
            game_over_music.play()
            c_score = C_PLAYER.scr
            hiscores.sort()
            for p in range(5):
                if c_score>hiscores[p]:
                    hiscores.append(c_score)
                    break
                
            hiscores.sort(reverse=True)
            if len(hiscores)>5:
                pickle.dump(hiscores[:5],open('highscore',"wb"))
            GAME_RUN = False
            C_PLAYER.scr = 0
            C_PLAYER.life_count = 3
            C_PLAYER.life = 10

        C_PLAYER.move(ENVIRONMENT)

        ENVIRONMENT.draw(WINDOW)
        C_PLAYER.draw(WINDOW)

        for o in ENEMYS:
            if(o.life == 0):
                ENEMYS.remove(o)

            o.draw(WINDOW)
            o.move(ENVIRONMENT, C_PLAYER)

        if(len(ENEMYS) == 0):
            ENVIRONMENT.level += 1
            if(ENVIRONMENT.level == 4):
                GAME_RUN = False
                ENVIRONMENT.level = 1
                C_PLAYER.life = 10
                C_PLAYER.life_count = 5
                C_PLAYER.scr = 0

            if(GAME_RUN): 
                ENVIRONMENT.loadlevel()
            for i in range(6):
                if(ENVIRONMENT.level == 2):
                    if(i%2):
                        E_PLAYER_M = Enemy(x=random.randint(100, 800), y=-15, life=10, speed=random.randint(3, 7), e_type='zombie', height=180, width=60,
                                images=['./assets/enemy/zombie_m/1.png','./assets/enemy/zombie_m/2.png','./assets/enemy/zombie_m/3.png','./assets/enemy/zombie_m/4.png','./assets/enemy/zombie_m/5.png','./assets/enemy/zombie_m/6.png'])
                        ENEMYS.append(E_PLAYER_M)
                    else:
                        E_PLAYER_F = Enemy(x=random.randint(100, 800), y=-15, life=10, speed=random.randint(4, 7), e_type='zombie', height=100, width=60,
                                images=['./assets/enemy/zombie_f/1.png','./assets/enemy/zombie_f/2.png','./assets/enemy/zombie_f/3.png','./assets/enemy/zombie_f/4.png','./assets/enemy/zombie_f/5.png','./assets/enemy/zombie_f/6.png'])
                        ENEMYS.append(E_PLAYER_F)
                if(ENVIRONMENT.level == 3):
                    if(i%2):
                        E_PLAYER_M = Enemy(x=random.randint(100, 800), y=-15, life=10, speed=random.randint(4, 7), e_type='zombie', height=180, width=60,
                                images=['./assets/enemy/zombie_m/1.png','./assets/enemy/zombie_m/2.png','./assets/enemy/zombie_m/3.png','./assets/enemy/zombie_m/4.png','./assets/enemy/zombie_m/5.png','./assets/enemy/zombie_m/6.png'])
                        ENEMYS.append(E_PLAYER_M)
                    else:
                        E_PLAYER_F = Enemy(x=random.randint(100, 800), y=-15, life=10, speed=random.randint(5, 7), e_type='zombie', height=100, width=60,
                                images=['./assets/enemy/zombie_f/1.png','./assets/enemy/zombie_f/2.png','./assets/enemy/zombie_f/3.png','./assets/enemy/zombie_f/4.png','./assets/enemy/zombie_f/5.png','./assets/enemy/zombie_f/6.png'])
                        ENEMYS.append(E_PLAYER_F) 

        pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            GAME_START = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            if (mouse_x<195 and mouse_x>94) and (mouse_y>595 and mouse_y<640):
                GAME_RUN = True
                startTune = pg.mixer.Sound("assets/start/start.wav")
                startTune.play()

            if (mouse_x<1263 and mouse_x>1168) and (mouse_y>596 and mouse_y<720):
                GAME_START = False
            if (mouse_x<826 and mouse_x>535) and (mouse_y>595 and mouse_y<648):
                highscorePage = True

pg.quit()