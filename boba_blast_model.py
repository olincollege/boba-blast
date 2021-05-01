"""
Boba blast game model implementation.
"""
import pygame, random, os, constants
from abc import ABC, abstractmethod

class Tapioca(pygame.sprite.Sprite):
    def __init__(self, screen, groups):
        # image and rect attributes need to be exactly that bc pygame accesses them
        super().__init__(groups)
        self.image = pygame.transform.scale(constants.TAPIOCA_IMAGE.convert(), (25, 25))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(random.randint(0, constants.DISPLAY_WIDTH), 0))
        # Set hitbox for collisions
        self._mask = pygame.mask.from_surface(self.image)
    
    def update(self, screen):
        # Falls on every update.
        self.rect.y += 4
        print(f"Tapioca falls @ ({self.rect.x}, {self.rect.y})")
        if self.rect.bottom >= constants.DISPLAY_HEIGHT:
            self.kill()

class Rock(pygame.sprite.Sprite):
    def __init__(self, screen, groups):
        """
        Args:
            groups: A list with all groups to which add the Rock.
        """
        super().__init__(groups)
        self.image = pygame.transform.scale(constants.ROCK_IMAGE.convert(), (35, 35))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(random.randint(0, constants.DISPLAY_WIDTH), 0))
        self._mask = pygame.mask.from_surface(self.image)

    def update(self, screen):
        self.rect.y += 3
        print(f"Rock falls @ ({self.rect.x}, {self.rect.y})")
        if self.rect.bottom >= constants.DISPLAY_HEIGHT:
            self.kill()
