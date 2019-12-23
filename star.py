import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A star in the sky"""
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the star image
        self.image = pygame.image.load('alien_invasion/images/star.bmp')
        self.rect = self.image.get_rect()

        # Start each star at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien horizontal and vertical position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)