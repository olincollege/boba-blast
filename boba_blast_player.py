"""
Display instance of a player that takes user inputs to move side to side
"""
import pygame

#initialize pygame
pygame.init()


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
        self.surface = pygame.Surface((75,25))
        self.rect = self.surf.get_rect()
    
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load(os.path.join('i')

    def move_sprite(self, pressed_keys):
        if pressed_keys[pygame.K_LEFT]:
            #self.

#initialize pygame
pygame.init()

#create screen using .display which eturns a surface that represents the inside dimensions
#of the window
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

#create instance of player
player = Player()

#set up game loop which 1. takes user input, updates state of all game objects, updates display and audio output, maintains speed of teh game
running = True
                                
#main loop
while running:
    #check events that are stored in queue (all user input results in an event)
    for event in pygame.event.get():
        #check if the user closed the window button and stop loop if they did
        if event.type == pygame.QUIT:
            running = False
    
    #set background color to all black
    game_display.fill((0,0,0))
    #draw player on the screen
    screen.blit(player.surface, (DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2))
    pygame.display.flip() #update screen
    
    #use pygame get_pressed() which returns a bool dictionary containing all keys that are pressed in queue
    pressed_keys = pygame.key.get_pressed()
    
            
        