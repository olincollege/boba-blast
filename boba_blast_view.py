"""
pylint
"""

import pygame
import constants
pygame.init()


class Display():
    """
    pylint
    """
    # Create display screen

    def __init__(self, screen):
        self._screen = screen

    def fill_background(self, color):
        """
        Args:
            color: A tuple, (R, G, B), representing a color.
        """
        self._screen.fill(color)

    def draw_background(self, image, dims):
        """
        Draws the background image.

        Args:
            image: Image to blit.
            dims: Dimensions of the display, as an integer tuple
        """
        _rect = image.get_rect()
        _image = pygame.transform.scale(image, dims)
        self._screen.blit(_image, _rect)

    def screen_blit(self, image, rect):
        """
        Blits a sprite.
        """
        self._screen.blit(image, rect)

    def draw_group(self, group):
        """
        Draws all sprites in a group onto a surface.

        Args:
            group: The group of sprites to be drawn.
        """
        group.draw(self._screen)

    def draw_lives(self, x_pos, y_pos, lives):
        """
        Draw images representing the number of lives the player has.

        Args:
            x_pos: An integer representing the x_pos-coordinate of the image.
            y_pos: An integer representing the y_pos-coordinate of the image.
            lives: An integer representing the number of lives a player has.
        """
        for i in range(lives):
            img_rect = constants.LIVES_IMAGE.get_rect()
            img_rect.x = x_pos + 40 * i
            img_rect.y = y_pos
            self._screen.blit(constants.LIVES_IMAGE, img_rect)

    # all fonts: pygame.font.get_fonts()
    def draw_text(self, text, size, x_pos, y_pos):
        """
        Draw text on the screen.

        Args:
            surf: Surface on which to draw.
            text: A string representing the text to render.
            size: An integer representing the size of the text.
            x_pos: An integer representing the x_pos-coordinate of the text.
            y_pos: An integer representing the y_pos-coordinate of the text.
        """

        font_name = pygame.font.match_font('sarai')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x_pos, y_pos)
        self._screen.blit(text_surface, text_rect)
