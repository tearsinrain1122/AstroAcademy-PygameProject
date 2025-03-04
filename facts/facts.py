from pygame.sprite import Sprite
from facts.db_utils import fact_data
import random
import pygame


class Facts(Sprite):
    # A class inherited from the pygame.Sprite class to control the space facts
    def __init__(self, space_game):
        super().__init__()

        # Retrieving fact from iterator and initialising the time interval for their appearance
        self.fact = next(fact_data)
        self.add_fact_timer()

        # Fact image and rect
        self.font = space_game.settings.small_pixel_font
        self.image = self.font.render(self.fact, True, (255, 255, 255))
        self.rect = self.image.get_rect()

        # Initial position of new fact
        self.rect.x = space_game.settings.screen_width
        self.rect.y = random.randint(100,space_game.settings.screen_height-100)

        # Speed of the fact
        self.speed = 3

    def update(self):
        # Facts slide from right to left
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right == 0:
            self.kill()

    # Timer for adding new facts
    def add_fact_timer(self, interval=20000):
        add_fact = pygame.USEREVENT + 2
        pygame.time.set_timer(add_fact, interval)





