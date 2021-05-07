"""
Creates the controller for the boba blast game.
"""
import sys
import pygame


class GraphicalController:
    """
    Creates an instance of a GraphicalController, which takes player input.
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
        pygame.init()
        pressed_keys = pygame.key.get_pressed()
        return pressed_keys

    def check_exit(self):
        """
        pylint
        """
        for event in pygame.event.get():
            # check for user closing window
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
                pygame.mixer.stop()
                break
