# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 20:22:59 2021

@author: aryam
"""

import pygame
from pygame.sprite import Sprite
from time import sleep

class Ship(Sprite):
    """A class to manage the ship"""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.explosion_value = 0
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()


        # start each new ship at the bottom centre of the screen
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False
        self.ship_exploded = False
        self.explosion_images = []
        self.explosion_rect = []
        for i in range(4):
            self.explosion_images.append(pygame.image.load('images/explosion%d.bmp'%(i+1)))
            self.explosion_rect.append(self.explosion_images[i].get_rect())
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

        if 0 < self.explosion_value < 5:
            self.explosion_value += 1
            self.explosion_rect[self.explosion_value-1].midbottom = self.rect.midbottom

                    
    def blitme(self):
        """Draw the ship at its current location"""
        if self.explosion_value == 0:
            self.screen.blit(self.image, self.rect)
        else:
            self.screen.blit(self.explosion_images[self.explosion_value-1], self.explosion_rect[self.explosion_value-1])

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def startExplosion(self):
        if self.explosion_value == 0:
            self.explosion_value = 1
            self.explosion_rect[0].midbottom = self.rect.midbottom

    def explosionComplete(self):
        if self.explosion_value >= 4:
            self.explosion_value = 0
            return True
        else:
            return False

    def explosionInProgress(self):
        if self.explosion_value > 0 and self.explosion_value < 5:
            return True
        else:
            return False
