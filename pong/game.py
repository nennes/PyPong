from pong import board, ball, paddle


class Game:

    def __init__(self, screen, speed=5):
        self.speed = speed
        self.screen = screen  # copy the reference to the screen in a local variable
        self.score = 0

        self.board = board.Board(screen)
        self.ball = ball.Ball(screen)
        self.paddles = {
            'user': paddle.Paddle(screen)
        }

    def update(self):

        # Handle collisions
        self.ball.bounce_wall()
        self.ball.bounce_paddle(self.paddles['user'])

        # draw objects
        self.board.draw(self.screen)
        self.ball.draw(self.screen)
        self.paddles['user'].draw(self.screen)
