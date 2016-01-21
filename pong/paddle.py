import settings
import pygame
from pygame.locals import *

class Paddle:

    _defaults = {
        'OFFSET':   settings.WINDOW['PADDLE_OFFSET']
    ,   'LENGTH':   100
    ,   'WIDTH':    10
    ,   'SPEED':    5
    ,   'COLOUR':   settings.COLOURS['GREEN']
    }

    _status = {
        'pos_x': 0
    ,   'pos_y': 0
    ,   'direction': settings.DIRECTION['NONE']
    }

    def __init__(self, screen, override=_defaults):
        self._settings = override
        self.screen = screen  # copy the reference to the screen in a local variable

        self._status['pos_x'] = settings.WINDOW_INNER_BORDERS['X_AXIS']['LEFT'] + settings.WINDOW['PADDLE_OFFSET']//2
        self._status['pos_y'] = settings.WINDOW['HEIGHT']//2 - (self._settings['LENGTH'] + self._settings['WIDTH'])//2

    def get_info(self):
        return {
            'x_axis': {
                    'left': self._status['pos_x']
                ,   'right': self._status['pos_x'] + self._settings['WIDTH']
                }
        ,   'y_axis': {
                'top': self._status['pos_y']
            ,   'bottom': self._status['pos_y'] + self._settings['LENGTH']
            }
        ,   'direction': self._status['direction']
        }

    def draw(self, screen):
        paddle = pygame.Surface((self._settings['WIDTH'],self._settings['WIDTH'] + self._settings['LENGTH']), pygame.SRCALPHA, 32)
        pygame.draw.circle(paddle, self._settings['COLOUR'], (self._settings['WIDTH']//2, self._settings['WIDTH']//2), self._settings['WIDTH']//2, 0)
        pygame.draw.rect(paddle, self._settings['COLOUR'], Rect((0,self._settings['WIDTH']//2),(self._settings['WIDTH'],self._settings['LENGTH']-self._settings['WIDTH'])), 0)
        pygame.draw.circle(paddle, self._settings['COLOUR'], (self._settings['WIDTH']//2, self._settings['LENGTH'] - self._settings['WIDTH']//2), self._settings['WIDTH']//2, 0)
        screen.blit(paddle, (self._status['pos_x'], self._status['pos_y']))

    def move(self, direction=None):
        if direction is not None:
            self._status['direction'] = direction
        self._status['pos_y'] += self._status['direction'] * self._settings['SPEED']

        if self._status['pos_y'] <= settings.WINDOW_INNER_BORDERS['Y_AXIS']['TOP']:
            self._status['pos_y'] = settings.WINDOW_INNER_BORDERS['Y_AXIS']['TOP'] + 1
        elif self._status['pos_y'] >= settings.WINDOW_INNER_BORDERS['Y_AXIS']['BOTTOM'] - self._settings['LENGTH']:
            self._status['pos_y'] = settings.WINDOW_INNER_BORDERS['Y_AXIS']['BOTTOM'] - self._settings['LENGTH']

    def move_auto(self, ball):

        ball_info =  ball.get_info()
        if ball_info['pos_y'] > self._status['pos_y'] + self._settings['LENGTH']//4:
            self._status['direction'] = settings.DIRECTION['DOWN']
        elif ball_info['pos_y'] < self._status['pos_y'] + 3*self._settings['LENGTH']//4:
            self._status['direction'] = settings.DIRECTION['UP']
        else:
            self._status['direction'] = settings.DIRECTION['NONE']

        self.move()





