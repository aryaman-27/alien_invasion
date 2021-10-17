# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 20:22:59 2021

@author: aryam
"""

import pygame

class Ship:
    """A class to manage the ship"""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()
        
        # start each new ship at the bottom centre of the screen
        self.rect.midbottom = self.screen_rect.midbottom
           
        self.x = float(self.rect.x)
            
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
                    
        self.rect.x = self.x
                    
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)


