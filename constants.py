import pygame, os
pygame.init()

# Frames per second
FPS = 60

#
GAME_FOLDER = os.path.dirname(__file__)     # figures out path to the folder with this file
IMAGES_FOLDER = os.path.join(GAME_FOLDER, 'images')

BACKGROUND_IMAGE = pygame.image.load(os.path.join(IMAGES_FOLDER, 'background.png'))
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

TAPIOCA_IMAGE = pygame.image.load(os.path.join(IMAGES_FOLDER, 'tapioca.png'))
ROCK_IMAGE = pygame.image.load(os.path.join(IMAGES_FOLDER, 'rock.png'))

PLAYER_IMAGE = pygame.image.load(os.path.join(IMAGES_FOLDER, 'Player(1).png'))
PLAYER_WIDTH, PLAYER_HEIGHT = PLAYER_IMAGE.get_size()

LIVES_IMAGE = pygame.image.load(os.path.join(IMAGES_FOLDER, 'lives.png'))
LIVES_IMAGE = pygame.transform.scale(LIVES_IMAGE, (35, 35))
LIVES_IMAGE.set_colorkey((247, 247, 247))

BOBA_IMAGE = pygame.image.load(os.path.join(IMAGES_FOLDER, 'boba.png'))
BOBA_IMAGE.set_colorkey((247, 247, 247))