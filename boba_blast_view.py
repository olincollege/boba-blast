import pygame, random, os
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)   # PNG background color
GREEN = (0, 255, 0)
game_folder = os.path.dirname(__file__)     # figures out path to the folder with this file
images_folder = os.path.join(game_folder, 'images')
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PLAYER_IMAGE = pygame.image.load(os.path.join(images_folder, 'Player(1).png')).convert()
PLAYER_WIDTH, PLAYER_HEIGHT = PLAYER_IMAGE.get_size()

all_sprites = pygame.sprite.Group()
tapioca_sprites = pygame.sprite.Group()
rock_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.GroupSingle()

class Display:

    def __init__(self):
        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)).fill((0, 255, 0))
        pygame.display.set_caption("Boba Blast!")
        
    def load_images(self):
        pass

    def blit(self):
        self.blit()


class Player(pygame.sprite.Sprite):
    """
    Create a player

    Attributes:
        image: A surface drawn on the screen visually representing a player.
    """

    def __init__(self):
        super(Player, self).__init__(all_sprites, player_sprite)
        #surface is pygame object for representing images
        self.image = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.set_colorkey(BLACK)
        #pygame object for storing rectangular coordinates)
        self.rect = self.image.get_rect(bottomleft=(SCREEN_WIDTH/2, SCREEN_HEIGHT - PLAYER_HEIGHT))
        # mask for collisions
        self.mask = pygame.mask.from_surface(self.image)
        # set number of lives
        self.lives = 3

    def move_sprite(self, pressed_keys):
        if pressed_keys[pygame.K_LEFT]:
            #move_ip() stands for move in place to move current rect
            self.rect.move_ip(-5,0)

        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)

        #set screen boundaries
        if self.rect.left < 0:
            self.rect.left = SCREEN_WIDTH - PLAYER_WIDTH
        if self.rect.right > SCREEN_WIDTH:
            self.rect.left = 0

