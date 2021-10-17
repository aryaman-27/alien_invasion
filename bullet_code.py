# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 12:02:34 2021

@author: aryam
"""


import pygame
from pygame.sprite import Sprite
from ship_code import Ship

class Bullet(Sprite):
    """A class to manage bullets"""
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        self.y = float(self.rect.y)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
    def update(self):
        """Move the bullet up to the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)