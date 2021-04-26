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
        _rect: A Rect representing the hitbox of the ACtor in pixels.
    """
    def __init__(self, image):
        """
        Initializes an instance of an Actor.
        """
        self._x_pos = None
        self._y_pos = None
        self._image = image
        self._width = image.get_width()
        self._height = image.get_height()
        self._rect = pygame.Rect(x_pos, y_pos, width, height)

    def __repr__(self):
        """
        """
        pass

    @property
    def x_pos(self):
        """
        Returns the value of the _x_pos attribute.
        """
        return self._x_pos

    @property
    def y_pos(self):
        """
        Returns the value of the _y_pos attribute.
        """
        return self._y_pos
    
    @property
    def width(self):
        """
        Returns the value of the width attribute.
        """
        return self._width
    
    @property
    def height(self):
        """
        Returns the value of the height attribute.
        """
        return self._height
    
    @property
    def rect(self):
        """
        Returns the value of the rect attribute.
        """
        return self._rect