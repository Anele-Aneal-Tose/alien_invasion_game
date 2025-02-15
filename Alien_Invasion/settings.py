"""
    Author: Anele Aneal Tose
    Description: This is a settings class or file to store all these values in one place.
    Date: 15/02/2025
"""
class Settings:
    """A class to store all the settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #Ship settings
        self.ship_speed = 1.5