from copy import copy
from abc import ABCMeta, abstractmethod
import pygame
import os


class Paddle:
    __metaclass__ = ABCMeta

    def __init__(self, screen, name, override=None):
        if override is None:
            self._settings = self.defaults  # point to the static defaults
        else:
            self._settings = copy(override) # make a local shallow copy of the override params

        self.screen = screen  # copy the reference to the screen in a local variable
        self.name = name

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
        ,   'name':         self.name
        }

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def move(self, direction=None):
        pass

    @abstractmethod
    def move_auto(self, ball):
        pass

    @abstractmethod
    def bounce(self, ball):
        pass

    @abstractmethod
    def bounce_direction(self, ball):
        pass

    def collided_with(self, ball) -> bool:
        ball_info   = ball.get_info()
        paddle_info = self.get_info()

        if( paddle_info['x_axis']['left']   - ball_info['RADIUS'] < ball_info['pos_x'] and
            paddle_info['x_axis']['right']  + ball_info['RADIUS'] > ball_info['pos_x'] and
            paddle_info['y_axis']['bottom'] + ball_info['RADIUS'] > ball_info['pos_y'] and
            paddle_info['y_axis']['top']    - ball_info['RADIUS'] < ball_info['pos_y']):
            return True
        else:
            return False
