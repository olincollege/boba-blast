import pygame, random
pygame.init()

class Display:

    def __init__(self):
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)).fill((0, 255, 0))
        pygame.display.set_caption("Boba Blast!")
        
    def load_images(self):
        pass

    def blit(self):
        self.blit()


