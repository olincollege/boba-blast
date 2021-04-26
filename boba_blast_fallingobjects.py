"""
Space to figure out FallingObjects.
"""

import random
# inherits from Actor class
# y-max = maximum y-coordinate of screen (very top)

class FallingObject(Actor, ABC):
    """
    Represents a falling object (tapioca and rocks).
    """

    def __init__(self, image, x=None, y=None, screen):
        """
        Initializes a FallingObject at y = 0 and a random x-position.
        """
        super().__init__(image, random.randint(0, SCREEN_WIDTH), 0, screen)

    def __repr__(self):
        return f"(x, y) = {super().x_pos, super().y_pos)}"

    @abstractmethod
    def update(self, other):
        """
        A method to update location or remove invalid objects.
        """
        if self.y_pos <= 0 or pygame.sprite.spritecollide()
            self.kill()

class Tapioca(FallingObject):
    """
    Represents a tapioca pearl.
    """
    # tapioca = pygame.sprite.Group() <-- this could be good for collisions
    
    def __repr__(self):
        """
        Returns a representation of a Tapioca object.
        """
        super.__repr__()

class Rock(FallingObject):
    """
    Represents a rock.
    """
    
    def __repr__(self):
        """
        Returns a representation of a Rock object.
        """
        super.__repr__()

class FallingObjectGenerator:
    """
    Generates
    """

    tapioca_image = pygame.image.load('tapioca.png').convert()

    rock_image = pygame.image.load('rock.png').convert()
