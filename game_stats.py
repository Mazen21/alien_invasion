class GameStats:
    """Track statistics for alien invasion"""

    def __init__(self,ai_game):
        """initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Start Alien invasion in an active mode state
        self.game_active = True
    
    def reset_stats(self):
        """Initialize statistics that can be changed during the game"""
        self.ship_left = self.settings.ship_limit