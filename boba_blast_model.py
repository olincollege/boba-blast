"""
Boba blast game model implementation.
"""
import pygame, random, os
from abc import ABC, abstractmethod

class Tapioca(pygame.sprite.Sprite):
    def __init__(self, screen, groups):
        super().__init__(groups)
        game_folder = os.path.dirname(__file__)     # figures out path to the folder with this file
        images_folder = os.path.join(game_folder, 'images')
        self.image = pygame.image.load(os.path.join(images_folder, 'tapioca.png')).convert()
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect(center=(random.randint(0, screen.DISPLAY_WIDTH), 0))
        # Set hitbox for collisions
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self, screen):
        # Falls on every update.
        self.rect.y += 1
        print(f"Tapioca falls @ ({self.rect.x}, {self.rect.y})")
        if self.rect.bottom >= screen.DISPLAY_HEIGHT:
            self.kill()

class Rock(pygame.sprite.Sprite):
    def __init__(self, screen, groups):
        """
        Args:
            groups: A list with all groups to which add the Rock.
        """
        super().__init__(groups)
        game_folder = os.path.dirname(__file__)     # figures out path to the folder with this file
        images_folder = os.path.join(game_folder, 'images')
        self.image = pygame.image.load(os.path.join(images_folder, 'rock.png')).convert()
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect(center=(random.randint(0, screen.DISPLAY_WIDTH), 0))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, screen):
        self.rect.y += 5
        print(f"Rock falls @ ({self.rect.x}, {self.rect.y})")
        if self.rect.bottom >= screen.DISPLAY_HEIGHT:
            self.kill()

# class Actor(pygame.sprite.Sprite):
#     """
#     Represents an actor.

#     Attributes:
#         _x_pos: An integer representing the x-coordinate of the location.
#         _y_pos: An integer representing the y-coordinate of the location.
#         _image: The image used to visually represent the Actor.
#         _width: An integer representing the width of the image in pixels.
#         _height: An integer representing the height of the image in pixels.
#         _rect: A Rect representing the hitbox of the Actor in pixels.
#         _screen: The screen/instance of the game the Actor is in.
#     """
#     def __init__(self):
#         """
#         Initializes an instance of an Actor.
#         """
#         super().__init__(self)
        
#         self._image = None
#         self.rect = self.image.get_rect()
#         self._screen = None

#     def __repr__(self):
#         """
#         """
#         pass

#     def move(self, dx, dy):
#         """
#         Moves an Actor by (dx, dy).

#         Args:
#             dx: An integer representing the # of pixels to move in the x-dir
#             dy: An integer representing the # of pixels to move in the y-dir
#         """
#         self.rect.x += dx
#         self.rect.y += dy

#     @property
#     def image(self):
#         """
#         Returns the value of the image attribute.
#         """
#         return self._image
    
#     @property
#     def rect(self):
#         """
#         Returns the value of the rect attribute.
#         """
#         return self._rect