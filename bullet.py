import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        #在飞船位置创建一个子弹对象
        super(Bullet,self).__init__()
        self.screen=screen

        #在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,
            ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top=ship.rect.top

        #存储子弹位置
        self.y = float(self.rect.y)

        self.colour = ai_settings.bullet_colour
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.y -=self.speed_factor
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.colour,self.rect)

    