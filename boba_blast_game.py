"""
Creates and runs an instance of the Boba Blast game!
"""
import pygame, random, os
from boba_blast_controller import GraphicalController
from boba_blast_view import Display
from boba_blast_model import Rock, Tapioca


pygame.init()
pygame.mixer.init() #for sound

# Track time
FPS = 60
fpsClock = pygame.time.Clock()

# # Load images
game_folder = os.path.dirname(__file__)     # figures out path to the folder with this file
images_folder = os.path.join(game_folder, 'images')

tapioca_image = pygame.image.load(os.path.join(images_folder, 'tapioca.png')).convert()
rock_image = pygame.image.load(os.path.join(images_folder, 'rock.png')).convert()

player_image = pygame.image.load(os.path.join(images_folder, 'Player(1).png')).convert()
PLAYER_WIDTH, PLAYER_HEIGHT = player_image.get_size()

lives_image = pygame.image.load(os.path.join(images_folder, 'lives.png')).convert()
lives_image = pygame.transform.scale(lives_image, (35, 35))
lives_image.set_colorkey((247, 247, 247))

boba_image = pygame.image.load(os.path.join(images_folder, 'boba.png')).convert()
boba_image.set_colorkey((247, 247, 247))

def draw_lives(surf, x, y, lives, lives_image):
    """
    Draw images representing the number of lives the player has.

    Args:
        surf: Surface on which to draw.
        x: An integer representing the x-coordinate of the image.
        y: An integer representing the y-coordinate of the image.
        lives: An integer representing the number of lives a player has.
        lives_image: An image representing a life.
    """
    for i in range(lives):
        img_rect = lives_image.get_rect()
        img_rect.x = x + 40 * i
        img_rect.y = y
        surf.blit(lives_image, img_rect)

def draw_boba(surf, x, y, score, boba_image):
    """
    Draw images representing the number of drinks a player has collected.

    Args:
        surf: Surface on which to draw.
        x: An integer representing the x-coordinate of the image.
        y: An integer representing the y-coordinate of the image.
        score: An integer representing the player's score (number of tapioca).
        boba_image: An image representing one boba drink.
    """
    # 10 tapioca = 1 boba
    bobas = score // 10
    for i in range(bobas):
        img_rect = boba_image.get_rect()
        img_rect.x = x + 20 * i
        img_rect.y = y
        surf.blit(boba_image, img_rect)

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    """
    Draw text on the screen.

    Args:
        surf: Surface on which to draw.
        text: A string representing the text to render.
        size: An integer representing the size of the text.
        x: An integer representing the x-coordinate of the text.
        y: An integer representing the y-coordinate of the text.
    """
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

all_sprites = pygame.sprite.Group()
tapioca_sprites = pygame.sprite.Group()
rock_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.GroupSingle()

class Player(pygame.sprite.Sprite):
    """
    """

    def __init__(self, screen):
        # Add this instance of the Player to groups `all_sprites` and `player_sprite`.
        super(Player, self).__init__(all_sprites, player_sprite)
        # surface is pygame object for representing images
        self.image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.set_colorkey((0,0,0))
        # pygame object for storing rectangular coordinates)
        self.rect = self.image.get_rect(bottomleft=(screen.DISPLAY_WIDTH/2, screen.DISPLAY_HEIGHT - PLAYER_HEIGHT))
        # mask for collisions (eventually change to just basket on head, once we have that)
        self.mask = pygame.mask.from_surface(self.image)
        # set number of lives to start with
        self.lives = 3

    def move_sprite(self, screen, pressed_keys):
        """
        Args:
            pressed_keys: 
        """
        if pressed_keys[pygame.K_LEFT]:
            # move_ip() stands for move in place to move current rect
            print("left")
            self.rect.move_ip(-5,0)

        if pressed_keys[pygame.K_RIGHT]:
            print("right")
            self.rect.move_ip(5,0)

        # set screen boundaries
        if self.rect.centerx < 0:
            self.rect.left = screen.DISPLAY_WIDTH - PLAYER_WIDTH
        if self.rect.centerx > screen.DISPLAY_WIDTH:
            self.rect.left = 0


# Ok this is the actual game section that belongs here
class Game:
    user = GraphicalController()
    game_over = False
    score = 0

    game_folder = os.path.dirname(__file__)     # figures out path to the folder with this file
    images_folder = os.path.join(game_folder, 'images')
    background_image = pygame.image.load(os.path.join(images_folder, 'background.png')).convert()
    DISPLAY_WIDTH = 800
    DISPLAY_HEIGHT = 600

    # def __init__(self, width, height, background_image):
    #     super().__init__((width, height))
    #     pygame.display.set_caption("Boba Blast!")

    # game_surface = pygame.Surface((800, 600))
    screen = pygame.display.set_mode((800, 600))
    screen = Display(screen)
    # screen = Display(DISPLAY_WIDTH, DISPLAY_HEIGHT, background_image)
    screen.load_images()
    # screen.draw_background(screen)
    screen.fill_background()
        
    player = Player(screen)   # This part isn't working
    # user = GraphicalController()

    while not game_over:
        fpsClock.tick(FPS)
        if player.lives == 0:
            game_over = True

        for event in pygame.event.get():
            # check for user closing window
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
        
        # # get user moves
        pressed_keys = user.get_move()

        #update player location
        player.move_sprite(screen, pressed_keys)
        screen.screen_blit(player.image, player.rect)

        if pygame.time.get_ticks() % 500 == 0:
            Rock(screen, [all_sprites, rock_sprites])
        elif pygame.time.get_ticks() % 150 == 0:
            Tapioca(screen, [all_sprites, tapioca_sprites])
        # Calls the update method of each group
        all_sprites.update(screen)

        # Check for collision between player instance and any tapioca, and delete tapioca if there is one
        tapioca_collision = pygame.sprite.groupcollide(player_sprite, tapioca_sprites, False, True, pygame.sprite.collide_mask)
        if tapioca_collision:
            # Increment score by 1
            score += 1

        # Check for collision between player instance and any rock, and delete rock is there is one
        rock_collision = pygame.sprite.groupcollide(player_sprite, rock_sprites, False, True, pygame.sprite.collide_mask)
        if rock_collision:
            # Player takes damage
            player.lives -= 1

        # fill background
        screen.fill_background()
        screen.draw_background(screen)
        screen.draw_group(all_sprites)
        # draw_lives(screen, 5, 5, player.lives, lives_image)
        # draw_text(screen, str(score), 48, screen.DISPLAY_WIDTH / 2, 10)
        # draw_boba(screen, 5, screen.DISPLAY_HEIGHT - 40, score, boba_image)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()