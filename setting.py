class Settings:
    """A class to store all settings for alien invasion"""
    def __init__(self):
        """Initialize the game settings"""
        # Screen settings
        self.screen_width = 900
        self.screen_height = 500
        self.bg_color = (230,230,230)

        # Ship settings
        self.ship_speed = 1.2
        self.ship_limit = 3
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color =(60,60,60)
        self.bullets_allowed = 50

        # Sky settings
        self.star_in_the_sky = 60

        # Alien settings
        self.alien_speed = .3
        self.fleet_drop_speed = 50
        self.fleet_direction = 1