"""
Implement the sprites for Boba Blast.
"""
from abc import abstractmethod
import random
import pygame
import constants


class Player(pygame.sprite.Sprite):
    """
    A Player class represents the player on screen.

    Attributes:
        image: An image visually representing the Player.
        rect: A Pygame rect for storing rectangular coordinates
        _mask: A Pygame mask for collision detection.
        lives: An integer representing the number of lives a player has.
    """

    def __init__(self, groups):
        """
        Initializes a Player.

        Args:
            groups: A list with all groups to which add the Player.
        """
        # Add this instance of the Player to groups `all_sprites` and `player_sprite`.
        super().__init__(groups)
        # surface is pygame object for representing images
        self.image = constants.PLAYER_IMAGE.convert()
        # pygame object for storing rectangular coordinates
        self.rect = self.image.get_rect(bottomleft=(
            constants.DISPLAY_WIDTH/2, constants.DISPLAY_HEIGHT - constants.PLAYER_HEIGHT))
        # mask for collisions (eventually change to just basket on head, once we have that)
        self._mask = pygame.mask.from_surface(self.image)
        # set number of lives to start with
        self.lives = 3

    def move_sprite(self, pressed_keys):
        """
        Takes keyboard input and moves location of the Player.

        Args:
            pressed_keys: A sequence representing the keys a user presses.
        """
        if pressed_keys[pygame.K_LEFT]:
            # move_ip() stands for move in place to move current rect
            self.rect.move_ip(-5, 0)

        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

        # set screen boundaries
        if self.rect.centerx < 0:
            self.rect.left = constants.DISPLAY_WIDTH - constants.PLAYER_WIDTH
        if self.rect.centerx > constants.DISPLAY_WIDTH:
            self.rect.left = 0


class FallingObject(pygame.sprite.Sprite):
    """
    A class to represent all Falling Objects, aka tapioca and rocks.

    Attributes:
        image: An image visually representing the FallingObject.
        rect: A Pygame rect for storing rectangular coordinates
        _mask: A Pygame mask for collision detection.
    """

    def __init__(self, groups, graphic):
        """
        Args:
            groups: A list with all groups to which add the Rock.
            graphic: The image to use.
        """
        # image and rect attributes need to be exactly that bc pygame accesses them
        super().__init__(groups)
        self.image = pygame.transform.scale(
            graphic.convert(), (30, 30))
        self.rect = self.image.get_rect(
            center=(random.randint(0, constants.DISPLAY_WIDTH), 0))
        # Set hitbox for collisions
        self._mask = pygame.mask.from_surface(self.image)

    @abstractmethod
    def update(self, rate):
        """
        Args:
            rate: An integer representing the number of pixels to fall per tick
        """
        self.rect.y += rate
        # Remove instance if it has reached bottom of screen
        if self.rect.bottom >= constants.DISPLAY_HEIGHT:
            self.kill()


class Tapioca(FallingObject):
    """
    A class representing an instance of a tapioca pearl.
    """

    def __init__(self, groups):
        """
        Creates an instance of a Tapioca.

        Args:
            groups: A list with all groups to which add the Tapioca.
        """
        super().__init__(groups, constants.TAPIOCA_IMAGE)

    def update(self):
        """
        Defines the Rock as falling 4 pixels per tick.
        """
        super().update(2)


class Rock(FallingObject):
    """
    A class representing an instance of a Rock.
    """

    def __init__(self, groups):
        """
        Creates an instance of a Rock.

        Args:
            groups: A list with all groups to which add the Rock.
        """
        super().__init__(groups, constants.ROCK_IMAGE)

    def update(self):
        """
        Defines the Rock as falling 4 pixels per tick.
        """
        super().update(4)
