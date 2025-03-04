import pygame
from health_bar.health_bar_utils import calculate_health_bar_width

class HealthBar():
    def __init__(self, space_game):
        # Initialise health bar attributes
        self.space_game = space_game
        self.screen = space_game.settings.screen
        self.screen_rect = space_game.settings.screen.get_rect()

        # Initialise health bar settings
        self.current_health = 80
        self.max_health = 80
        self.health_bar_length = 100  # In pixels
        self.health_ratio = self.max_health / self.health_bar_length  # Converts health to length of health bar

    def draw_health_bar(self):
        pygame.draw.rect(self.screen, (115, 236, 139), (75, 55, calculate_health_bar_width(self.current_health,
                                                                                           self.health_ratio), 20))
        pygame.draw.rect(self.screen, (255, 255, 255), (75, 55, self.health_bar_length, 20), 3)  # White outline around bar



