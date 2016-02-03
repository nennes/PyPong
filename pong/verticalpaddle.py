from pong import paddle
import settings
import pygame
from pygame.locals import *


class VerticalPaddle(paddle.Paddle):

    defaults = {
        'OFFSET':       settings.WINDOW['PADDLE_OFFSET']
    ,   'ORIENTATION':  'VERTICAL'
    ,   'POSITION':     'LEFT'
    ,   'HEIGHT':       100
    ,   'WIDTH':        10
    ,   'SPEED':        7
    ,   'COLOUR':       settings.COLOURS['GREEN']
    }

    def __init__(self, screen, name, override=None):
        super().__init__(screen, name, override)
        self._status = {
            'pos_x':        settings.WINDOW['WIDTH']- self._settings['OFFSET'] - self._settings['WIDTH'] if self._settings['POSITION'] == 'RIGHT' else self._settings['OFFSET']
        ,   'pos_y':        settings.WINDOW['HEIGHT']//2 + self._settings['HEIGHT']//2
        ,   'direction':    settings.DIRECTION['NONE']
        }

    def draw(self, screen):
        paddle = pygame.Surface((self._settings['WIDTH'],self._settings['HEIGHT']), pygame.SRCALPHA, 32)
        pygame.draw.circle(paddle, self._settings['COLOUR'], (self._settings['WIDTH']//2, self._settings['WIDTH']//2), self._settings['WIDTH']//2, 0)
        pygame.draw.rect(paddle, self._settings['COLOUR'], Rect((0,self._settings['WIDTH']//2),(self._settings['WIDTH'],self._settings['HEIGHT']-self._settings['WIDTH'])), 0)
        pygame.draw.circle(paddle, self._settings['COLOUR'], (self._settings['WIDTH']//2, self._settings['HEIGHT'] - self._settings['WIDTH']//2), self._settings['WIDTH']//2, 0)
        screen.blit(paddle, (self._status['pos_x'], self._status['pos_y']))

    def move(self, direction=None, ball_info=None):
        if direction is not None:
            self._status['direction'] = direction[1]

        self._status['pos_y'] += self._status['direction'] * self._settings['SPEED']

        # Handle reaching the edges
        if self._status['pos_y'] <= settings.WINDOW_INNER_BORDERS['Y_AXIS']['TOP']:
            self._status['pos_y'] = settings.WINDOW_INNER_BORDERS['Y_AXIS']['TOP'] + 1
        elif self._status['pos_y'] >= settings.WINDOW_INNER_BORDERS['Y_AXIS']['BOTTOM'] - self._settings['HEIGHT']:
            self._status['pos_y'] = settings.WINDOW_INNER_BORDERS['Y_AXIS']['BOTTOM'] - self._settings['HEIGHT']

    def move_auto(self, ball):
        ball_info =  ball.get_info()

        if ball_info['pos_y'] > self._status['pos_y'] + self._settings['HEIGHT']//4:
            self._status['direction'] = settings.DIRECTION['DOWN']
        elif ball_info['pos_y'] < self._status['pos_y'] + 3*self._settings['HEIGHT']//4:
            self._status['direction'] = settings.DIRECTION['UP']
        else:
            self._status['direction'] = settings.DIRECTION['NONE']
        self.move(ball_info=ball_info)

    def bounce(self, ball) -> bool:
        if self.collided_with(ball):

            if self.bounce_direction(ball) == settings.C_HORIZONTAL:
                ball._status['direction_y'] *= -1
                return True
            else:
                ball._status['direction_x'] *= -1
                return True
        else:
            return False

    def bounce_direction(self, ball) -> str:
        ball_info   = ball.get_info()
        paddle_info = self.get_info()

        if( ball_info['pos_y'] - ball_info['RADIUS'] < paddle_info['y_axis']['top'] or
            ball_info['pos_y'] + ball_info['RADIUS'] > paddle_info['y_axis']['bottom']):
            return settings.C_HORIZONTAL
        else:
            return settings.C_VERTICAL
