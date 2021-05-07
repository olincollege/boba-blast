"""
Store constant values for Boba Blast.
"""

import os
import pygame
pygame.init()

# Frames per second
FPS = 60

# figures out path to the folder with this file
GAME_FOLDER = os.path.dirname(__file__)
IMAGES_FOLDER = os.path.join(GAME_FOLDER, 'images')


BACKGROUND_IMAGE = pygame.image.load(
    os.path.join(IMAGES_FOLDER, 'Boba-Blast-Background.png'))
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

SPRITESHEET = pygame.image.load(
    os.path.join(IMAGES_FOLDER, 'Spritesheet.png'))
SPRITESHEET_WIDTH, SPRITESHEET_HEIGHT = SPRITESHEET.get_size()
SCALED_SPRITESHEET_WIDTH = int(SPRITESHEET_WIDTH * 0.5)
SCALED_SPRITESHEET_HEIGHT = int(SPRITESHEET_HEIGHT * 0.5)


PLAYER_WIDTH = 123
PLAYER_HEIGHT = 200

WELCOME_IMAGE = pygame.image.load(os.path.join(
    IMAGES_FOLDER, 'Boba-Blast-Welcome.png'))  # .convert()
WELCOME_IMAGE = pygame.transform.scale(WELCOME_IMAGE, (800, 600))


END_IMAGE = pygame.image.load(os.path.join(
    IMAGES_FOLDER, 'Boba-Blast-End.png'))  # .convert()
END_IMAGE = pygame.transform.scale(END_IMAGE, (800, 600))


LIVES_IMAGE = pygame.image.load(os.path.join(
    IMAGES_FOLDER, 'Boba-Blast(2)-lives.png'))
LIVES_IMAGE = pygame.transform.scale(LIVES_IMAGE, (45, 45))
LIVES_IMAGE.set_colorkey((255, 255, 255))
