"""
Creates and runs an instance of the Boba Blast game!
"""
import pygame
pygame.init()

# Track time
FPS = 60
fpsClock = pygame.time.Clock()


tapioca_image = pygame.image.load('tapioca.png').convert()
rock_image = pygame.image.load('rock.png').convert()


pygame.Display.update()
fpsClock.tick(FPS)