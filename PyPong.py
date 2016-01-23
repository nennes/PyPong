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

    try:
        jstick = pygame.joystick. Joystick(1) # create a joystick instance
        jstick.init() # init instance
    except pygame.error:
        print('No Joystick Present')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == pygame.JOYHATMOTION:
                # jstick.get_hat(0) provides a list of the hat buttons state
                # jstick.get_hat(0)[1] is the vertical axis:
                #  1 us UP, -1 is DOWN
                #  This is the opposite of the direction format we use
                paddle_direction = -jstick.get_hat(0)[1]

        pong.ball.move()
        pong.paddles[0].move(paddle_direction)
        pong.paddles[1].move_auto(pong.ball)
        pong.update()
        pygame.display.update()
        clock.tick(settings.WINDOW['FPS'])

if __name__ == '__main__':
    main()