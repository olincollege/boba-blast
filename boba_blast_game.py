"""
Creates and runs an instance of the Boba Blast game!
"""
import pygame, random, os
# from boba_blast_view import Display

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

background_image = pygame.image.load(os.path.join(images_folder, 'background.png')).convert()

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

def draw_background(surf, background_image):
    """
    Draws the background image.

    Args:
        surf: Surface on which to draw.
        background_image: The image to be used for the background. It should
            have the same aspect ratio as the display.
    """
    background_rect = background_image.get_rect()
    background_image = pygame.transform.scale(background_image, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
    surf.blit(background_image, background_rect)

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

    def __init__(self):
        # Add this instance of the Player to groups `all_sprites` and `player_sprite`.
        super(Player, self).__init__(all_sprites, player_sprite)
        # surface is pygame object for representing images
        self.image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.set_colorkey((0,0,0))
        # pygame object for storing rectangular coordinates)
        self.rect = self.image.get_rect(bottomleft=(DISPLAY_WIDTH/2, DISPLAY_HEIGHT - PLAYER_HEIGHT))
        # mask for collisions (eventually change to just basket on head, once we have that)
        self.mask = pygame.mask.from_surface(self.image)
        # set number of lives to start with
        self.lives = 3

    def move_sprite(self, pressed_keys):
        if pressed_keys[pygame.K_LEFT]:
            #m ove_ip() stands for move in place to move current rect
            self.rect.move_ip(-5,0)

        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)

        # set screen boundaries
        if self.rect.centerx < 0:
            self.rect.left = DISPLAY_WIDTH - PLAYER_WIDTH
        if self.rect.centerx > DISPLAY_WIDTH:
            self.rect.left = 0

# Eventually put Tapioca and Rock under FallingObject subclass
class Tapioca(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites, tapioca_sprites)
        self.image = pygame.transform.scale(tapioca_image, (25, 25))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect(center=(random.randint(0, DISPLAY_WIDTH), 0))
        # Set hitbox for collisions
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        # Falls on every update.
        self.rect.y += 1
        if self.rect.bottom >= DISPLAY_HEIGHT:
            self.kill()
    
    def __repr__(self):
        return f"There is tapioca at {self.rect.center}."

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites, rock_sprites)
        self.image = pygame.transform.scale(rock_image, (35, 35))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect(center=(random.randint(0, DISPLAY_WIDTH), 0))
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        self.rect.y += 5
        if self.rect.bottom >= DISPLAY_HEIGHT:
            self.kill()
    
    def __repr__(self):
        return f"There is a rock at {self.rect.center}."

# Ok this is the actual game section that belongs here
player = Player()   # This part isn't working
# user = GraphicalController()

def main():
    game_over = False
    score = 0
    
    while not game_over:
        fpsClock.tick(FPS)
        if player.lives == 0:
            game_over = True

        for event in pygame.event.get():
            # check for user closing window
            if event.type == pygame.QUIT:
                game_over = True

        # # get user moves
        # pressed_keys = user.get_move()
        # use pygame get_pressed() which returns a bool dictionary containing all keys that are pressed in queue
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
        screen.fill((0,0,0))
        draw_background(screen, background_image)
        all_sprites.draw(screen)
        draw_lives(screen, 5, 5, player.lives, lives_image)
        draw_text(screen, str(score), 48, DISPLAY_WIDTH / 2, 10)
        draw_boba(screen, 5, DISPLAY_HEIGHT - 40, score, boba_image)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()