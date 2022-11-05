import pygame as pg
import math

class Bullet:
    def __init__(self, bulletPath, cords, targetCords) -> None:
        self.bullet = None
        self.bulletPath = bulletPath
        self.cords = cords
        self.targetCords = targetCords
        self.width = self.height = 25
        self.hitbox = self.cords+[self.width, self.height]
        self.speed = 10

        self.angle = math.atan2(self.cords[1]-targetCords[1], self.cords[0]-targetCords[0])
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

        self.loadAssets()


    def loadAssets(self):
        self.bullet = pg.image.load(self.bulletPath)
        self.bullet = pg.transform.scale(self.bullet, (self.width, self.height))

    def draw(self, window):
        self.cords[0] -= int(self.x_vel)
        self.cords[1] -= int(self.y_vel)
        window.blit(self.bullet, self.cords)

        
class Weapon:
    def __init__(self, name, cords) -> None:
        self.name = name
        self.cords = cords
        self.bulletsFired = []
        self.gun = None
        self.bulletName = None
        self.shootSound = pg.mixer.Sound("./assets/bullet.wav")
        self.loadWeapon()


    def loadWeapon(self):
        if self.name=="pumpgun":
            self.bulletName = "pumpbullet"
            self.gun = pg.image.load("./assets/weapons/pumpgun.png")
            self.gun = pg.transform.scale(self.gun, (60, 60))


    def attachWithPlayer(self, cords):
        self.cords = cords

    def checkFire(self):
        mouse_x, mouse_y = pg.mouse.get_pos()    
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                self.bulletsFired.append(Bullet(f"./assets/weapons/{self.bulletName}.png", [self.cords[0], self.cords[1]], [mouse_x, mouse_y]))
                self.shootSound.play()

    def draw(self, window):
        window.blit(self.gun, (self.cords[0],self.cords[1]))
        for bullet in self.bulletsFired:
            if bullet.cords[0]>1366 and bullet.cords[0]<0:
                del bullet
            elif bullet.cords[1]>760 and bullet.cords[1]<0:
                del bullet
            else:
                bullet.draw(window)
        
