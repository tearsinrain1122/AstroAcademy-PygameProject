import pygame
from pygame.sprite import Sprite


class Astronaut(Sprite):
    # A class inherited from the pygame.sprite.Sprite base class to control the player astronaut sprite
    def __init__(self, space_game):
        super().__init__()
        self.screen = space_game.settings.screen
        self.screen_rect = space_game.settings.screen.get_rect()

        # Loading astronaut image and rect
        self.image = pygame.image.load('images/Simple.png')
        self.rect = self.image.get_rect()    

        # Initial position of astronaut
        self.rect.midbottom = self.screen_rect.midbottom

        # Initiating lives for astronaut
        self.lives = 3

        # Defining default astronaut movement status
        self.flying_right = False
        self.flying_left = False
        self.flying_up = False
        self.flying_down = False

    # Updating position of the astronaut
    def update(self):
        if self.flying_right:
            self.rect.move_ip(5, 0)
            #print('moving right') # manually testing movement 
        if self.flying_left:
            self.rect.move_ip(-5, 0)
            # print('moving left')
        if self.flying_up:
            self.rect.move_ip(0, -5)
            # print('moving up')
        if self.flying_down:
            self.rect.move_ip(0, 5)
            # print('moving down')

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
            # print("Hit the left edge!") # Manual testing screen boundaries
        if self.rect.right > 750:
            self.rect.right = 750
            # print("Hit the right edge!")
        if self.rect.top <= 0:
            self.rect.top = 0
            # print("Hit the top edge!")
        if self.rect.bottom >= 750:
            self.rect.bottom = 750
            # print("Hit the bottom edge!")

    # Function to return astronaut position for movement unit testing
    def position(self):
        return f"x: {self.rect.x}, y: {self.rect.y}"
