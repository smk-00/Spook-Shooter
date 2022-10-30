from random import random
import pygame as pg

class Enemy(object):
    def __init__(self,x,y,life,speed,e_type,height,width,images):
        self.x = x
        self.y = y
        self.life = life
        self.speed = speed
        self.e_type = e_type
        self.height = height
        self.width = width
        self.hitbox = [self.x, self.y, self.height, self.width]
        self.eat = pg.mixer.Sound("./assets/enemy/zombie.wav")
        self.ast_position = 0
        self.enemy_assets = images

        self.loadcharacter()
        self.enemy = None
        self.movew = 'R'

    def loadcharacter(self):
        self.enemy_img = [pg.image.load(path) for path in self.enemy_assets]  
        self.enemy_img = [pg.transform.scale(img, (self.width, self.height)) for img in self.enemy_img]

    def draw(self,win):
        pg.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)) # NEW
        pg.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.life)), 10))
        self.hitbox = (self.x, self.y, 31, 57)
        #pg.draw.rect(win, (255,0,0), self.hitbox,2)
        if(self.ast_position == 5):
            self.ast_position = 0
        if(self.enemy):
            win.blit(self.enemy,(self.x, self.y))
        pg.display.update()

    def move(self,ENVIRONMENT,C_PLAYER):
        for j in C_PLAYER.weapon.bulletsFired:
            if ((self.x > j.cords[0] and self.x < j.cords[0]+j.width) and (self.y < j.cords[1] and self.y + 600 > j.cords[1]+j.height)):
                self.life -= 5
                C_PLAYER.weapon.bulletsFired.remove(j)
        
                if(self.life == 0):
                    C_PLAYER.scr += 10
                else:
                    C_PLAYER.scr += 5
        if self.y+self.height <= 640:
            self.y += self.speed

        if C_PLAYER.y < 540:
            if self.x > 1366:
                self.movew = 'L'            
            if self.x < 0:
                self.movew = 'R'
        else:
            if self.x > C_PLAYER.x:
                self.movew = 'L'            
            if self.x < C_PLAYER.x:
                self.movew = 'R'

        if self.movew == 'R':
            self.enemy = self.enemy_img[self.ast_position%6]
            self.ast_position += 1
            self.x += self.speed
        else:
            self.enemy = self.enemy_img[self.ast_position%6]
            self.enemy = pg.transform.flip(self.enemy, True, False) 
            self.ast_position += 1
            self.x -= self.speed

        if ((self.x >C_PLAYER.hitbox[0] and self.x < C_PLAYER.hitbox[0]+C_PLAYER.hitbox[2]) and (self.y < C_PLAYER.hitbox[1] and self.y > C_PLAYER.hitbox[3])):
            #print(C_PLAYER.life)
            if(C_PLAYER.life < 0):
                C_PLAYER.life_count -= 1
                self.eat.play()
                C_PLAYER.life = 10
            if(C_PLAYER.life_count != 0):
                C_PLAYER.life -= 0.1
            else:
                C_PLAYER.y = 0 