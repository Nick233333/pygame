# -*- coding: utf-8 -*-
'''
设置类
'''
class Settings():

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 500
        self.bg_color = (230, 230, 230)
        # 飞船的移动速度
        self.ship_speed_factor = 3.5
        # 子弹设置
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 51, 0
        self.bullets_allowed = 10
        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1