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
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 15

        # 1 is right and -1 is left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        """Initialise settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    