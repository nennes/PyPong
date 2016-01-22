import pygame
from pygame.locals import *
from sys import exit

import settings
from pong import game


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption(settings.WINDOW['TITLE'])
    paddle_direction = settings.DIRECTION['NONE']

    pong = game.Game(screen=pygame.display.set_mode((settings.WINDOW['WIDTH'], settings.WINDOW['HEIGHT']), 0, 32))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    paddle_direction = settings.DIRECTION['UP']
                elif event.key == K_DOWN:
                    paddle_direction = settings.DIRECTION['DOWN']
            elif event.type == KEYUP:
                if event.key == K_UP:
                    paddle_direction = settings.DIRECTION['NONE']
                elif event.key == K_DOWN:
                    paddle_direction = settings.DIRECTION['NONE']

        pong.ball.move()
        pong.paddles[0].move(paddle_direction)
        pong.paddles[1].move_auto(pong.ball)
        pong.update()
        pygame.display.update()
        clock.tick(settings.WINDOW['FPS'])

if __name__ == '__main__':
    main()