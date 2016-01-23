import settings
import pygame
from pygame.locals import *
from copy import copy

class Paddle:

    defaults = {
        'OFFSET':       settings.WINDOW['PADDLE_OFFSET']
    ,   'ORIENTATION':  'VERTICAL'
    ,   'HEIGHT':       100
    ,   'WIDTH':        10
    ,   'SPEED':        6
    ,   'COLOUR':       settings.COLOURS['GREEN']
    }

    def __init__(self, screen, name, override=None):
        if override is None:
            self._settings = self.defaults  # point to the static defaults
        else:
            self._settings = copy(override) # make a local shallow copy of the override params

        self.screen = screen  # copy the reference to the screen in a local variable
        self.name = name

        self._status = {
            'pos_x':        settings.WINDOW_INNER_BORDERS['X_AXIS']['LEFT'] + self._settings['OFFSET']
        ,   'pos_y':        settings.WINDOW['HEIGHT']//2 - (self._settings['HEIGHT'] + self._settings['WIDTH'])//2
        ,   'direction':    settings.DIRECTION['NONE']
        }

        if self._settings['ORIENTATION'] == 'VERTICAL':
            pass
        elif self._settings['ORIENTATION'] == 'HORIZONTAL':
            # swap width and height
            self._settings['WIDTH'], self._settings['HEIGHT'] = self._settings['HEIGHT'], self._settings['WIDTH']
        else:
            raise ValueError('Incorrect orientation provided for the paddle %s' % self.name)

    def get_info(self):
        return {
            'x_axis': {
                    'left':     self._status['pos_x']
                ,   'right':    self._status['pos_x'] + self._settings['WIDTH']
                }
        ,   'y_axis': {
                'top':      self._status['pos_y']
            ,   'bottom':   self._status['pos_y'] + self._settings['HEIGHT']
            }
        ,   'direction':    self._status['direction']
        }

    def draw(self, screen):
        paddle = pygame.Surface((self._settings['WIDTH'],self._settings['HEIGHT']), pygame.SRCALPHA, 32)
        if self._settings['ORIENTATION'] == 'VERTICAL':
            pygame.draw.circle(paddle, self._settings['COLOUR'], (self._settings['WIDTH']//2, self._settings['WIDTH']//2), self._settings['WIDTH']//2, 0)
            pygame.draw.rect(paddle, self._settings['COLOUR'], Rect((0,self._settings['WIDTH']//2),(self._settings['WIDTH'],self._settings['HEIGHT']-self._settings['WIDTH'])), 0)
            pygame.draw.circle(paddle, self._settings['COLOUR'], (self._settings['WIDTH']//2, self._settings['HEIGHT'] - self._settings['WIDTH']//2), self._settings['WIDTH']//2, 0)
        elif self._settings['ORIENTATION'] == 'HORIZONTAL':
            pygame.draw.circle(paddle, self._settings['COLOUR'], (self._settings['HEIGHT']//2, self._settings['HEIGHT']//2), self._settings['HEIGHT']//2, 0)
            pygame.draw.rect(paddle, self._settings['COLOUR'], Rect((self._settings['HEIGHT']//2,0),(self._settings['WIDTH'] - self._settings['HEIGHT'], self._settings['HEIGHT'])), 0)
            pygame.draw.circle(paddle, self._settings['COLOUR'], (self._settings['WIDTH'] - self._settings['HEIGHT']//2, self._settings['HEIGHT']//2), self._settings['HEIGHT']//2, 0)


        screen.blit(paddle, (self._status['pos_x'], self._status['pos_y']))

    def move(self, direction=None):
        if direction is not None:
            self._status['direction'] = direction

        if self._settings['ORIENTATION'] == 'VERTICAL':
            self._status['pos_y'] += self._status['direction'] * self._settings['SPEED']
            if self._status['pos_y'] <= settings.WINDOW_INNER_BORDERS['Y_AXIS']['TOP']:
                self._status['pos_y'] = settings.WINDOW_INNER_BORDERS['Y_AXIS']['TOP'] + 1
            elif self._status['pos_y'] >= settings.WINDOW_INNER_BORDERS['Y_AXIS']['BOTTOM'] - self._settings['HEIGHT']:
                self._status['pos_y'] = settings.WINDOW_INNER_BORDERS['Y_AXIS']['BOTTOM'] - self._settings['HEIGHT']
        elif self._settings['ORIENTATION'] == 'HORIZONTAL':
            self._status['pos_x'] += self._status['direction'] * self._settings['SPEED']
            if self._status['pos_x'] >= settings.WINDOW_INNER_BORDERS['X_AXIS']['RIGHT'] - self._settings['WIDTH']:
                self._status['pos_x'] = settings.WINDOW_INNER_BORDERS['X_AXIS']['RIGHT'] - self._settings['WIDTH']
            elif self._status['pos_x'] <= settings.WINDOW_INNER_BORDERS['X_AXIS']['LEFT']:
                self._status['pos_x'] = settings.WINDOW_INNER_BORDERS['X_AXIS']['LEFT'] + 1



    def move_auto(self, ball):

        ball_info =  ball.get_info()

        if self._settings['ORIENTATION'] == 'VERTICAL':
            if ball_info['pos_y'] > self._status['pos_y'] + self._settings['HEIGHT']//4:
                self._status['direction'] = settings.DIRECTION['DOWN']
            elif ball_info['pos_y'] < self._status['pos_y'] + 3*self._settings['HEIGHT']//4:
                self._status['direction'] = settings.DIRECTION['UP']
            else:
                self._status['direction'] = settings.DIRECTION['NONE']
        elif self._settings['ORIENTATION'] == 'HORIZONTAL':
            if ball_info['pos_x'] > self._status['pos_x'] - self._settings['WIDTH']//4:
                self._status['direction'] = settings.DIRECTION['RIGHT']
            elif ball_info['pos_x'] < self._status['pos_x'] + self._settings['WIDTH']//4:
                self._status['direction'] = settings.DIRECTION['LEFT']
            else:
                self._status['direction'] = settings.DIRECTION['NONE']



        self.move()





