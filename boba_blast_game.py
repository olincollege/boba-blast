"""
Creates and runs an instance of the Boba Blast game!
"""
import pygame, random, os, constants
from boba_blast_controller import GraphicalController
from boba_blast_view import Display
from boba_blast_model import Player, Rock, Tapioca

pygame.init()
pygame.mixer.init() #for sound

all_sprites = pygame.sprite.Group()
tapioca_sprites = pygame.sprite.Group()
rock_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.GroupSingle()

class Game:
    user = GraphicalController()
    game_over = False
    score = 0
    fpsClock = pygame.time.Clock()

    # Create screen and initialize Display
    screen = pygame.display.set_mode((800, 600))
    screen = Display(screen)
    screen.draw_background(constants.BACKGROUND_IMAGE, (constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT))
    pygame.display.set_caption("Boba Blast!")
        
    player = Player(screen, [all_sprites, player_sprite])

    while not game_over:
        fpsClock.tick(constants.FPS)
        if player.lives == 0:
            game_over = True

        for event in pygame.event.get():
            # check for user closing window
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
        
        # get user moves
        pressed_keys = user.get_move()

        # update player location
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
        screen.fill_background((0, 255, 0))
        # Draw background image
        screen.draw_background(constants.BACKGROUND_IMAGE, (constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT))
        # Draw all sprites (player, tapioca, rocks)
        screen.draw_group(all_sprites)
        # Draw remaining lives
        screen.draw_lives(5, 5, player.lives)
        # Draw score (tapioca collected)
        screen.draw_text(str(score), 60, constants.DISPLAY_WIDTH / 2, 7)
        # Draw # of boba made
        screen.draw_text(f"x{score // 10}", 60, constants.DISPLAY_WIDTH - 50, 25)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()