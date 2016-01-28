import pygame
from pygame.locals import *
from sys import exit

import settings
from pong import game


def main():
    pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption(settings.WINDOW['TITLE'])
    paddle_direction = [settings.DIRECTION['NONE'], settings.DIRECTION['NONE']]  # horizontal and vertical directions

    pong = game.Game()

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
                paddle_direction = [jstick.get_hat(0)[0],-jstick.get_hat(0)[1]]
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    paddle_direction[1] = settings.DIRECTION['UP']
                elif event.key == K_DOWN:
                    paddle_direction[1] = settings.DIRECTION['DOWN']
                if event.key == K_LEFT:
                    paddle_direction[0] = settings.DIRECTION['LEFT']
                elif event.key == K_RIGHT:
                    paddle_direction[0] = settings.DIRECTION['RIGHT']
            elif event.type == KEYUP:
                if event.key == K_UP:
                    paddle_direction[1] = settings.DIRECTION['NONE']
                elif event.key == K_DOWN:
                    paddle_direction[1] = settings.DIRECTION['NONE']
                if event.key == K_LEFT:
                    paddle_direction[0] = settings.DIRECTION['NONE']
                elif event.key == K_RIGHT:
                    paddle_direction[0] = settings.DIRECTION['NONE']

        pong.update(paddle_direction)
        pygame.display.update()
        clock.tick(settings.WINDOW['FPS'])

if __name__ == '__main__':
    main()