import pygame, random, os, constants
pygame.init()


# class Display(pygame.Surface):
class Display():

    # Create display screen
    def __init__(self, screen):
        self._screen = screen

    def fill_background(self, color):
        """
        Args:
            color: A tuple, (R, G, B), representing a color.
        """
        self._screen.fill(color)

    def draw_background(self, image, dims):
        """
        Draws the background image.

        Args:
            image: Image to blit.
            dims: Dimensions of the display, as an integer tuple
        """
        _rect = image.get_rect()
        _image = pygame.transform.scale(image, dims)
        self._screen.blit(_image, _rect)
    
    def screen_blit(self, image, rect):
        """
        Blits a sprite.
        """
        self._screen.blit(image, rect)
    
    def draw_group(self, group):
        """
        Draws all sprites in a group onto a surface.

        Args:
            group: The group of sprites to be drawn.
        """
        group.draw(self._screen)


# class Player(pygame.sprite.Sprite):
#     """
#     Create a player

#     Attributes:
#         image: A surface drawn on the screen visually representing a player.
#     """

#     def __init__(self):
#         super(Player, self).__init__(all_sprites, player_sprite)
#         #surface is pygame object for representing images
#         self.image = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))
#         self.image.set_colorkey(BLACK)
#         #pygame object for storing rectangular coordinates)
#         self.rect = self.image.get_rect(bottomleft=(SCREEN_WIDTH/2, SCREEN_HEIGHT - PLAYER_HEIGHT))
#         # mask for collisions
#         self.mask = pygame.mask.from_surface(self.image)
#         # set number of lives
#         self.lives = 3

#     def move_sprite(self, pressed_keys):
#         if pressed_keys[pygame.K_LEFT]:
#             #move_ip() stands for move in place to move current rect
#             self.rect.move_ip(-5,0)

#         if pressed_keys[pygame.K_RIGHT]:
#             self.rect.move_ip(5,0)

#         #set screen boundaries
#         if self.rect.left < 0:
#             self.rect.left = SCREEN_WIDTH - PLAYER_WIDTH
#         if self.rect.right > SCREEN_WIDTH:
#             self.rect.left = 0
