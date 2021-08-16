"""
TODO:Add module documentation
"""
import pygame


class Ship:
    """TODO: Class documentation"""

    def __init__(self, space_invasion):
        """ TODO: Document method"""
        self.screen = space_invasion.screen
        self.settings = space_invasion.settings
        self.screen_rect = space_invasion.screen.get_rect()
        self.image = pygame.image.load("E:\Space-Invasion\IMAGES\ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def update_movement(self):
        """TODO: Add documentation"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """TODO: Document method"""
        self.screen.blit(self.image, self.rect)