"""
Creates and runs an instance of the Boba Blast game!
"""
# Import necessary packages and classes from files
import sys
import pygame
import constants
from boba_blast_controller import GraphicalController
from boba_blast_view import Display
from boba_blast_model import Rock, Tapioca, Player, is_collision


def main():
    """
    Runs Boba Blast game.
    """
    pygame.init()
    pygame.mixer.init()  # for sound

    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    tapioca_sprites = pygame.sprite.Group()
    rock_sprites = pygame.sprite.Group()
    player_sprite = pygame.sprite.GroupSingle()

    # load variables
    user = GraphicalController()
    score = 0
    fps_clock = pygame.time.Clock()

    # load music and sound effect
    pygame.mixer.music.load("audio/bensound-littleidea.ogg")
    pygame.mixer.music.set_volume(1.1)
    pygame.mixer.music.play(-1)
    lose_life = pygame.mixer.Sound("audio/Lost-life-sound-effect.ogg")
    add_tapioca = pygame.mixer.Sound("audio/tapioca_sound.ogg")

    # Set game states
    running = True
    welcome_page = True
    game_play = True
    end_page = True

    # Create screen and initialize Display
    screen = pygame.display.set_mode((800, 600))
    screen = Display(screen)
    screen.draw_background(constants.BACKGROUND_IMAGE,
                           (constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT))
    pygame.display.set_caption("Boba Blast!")

    # Create player
    player = Player([all_sprites, player_sprite])

    # Run game until over
    while running:
        fps_clock.tick(constants.FPS)

        while welcome_page:
            for event in pygame.event.get():
                # check if the user closed the window button and stop loop if they did
                if event.type == pygame.KEYDOWN:
                    welcome_page = False
                    break
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                    pygame.mixer.stop()
                    break

            screen.draw_background(constants.WELCOME_IMAGE.convert(
            ), (constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT))

            pygame.display.flip()

        while game_play:
            pygame.mixer.music.unpause()
            # Check if the game is over
            user.check_exit()

            # get user moves
            pressed_keys = user.get_move()

            # update player location
            player.move_sprite(pressed_keys)
            screen.screen_blit(player.image, player.rect)

            # generate Rocks and Tapioca
            if pygame.time.get_ticks() % 1000 == 0:
                Rock([all_sprites, rock_sprites])
            elif pygame.time.get_ticks() % 350 == 0:
                Tapioca([all_sprites, tapioca_sprites])

            # Calls the update method of each group
            all_sprites.update()

            # Check for collision between player instance and any tapioca
            if is_collision(player_sprite, tapioca_sprites):
                pygame.mixer.Sound.play(add_tapioca)
                # Increment score by 1
                score += 1

            # Check for collision between player instance and any rock
            if is_collision(player_sprite, rock_sprites):
                pygame.mixer.Sound.play(lose_life)
                # Player takes damage
                player.lives -= 1
                if player.lives == 0:
                    game_play = False

            screen.draw_all(player, all_sprites, score)

            pygame.display.flip()

        while end_page:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    main()
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                    break

            screen.draw_background(constants.END_IMAGE.convert(
            ), (constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT))

            pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
