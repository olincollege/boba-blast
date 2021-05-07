"""
Implement the sprites for Boba Blast.
"""
from abc import abstractmethod
import random
import pygame
import constants

pygame.init()


class Spritesheet():
    """
    Access spritesheet.

    Attributes:
        _sheet: An image representing the spritesheet.
    """
    screen = pygame.display.set_mode((800, 600))

    def __init__(self):
        """
        Initialize the spritesheet.
        """
        self._sheet = constants.SPRITESHEET.convert()
        self._sheet = pygame.transform.scale(self._sheet,
            (constants.SCALED_SPRITESHEET_WIDTH,
            constants.SCALED_SPRITESHEET_HEIGHT))

    def get_image(self, x_pos, y_pos, width, height):
        """
        Get an image from the spritesheet.
        """
        image = pygame.Surface([width, height]).convert()
        # copy sprite from large sheet onto smaller image
        image.blit(self._sheet, (0, 0), (x_pos, y_pos, width, height))
        image.set_colorkey((68, 68, 68), pygame.RLEACCEL)
        return image


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

        # create list that stores player images
        spritesheet = Spritesheet()
        self.image = spritesheet.get_image(0, 66, 123, 200)
        self.rect = self.image.get_rect()

        self.y_pos = constants.DISPLAY_HEIGHT - 175/2
        self.x_pos = constants.DISPLAY_WIDTH/2
        self.rect.midbottom = (self.x_pos, self.y_pos)

        self.animation_index_left = 0
        self.animation_index_right = 0

        #create a list that stores all the player animation images
        self.static_image = self.image
        self.animate_right = []
        self.animate_left = []

        self.right0 = spritesheet.get_image(123, 67, constants.PLAYER_WIDTH,
            constants.PLAYER_HEIGHT)
        self.right1 = spritesheet.get_image(246, 66, constants.PLAYER_WIDTH,
            constants.PLAYER_HEIGHT)
        self.right2 = spritesheet.get_image(369, 67, constants.PLAYER_WIDTH,
            constants.PLAYER_HEIGHT)
        self.right3 = spritesheet.get_image(246, 66, constants.PLAYER_WIDTH,
            constants.PLAYER_HEIGHT)
        self.left0 = spritesheet.get_image(492, 333, constants.PLAYER_WIDTH,
            constants.PLAYER_HEIGHT)
        self.left1 = spritesheet.get_image(368, 333, constants.PLAYER_WIDTH,
            constants.PLAYER_HEIGHT)
        self.left2 =spritesheet.get_image(492, 66, constants.PLAYER_WIDTH,
            constants.PLAYER_HEIGHT)
        self.left3 =spritesheet.get_image(368, 333, constants.PLAYER_WIDTH,
            constants.PLAYER_HEIGHT)

        self.animate_right.extend([self.right0, self.right1, self.right2,
            self.right3])
        self.animate_left.extend([self.left0, self.left1, self.left2,
            self.left3])

        # mask for collisions
        self._mask = pygame.mask.from_surface(self.image)
        # set number of lives to start with
        self.lives = 3

    def move_sprite(self, pressed_keys):
        """
        Takes keyboard input and moves location of the Player.

        Args:
            pressed_keys: A sequence representing the keys a user presses.
        """
        if self.animation_index_left > 3:
            self.animation_index_left = 0
        if self.animation_index_right > 3:
            self.animation_index_right = 0

        #player moves left
        if pressed_keys[pygame.K_LEFT]:
            self.image = self.animate_left[self.animation_index_left//3]
            self.rect = self.image.get_rect()
            self.rect.midbottom = (self.x_pos, self.y_pos)
            self.rect.move(-4, 0)
            self.animation_index_left += 1
            self.x_pos = self.x_pos-4

        #player moves right
        elif pressed_keys[pygame.K_RIGHT]:
            self.image = self.animate_right[self.animation_index_right//3]
            self.rect = self.image.get_rect()
            self.rect.midbottom = (self.x_pos, self.y_pos)
            self.rect.move(4, 0)
            self.animation_index_right += 1
            self.x_pos = self.x_pos+4

        #player is static
        else:
            self.image = self.static_image
            self.rect = self.image.get_rect()
            self.rect.midbottom = (self.x_pos, self.y_pos)

        # set screen boundaries
        if self.rect.centerx < 0:
            self.x_pos = constants.DISPLAY_WIDTH
            self.rect.midbottom = (self.x_pos, self.y_pos)
        if self.rect.centerx > constants.DISPLAY_WIDTH:
            self.x_pos = 0
            self.rect.midbottom = (self.x_pos, self.y_pos)


class FallingObject(pygame.sprite.Sprite):
    """
    A class to represent all Falling Objects, aka tapioca and rocks.

    Attributes:
        image: An image visually representing the FallingObject.
        rect: A Pygame rect for storing rectangular coordinates
        _mask: A Pygame mask for collision detection.
    """

    def __init__(self, groups, sprite_coords):
        """
        Args:
            groups: A list with all groups to which add the Rock.
            graphic: The image to use.
        """
        # image and rect attributes need to be exact bc pygame accesses them
        super().__init__(groups)
        spritesheet = Spritesheet()
        self.image = spritesheet.get_image(sprite_coords[0], sprite_coords[1],
                                           sprite_coords[2], sprite_coords[3])

        self.image = pygame.transform.scale(self.image, (30, 30))
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
        super().__init__(groups, [246, 333, 133, 123])

    def update(self, rate=9):
        """
        Defines the Rock as falling 1 pixel per tick.
        """
        super().update(1)


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
        super().__init__(groups, [123, 333, 133, 123])

    def update(self, rate=12):
        """
        Defines the Rock as falling 3 pixels per tick.
        """
        super().update(3)

def is_collision(group1, group2):
    """
    Checks for a collision between two sprite groups, and removes the
    sprite in group2 if a collision occurs.

    Args:
        group1: A pygame sprite group.
        group2: A pygame sprite group, different instance than group1.

    Returns:
        Boolean True if collision, False otherwise.
    """
    return pygame.sprite.groupcollide(group1, group2, False, True,
        pygame.sprite.collide_mask)
