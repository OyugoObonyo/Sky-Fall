"""
TODO: Add documentation
"""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """TODO: Add class documentation"""
    def __init__(self, space_invasion):
        """TODO: Method documentation"""
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = space_invasion.screen
        self.settings = space_invasion.settings
        self.color = self.settings.bullet_color
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = space_invasion.ship.rect.midtop
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Moves the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y
 
    def draw_bullet(self):
        """Draws the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)