import settings
import pygame
import math

class Ball():

    defaults = {
        'RADIUS':   7
    ,   'SPEED':    8
    ,   'COLOUR':   settings.COLOURS['BLUE']
    }

    def __init__(self, screen, override = defaults):
        self._settings = override
        self.screen = screen  # copy the reference to the screen in a local variable

        self._status = {
            'pos_x':        settings.WINDOW['WIDTH']//2
        ,   'pos_y':        settings.WINDOW['HEIGHT']//2
        ,   'direction_x':  1
        ,   'direction_y':  0.8
        }

    def get_info(self):
        return {
            'pos_x':    self._status['pos_x']
        ,   'pos_y':    self._status['pos_y']
        }

    def draw(self, screen):
        ball = pygame.Surface((2*self._settings['RADIUS'],2*self._settings['RADIUS']), pygame.SRCALPHA, 32)
        pygame.draw.circle(ball, self._settings['COLOUR'], (self._settings['RADIUS'], self._settings['RADIUS']), self._settings['RADIUS'], 0)
        screen.blit(ball, (self._status['pos_x'] - self._settings['RADIUS'], self._status['pos_y'] - self._settings['RADIUS']))

    def bounce_wall(self):
        if(self._status['pos_x'] <= settings.WINDOW_INNER_BORDERS['X_AXIS']['LEFT'] + self._settings['RADIUS']) or (self._status['pos_x'] >= settings.WINDOW_INNER_BORDERS['X_AXIS']['RIGHT'] - self._settings['RADIUS']):
            self._status['direction_x'] *= -1
        if (self._status['pos_y'] <= settings.WINDOW_INNER_BORDERS['Y_AXIS']['TOP'] + self._settings['RADIUS']) or (self._status['pos_y'] >= settings.WINDOW_INNER_BORDERS['Y_AXIS']['BOTTOM'] - self._settings['RADIUS']):
            self._status['direction_y'] *= -1

    def collided(self, paddle):
        paddle_info = paddle.get_info()  # get the position and direction info for the paddle object

        return True if( self._status['pos_x'] < paddle_info['x_axis']['right'] and
            self._status['pos_x'] > paddle_info['x_axis']['left'] and
            self._status['pos_y'] > paddle_info['y_axis']['top'] and
            self._status['pos_y'] < paddle_info['y_axis']['bottom']) else False

    def bounce_paddle(self, paddle):
        if self.collided(paddle):
            self._status['direction_x'] *= -1

    def move(self):
        self._status['pos_x'] += self._status['direction_x'] * self._settings['SPEED']
        self._status['pos_y'] += self._status['direction_y'] * self._settings['SPEED']

    def _rotate(self, theta):
        theta = math.radians(theta)
        cos = math.cos(theta)
        sin = math.sin(theta)
        self._status['direction_x'] = self._status['direction_x']*cos - self._status['direction_y']*sin
        self._status['direction_y'] = self._status['direction_x']*cos + self._status['direction_y']*sin
