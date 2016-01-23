import settings
from copy import copy
from abc import ABCMeta, abstractmethod


class Paddle:
    __metaclass__ = ABCMeta

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

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def move(self, direction=None):
        pass

    @abstractmethod
    def move_auto(self, ball):
        pass
