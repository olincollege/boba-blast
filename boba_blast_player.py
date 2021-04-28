"""
Display instance of a player that takes user inputs to move side to side
"""
import pygame
from boba_blast_controller import GraphicalController
from PIL import Image

#initialize pygame
pygame.init()

#get dimensions of player sprite using Pillow
im = Image.open("Player(1).png")
PLAYER_WIDTH, PLAYER_HEIGHT = im.size

#view
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600


class Player(pygame.sprite.Sprite):
    """
    Create a player

    Attributes:
        surface: surface drawn on the screen
    """

    def __init__(self):
        super(Player, self).__init__()
        #surface is pygame object for representing images
        self.surface = pygame.image.load("Player(1).png").convert()
        #pygame object for storing rectangular coordinates)
        self.rect = self.surface.get_rect(bottomleft = (DISPLAY_WIDTH/2, DISPLAY_HEIGHT - PLAYER_HEIGHT))

    def move_sprite(self, pressed_keys):
        if pressed_keys[pygame.K_LEFT]:
            #move_ip() stands for move in place to move current rect
            self.rect.move_ip(-5,0)

        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)

        #set screen boundaries
        if self.rect.left < 0:
            self.rect.right = DISPLAY_WIDTH
        if self.rect.right > DISPLAY_WIDTH:
            self.rect.left = 0

#initialize pygame
pygame.init()

#create screen using .display which eturns a surface that represents the inside dimensions
#of the window
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

#create instance of player
player = Player()
user = GraphicalController()

#set up game loop which 1. takes user input, updates state of all game objects, updates display and audio output, maintains speed of teh game
running = True

#establish playable frame rate
clock = pygame.time.Clock()

#main loop
while running:
    #check events that are stored in queue (all user input results in an event)
    for event in pygame.event.get():
        #check if the user closed the window button and stop loop if they did
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = user.get_move()
    
    #update player location
    player.move_sprite(pressed_keys)

    game_display.blit(player.surface, player.rect)
    pygame.display.flip()
                                
    #set background color to all black
    game_display.fill((0,0,0))
    
    #keep a frame rate of 30 frames per second
    clock.tick(30)
            
        