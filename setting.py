class Settings:
    """A class to store all settings for alien invasion"""
    def __init__(self):
        """Initialize the game settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 650
        self.bg_color = (230,230,230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color =(60,60,60)
        self.bullets_allowed = 36

        # Sky settings
        self.star_in_the_sky = 50
