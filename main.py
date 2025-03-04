import pygame
import sys


from settings.settings import Settings
from astronaut_asteroids.astronaut import Astronaut
from astronaut_asteroids.asteroids import Asteroids
from timer.timer import Timer
from health_bar.health_bar import HealthBar
from facts.facts import Facts
from settings.screens import WelcomeScreen, GameOverScreen
from pygame.locals import *
pygame.font.init()


class SpaceGame:

    def __init__(self, running):
        pygame.init()

        # Initialising classes
        self.settings = Settings(self)
        self.astronaut = Astronaut(self)
        self.asteroid = Asteroids(self)
        self.fact = Facts(self)
        self.health_bar = HealthBar(self)
        self.timer = None  # Placeholder as only initialised when game loop begins

        # Welcome screen player name input
        self.user_text = ""

        # Initialising sprite groups
        self.asteroids = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.astronaut)
        self.facts_group = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

        self.running = running

    # Custom event for adding asteroids
    def add_asteroid(self):
        new_asteroid = Asteroids(self)
        self.asteroids.add(new_asteroid)
        self.all_sprites.add(new_asteroid)

    # Custom event for adding facts
    def add_fact(self):
        new_fact = Facts(self)
        self.facts_group.add(new_fact)
        self.all_sprites.add(new_fact)

    # Collision function to control lives, health bar and game status
    def collision(self):
        for asteroid in self.asteroids:
            if pygame.sprite.collide_rect(self.astronaut, asteroid) and not asteroid.collided_with_player:
                self.settings.life_lost_sfx.play()  # Play life lost sound effect
                self.astronaut.lives -= 1
                asteroid.collided_with_player = True
                asteroid.kill()
                print(self.astronaut.lives) # manually testing to view the amount of lives
                print('hit')  # Manually testing collisions
                self.health_bar.current_health -= 30  # Decrease health bar
                print('health bar reduced') # manual testing for health bar

                if self.astronaut.lives <= 0:
                    self.timer.check_longest_time(self.timer.counting_string)
                    self.running = False
                    text_five = f'{self.user_text} the astronaut survived for {self.timer.counting_string}'
                    GameOverScreen(self, self.settings.text_four, text_five, self.settings.text_six).run_screen()

    # Checking for new events every frame (including closing the window, adding facts/asteroids and key presses)
    def check_events(self):
        for event in pygame.event.get():
            try:
                if event.type == pygame.QUIT:
                    print("Exit button pressed on screen") # manual testing for exiting the game
                    self.timer.check_longest_time(self.timer.counting_string)
                    sys.exit()
                    
                # adding asteroids
                elif event.type == pygame.USEREVENT + 1:
                    self.add_asteroid()
                # adding facts
                elif event.type == pygame.USEREVENT + 2:
                    self.add_fact()
                elif event.type == pygame.KEYDOWN:
                    self.check_key_events(event, True)  
                    self.settings.arrow_keys_sfx.play()
                elif event.type == pygame.KEYUP:
                    self.check_key_events(event, False) 
            except Exception as e:
                print(f"Error checking event: {e}")

    # Defining astronaut movement status
    def check_key_events(self, event, movement_status: bool):
        if event.key == pygame.K_RIGHT:
            self.astronaut.flying_right = movement_status
        elif event.key == pygame.K_LEFT:
            self.astronaut.flying_left = movement_status
        elif event.key == pygame.K_UP:
            self.astronaut.flying_up = movement_status
        elif event.key == pygame.K_DOWN:
            self.astronaut.flying_down = movement_status

    # Drawing all sprites (astronaut, asteroids, facts), timer, health bar and lives on screen
    def draw_sprites_on_screen(self):
        text = self.settings.pixel_font.render(f'Lives:{self.astronaut.lives}', True, (255, 255, 255))
        self.settings.screen.blit(text, (20, 20))
        for entity in self.all_sprites:
            self.settings.screen.blit(entity.image, entity.rect)
        # draw timer
        self.timer.draw_time()
        # draw health bar
        self.health_bar.draw_health_bar()

    # Main game loop
    def run(self):
        welcome_screen = WelcomeScreen(self, self.settings.text_one, self.settings.text_two, self.settings.text_three)
        welcome_screen.run_screen()
        self.timer = Timer(self)

        while self.running:
            # Draw scrolling background
            self.settings.screen.blit(self.settings.background_image, self.settings.background_rect)
            self.settings.background_scrolling()

            self.check_events()
            self.facts_group.update()
            self.asteroids.update()
            self.astronaut.update()

            self.collision()
            self.draw_sprites_on_screen()

            pygame.display.flip()
            self.clock.tick(30)


if __name__ == '__main__':
    game = SpaceGame(False)
    game.run()