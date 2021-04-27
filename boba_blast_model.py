"""
Boba blast game model implementation.
"""
import pygame
from abc import ABC, abstractmethod

class Actor(pygame.sprite.Sprite):
    """
    Represents an actor.

    Attributes:
        _x_pos: An integer representing the x-coordinate of the location.
        _y_pos: An integer representing the y-coordinate of the location.
        _image: The image used to visually represent the Actor.
        _width: An integer representing the width of the image in pixels.
        _height: An integer representing the height of the image in pixels.
        _rect: A Rect representing the hitbox of the Actor in pixels.
        _screen: The screen/instance of the game the Actor is in.
    """
    def __init__(self):
        """
        Initializes an instance of an Actor.
        """
        super().__init__(self)
        
        self._image = None
        self.rect = self.image.get_rect()
        self._screen = None

    def __repr__(self):
        """
        """
        pass

    def move(self, dx, dy):
        """
        Moves an Actor by (dx, dy).

        Args:
            dx: An integer representing the # of pixels to move in the x-dir
            dy: An integer representing the # of pixels to move in the y-dir
        """
        self.rect.x += dx
        self.rect.y += dy

    @property
    def image(self):
        """
        Returns the value of the image attribute.
        """
        return self._image
    
    @property
    def rect(self):
        """
        Returns the value of the rect attribute.
        """
        return self._rect