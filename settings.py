import math


# CONSTANTS
WINDOW = {
    'WIDTH':  600
,   'HEIGHT': 600
,   'INFO_HEIGHT': 150
,   'FPS': 60
,   'TITLE':  "PyPong"
,   'LINE_THICKNESS': 3
,   'PADDLE_OFFSET': 6
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
WINDOW_INNER_BORDERS = {
    'X_AXIS': {
        'LEFT': WINDOW['PADDLE_OFFSET']//2 + WINDOW['LINE_THICKNESS']
    ,   'RIGHT': WINDOW['WIDTH'] - WINDOW['PADDLE_OFFSET']//2 - WINDOW['LINE_THICKNESS']
    }
,   'Y_AXIS': {
        'TOP': WINDOW['PADDLE_OFFSET']//2 + WINDOW['LINE_THICKNESS']
    ,   'BOTTOM': WINDOW['HEIGHT'] - WINDOW['PADDLE_OFFSET']//2 - WINDOW['LINE_THICKNESS']
    }
}
DIRECTION={
    'UP':       -1
,   'DOWN':     1
,   'LEFT':     -1
,   'RIGHT':    1
,   'NONE':     0
}
C_VERTICAL      = 'VERTICAL'
C_HORIZONTAL    = 'HORIZONTAL'