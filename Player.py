import pygame as pg

class Player(object):
    def __init__(self,x,y,life,height,width,scr,speed,jump):
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
        self.player_assets = ['ast1','ast2','ast3']

    def draw(self,win):
        if(self.ast_position == 3):
            self.ast_position = 0
        player = pg.image.load(self.player_assets[self.ast_position])
        win.blit(player,(self.x, self.y))
        self.ast_position += 1
        pg.display.update()

    def move(self):
        self.jump = False
        jumpCount = 20

        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.jump = True

        if keys[pg.K_LEFT] and self.x > self.speed:
            self.x -= self.speed

        if keys[pg.K_RIGHT] and self.x < 1240 - self.speed - self.width:
            self.x += self.speed

        if not(self.jump):
            if keys[pg.K_UP] and self.y > self.speed:
                self.y -= self.speed

            if keys[pg.K_SPACE]:
                self.jump = True
        else:
            jumpCount -= 1