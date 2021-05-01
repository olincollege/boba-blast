"""
Creates the controller for the boba blast game
"""
import pygame, random, os

class GraphicalController:
    """
    """
    def __init__(self):
        pass

    def get_move(self):
        pressed_keys = pygame.key.get_pressed()
        return pressed_keys

    def check_exit(self):
        for event in pygame.event.get():
            # check for user closing window
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
