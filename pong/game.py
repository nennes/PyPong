from copy import copy
from pong import board, ball, paddle
import settings


class Game:

    def __init__(self, screen, speed=5):
        self.speed = speed
        self.screen = screen  # copy the reference to the screen in a local variable
        self.score = 0

        self.board = board.Board(screen)
        self.ball = ball.Ball(screen)

        cpu_paddle_settings = copy(paddle.Paddle.defaults)  # a shallow copy is sufficient
        cpu_paddle_settings['OFFSET'] = settings.WINDOW['WIDTH'] - 3*(settings.WINDOW['PADDLE_OFFSET'] + settings.WINDOW['LINE_THICKNESS']) - 200
        cpu_paddle_settings['ORIENTATION'] = 'HORIZONTAL'
        self.paddles = [
            paddle.Paddle(screen, 'user')
        ,   paddle.Paddle(screen, 'cpu', override=cpu_paddle_settings)
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
