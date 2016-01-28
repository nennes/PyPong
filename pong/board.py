import settings
import pygame
from pygame.locals import *


class Board:

    settings = {
        'line_colour':  settings.COLOURS['WHITE']
    }

    def __init__(self, screen):
        self.screen = screen  # copy the reference to the screen in a local variable

    def draw(self, screen):
        background = pygame.Surface((settings.WINDOW['WIDTH'], settings.WINDOW['HEIGHT'])).convert()
        background.fill(settings.COLOURS['BLACK'])
        pygame.draw.rect(
            background
        ,   self.settings['line_colour']
        ,   Rect(
                (
                    settings.WINDOW_INNER_BORDERS['X_AXIS']['LEFT'] - settings.WINDOW['LINE_THICKNESS']//2
                ,   settings.WINDOW_INNER_BORDERS['Y_AXIS']['TOP'] - settings.WINDOW['LINE_THICKNESS']//2
                )
            ,   (
                    settings.WINDOW['WIDTH'] - settings.WINDOW['PADDLE_OFFSET'] - settings.WINDOW['LINE_THICKNESS']
                ,   settings.WINDOW['HEIGHT'] - settings.WINDOW['PADDLE_OFFSET'] - settings.WINDOW['LINE_THICKNESS']
                )
            )
        ,   settings.WINDOW['LINE_THICKNESS']
        )
        pygame.draw.aaline(background, settings.COLOURS['WHITE'], (settings.WINDOW['PADDLE_OFFSET']//2, settings.WINDOW['PADDLE_OFFSET']//2), ((settings.WINDOW['WIDTH'] - settings.WINDOW['PADDLE_OFFSET']//2), (settings.WINDOW['HEIGHT'] - settings.WINDOW['PADDLE_OFFSET']//2)))
        screen.blit(background, (0, 0))



