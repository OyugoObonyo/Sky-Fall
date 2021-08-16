"""
TODO: Document class
"""

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, space_invasion):
        """Initialize statistics."""
        self.settings = space_invasion.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1