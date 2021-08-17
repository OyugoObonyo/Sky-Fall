"""
A module that contains the Bullet class and all its methods
"""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    A player can fire bullets from their ship.
    This class manages the movement, attributes and behaviour of bullets fired
    """
    def __init__(self, sky_fall):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = sky_fall.screen
        self.settings = sky_fall.settings
        self.color = self.settings.bullet_color
        # Initialize bullet position at origin before moving it to correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = sky_fall.ship.rect.midtop
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Manages bullet's movement and positioning on the screen"""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y
 
    def draw_bullet(self):
        """Draws the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)