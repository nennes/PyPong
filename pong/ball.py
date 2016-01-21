import settings
import pygame
import math

class Ball():

    _defaults = {
        'RADIUS':   7
    ,   'SPEED':    5
    ,   'COLOUR':   settings.COLOURS['BLUE']
    }

    _status = {
        'pos_x':        settings.WINDOW['WIDTH']//2
    ,   'pos_y':        settings.WINDOW['HEIGHT']//2
    ,   'direction_x':  1
    ,   'direction_y':  0.8
    }

    def __init__(self, screen, settings = _defaults):
        self._settings = settings
        self.screen = screen  # copy the reference to the screen in a local variable

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

    def bounce_paddle(self, paddle):

        paddle_info = paddle.get_info()  # get the position and direction info for the paddle object

        if self._status['pos_x'] <= paddle_info['x_axis']['right'] + self._settings['RADIUS']:
            if (self._status['pos_y'] >= paddle_info['y_axis']['top'] + self._settings['RADIUS']) and (self._status['pos_y'] <= paddle_info['y_axis']['bottom'] - self._settings['RADIUS']):
                # the ball should bounce
                self._status['direction_x'] *= -1
                # Depending on the direction of the paddle, the angle will be different
                if(paddle_info['direction'] == settings.DIRECTION['UP'] and self._status['direction_y'] < 0) \
                    or \
                    (paddle_info['direction'] == settings.DIRECTION['DOWN'] and self._status['direction_y'] > 0):
                    # Both going in the same direction, increase the angle
                    self._rotate(settings.DIRECTION['ANGLE_CHANGE_THETA'])
                elif paddle_info['direction'] != settings.DIRECTION['NONE']:
                    # The paddle is moving but the ball is moving in the opposite direction, decrease the angle
                    self._rotate((2*math.pi) - settings.DIRECTION['ANGLE_CHANGE_THETA'])

    def move(self):
        self._status['pos_x'] += self._status['direction_x'] * self._settings['SPEED']
        self._status['pos_y'] += self._status['direction_y'] * self._settings['SPEED']

    def _rotate(self, theta):
        theta = math.radians(theta)
        cos = math.cos(theta)
        sin = math.sin(theta)
        self._status['direction_x'] = self._status['direction_x']*cos - self._status['direction_y']*sin
        self._status['direction_y'] = self._status['direction_x']*cos + self._status['direction_y']*sin
