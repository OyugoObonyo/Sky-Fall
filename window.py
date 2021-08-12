"""
TODO: ADD MODULE DOCUMENTATION!
"""
import sys
import pygame


class SpaceInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        # Assign surface i.e where game elements can be displayed
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Oyugo's Space Invasion")
        self.bg_colour = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Make the most recently drawn screen visible.
            self.screen.fill(self.bg_colour)
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    si = SpaceInvasion()
    si.run_game()
