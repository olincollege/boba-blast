"""
Creates and runs an instance of the Boba Blast game!
"""
import pygame, random, os
from PIL import Image
from boba_blast_view import Display

pygame.init()

# Track time
FPS = 60
fpsClock = pygame.time.Clock()

# Create display screen
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Boba Blast!")

# Load images
BLACK = (0, 0, 0)   # PNG background color
GREEN = (0, 255, 0)
game_folder = os.path.dirname(__file__)     # figures out path to the folder with this file
images_folder = os.path.join(game_folder, 'images')

tapioca_image = pygame.image.load(os.path.join(images_folder, 'tapioca.png')).convert()
rock_image = pygame.image.load(os.path.join(images_folder, 'rock.png')).convert()
player_image = pygame.image.load(os.path.join(images_folder, 'Player(1).png')).convert()
PLAYER_WIDTH, PLAYER_HEIGHT = player_image.get_size()
background_image = pygame.image.load(os.path.join(images_folder, 'background.png')).convert()
background_rect = background_image.get_rect()

all_sprites = pygame.sprite.Group()
tapioca_sprites = pygame.sprite.Group()
rock_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.GroupSingle()     # pass as argument to Player __init__

class Player(pygame.sprite.Sprite):
    """
    Create a player

    Attributes:
        image: A surface drawn on the screen visually representing a player.
    """

    def __init__(self):
        super(Player, self).__init__(all_sprites, player_sprite)
        #surface is pygame object for representing images
        self.image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.set_colorkey(BLACK)
        #pygame object for storing rectangular coordinates)
        self.rect = self.image.get_rect(bottomleft=(DISPLAY_WIDTH/2, DISPLAY_HEIGHT - PLAYER_HEIGHT))

    def move_sprite(self, pressed_keys):
        if pressed_keys[pygame.K_LEFT]:
            #move_ip() stands for move in place to move current rect
            self.rect.move_ip(-5,0)

        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)

        #set screen boundaries
        if self.rect.left < 0:
            self.rect.left = DISPLAY_WIDTH - PLAYER_WIDTH
        if self.rect.right > DISPLAY_WIDTH:
            self.rect.left = 0

class Tapioca(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites, tapioca_sprites)
        self.image = pygame.transform.scale(tapioca_image, (25, 25))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect(center=(random.randint(0, DISPLAY_WIDTH), 0))
        # self.rect.center = (random.randint(0, DISPLAY_WIDTH), 0)
    
    def update(self):
        self.rect.y += 1
        if self.rect.bottom >= DISPLAY_HEIGHT:
            self.kill()
    
    def __repr__(self):
        return f"There is tapioca at {self.rect.center}."

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites, rock_sprites)
        self.image = pygame.transform.scale(rock_image, (35, 35))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect(center=(random.randint(0, DISPLAY_WIDTH), 0))
        # self.rect.center = (random.randint(0, DISPLAY_WIDTH), 0)
    
    def update(self):
        self.rect.y += 5
        if self.rect.bottom >= DISPLAY_HEIGHT:
            self.kill()
    
    def __repr__(self):
        return f"There is a rock at {self.rect.center}."

# Ok this is the actual game section that belongs here
player = Player()   # This part isn't working

def main():
    game_over = False
    
    while not game_over:
        fpsClock.tick(FPS)

        for event in pygame.event.get():
            # check for user closing window
            if event.type == pygame.QUIT:
                game_over = True

        #use pygame get_pressed() which returns a bool dictionary containing all keys that are pressed in queue
        pressed_keys = pygame.key.get_pressed()
        
        #update player location
        player.move_sprite(pressed_keys)

        screen.blit(player.image, player.rect)

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

        # Check for collision between player instance and any rock, and delete rock is there is one
        tapioca_collision = pygame.sprite.groupcollide(player_sprite, tapioca_sprites, False, True)
        if tapioca_collision:
            # Player takes damage
            pass

        # fill background
        screen.fill(BLACK)
        screen.blit(background_image, background_rect)
        all_sprites.draw(screen)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()