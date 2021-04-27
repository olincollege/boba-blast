"""
Creates and runs an instance of the Boba Blast game!
"""
import pygame, random, os
from boba_blast_view import Display

pygame.init()

# Track time
FPS = 60
fpsClock = pygame.time.Clock()

# Create display screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Boba Blast!")

BLACK = (0, 0, 0)   # PNG background color
GREEN = (0, 255, 0)
game_folder = os.path.dirname(__file__)     # figures out path to the folder with this file
images_folder = os.path.join(game_folder, 'images')
tapioca_image = pygame.image.load(os.path.join(images_folder, 'tapioca.png')).convert()

all_sprites = pygame.sprite.Group()
tapioca_sprites = pygame.sprite.Group()
rock_sprites = pygame.sprite.Group()

class FallingObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites, tapioca_sprites)
        self.image = tapioca_image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (self.image.get_width() / 2, self.image.get_height() / 2)
    
    def update(self):
        self.rect.y += 5
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.kill()

falling_tapioca = FallingObject()

game_over = False
while not game_over:
    fpsClock.tick(FPS)

    for event in pygame.event.get():
        # check for user closing window
        if event.type == pygame.QUIT:
            game_over = True

    all_sprites.update()

    # fill background
    screen.fill(GREEN)
    all_sprites.draw(screen)

    pygame.display.flip()

    # if pygame.time.get_ticks() % 1500:
    #     # generate tapioca instance and view
    #     pass
    # elif pygame.time.get_ticks() % 2500:
    #     # generate rock instance and view
    #     pass

pygame.quit()
