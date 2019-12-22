import sys
import pygame
from setting import Settings
from ship import Ship

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
    
    def _check_key_down_events(self,e):
        if e.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif e.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif e.key == pygame.K_q: #press a if it is an azerty keyboard
            sys.exit()

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

    def _update_screen(self):
        """Redraw the screen during each game iteration"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            pygame.display.flip()

if __name__=='__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()

