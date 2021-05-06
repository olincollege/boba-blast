# Boba Blast! The Game

This is a repository housing Claire's second, and Berwin's first, boba-centric SoftDes project, **Boba Blast!**.
## Game Overview
The mission in this game is to collect as many tapioca pearls as you can to make some delicious bubble tea while avoiding the rocks falling from the sky.

## Installation and setup
Running the game uses [pygame](https://www.pygame.org/news), which can be installed by running `$ pip install pygame`.

While not required to run the game, the test framework uses pytest, which can be installed by running `$ pip install pytest`.

## File Structure
The file structure consists of the following `.py` files:
* `main.py`: Run this to play the game!
* `constants.py`: Static paths are stored here.
* `boba_blast_model`: Contains classes and attributes to store information such as the location, speed of movement, etc. for the player, tapioca, and rocks
* `boba_blast_view`: Contains a Display class and attributes to display information such as statistics, objects, and backgrounds as visuals.
* `boba_blast_controller`: Contains a GraphicalController class with attributes that translate user key and exit inputs into appropriate actions.

### Static files
The `/images` folder houses files used for graphics. The `/audio` folder houses files used for sounds. Both paths are somewhat hard-coded, meaning that the specific files **must** be in **those** folders. If you're downloading straight from the repo, you shouldn't run into any issues.

## Attributions
We looked at [KidsCanCode](http://kidscancode.org/lessons/) as a resource when starting this project to learn some of the basic components of Pygame.

For our game music and sound effects, we used audio from the following sites:

Music: [bensound.com](https://www.bensound.com/)

Sound effects: [orangefreesounds.com](https://orangefreesounds.com/)

We created the images and visuals used in this game.