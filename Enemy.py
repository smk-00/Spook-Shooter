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

    def draw(self,win):
        if(self.ast_position == 3):
            self.ast_position = 0
        player = pygame.image.load(self.enemy_assets[self.ast_position])
        win.blit(player,(self.x, self.y))
        self.ast_position += 1
        pg.display.update()