import sys
import pygame
from setting import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.fired_bullet = 0

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
        if self.fired_bullet < self.settings.bullets_allowed : 
            hot_bullet = Bullet(self)
            self.bullets.add(hot_bullet)
            self.fired_bullet +=1

    def _update_bullet(self):
        """Update position of the bullet and get rid of old bullets"""
        # Update bullet position
        self.bullets.update()

        # Get rid of the bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Redraw the screen during each game iteration"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullet()
            self._update_screen()
            pygame.display.flip()

if __name__=='__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()

