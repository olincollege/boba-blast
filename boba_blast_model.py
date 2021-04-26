"""
Boba blast game model implementation.
"""
import pygame


class Actor(pygame.sprite.Sprite):
    """
    Represents an actor.

    Attributes:
        _x_value: An integer representing the x-coordinate of the location.
        _y_value: An integer representing the y-coordinate of the location.
    """
    def __init__(self):
        """
        Initializes an instance of an Actor.
        """
        self._x_value = None
        self._y_value = None

    def __repr__(self):
        """
        """
        pass

    @property
    def x_value(self):
        """
        Returns the value of the _x_value attribute.
        """
        return self._x_value

    @property
    def y_value(self):
        """
        Returns the value of the _y_value attribute.
        """
        return self._y_value