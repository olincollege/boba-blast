"""
Boba blast game model implementation.
"""
import pygame


class Actor(pygame.sprite.Sprite):
    """
    Represents an actor.

    Attributes:
        _x_pos: An integer representing the x-coordinate of the location.
        _y_pos: An integer representing the y-coordinate of the location.
    """
    def __init__(self):
        """
        Initializes an instance of an Actor.
        """
        self._x_pos = None
        self._y_pos = None

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