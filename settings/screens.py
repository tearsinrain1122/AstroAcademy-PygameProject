import pygame
import sys
from pygame.locals import *
from abc import ABC, abstractmethod


class GameScreens(ABC):

    def __init__(self, space_game, text_1, text_2, text_3):
        self.space_game = space_game
        self.settings = space_game.settings
        self.screen = space_game.settings.screen
        self.clock = space_game.clock

        self.text_1 = text_1
        self.text_1Surface = self.settings.space_font.render(f'{text_1}', True, (255, 255, 255))
        self.text_1Rect = self.text_1Surface.get_rect()
        self.text_1Rect.midtop = (self.settings.screen_width/2, self.settings.screen_height/6)

        self.text_2 = text_2
        self.text_2Surface = self.settings.small_pixel_font.render(f'{text_2}', True, (255, 255, 255))
        self.text_2Rect = self.text_2Surface.get_rect()
        self.text_2Rect.midtop = (self.settings.screen_width/2, self.settings.screen_height/3+10)

        self.text_3 = text_3
        self.text_3Surface = self.settings.small_pixel_font.render(f'{text_3}', True, (255, 255, 255))
        self.text_3Rect = self.text_3Surface.get_rect()
        self.text_3Rect.midbottom = (self.settings.screen_width/2, 600)

    @abstractmethod
    def run_screen(self):
        pass

    def blit_things(self, show_user_text=False):
        self.settings.screen.blit(self.settings.background_image, self.settings.background_rect)
        self.settings.background_scrolling()

        # Blit the welcome message and name request
        self.settings.screen.blit(self.text_1Surface, self.text_1Rect)
        self.settings.screen.blit(self.text_2Surface, self.text_2Rect)
        self.settings.screen.blit(self.text_3Surface, self.text_3Rect)

        if show_user_text:
            text_surface = self.settings.pixel_font.render(self.space_game.user_text, True, (255, 255, 255))
            text_width = text_surface.get_width()
            x_position = (self.settings.screen_width / 2) - (text_width / 2)
            self.settings.screen.blit(text_surface, (x_position, self.settings.screen_height / 2 + 20))

        pygame.display.flip()
        self.clock.tick(60)  # Limit the frame rate


class WelcomeScreen(GameScreens):
    def __init__(self, space_game, text_1, text_2, text_3):
        super().__init__(space_game, text_1, text_2, text_3)

    def run_screen(self):
        while not self.space_game.running:  # Continue loop until the game starts
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN:  # If Enter is pressed, game starts
                        print('start game')
                        self.space_game.running = True
                        break

                    elif event.key == pygame.K_BACKSPACE:
                        self.space_game.user_text = self.space_game.user_text[:-1]
                    else:
                        if len(self.space_game.user_text) < 10:
                            self.space_game.user_text += event.unicode

            self.blit_things(show_user_text=True)


class GameOverScreen(GameScreens):

    def __init__(self, space_game, text_1, text_2, text_3):
        super().__init__(space_game, text_1, text_2, text_3)
        self.text_2Rect.midtop = (self.settings.screen_width/2, self.settings.screen_height/2)

    def run_screen(self):
        while not self.space_game.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN:  # If Enter is pressed, game starts
                        # Reinitialize the game state
                        self.space_game.__init__(False)
                        self.space_game.run()
                        return
            self.blit_things(show_user_text=False)
