"""
TODO: Add documentation
"""
import pygame
from pygame.sprite import Sprite


class SpeBullet(Sprite):
    """ TODO: Add class documentation"""

    def __init__(self, space_invasion):
        """TODO: Document method"""
        super().__init__()
        self.screen = space_invasion.screen
        self.settings = space_invasion.settings
        self.color = self.settings.sp_bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.sp_bullet_width, self.settings.sp_bullet_height)
        self.rect.midtop = space_invasion.ship.rect.midtop
        self.y = float(self.rect.y)

    def special_update(self):
        """TODO: Document method"""
        self.y -= self.settings.sp_bullet_speed
        self.rect.y = self.y

    def draw_special_bullet(self):
        """TODO: Document method"""
        pygame.draw.rect(self.screen, self.color, self.rect)