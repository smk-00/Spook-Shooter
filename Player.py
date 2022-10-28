import pygame as pg

class Player(object):
    def __init__(self,x,y,life,height,width,scr,speed):
        self.x = x
        self.y = y
        self.life = life
        self.scr = scr
        self.height = height
        self.width = width
        self.speed = speed
        self.hitbox = [self.x, self.y, self.height, self.width]

        self.ast_position = 0
        self.player_assets = ['ast1','ast2','ast3']

    def draw(self,win):
        if(self.ast_position == 3):
            self.ast_position = 0
        player = pygame.image.load(self.player_assets[self.ast_position])
        win.blit(player,(self.x, self.y))
        self.ast_position += 1
        pg.display.update()

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and keys[pg.K_UP]:
            self.x -= self.speed
            self.y -= self.speed 
        elif keys[pg.K_RIGHT] and keys[pg.K_UP]:
            self.x += self.speed
            self.y -= self.speed
        elif keys[pg.K_LEFT] and keys[pg.K_DOWN]:
            self.x -= self.speed
            self.y += self.speed
        elif keys[pg.K_RIGHT] and keys[pg.K_UP]:
            self.x += self.speed
            self.y += self.speed
        elif keys[pg.K_LEFT]:
            self.x -= self.speed
        elif keys[pg.K_RIGHT]:
            self.x += self.speed
        elif keys[pg.K_UP]:
            self.y -= self.speed
        elif keys[pg.K_DOWN]:
            self.y += self.speed