"""
TODO: Add class documentation
"""
import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a star from the galaxy."""
    def __init__(self, sky_fall):
        """Initialize a star and set its starting position."""
        super().__init__()
        self.screen = sky_fall.screen
        self.settings = sky_fall.settings
        # Load the star image and set its rect attribute.
        self.image = pygame.image.load("E:\Space-Invasion\IMAGES\Star.bmp")
        self.rect = self.image.get_rect()
        # Start each new star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the star's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if star is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the star to the right."""
        self.x += (self.settings.star_speed * self.settings.galaxy_direction)
        self.rect.x = self.x