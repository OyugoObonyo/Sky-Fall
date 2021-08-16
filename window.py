"""
TODO: ADD MODULE DOCUMENTATION!
"""
import sys
import pygame
from pygame.constants import KEYDOWN
from settings import Settings
from ship import Ship


class SpaceInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        # Assign surface i.e where game elements can be displayed
        self.settings = Settings()
        # Enable Full screen mode
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Oyugo's Space Invasion")
        self.bg_colour = (self.settings.bg_colour)
        self.ship = Ship(self)

    def check_events(self):
        """TODO: Add method documentation"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def update_screen(self):
        """TODO: Document method"""
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self.check_events()
            self.ship.update_movement()
            # Make the most recently drawn screen visible.
            self.update_screen()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    si = SpaceInvasion()
    si.run_game()
