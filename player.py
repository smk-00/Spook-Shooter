import pygame as pg
from weapon import Weapon

class Player(object):
    def __init__(self,height,width,speed, font):
        self.x = 20
        self.y = 20
        self.life = 10
        self.life_count = 5
        self.scr = 0
        self.jump = False
        self.height = height
        self.width = width
        self.speed = speed
        self.jumpcount = speed
        self.hitbox = [self.x, self.y, self.height, self.width]
        self.weapon = Weapon("pumpgun", [self.x, self.y])
        self.font = font

        self.ast_position = 0

        self.player_img = None
        self.player_assets = ['./assets/player/1.png','./assets/player/2.png','./assets/player/3.png',
                                './assets/player/4.png','./assets/player/5.png', './assets/player/6.png']
        self.player = None
        self.loadcharacter()

    def loadcharacter(self):
        self.player_img = [pg.image.load(path) for path in self.player_assets]  
        self.player_img = [pg.transform.scale(img, (self.width, self.height)) for img in self.player_img]

    def draw(self,window):
        pg.draw.rect(window, (255,0,0), (30, 30 - 20, 50, 10)) # NEW
        pg.draw.rect(window, (0,128,0), (30, 30 - 20, 50 - (5 * (10 - self.life)), 10))
        self.hitbox = (self.x, self.y, self.height, self.width)
        self.weapon.checkFire()
        self.weapon.draw(window)
        text_l = self.font.render('Life : ' + str(self.life_count), 1, (0,0,0))
        window.blit(text_l, (50, 50))

        text_s = self.font.render('Score : ' + str(self.scr), 1, (255,0,0))
        window.blit(text_s, (1100, 50))
        if(self.ast_position == 5):
            self.ast_position = 0
        if(self.player):
            window.blit(self.player,(self.x, self.y))

    def move(self, ENVIRONMENT):
        self.weapon.attachWithPlayer([self.x, self.y])
        keys = pg.key.get_pressed()

        if keys[pg.K_UP] or keys[pg.K_w]:
            self.jump = True

        if (keys[pg.K_LEFT] or keys[pg.K_a]) and self.x > self.speed: 
            self.x -= self.speed
            self.ast_position += 1
            self.player = self.player_img[self.ast_position%6]
            self.player = pg.transform.flip(self.player, True, False)

            self.weapon.gun = pg.image.load("./assets/weapons/pumpgun.png")
            self.weapon.gun = pg.transform.scale(self.weapon.gun, (60, 60))
            self.weapon.gun = pg.transform.flip(self.weapon.gun, True, False)

        if (keys[pg.K_RIGHT] or keys[pg.K_d]) and self.x < 1366 - self.speed - self.width:  
            self.x += self.speed
            self.ast_position += 1
            self.weapon.gun = pg.image.load("./assets/weapons/pumpgun.png")
            self.weapon.gun = pg.transform.scale(self.weapon.gun, (60, 60))
            self.player = self.player_img[self.ast_position%6]
            
        if self.jump:
            if self.jumpcount >= -self.speed:
                neg = 1
                if self.jumpcount < 0:
                    neg = -1
                self.y -= (self.jumpcount **2) * 0.5* neg
                self.jumpcount -= 1
            else:
                self.jump = False
                self.jumpcount = self.speed
                
        else:
            if self.y+self.height <= 640:
                self.y += self.speed
        
        for i in range(len(ENVIRONMENT.platformSlides)):
            if ((self.x > ENVIRONMENT.platformSlides[i].hitbox[0] and self.x < ENVIRONMENT.platformSlides[i].hitbox[0]+ENVIRONMENT.platformSlides[i].hitbox[2]) and (self.y < ENVIRONMENT.platformSlides[i].hitbox[1] and self.y > ENVIRONMENT.platformSlides[i].hitbox[1]-ENVIRONMENT.platformSlides[i].hitbox[3])):
                if keys[pg.K_UP]:
                    self.jump = True
                else:
                    self.y = ENVIRONMENT.platformSlides[i].hitbox[1] - ENVIRONMENT.platformSlides[i].hitbox[3]
