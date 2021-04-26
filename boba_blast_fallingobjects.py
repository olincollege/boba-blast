"""
Space to figure out FallingObjects.
"""
from abc import ABC, abstractmethod

# inherits from Actor class
# y-max = maximum y-coordinate of screen (very top)

class FallingObject(Actor, ABC):
    """
    Represents a falling object (tapioca and rocks).
    """
    def __init__(self):
        """
        Initializes an instance of a FallingObject.
        """
        super().__init__()
        self._y_value = `screen.get_height`

    def __repr__(self):
        return (super().x_pos, super().y_pos)

    @abstractmethod
    def update(self):
        """
        A method to update location or remove invalid objects.
        """
        if self.y_pos <= 0 or `there is a collision`:
            self.kill()

class Tapioca(FallingObject):
    """
    Represents a tapioca pearl.
    """
    tapioca = pygame.sprite.Group()

