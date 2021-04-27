"""
Creates and runs an instance of the Boba Blast game!
"""
import pygame, random
from boba_blast_view import Display

pygame.init()

# Track time
FPS = 60
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))

BLACK = (0, 0, 0)   # temporary background color
GREEN = (0, 255, 0)
tapioca_image = pygame.image.load('tapioca.png')
rock_image = pygame.image.load('rock.png')

all_sprites = pygame.sprite.Group()
tapioca_sprites = pygame.sprite.Group()
rock_sprites = pygame.sprite.Group()

class FallingObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites, tapioca_sprites)
        self.image = tapioca_image
        # self.image = pygame.Surface((50, 50))
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (self.image.get_width() / 2, self.image.get_height() / 2)

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
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()

    # if pygame.time.get_ticks() % 1500:
    #     # generate tapioca instance and view
    #     pass
    # elif pygame.time.get_ticks() % 2500:
    #     # generate rock instance and view
    #     pass

pygame.quit()
