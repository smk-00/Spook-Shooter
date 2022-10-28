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

        self.ast_position = 0
        self.enemy_assets = images

        self.loadcharacter()

    def loadcharacter(self):
        self.enemy_img = [pg.image.load(path) for path in self.enemy_assets]  
        self.enemy_img = [pg.transform.scale(img, (self.width, self.height)) for img in self.enemy_img]

    def draw(self,win):
        if(self.ast_position == 5):
            self.ast_position = 0
        player = self.enemy_img[self.ast_position%6]
        win.blit(player,(self.x, self.y))
        self.ast_position += 1
        pg.display.update()