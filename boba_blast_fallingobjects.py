"""
Space to figure out FallingObjects.
"""


# inherits from Actor class
# y-max = maximum y-coordinate of screen (very top)

class FallingObject(Actor, ABC):
    """
    Represents a falling object (tapioca and rocks).
    """

    def __repr__(self):
        return (super().x_pos, super().y_pos)

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
    def __init__(self, image):
        """
        Initializes an instance of a Tapioca with an image.
        """
        image = pygame.image.load('tapioca.png').convert()
        super().__init__(image)
    
    def __repr__(self):
        """
        Returns a representation of a Tapioca object.
        """
        super.__repr__()

class Rock(FallingObject):
    """
    Represents a rock.
    """
    def __init__(self, image):
        """
        Initializes an instance of a Rock with an image.
        """
        image = pygame.image.load('rock.png').convert()
        super().__init__(image)
    
    def __repr__(self):
        """
        Returns a representation of a Rock object.
        """
        super.__repr__()


