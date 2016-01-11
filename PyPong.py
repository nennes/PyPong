import pygame
import random
from pygame.locals import *
from sys import exit
   
def draw_bar(screen, colour, pos_x, pos_y, len_x, len_y):
    bar = pygame.Surface((len_x,len_x + len_y), pygame.SRCALPHA, 32)
    pygame.draw.circle(bar, colour, (len_x//2, len_x//2), len_x//2, 0)
    pygame.draw.rect(bar, colour, Rect((0,len_x//2),(len_x,len_y-len_x)), 0)
    pygame.draw.circle(bar, colour, (len_x//2, len_y - len_x//2), len_x//2, 0)
    screen.blit(bar,(pos_x,pos_y))

def draw_ball(screen, colour, pos_x, pos_y, radius):
    ball = pygame.Surface((2*radius,2*radius), pygame.SRCALPHA, 32)
    pygame.draw.circle(ball, colour, (radius, radius), radius, 0)
    screen.blit(ball,(pos_x - radius,pos_y - radius))
    
def draw_text(screen, colour, pos_x, pos_y, text):
    rendered_text = font.render(str(text), True, colour)
    screen.blit(rendered_text,(pos_x,pos_y))
    
def draw_background(screen):
    background = pygame.Surface((WINDOW['WIDTH'],WINDOW['HEIGHT'])).convert()
    background.fill(COLOURS['BLACK'])
    pygame.draw.rect(background,COLOURS['WHITE'],Rect((BAR['OFFSET']//2,BAR['OFFSET']//2),(WINDOW['WIDTH'] - BAR['OFFSET'],WINDOW['HEIGHT'] - BAR['OFFSET'])),LINE_THICKNESS)
    pygame.draw.aaline(background,COLOURS['WHITE'],((WINDOW['WIDTH'] - BAR['OFFSET']//2)/2,BAR['OFFSET']//2),((WINDOW['WIDTH'] - BAR['OFFSET']//2)/2,(WINDOW['HEIGHT'] - BAR['OFFSET']//2)))
    screen.blit(background,(0,0))

# CONSTANTS
WINDOW = {
    'WIDTH':  600
,   'HEIGHT': 600
,   'TITLE':  "PyPong"
}
FONT = {
    'NAME': "calibri"
,   'SIZE': 40
}
COLOURS = {
    'BLACK': [0  , 0  , 0  ]
,   'WHITE': [255, 255, 255]
,   'RED':   [255, 0  , 0  ]
,   'GREEN': [  0, 255, 0  ]
,   'BLUE':  [  0, 0  , 255]
}
BAR = {
    'OFFSET':   10
,   'LENGTH':   60
,   'WIDTH':    10
,   'SPEED':    10
}
BALL = {
    'RADIUS':   5
,   'SPEED':    7
}
LINE_THICKNESS = 2

WINDOW_INNER_BORDERS = {
    'X_AXIS': {'LEFT': BAR['OFFSET']//2 + LINE_THICKNESS, 'RIGHT': WINDOW['WIDTH'] - BAR['OFFSET']//2 - LINE_THICKNESS}
,   'Y_AXIS': {'TOP': BAR['OFFSET']//2 + LINE_THICKNESS, 'BOTTOM': WINDOW['HEIGHT'] - BAR['OFFSET']//2 - LINE_THICKNESS}
}

# Game Variables
player_1_bar_x   = BAR['OFFSET']
player_1_bar_y   = WINDOW['WIDTH']//2 - (BAR['LENGTH'] + BAR['WIDTH'])//2
player_1_speed   = 0
player_1_score   = 0
player_2_bar_x   = WINDOW['WIDTH'] - BAR['WIDTH'] - BAR['OFFSET']
player_2_bar_y   = WINDOW['HEIGHT']//2 - (BAR['LENGTH'] + BAR['WIDTH'])//2
player_2_speed   = 0
player_2_score   = 0
ball_x           = WINDOW['WIDTH']//2
ball_y           = WINDOW['HEIGHT']//2
ball_direction_x = -BALL['SPEED']
ball_direction_y = BALL['SPEED']/2

# Initialisation
pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont(FONT['NAME'],FONT['SIZE'])
screen=pygame.display.set_mode((WINDOW['WIDTH'],WINDOW['HEIGHT']),0,32)
pygame.display.set_caption(WINDOW['TITLE'])

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                player_1_speed = -BAR['SPEED']
            elif event.key == K_DOWN:
                player_1_speed = BAR['SPEED']
        elif event.type == KEYUP:
            if event.key == K_UP:
                player_1_speed = 0
            elif event.key == K_DOWN:
                player_1_speed = 0
                
    player_1_bar_y = player_1_bar_y + player_1_speed
    
    if player_1_bar_y <= WINDOW_INNER_BORDERS['Y_AXIS']['TOP']:
        player_1_bar_y = WINDOW_INNER_BORDERS['Y_AXIS']['TOP']
    elif player_1_bar_y >= WINDOW_INNER_BORDERS['Y_AXIS']['BOTTOM'] - BAR['LENGTH']:
         player_1_bar_y = WINDOW_INNER_BORDERS['Y_AXIS']['BOTTOM'] - BAR['LENGTH']
    
    draw_background(screen)

    draw_bar(screen, COLOURS['BLUE'], player_1_bar_x,player_1_bar_y, BAR['WIDTH'], BAR['LENGTH'])
    draw_bar(screen, COLOURS['RED'], player_2_bar_x,player_2_bar_y, BAR['WIDTH'], BAR['LENGTH'])
    draw_ball(screen, COLOURS['GREEN'], ball_x, ball_y, BALL['RADIUS'])
    draw_text(
        screen
    ,   COLOURS['WHITE']
    ,   (WINDOW_INNER_BORDERS['X_AXIS']['RIGHT'] - WINDOW_INNER_BORDERS['X_AXIS']['LEFT'])//2 - WINDOW['WIDTH']//5
    ,   (WINDOW_INNER_BORDERS['Y_AXIS']['BOTTOM'] - WINDOW_INNER_BORDERS['Y_AXIS']['TOP'])//2 - WINDOW['HEIGHT']//20
    ,   player_1_score
    )
    draw_text(
        screen
    ,   COLOURS['WHITE']
    ,   (WINDOW_INNER_BORDERS['X_AXIS']['RIGHT'] - WINDOW_INNER_BORDERS['X_AXIS']['LEFT'])//2 + WINDOW['WIDTH']//5
    ,   (WINDOW_INNER_BORDERS['Y_AXIS']['BOTTOM'] - WINDOW_INNER_BORDERS['Y_AXIS']['TOP'])//2 - WINDOW['HEIGHT']//20
    ,   player_2_score
    )
    
    # movement of circle
    time_passed = clock.tick(60)
    time_sec = time_passed / 1000
    
    ball_x += ball_direction_x
    ball_y += ball_direction_y
    
    # wall bounce
    if(ball_x <= WINDOW_INNER_BORDERS['X_AXIS']['LEFT'] + BALL['RADIUS']) or (ball_x >= WINDOW_INNER_BORDERS['X_AXIS']['RIGHT'] - BALL['RADIUS']):
        ball_direction_x = -ball_direction_x
    if (ball_y <= WINDOW_INNER_BORDERS['Y_AXIS']['TOP'] + BALL['RADIUS']) or (ball_y >= WINDOW_INNER_BORDERS['Y_AXIS']['BOTTOM'] - BALL['RADIUS']):
        ball_direction_y = -ball_direction_y
    
    pygame.display.update()