import pygame
import sys


class Settings:

    def __init__(self, space_game):
        self.space_game = space_game

        self.screen_width = 750
        self.screen_height = 750

        try:
            self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
            pygame.display.set_caption('Astro Academy')
        except pygame.error as e:
            print(f"Failed to initialize the game window: {e}")
            sys.exit()

        # Initialising game text for rendering
        self.text_one = "Astro Academy"
        self.text_two = "Enter your name"
        self.text_three = "Press the enter key to continue"

        self.text_four = "Game Over"
        self.text_six = "Press the enter key to play again"

        self.load_fonts()
        self.load_sounds()
        self.load_background()

    def load_sounds(self):
        try:
            # Loading sound effects
            self.game_soundtrack_sfx = pygame.mixer.Sound('sounds/game_soundtrack_sfx.wav')  # Background music
            self.arrow_keys_sfx = pygame.mixer.Sound('sounds/arrow_keys_sfx.wav')  # Arrow key tone
            self.arrow_keys_sfx.set_volume(0.3)  # Setting volume for arrow keys
            self.life_lost_sfx = pygame.mixer.Sound('sounds/life_lost_sfx.wav')  # Sound when losing a life
            self.life_lost_sfx.set_volume(0.9)  # Setting volume for life lost sound
            self.game_over_sfx = pygame.mixer.Sound('sounds/game_over_sfx.wav')  # Game over sound

            # Background music
            pygame.mixer.music.load('sounds/game_soundtrack_sfx.wav')
            pygame.mixer.music.set_volume(0.25)
            pygame.mixer.music.play(-1)  # -1 = infinite looping

        except pygame.error as e:
            print(f"Error loading sounds: {e}")

    def load_fonts(self):
        # Fonts for the game
        try:
            self.space_font = pygame.font.Font("fonts/game_font2.otf", 70)
            self.pixel_font = pygame.font.Font("fonts/PressStart2P.ttf", 30)
            self.small_pixel_font = pygame.font.Font('fonts/PressStart2P.ttf', 15)
        except (pygame.error, FileNotFoundError) as e:
            print(f"Error loading fonts: {e}")
            self.space_font = pygame.font.SysFont('Comic Sans MS', 60)
            self.pixel_font = pygame.font.SysFont('Comic Sans MS', 30)
            self.small_pixel_font = pygame.font.SysFont('Comic Sans MS', 15)

    def load_background(self):
        # Initialising background
        self.scroll_x = 0
        self.scroll_y = 0

        try:
            self.background_image = pygame.image.load('images/stars.jpg')
        except pygame.error as e:
            print(f"Error loading image: {e}")
            self.background_image = pygame.Surface((self.screen_width, self.screen_height))  # Fallback to a plain surface if image fails

        self.background_rect = self.background_image.get_rect()
        self.background_y = -self.background_rect.height


    # Make the background scroll infinitely
    def background_scrolling(self):
        self.scroll_y += 1
        self.background_y += 1

        # Draw the background twice
        self.screen.blit(self.background_image, (self.scroll_x, self.scroll_y))
        self.screen.blit(self.background_image, (self.scroll_x, self.background_y))

        # Reset the background position at the end of game window
        if self.scroll_y > self.background_rect.height:
            self.scroll_y = -self.background_rect.height

        if self.background_y > self.background_rect.height:
            self.background_y = -self.background_rect.height