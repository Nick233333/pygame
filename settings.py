# -*- coding: utf-8 -*-
'''
设置类
'''
class Settings():

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # 飞船的移动速度
        self.ship_speed_factor = 5
        self.ship_limit = 3
        # 子弹设置
        self.bullet_speed_factor = 2
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 255, 51, 0
        self.bullets_allowed = 10
        # 外星人设置
        self.alien_speed_factor = 8
        self.fleet_drop_speed = 5
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        self.score_scale = 1.5

        self.speedup_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 3
        # fleet_direction为1表示向右;为-1表示向左
        self.fleet_direction = 2
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
