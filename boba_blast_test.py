"""
Test file for the Boba Blast game.
"""
# Import necessary packages and classes from files
import pytest
import pygame
from boba_blast_model import Rock, Tapioca, Player, is_collision

pygame.init()

all_sprites = pygame.sprite.Group()
tapioca_sprites = pygame.sprite.Group()
rock_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.GroupSingle()

# Create player
test_player = Player([all_sprites, player_sprite])
test_rock = Rock([all_sprites, rock_sprites])
test_tapioca = Tapioca([all_sprites, tapioca_sprites])

# Define sets of test cases.

# Test __init__ methods of sprites.
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

# Test player controls.

right_arrow = pygame.event.Event(pygame.KEYDOWN, {'unicode': '',
    'key': 1073741903, 'mod': 0, 'scancode': 79, 'window': None})

left_arrow = pygame.event.Event(pygame.KEYDOWN, {'unicode': '',
    'key': 1073741904, 'mod': 0, 'scancode': 80, 'window': None})

other_key = pygame.event.Event(pygame.KEYDOWN, {'unicode': '',
    'key': 1073741906, 'mod': 0, 'scancode': 82, 'window': None})

get_input_cases = [
    # Test that right arrow moves right.
    (right_arrow, 1073741903),
    # Test that left arrow moves left.
    (left_arrow, 1073741904),
    # Test that another key does nothing.
    (other_key, 1073741906)
]

# Test random location generation for FallingObjects.
get_randomness_cases = [
    # Test that two FallingObjects are generated at different x-values.
    (Rock([all_sprites]), Rock([all_sprites])),
    (Tapioca([all_sprites]), Rock([all_sprites])),
    (Tapioca([all_sprites]), Rock([all_sprites]))
]

get_update_cases = [
    # Test that FallingObjects fall when updated.
    test_rock,
    test_tapioca
]

# Test collisions (limited due to random generation)
collision_player_sprite = pygame.sprite.GroupSingle()
test_collision_player = Player([collision_player_sprite])

get_collision_cases = [
    # Players spawn at the same location, so they should collide.
    (player_sprite, collision_player_sprite)
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

@pytest.mark.parametrize("event, key",
    get_input_cases)
def test_input(event, key):
    """
    Test that user input is correctly queued.

    Args:
        event: The event in the event queue caused by pressing the key.
        key: The key pressed.
    """
    pygame.event.clear()
    # Add event to the queue
    pygame.event.post(event)
    # Check characteristics of the event, and that it was added to the queue.
    for each_event in pygame.event.get(pygame.KEYDOWN):
        assert each_event.key == key

@pytest.mark.parametrize("sprite1, sprite2", get_randomness_cases)
def test_randomness(sprite1, sprite2):
    """
    Test that FallingObjects are being generated at random x-locations.

    Args:
        sprite1: An instance of a FallingObject.
        sprite2: A separate instance of a FallingObject.
    """
    assert sprite1.rect.centerx != sprite2.rect.centerx


@pytest.mark.parametrize("sprite", get_update_cases)
def test_update(sprite):
    """
    Test that FallingObjects increase y-val when updated.

    Args:
        sprite: An instance of a FallingObject.
    """
    current_y = sprite.rect.centery
    sprite.update()
    assert sprite.rect.centery > current_y

@pytest.mark.parametrize("group1, group2", get_collision_cases)
def test_collision(group1, group2):
    """
    Test that sprites will collide.

    Args:
        group1: A Pygame group of sprites.
        group2: A separate Pygame group of sprites.
    """
    assert is_collision(group1, group2)

# pygame.tests.run(blit)
