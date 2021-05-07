"""
Creates the controller for the boba blast game.
"""
import sys
import pygame


class GraphicalController:
    """
    Creates an instance of a GraphicalController which takes player input.
    """

    def __init__(self):
        """
        Initializes the object's state
        """
        pass

    def get_move(self):
        """
        Gets the keys that the user is pressing

        Returns:
        pressed_keys: A sequence of boolean values containing the state
        of every key on the keyboard, with True indicating a key is pressed.
        """
        pygame.init()
        pressed_keys = pygame.key.get_pressed()
        return pressed_keys

    def check_exit(self):
        """
        Checks whether the user is wanting to exit the window and stops the
        pygame program from running.
        """
        for event in pygame.event.get():
            # check for user closing window
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
                pygame.mixer.stop()
                break
