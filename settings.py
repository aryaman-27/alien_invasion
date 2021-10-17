# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 19:53:59 2021

@author: aryam
"""


class Settings:
    """A class to score all settings for alien invasion"""
    
    def __init__(self):
        """initialise the game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.ship_speed = 1
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
    