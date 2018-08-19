import pygame

from pygame.sprite import Sprite

'''
子弹类
'''
class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        # 在飞船所处的位置创建一个子弹对象
        super(Bullet, self).__init__()
        self.screen = screen
        # 子弹位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 子弹位置
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # 更新子弹的数量
        self.y -= self.speed_factor
        # 更新子弹位置
        self.rect.y = self.y

    def draw_bullet(self):
        # 绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)