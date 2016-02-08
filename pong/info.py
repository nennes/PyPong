import settings
import pygame
from pygame.locals import *


class Info:

    def __init__(self, screen):
        """

        :rtype: object
        """
        self.screen = screen    # copy the reference to the screen in a local variable

    @staticmethod
    def draw_text(screen, colour, pos_x, pos_y, text):
        font = pygame.font.SysFont(settings.FONT['NAME'], settings.FONT['SIZE'])
        rendered_text = font.render(str(text), True, colour)
        screen.blit(rendered_text, (pos_x, pos_y))

    def draw(self, screen, score, high_score):
        scoreboard = pygame.Surface((settings.WINDOW['WIDTH'], settings.WINDOW['INFO_HEIGHT'])).convert()
        scoreboard.fill(settings.COLOURS['BLACK'])
        pygame.draw.rect(
            scoreboard
        ,   settings.COLOURS['WHITE']
        ,   Rect(
                (
                    settings.SCOREBOARD_INNER_BORDERS['X_AXIS']['LEFT'] - settings.WINDOW['LINE_THICKNESS']//2
                ,   settings.SCOREBOARD_INNER_BORDERS['Y_AXIS']['TOP'] - settings.WINDOW['LINE_THICKNESS']
                )
            ,   (
                    settings.SCOREBOARD_INNER_BORDERS['X_AXIS']['RIGHT'] - settings.WINDOW['LINE_THICKNESS']
                ,   settings.SCOREBOARD_INNER_BORDERS['Y_AXIS']['BOTTOM'] - settings.SCOREBOARD_INNER_BORDERS['Y_AXIS']['TOP'] - settings.WINDOW['LINE_THICKNESS']//2
                )
            )
        ,   settings.WINDOW['LINE_THICKNESS']
        )
        self.draw_text(
           scoreboard
        ,   settings.COLOURS['WHITE']
        ,   (settings.WINDOW_INNER_BORDERS['X_AXIS']['LEFT'] + settings.WINDOW['WIDTH']//20)
        ,   (settings.WINDOW_INNER_BORDERS['Y_AXIS']['TOP'] + settings.WINDOW['INFO_HEIGHT']//10)
        ,   "Score:  " + str(score)
        )
        self.draw_text(
            scoreboard
        ,   settings.COLOURS['WHITE']
        ,   (settings.WINDOW_INNER_BORDERS['X_AXIS']['LEFT'] + settings.WINDOW['WIDTH']//20)
        ,   (settings.WINDOW_INNER_BORDERS['Y_AXIS']['TOP'] + settings.WINDOW['INFO_HEIGHT']//2)
        ,   "High Score:  " + str(high_score)
        )
        screen.blit(scoreboard, (0, settings.WINDOW['HEIGHT']))


