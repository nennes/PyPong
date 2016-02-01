from copy import copy
from abc import ABCMeta, abstractmethod
import pygame
import os

from info import Info


class Paddle:
    __metaclass__ = ABCMeta

    _sounds = {
         'BOUNCE':   os.path.join("sounds", "bounce.wav")
    }

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
            pygame.mixer.music.load(self._sounds['BOUNCE'])
            pygame.mixer.music.play()
            Info.increase_score()
            return True
        else:
            return False
