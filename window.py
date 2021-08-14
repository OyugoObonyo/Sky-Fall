"""
TODO: ADD MODULE DOCUMENTATION!
"""
import sys
import pygame
from settings import Settings
from ship import Ship


class SpaceInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        # Assign surface i.e where game elements can be displayed
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Oyugo's Space Invasion")
        self.bg_colour = (self.settings.bg_colour)
        self.ship = Ship(self) 

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Make the most recently drawn screen visible.
            self.screen.fill(self.settings.bg_colour)
            self.ship.blitme() 
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    si = SpaceInvasion()
    si.run_game()
