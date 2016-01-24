from pong import paddle
import settings
import pygame
from pygame.locals import *


class HorizontalPaddle(paddle.Paddle):

    defaults = {
        'OFFSET':       settings.WINDOW['PADDLE_OFFSET']
    ,   'ORIENTATION':  'HORIZONTAL'
    ,   'POSITION':     'BOTTOM'
    ,   'HEIGHT':       10
    ,   'WIDTH':        100
    ,   'SPEED':        7
    ,   'COLOUR':       settings.COLOURS['GREEN']
    }

    def __init__(self, screen, name, override=None):
        super().__init__(screen, name, override)
        self._status = {
            'pos_x':        settings.WINDOW['WIDTH']//2 - self._settings['WIDTH']//2
        ,   'pos_y':        settings.WINDOW['HEIGHT']- self._settings['OFFSET'] - self._settings['HEIGHT'] if self._settings['POSITION'] == 'BOTTOM' else self._settings['OFFSET']
        ,   'direction':    settings.DIRECTION['NONE']
        }


    def draw(self, screen):
        paddle = pygame.Surface((self._settings['WIDTH'],self._settings['HEIGHT']), pygame.SRCALPHA, 32)
        pygame.draw.circle(paddle, self._settings['COLOUR'], (self._settings['HEIGHT']//2, self._settings['HEIGHT']//2), self._settings['HEIGHT']//2, 0)
        pygame.draw.rect(paddle, self._settings['COLOUR'], Rect((self._settings['HEIGHT']//2,0),(self._settings['WIDTH'] - self._settings['HEIGHT'], self._settings['HEIGHT'])), 0)
        pygame.draw.circle(paddle, self._settings['COLOUR'], (self._settings['WIDTH'] - self._settings['HEIGHT']//2, self._settings['HEIGHT']//2), self._settings['HEIGHT']//2, 0)
        screen.blit(paddle, (self._status['pos_x'], self._status['pos_y']))

    def move(self, direction=None):
        if direction is not None:
            self._status['direction'] = direction[0]

        self._status['pos_x'] += self._status['direction'] * self._settings['SPEED']
        if self._status['pos_x'] >= settings.WINDOW_INNER_BORDERS['X_AXIS']['RIGHT'] - self._settings['WIDTH']:
            self._status['pos_x'] = settings.WINDOW_INNER_BORDERS['X_AXIS']['RIGHT'] - self._settings['WIDTH']
        elif self._status['pos_x'] <= settings.WINDOW_INNER_BORDERS['X_AXIS']['LEFT']:
            self._status['pos_x'] = settings.WINDOW_INNER_BORDERS['X_AXIS']['LEFT'] + 1

    def move_auto(self, ball):
        ball_info = ball.get_info()

        if ball_info['pos_x'] > self._status['pos_x'] - self._settings['WIDTH']//4:
            self._status['direction'] = settings.DIRECTION['RIGHT']
        elif ball_info['pos_x'] < self._status['pos_x'] + self._settings['WIDTH']//4:
            self._status['direction'] = settings.DIRECTION['LEFT']
        else:
            self._status['direction'] = settings.DIRECTION['NONE']

        self.move()
