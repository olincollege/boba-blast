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

# Load images
BLACK = (0, 0, 0)   # PNG background color
GREEN = (0, 255, 0)
game_folder = os.path.dirname(__file__)     # figures out path to the folder with this file
images_folder = os.path.join(game_folder, 'images')

tapioca_image = pygame.image.load(os.path.join(images_folder, 'tapioca.png')).convert()
rock_image = pygame.image.load(os.path.join(images_folder, 'rock.png')).convert()
background_image = pygame.image.load(os.path.join(images_folder, 'background.png')).convert()
background_rect = background_image.get_rect()

all_sprites = pygame.sprite.Group()
tapioca_sprites = pygame.sprite.Group()
rock_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.GroupSingle()     # pass as argument to Player __init__

class Tapioca(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites, tapioca_sprites)
        self.image = pygame.transform.scale(tapioca_image, (25, 25))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, SCREEN_WIDTH), 0)
    
    def update(self):
        self.rect.y += 1
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.kill()

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites, rock_sprites)
        self.image = pygame.transform.scale(rock_image, (35, 35))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, SCREEN_WIDTH), 0)
    
    def update(self):
        self.rect.y += 5
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.kill()

# Ok this is the actual game section that belongs here
game_over = False
while not game_over:
    fpsClock.tick(FPS)

    for event in pygame.event.get():
        # check for user closing window
        if event.type == pygame.QUIT:
            game_over = True

    if pygame.time.get_ticks() % 500 == 0:
        Rock()
    elif pygame.time.get_ticks() % 150 == 0:
        Tapioca()
    all_sprites.update()

    # Check for collision between player instance and any tapioca, and delete tapioca if there is one
    tapioca_collision = pygame.sprite.groupcollide(player_sprite, tapioca_sprites, False, True)
    if tapioca_collision:
        # Increment player's tapioca count by 1
        pass

    # fill background
    screen.fill(GREEN)
    screen.blit(background_image, background_rect)
    all_sprites.draw(screen)

    pygame.display.flip()


pygame.quit()
