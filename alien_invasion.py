import sys
from time import sleep
import pygame
from random import *
from setting import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from game_stats import GameStats

class AlienInvasion:
    """Overall class to manage assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        self._create_sky()
        self._create_fleet()

    def _ship_hit(self):
        """Response to the ship being hit by an alien"""
        if self.stats.ship_left > 0:
            # Decrement ships_left
            self.stats.ship_left -= 1 

            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _check_key_down_events(self,e):
        if e.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif e.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif e.key == pygame.K_q: #press a if it is an azerty keyboard
            sys.exit()
        elif e.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_key_up_events(self,e):
        if e.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif e.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_events(self):
        """Watch for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up_events(event)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group"""
        if self.ship.fired_bullet < self.settings.bullets_allowed : 
            hot_bullet = Bullet(self)
            self.bullets.add(hot_bullet)
            self.ship.fired_bullet +=1

    def _update_bullet(self):
        """Update position of the bullet and get rid of old bullets"""
        # Update bullet position
        self.bullets.update()

        # Get rid of the bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # Check for any bullet that have hit aliens
        self._check_bullet_alien_collision()
    
    def _check_alien_bottom(self):
        """Check if any alien have reached the bottom of the screen"""
        self.screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen_rect.bottom:
                self._ship_hit()
                break
        
    def _check_bullet_alien_collision(self):
        """Respond to alien collision"""
        # Check for any bullet that have hit aliens
        # if so get rid of the bullet and the alien
        collisions = pygame.sprite.groupcollide(
            self.bullets,self.aliens,True,True
        )
        if not self.aliens:
            # Destroy existing bullet and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.ship.refill()
        
    def _update_aliens(self):
        """Update the position of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien ship collision
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        
        # Loof for aliens hitttings the bottom of the screen
        self._check_alien_bottom()

    def _create_alien(self,alien_number,row_number):
        """Create an alien and place it in the row"""
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2* alien.rect.height * row_number
        self.aliens.add(alien)

    def _create_star(self,star_x,star_y):
        """Create a star and place it in the sky"""
        star = Star(self)
        star_width,star_height = star.rect.size
        star.rect.x = star_width + 2 * star_width * star_x
        star.rect.y = star_height + 2 * star_height * star_y
        self.stars.add(star)

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Create an alien and find the number of aliens in a row
        # Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)
        # Determine the number of rows of aliens that fits in the screen
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - 3 * alien_height - ship_height
        number_rowns = available_space_y // (2 * alien_height)
        # Create the full fleet
        for row_number in range(number_rowns):
            for alien_number in range(number_alien_x):
                #Create an alien and place it in the row
                self._create_alien(alien_number,row_number)

    def _create_sky(self):
        """Create the sky that holds all the stars"""
        star = Star(self)
        star_width,star_height = star.rect.size
        available_space_x = self.settings.screen_width - (2*star_width)
        available_space_y = self.settings.screen_height - (2*star_height)
        number_star_x = available_space_x // (2 * star_width)
        number_star_y = available_space_y // (2 * star_height)
        for i in range(self.settings.star_in_the_sky):
            self._create_star(randrange(number_star_x),randrange(number_star_x))
    
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change directions"""
        for alien in self.aliens.sprites():
            alien.rect.y +=self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Redraw the screen during each game iteration"""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.ship.blitme()
        
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullet()
                self._update_aliens()

            self._update_screen()
            pygame.display.flip()

if __name__=='__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()

