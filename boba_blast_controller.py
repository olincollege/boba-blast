"""
Creates the controller for the boba blast game
"""
import pygame

class GraphicalController:
    """
    pylint
    """

    def __init__(self):
        """
        pylint
        """
        pass

    def get_move(self):
        """
        pylint
        """
        pressed_keys = pygame.key.get_pressed()
        return pressed_keys

    def check_exit(self):
        """
        pylint
        """
        for event in pygame.event.get():
            # check for user closing window
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
