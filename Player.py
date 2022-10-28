import pygame as pg

class Player(object):
    def __init__(self,x,y,life,scr,jump,height,width,speed):
        self.x = x
        self.y = y
        self.life = life
        self.scr = scr
        self.jump = jump
        self.height = height
        self.width = width
        self.speed = speed
        self.hitbox = [self.x, self.y, self.height, self.width]

        self.ast_position = 0

        self.player_img = None
        self.player_assets = ['./assets/player/1.png','./assets/player/2.png','./assets/player/3.png',
                                './assets/player/4.png','./assets/player/5.png', './assets/player/6.png']
        self.player = None
        self.loadcharacter()

    def loadcharacter(self):
        self.player_img = [pg.image.load(path) for path in self.player_assets]  
        self.player_img = [pg.transform.scale(img, (self.width, self.height)) for img in self.player_img]

    def draw(self,win):
        if(self.ast_position == 5):
            self.ast_position = 0
        if(self.player):
            win.blit(self.player,(self.x, self.y))

    def move(self):
        self.jump = False
        jumpCount = 10

        keys = pg.key.get_pressed()
         
        if keys[pg.K_SPACE]:
            self.jump = True

        if keys[pg.K_LEFT] and self.x > self.speed: 
            self.x -= self.speed
            self.ast_position += 1
            self.player = self.player_img[self.ast_position%6]
            self.player = pg.transform.flip(self.player, True, False) 

        if keys[pg.K_RIGHT] and self.x < 1366 - self.speed - self.width:  
            self.x += self.speed
            self.ast_position += 1
            self.player = self.player_img[self.ast_position%6]
            
        if not(self.jump): 
            if keys[pg.K_UP] and self.y > self.speed:
                self.y -= self.speed

            if self.y < 680 - self.height - self.speed:
                self.y += self.speed

            if keys[pg.K_SPACE]:
                self.jump = True
        else:
            if jumpCount > -10:
                self.y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else: 
                jumpCount = 10
                self.jump = False