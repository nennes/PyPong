import settings
import pygame
from pygame.locals import *


class Info:

    def __init__(self, screen):
        self.screen = screen  # copy the reference to the screen in a local variable

    def draw(self, screen):
        scoreboard = pygame.Surface((settings.WINDOW['WIDTH'], settings.WINDOW['INFO_HEIGHT'])).convert()
        scoreboard.fill(settings.COLOURS['BLACK'])
        pygame.draw.rect(
            scoreboard
        ,   settings.COLOURS['WHITE']
        ,   Rect(
                (
                    settings.WINDOW_INNER_BORDERS['X_AXIS']['LEFT'] - settings.WINDOW['LINE_THICKNESS']//2
                ,   settings.WINDOW_INNER_BORDERS['Y_AXIS']['TOP'] - settings.WINDOW['LINE_THICKNESS']//2
                )
            ,   (
                    settings.WINDOW['WIDTH'] - settings.WINDOW['PADDLE_OFFSET'] - settings.WINDOW['LINE_THICKNESS']
                ,   settings.WINDOW['INFO_HEIGHT'] - settings.WINDOW['PADDLE_OFFSET'] - settings.WINDOW['LINE_THICKNESS']
                )
            )
        ,   settings.WINDOW['LINE_THICKNESS']
        )
        screen.blit(scoreboard, (0, settings.WINDOW['HEIGHT']))


