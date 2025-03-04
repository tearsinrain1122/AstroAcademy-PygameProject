import pygame
from pygame.sprite import Sprite

# Importing random to calculate asteroid speed
import random


class Asteroids(Sprite):
    # A class inherited from the pygame.sprite.Sprite base class to control the asteroids

    def __init__(self, space_game):
        super().__init__()
        self.screen = space_game.settings.screen
        self.screen_rect = space_game.settings.screen.get_rect()
        self.add_asteroid_timer()

        # Loading the asteroid image and rect
        self.image = pygame.image.load('images/asteroid3.png')
        self.rect = self.image.get_rect()

        # Initial position of asteroid
        self.rect.x = random.randint(0, space_game.settings.screen_width)
        self.rect.y = 0

        # Speed of the asteroids
        self.speed = random.randint(2, 10)

        # Defining player collision to calculate lives and health
        self.collided_with_player = False

    # Updating position of the asteroid
    def update(self):
        self.rect.move_ip(0, self.speed)   # Asteroids fall vertically
        if self.rect.top > 750:
            self.kill()

    # Timer for adding new asteroids
    def add_asteroid_timer(self, interval=500):
        add_asteroid = pygame.USEREVENT + 1
        pygame.time.set_timer(add_asteroid, interval)
