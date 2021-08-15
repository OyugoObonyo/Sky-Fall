"""
TODO:Add module documentation
"""
import pygame


class Ship:
    """TODO: Class documentation"""

    def __init__(self, space_invasion):
        """ TODO: Document method"""
        self.screen = space_invasion.screen
        self.screen_rect = space_invasion.screen.get_rect()
        self.image = pygame.image.load("E:\Space-Invasion\IMAGES\ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False

    def update_movement(self):
        """TODO: Add documentation"""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """TODO: Document method"""
        self.screen.blit(self.image, self.rect)