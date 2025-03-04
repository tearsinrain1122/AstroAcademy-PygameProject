import pygame
from timer.timer_utils import convert_msecs, highest_str_time
pygame.font.init()


class Timer:
    # A class to record user-time information

    def __init__(self, space_game):
        # Initialise timer attributes
        self.space_game = space_game
        self.screen = space_game.settings.screen
        self.screen_rect = space_game.settings.screen.get_rect()
        self.start_time = pygame.time.get_ticks()
        self.font = space_game.settings.pixel_font
        self.counting_string = ""
        self.counting_image = None

        # Prep initial timer and high score
        self.prep_timer()
        self.prep_longest_time()

    def prep_timer(self):
        # Calculate gameplay time and turn into rendered image
        counting_time = pygame.time.get_ticks() - self.start_time
        self.counting_string = convert_msecs(counting_time)
        self.counting_image = self.font.render(self.counting_string, True,
                                               (255, 255, 255))

        # Position timer
        self.timer_rect = self.counting_image.get_rect()
        self.timer_rect.right = self.screen_rect.right - 20
        self.timer_rect.top = 20

    # Read high score from high score file
    def longest_time_file_read(self):
        leaderboard_file = open("timer/high_score.txt", "r")
        high_score = leaderboard_file.read()
        leaderboard_file.close()
        return str(high_score)

    # Write new high score to high score file
    def longest_time_file_write(self, new_time):
        leaderboard_file = open("timer/high_score.txt", "w")
        leaderboard_file.write(new_time)
        leaderboard_file.close()

    # Check for high score
    def check_longest_time(self, counting_string):
        """Check to see if there's a new high score."""
        self.high_score = self.longest_time_file_read()
        updated_high_score = highest_str_time(self.counting_string, self.high_score)
        self.longest_time_file_write(updated_high_score)

    # Position high score
    def prep_longest_time(self):
        self.high_score = self.longest_time_file_read()
        self.high_score_image = self.font.render(self.high_score, True,
                                                 (255, 255, 255))

        # Centre the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.timer_rect.top

    # Draw high score and timer to screen
    def draw_time(self):
        # Draw time to screen
        self.prep_timer()
        self.prep_longest_time()
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.counting_image, self.timer_rect)
