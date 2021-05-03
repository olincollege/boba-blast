"""
Test file for the Boba Blast game.
"""
# Import necessary packages and classes from files
import pytest
import pygame
import constants
from boba_blast_controller import GraphicalController
from boba_blast_view import Display
from boba_blast_model import Rock, Tapioca, Player

pygame.init()

all_sprites = pygame.sprite.Group()
tapioca_sprites = pygame.sprite.Group()
rock_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.GroupSingle()

#
user = GraphicalController()
score = 0
fpsClock = pygame.time.Clock()

# Set game states
running = True
welcome_page = True
game_play = True

# Create screen and initialize Display
screen = pygame.display.set_mode((800, 600))
screen = Display(screen)
screen.draw_background(constants.BACKGROUND_IMAGE,
                       (constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT))
pygame.display.set_caption("Boba Blast!")

# Create player
test_player = Player([all_sprites, player_sprite])
test_rock = Rock([all_sprites, rock_sprites])
test_tapioca = Tapioca([all_sprites, tapioca_sprites])

# Define sets of test cases.

get_group_cases = [
    # Test that player is in intended groups
    (test_player, all_sprites, True),
    (test_player, player_sprite, True),
    # Test that player is not in unintended groups
    (test_player, tapioca_sprites, False),
    # Test that tapioca is in intended groups
    (test_tapioca, tapioca_sprites, True),
    # Test that tapioca is not in unintended groups
    (test_tapioca, player_sprite, False),
    # Test that rock is in intended groups
    (test_rock, rock_sprites, True),
    # Test that rock is not in unintended groups
    (test_rock, tapioca_sprites, False),
    # Test that all sprites are in group all_sprites
    ([test_player, test_rock, test_tapioca], all_sprites, True)
]

# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("sprite, expected_group, expected_bool", 
    get_group_cases)
def test_groups(sprite, expected_group, expected_bool):
    """
    Test that sprites are being added to the correct groups.

    Args:
        sprite: The sprite to add to a group.
        expected_group: The group the sprite should be added to.
        expected_bool: Whether or not the sprite is expected to be in 
            expected_group.
    """
    assert expected_group.has(sprite) == expected_bool
