import os

import pygame
from copy import copy
from pong import board, info, ball, horizontalpaddle, verticalpaddle
import settings


class Game:

    _sounds = {
         'BOUNCE':   os.path.join("sounds", "bounce.wav")
    }

    def increase_score(self):
        self._score += 1
        if self._score > self._high_score:
            self._high_score = self._score

    def reset_score(self):
        self._score = 0

    def __init__(self, speed=5):
        self._score = 0
        self._high_score = 0

        self.speed = speed
        self.screen = pygame.display.set_mode((settings.WINDOW['WIDTH'], settings.WINDOW['HEIGHT'] + settings.WINDOW['INFO_HEIGHT']), 0, 32)

        self.board = board.Board(self.screen)
        self.info = info.Info(self.screen)
        self.ball = ball.Ball(self.screen)

        user_horizontal_settings = copy(horizontalpaddle.HorizontalPaddle.defaults)  # a shallow copy is sufficient
        user_horizontal_settings['POSITION'] = 'BOTTOM'

        cpu_horizontal_settings = copy(horizontalpaddle.HorizontalPaddle.defaults)  # a shallow copy is sufficient
        cpu_horizontal_settings['POSITION'] = 'TOP'
        cpu_horizontal_settings['COLOUR'] = settings.COLOURS['RED']

        cpu_vertical_settings = copy(verticalpaddle.VerticalPaddle.defaults)  # a shallow copy is sufficient
        cpu_vertical_settings['POSITION'] = 'RIGHT'
        cpu_vertical_settings['COLOUR'] = settings.COLOURS['RED']

        self.paddles = [
            verticalpaddle.VerticalPaddle(self.screen, 'user_vertical')
        ,   horizontalpaddle.HorizontalPaddle(self.screen, 'user_horizontal', override=user_horizontal_settings)
        ,   verticalpaddle.VerticalPaddle(self.screen, 'cpu_vertical', override=cpu_vertical_settings)
        ,   horizontalpaddle.HorizontalPaddle(self.screen, 'cpu_horizontal', override=cpu_horizontal_settings)
        ]

    def update(self, direction):

        # Move the objects
        self.ball.move()
        self.paddles[0].move(direction)
        self.paddles[1].move(direction)
        self.paddles[2].move_auto(self.ball) # move(direction)
        self.paddles[3].move_auto(self.ball) # move_auto(self.ball)

        # Handle collisions
        if self.ball.bounce_wall():
            self.board.settings['line_colour'] = settings.COLOURS['RED']
            self.reset_score()
            self.ball.reset_status()
        else:
            self.board.settings['line_colour'] = settings.COLOURS['WHITE']

        for p in self.paddles:
            if p.bounce(self.ball):
                self.increase_score()
                pygame.mixer.music.load(self._sounds['BOUNCE'])
                pygame.mixer.music.play()

        # draw objects
        self.board.draw(self.screen)
        self.info.draw(self.screen, self._score, self._high_score)
        self.ball.draw(self.screen)
        for p in self.paddles:
            p.draw(self.screen)
