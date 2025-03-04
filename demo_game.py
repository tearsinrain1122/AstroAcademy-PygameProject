import pygame.locals

from main import SpaceGame
import pygame


class DemoGame(SpaceGame):
    def __init__(self):
        SpaceGame.__init__(self, running=True)
        self.background_image = pygame.Surface((self.settings.screen_width, self.settings.screen_height))
        self.background_rect = self.background_image.get_rect()
        self.screen = pygame.display.set_mode([self.settings.screen_width, self.settings.screen_height])

    def run(self, key):
        self.screen.blit(self.background_image, self.background_rect)
        new_event = pygame.event.Event(pygame.locals.KEYDOWN, key=key)
        pygame.event.post(new_event)
        self.check_events()
        self.astronaut.update()
        pygame.display.flip()
        self.clock.tick(1)
        return self.astronaut.position()


demo_game = DemoGame()

