"""
TODO: Document module
"""

class Settings:
    """TODO: Document Class"""

    def __init__(self):
        """TODO:Document method"""
        self.ship_speed = 1.5
        self.ship_limit = 3
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (0, 0, 0)
        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 5
        # Star settings
        self.star_speed = 1.0
        self.galaxy_drop_speed = 10
        # galaxy_direction of 1 represents right; -1 represents left.
        self.galaxy_direction = 1
        # Game speed
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.star_speed = 1.0
        # galaxy_direction of 1 represents right; -1 represents left.
        self.galaxy_direction = 1
        self.star_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.star_speed *= self.speedup_scale
        self.star_points = int(self.star_points * self.score_scale)
        print(self.star_points)