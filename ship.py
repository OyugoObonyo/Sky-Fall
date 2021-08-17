"""
Module storing the ship class
"""
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """
    A player's ship ought to be managed.
    This class dicatates important aspects of the ship's management such as position, movement and speed
    """

    def __init__(self, sky_fall):
        """Initialize the ship with various attributes"""
        super().__init__()
        self.screen = sky_fall.screen
        self.settings = sky_fall.settings
        # Assign ship position on the screen
        self.screen_rect = sky_fall.screen.get_rect()
        self.image = pygame.image.load("E:\Space-Invasion\IMAGES\humanship.bmp")
        # Place ship on assigned position
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        # Store ship's horizontal position as a decimal
        self.x = float(self.rect.x)
        # Flags to be utilized in the event of continuous ship movement
        self.moving_right = False
        self.moving_left = False

    def update_movement(self):
        """Change ship position based on movement status"""
        # Ensure ship does not move past screen's edges
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """Draws ship image to the position assigned to self.rect"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)