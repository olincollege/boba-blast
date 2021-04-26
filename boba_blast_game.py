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

game_over = False
while not game_over:
    if pygame.time.get_ticks() % 1500:
        # generate tapioca instance and view
        pass
    elif pygame.time.get_ticks() % 2500:
        # generate rock instance and view
        pass


pygame.Display.update()
fpsClock.tick(FPS)