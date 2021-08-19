"""
The main program module that handles the game's functionality
"""
import sys
from time import sleep
import pygame
from pygame import mixer
from pygame.constants import KEYDOWN
from settings import Settings
from stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from stars import Star

class SkyFall:
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
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.special_bullet = pygame.sprite.Group()
        self.bomb_status = False
        self.stars = pygame.sprite.Group()
        self._create_galaxy()
        self.play_button = Button(self, "Play")
        
    def _create_galaxy(self):
        """Create the galaxy of stars."""
        # Make a star.
        star = Star(self)
        stars_width, stars_height = star.rect.size
        # Fill galaxy across the screen
        available_space_x = self.settings.screen_width - (2 * stars_width)
        number_stars_x = available_space_x // (2 * stars_width)
        # Determine the number of rows of stars that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * stars_height) - ship_height)
        number_rows = available_space_y // (2 * stars_height)
        # Create the full galaxy of stars.
        for row_number in range(number_rows):
            # Create the first row of stars.
            for stars_number in range(number_stars_x):
                self._create_stars(stars_number, row_number) 
 
    def _create_stars(self, stars_number, row_number):
        """Create an stars and place it in the row."""
        star = Star(self)
        stars_width, stars_height = star.rect.size
        star.x = stars_width + 2 * stars_width * stars_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)

    def _update_stars(self):
        """Update the positions of all stars in the galaxy."""
        self._check_galaxy_edges()
        self.stars.update()
        if pygame.sprite.spritecollideany(self.ship, self.stars):
            self._ship_hit()
        self._check_stars_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an stars."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.stars.empty()
            self.bullets.empty()
            self._create_galaxy()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_stars_bottom(self):
        """Check if any stars have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for stars in self.stars.sprites():
            if stars.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _check_galaxy_edges(self):
        """Respond appropriately if any stars have reached an edge."""
        for stars in self.stars.sprites():
            if stars.check_edges():
                self._change_galaxy_direction()
                break

    def _change_galaxy_direction(self):
        """Drop the entire galaxy and change the galaxy's direction."""
        for star in self.stars.sprites():
            star.rect.y += self.settings.galaxy_drop_speed
        self.settings.galaxy_direction *= -1


    def _check_events(self):
        """Checks for player's input and acts accordingly"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Modify game response when player presses a key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self.bomb_status = False
                    self.settings.debomb()
                    self._fire_bullet()
                    mixer.music.load('E:\Sky-Fall\SOUNDS\shots.ogg')
                    mixer.music.play()
                elif event.key == pygame.K_b:
                    self.bomb_status = True
                    self.settings.bomb()
                    self._fire_bullet()                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()
            # Reset the game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            # Get rid of any remaining stars and bullets.
            self.stars.empty()
            self.bullets.empty()
            # Create a new galaxy and center the ship.
            self._create_galaxy()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_collisions()

    def _check_collisions(self):
        """Check for any bullets that have hit stars and get rid of the bullet and the stars"""
        if self.bomb_status ==  False:
            collisions = pygame.sprite.groupcollide(self.bullets, self.stars, True, True)
        else:
            collisions = pygame.sprite.groupcollide(self.bullets, self.stars, False , True)
        if collisions:
            for stars in collisions.values():
                self.stats.score += self.settings.star_points * len(stars)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.stars:
            # Destroy existing bullets and create new galaxy.
            self.bullets.empty()
            self._create_galaxy()
            self.settings.increase_speed()
            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _update_screen(self):
        """Manages output on the screen"""
        self.screen.fill(self.settings.bg_colour)
        # Draw ship on the screen
        self.ship.blitme()
        # Draw all bullets in the sprites group on the screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.stars.draw(self.screen)
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update_movement()
                self._update_bullets()
                self.special_bullet.update()
                self._update_stars()
            
            self._update_screen()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    si = SkyFall()
    si.run_game()