import settings
import pygame
import math
import utilities

class Ball():
    C_VERTICAL = 'VERTICAL'
    C_HORIZONTAL = 'HORIZONTAL'

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
        ,   'direction_x':  1.0
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

    def _last_pos(self):
        return [
            self._status['pos_x'] - self._status['direction_x'] * self._settings['SPEED']
        ,   self._status['pos_y'] - self._status['direction_y'] * self._settings['SPEED']
        ]

    def collision_side(self, paddle):
        paddle_info = paddle.get_info()  # get the position and direction info for the paddle object

        if( self._status['pos_x'] + self._settings['RADIUS'] < paddle_info['x_axis']['right']  and
            self._status['pos_x'] - self._settings['RADIUS'] > paddle_info['x_axis']['left']   and
            self._status['pos_y'] + self._settings['RADIUS'] > paddle_info['y_axis']['top']    and
            self._status['pos_y'] - self._settings['RADIUS'] < paddle_info['y_axis']['bottom']):
            # The ball has collided with the paddle. Determine on which side
            ball_line = utilities.line(self._last_pos(), [self._status['pos_x'], self._status['pos_y']])
            paddle_line_h1 = utilities.line([paddle_info['x_axis']['left'], paddle_info['y_axis']['top']], [paddle_info['x_axis']['right'], paddle_info['y_axis']['top']])
            paddle_line_h2 = utilities.line([paddle_info['x_axis']['left'], paddle_info['y_axis']['bottom']], [paddle_info['x_axis']['right'], paddle_info['y_axis']['bottom']])

            paddle_line_v1 = utilities.line([paddle_info['x_axis']['left'], paddle_info['y_axis']['top']], [paddle_info['x_axis']['left'], paddle_info['y_axis']['bottom']])
            paddle_line_v2 = utilities.line([paddle_info['x_axis']['right'], paddle_info['y_axis']['top']], [paddle_info['x_axis']['right'], paddle_info['y_axis']['bottom']])

            if utilities.intersection(ball_line, paddle_line_h1) or utilities.intersection(ball_line, paddle_line_h2):
                return self.C_HORIZONTAL
            elif utilities.intersection(ball_line, paddle_line_v1) or utilities.intersection(ball_line, paddle_line_v2):
                return self.C_VERTICAL
            else:
                print(self._status['pos_x'], self._status['pos_y'], paddle_info['x_axis']['left'], paddle_info['x_axis']['right'], paddle_info['y_axis']['top'], paddle_info['y_axis']['bottom'])
        else:
            return None

    def bounce_paddle(self, paddle):
        collision_side = self.collision_side(paddle)
        if collision_side == self.C_VERTICAL:
            self._status['direction_x'] *= -1
        elif collision_side == self.C_HORIZONTAL:
            self._status['direction_y'] *= -1

    def move(self):
        self._status['pos_x'] += self._status['direction_x'] * self._settings['SPEED']
        self._status['pos_y'] += self._status['direction_y'] * self._settings['SPEED']

    def _rotate(self, theta):
        theta = math.radians(theta)
        cos = math.cos(theta)
        sin = math.sin(theta)
        self._status['direction_x'] = self._status['direction_x']*cos - self._status['direction_y']*sin
        self._status['direction_y'] = self._status['direction_x']*cos + self._status['direction_y']*sin
