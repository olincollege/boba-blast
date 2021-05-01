"""
Display instance of a player that takes user inputs to move side to side
"""
import pygame, os
from boba_blast_controller import GraphicalController
from boba_blast_view import Display
from PIL import Image

#initialize pygame
pygame.init()

#view
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

FPS = 60
fpsClock = pygame.time.Clock()

display = pygame.display.set_mode(size = (DISPLAY_WIDTH, DISPLAY_HEIGHT))

#load images
game_folder = os.path.dirname(__file__)     # figures out path to the folder with this file
images_folder = os.path.join(game_folder, 'images')

player_image = pygame.image.load(os.path.join(images_folder, 'Player(1).png')).convert()
player_image.set_colorkey((0,0,0))

game_image = pygame.image.load(os.path.join(images_folder, 'Boba-Blast(2)-03.png')).convert()
game_image = pygame.transform.scale(game_image, (800,600))

welcome_image = pygame.image.load(os.path.join(images_folder, 'Boba-Blast(2)-02.png')).convert()
welcome_image = pygame.transform.scale(welcome_image, (800,600))

end_image = pygame.image.load(os.path.join(images_folder, 'Boba-Blast(2)-04-04.png')).convert()
end_image = pygame.transform.scale(end_image, (800,600))

#get dimensions of player sprite using Pillow
im = Image.open(os.path.join(images_folder, 'Player(1).png'))
PLAYER_WIDTH, PLAYER_HEIGHT = im.size



class Player(pygame.sprite.Sprite):
    """
    Create a player
    Attributes:
        surface: surface drawn on the screen
    """

    def __init__(self):
        super(Player, self).__init__()
        #surface is pygame object for representing images
        self.surface = player_image
        #pygame object for storing rectangular coordinates)
        self.rect = self.surface.get_rect(bottomleft = (DISPLAY_WIDTH/2, DISPLAY_HEIGHT - PLAYER_HEIGHT))

    def move_sprite(self, pressed_keys):
        if pressed_keys[pygame.K_LEFT]:
            #move_ip() stands for move in place to move current rect
            self.rect.move_ip(-5,0)

        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)

        #set screen boundaries
        if self.rect.centerx < 0:
            self.rect.right = DISPLAY_WIDTH
        if self.rect.centerx > DISPLAY_WIDTH:
            self.rect.left = 0

#initialize pygame
pygame.init()

#create screen using .display which eturns a surface that represents the inside dimensions
#of the window
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

#create instance of player
player = Player()
user = GraphicalController()

def check_exit_game():
    pass

#set up game loop which 1. takes user input, updates state of all game objects, updates display and audio output, maintains speed of teh game
running = True
welcome_page = True
game_play = True
Game_over = False

#establish playable frame rate
clock = pygame.time.Clock()

#main loop
while running:
    fpsClock.tick(FPS)
    #check events that are stored in queue (all user input results in an event)
    for event in pygame.event.get():
        #check if the user closed the window button and stop loop if they did
        if event.type == pygame.QUIT:
            running = False
    
    while welcome_page:
        for event in pygame.event.get():
        #check if the user closed the window button and stop loop if they did
            if event.type == pygame.KEYDOWN:
                welcome_page = False
            if event.type == pygame.QUIT:
                running = False

        game_display.blit(welcome_image, [0,0])  
        pygame.display.flip()
    

    while game_play:
        for event in pygame.event.get():
        #check if the user closed the window button and stop loop if they did
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        pressed_keys = user.get_move()
        #update player location
        player.move_sprite(pressed_keys)
        game_display.blit(game_image, [0,0])  
        game_display.blit(player.surface, player.rect)
        pygame.display.flip()
        #keep a frame rate of 30 frames per second
    pygame.quit()
