"""
Boba blast game model implementation.
"""
import pygame, random, os, constants
from abc import ABC, abstractmethod
from boba_blast_controller import GraphicalController

class Player(pygame.sprite.Sprite):
    """
    """

    def __init__(self, screen, groups):
        """
        Args:
            groups: A list with all groups to which add the Rock.
        """
        # Add this instance of the Player to groups `all_sprites` and `player_sprite`.
        super(Player, self).__init__(groups)
        # surface is pygame object for representing images
        self.image = pygame.transform.scale(constants.PLAYER_IMAGE, (constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT))
        self.image.set_colorkey((0,0,0))
        # pygame object for storing rectangular coordinates)
        self.rect = self.image.get_rect(bottomleft=(constants.DISPLAY_WIDTH/2, constants.DISPLAY_HEIGHT - constants.PLAYER_HEIGHT))
        # mask for collisions (eventually change to just basket on head, once we have that)
        self.mask = pygame.mask.from_surface(self.image)
        # set number of lives to start with
        self.lives = 3

    def move_sprite(self, screen, pressed_keys):
        """
        Args:
            pressed_keys: 
        """
        if pressed_keys[pygame.K_LEFT]:
            # move_ip() stands for move in place to move current rect
            print("left")
            self.rect.move_ip(-5,0)

        if pressed_keys[pygame.K_RIGHT]:
            print("right")
            self.rect.move_ip(5,0)

        # set screen boundaries
        if self.rect.centerx < 0:
            self.rect.left = constants.DISPLAY_WIDTH - constants.PLAYER_WIDTH
        if self.rect.centerx > constants.DISPLAY_WIDTH:
            self.rect.left = 0

class Tapioca(pygame.sprite.Sprite):
    def __init__(self, screen, groups):
        """
        Args:
            groups: A list with all groups to which add the Rock.
        """
        # image and rect attributes need to be exactly that bc pygame accesses them
        super().__init__(groups)
        self.image = pygame.transform.scale(constants.TAPIOCA_IMAGE.convert(), (30, 30))
        self.rect = self.image.get_rect(center=(random.randint(0, constants.DISPLAY_WIDTH), 0))
        # Set hitbox for collisions
        self._mask = pygame.mask.from_surface(self.image)
    
    def update(self, screen):
        # Falls on every update.
        self.rect.y += 2
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
        self.rect = self.image.get_rect(center=(random.randint(0, constants.DISPLAY_WIDTH), 0))
        self._mask = pygame.mask.from_surface(self.image)

    def update(self, screen):
        self.rect.y += 4
        print(f"Rock falls @ ({self.rect.x}, {self.rect.y})")
        if self.rect.bottom >= constants.DISPLAY_HEIGHT:
            self.kill()
