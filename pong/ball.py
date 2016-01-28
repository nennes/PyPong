from typing import Dict
import settings
import pygame


class Ball:

    defaults = {
        'RADIUS':   7
    ,   'SPEED':    7
    ,   'COLOUR':   settings.COLOURS['BLUE']
    }

    def __init__(self, screen, override = defaults):
        self._settings = override
        self.screen = screen  # copy the reference to the screen in a local variable

        self._status = {
            'pos_x':        settings.WINDOW['WIDTH']//2
        ,   'pos_y':        settings.WINDOW['HEIGHT']//2
        ,   'direction_x':  1.0
        ,   'direction_y':  0.8
        }

    def get_info(self) -> Dict[str, int]:
        return {
            'pos_x':    self._status['pos_x']
        ,   'pos_y':    self._status['pos_y']
        ,   'RADIUS':   self._settings['RADIUS']
        }

    def draw(self, screen) -> None:
        ball = pygame.Surface((2*self._settings['RADIUS'],2*self._settings['RADIUS']), pygame.SRCALPHA, 32)
        pygame.draw.circle(ball, self._settings['COLOUR'], (self._settings['RADIUS'], self._settings['RADIUS']), self._settings['RADIUS'], 0)
        screen.blit(ball, (self._status['pos_x'] - self._settings['RADIUS'], self._status['pos_y'] - self._settings['RADIUS']))

    def bounce_wall(self) -> bool:
        if(self._status['pos_x'] <= settings.WINDOW_INNER_BORDERS['X_AXIS']['LEFT'] + self._settings['RADIUS']) or (self._status['pos_x'] >= settings.WINDOW_INNER_BORDERS['X_AXIS']['RIGHT'] - self._settings['RADIUS']):
            self._status['direction_x'] *= -1
            return True
        if (self._status['pos_y'] <= settings.WINDOW_INNER_BORDERS['Y_AXIS']['TOP'] + self._settings['RADIUS']) or (self._status['pos_y'] >= settings.WINDOW_INNER_BORDERS['Y_AXIS']['BOTTOM'] - self._settings['RADIUS']):
            self._status['direction_y'] *= -1
            return True
        return False

    def move(self) -> None:
        self._status['pos_x'] += self._status['direction_x'] * self._settings['SPEED']
        self._status['pos_y'] += self._status['direction_y'] * self._settings['SPEED']
