from copy import copy
from pong import board, ball, horizontalpaddle, verticalpaddle
import settings


class Game:

    def __init__(self, screen, speed=5):
        self.speed = speed
        self.screen = screen  # copy the reference to the screen in a local variable
        self.score = 0

        self.board = board.Board(screen)
        self.ball = ball.Ball(screen)

        user_horizontal_settings = copy(horizontalpaddle.HorizontalPaddle.defaults)  # a shallow copy is sufficient
        user_horizontal_settings['POSITION'] = 'BOTTOM'

        cpu_horizontal_settings = copy(horizontalpaddle.HorizontalPaddle.defaults)  # a shallow copy is sufficient
        cpu_horizontal_settings['POSITION'] = 'TOP'
        cpu_horizontal_settings['COLOUR'] = settings.COLOURS['RED']

        cpu_vertical_settings = copy(verticalpaddle.VerticalPaddle.defaults)  # a shallow copy is sufficient
        cpu_vertical_settings['POSITION'] = 'RIGHT'
        cpu_vertical_settings['COLOUR'] = settings.COLOURS['RED']

        self.paddles = [
            verticalpaddle.VerticalPaddle(screen, 'user_vertical')
        ,   horizontalpaddle.HorizontalPaddle(screen, 'user_horizontal', override=user_horizontal_settings)
        ,   verticalpaddle.VerticalPaddle(screen, 'cpu_vertical', override=cpu_vertical_settings)
        ,   horizontalpaddle.HorizontalPaddle(screen, 'cpu_horizontal', override=cpu_horizontal_settings)
        ]

    def update(self):

        # Handle collisions
        self.ball.bounce_wall()
        for p in self.paddles:
            self.ball.bounce_paddle(p)

        # draw objects
        self.board.draw(self.screen)
        self.ball.draw(self.screen)
        for p in self.paddles:
            p.draw(self.screen)
