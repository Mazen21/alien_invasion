class Settings:
    """A class to store all settings for alien invasion"""
    def __init__(self):
        """Initialize the game settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 650
        self.bg_color = (230,230,230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color =(60,60,60)
        self.bullets_allowed = 50000

        # Sky settings
        self.star_in_the_sky = 60

        # Alien settings
        self.fleet_drop_speed = 20
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien value increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that changes through the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.2

        # fleet_direction of 1 represents right; -1 represent left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 30
    
    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)