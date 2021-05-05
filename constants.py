import pygame
import os
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

SPRITESHEET = pygame.image.load(os.path.join(IMAGES_FOLDER, 'Spritesheet-07.png'))

WELCOME_IMAGE = pygame.image.load(os.path.join(IMAGES_FOLDER, 'Boba-Blast-Welcome.png'))#.convert()
WELCOME_IMAGE = pygame.transform.scale(WELCOME_IMAGE, (800,600))


END_IMAGE = pygame.image.load(os.path.join(IMAGES_FOLDER, 'Boba-Blast-End.png'))#.convert()
END_IMAGE = pygame.transform.scale(END_IMAGE, (800,600))



TAPIOCA_IMAGE = pygame.image.load(os.path.join(
    IMAGES_FOLDER, 'Boba-Blast(2)-05-tapioca.png'))
TAPIOCA_IMAGE.set_colorkey((255, 255, 255))

ROCK_IMAGE = pygame.image.load(os.path.join(
    IMAGES_FOLDER, 'Boba-Blast(2)-05-rock.png'))
ROCK_IMAGE.set_colorkey((255, 255, 255))

PLAYER_IMAGE = pygame.image.load(os.path.join(IMAGES_FOLDER, 'player-facing-front.png'))
PLAYER_IMAGE.set_colorkey((0,255,128))
PLAYER_WIDTH, PLAYER_HEIGHT = PLAYER_IMAGE.get_size()
SCALED_PLAYER_WIDTH = int(PLAYER_WIDTH * 0.1)
SCALED_PLAYER_HEIGHT = int(PLAYER_HEIGHT * 0.1)

LIVES_IMAGE = pygame.image.load(os.path.join(IMAGES_FOLDER, 'Boba-Blast(2)-lives.png'))
LIVES_IMAGE = pygame.transform.scale(LIVES_IMAGE, (45, 45))
LIVES_IMAGE.set_colorkey((255, 255, 255))
