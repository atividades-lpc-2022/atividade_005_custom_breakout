import os

# CONSTANTS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
INITIAL_BALL_X_POS = 300
INITIAL_BALL_Y_POS = 400
INITIAL_RIGHT_PADDLE_X_POS = 380
INITIAL_RIGHT_PADDLE_Y_POS = 699
INITIAL_LEFT_PADDLE_X_POS = 220
INITIAL_LEFT_PADDLE_Y_POS = 699
RIGHT_OBJECT_X_POS = 475
RIGHT_OBJECT_Y_POS = 620
LEFT_OBJECT_X_POS = 125
LEFT_OBJECT_Y_POS = 620
RIGHT_TRIANGLE_X_POS = 550
RIGHT_TRIANGLE_Y_POS = 500
LEFT_TRIANGLE_X_POS = 50
LEFT_TRIANGLE_Y_POS = 500
GAME_LIFES = 3
SCREEN_WALLPAPER = os.path.join(os.getcwd(), 'sprites', 'wallpaper.png')
BALL_SPRITE = os.path.join(os.getcwd(), 'sprites', 'ball.png')
RIGHT_PADDLE_SPRITE = os.path.join(os.getcwd(), 'sprites', 'rightpaddle.png')
RIGHT_PADDLE_UP_SPRITE = os.path.join(os.getcwd(), 'sprites', 'rightpaddleup.png')
LEFT_PADDLE_SPRITE = os.path.join(os.getcwd(), 'sprites', 'leftpaddle.png')
LEFT_PADDLE_UP_SPRITE = os.path.join(os.getcwd(), 'sprites', 'leftpaddleup.png')
RIGHT_TRIANGLE_SPRITE = os.path.join(os.getcwd(), 'sprites', 'righttriangle.png')
LEFT_TRIANGLE_SPRITE = os.path.join(os.getcwd(), 'sprites', 'lefttriangle.png')
RIGHT_OBJECT_SPRITE = os.path.join(os.getcwd(), 'sprites', 'rightobject.png')
LEFT_OBJECT_SPRITE = os.path.join(os.getcwd(), 'sprites', 'leftobject.png')
RED_BRICK_SPRITE = os.path.join(os.getcwd(), 'sprites', 'redbrick.png')
RED_BRICK_VALUE = 7
BLUE_BRICK_SPRITE = os.path.join(os.getcwd(), 'sprites', 'bluebrick.png')
BLUE_BRICK_VALUE = 5
GREEN_BRICK_SPRITE = os.path.join(os.getcwd(), 'sprites', 'greenbrick.png')
GREEN_BRICK_VALUE = 3
YELLOW_BRICK_SPRITE = os.path.join(os.getcwd(), 'sprites', 'yellowbrick.png')
YELLOW_BRICK_VALUE = 1
BRICKS_COLLISION_SOUND = os.path.join(os.getcwd(), 'sounds', 'brick.wav')
GAME_WIN_SOUND = os.path.join(os.getcwd(), 'sounds', 'game_win.mp3')
GAME_OVER_SOUND = os.path.join(os.getcwd(), 'sounds', 'game_over.wav')
PADDLES_COLLISION_SOUND = os.path.join(os.getcwd(), 'sounds', 'paddle.wav')
WALLS_AND_TRIANGLES_SOUND = os.path.join(os.getcwd(), 'sounds', 'wall_and_triangle.wav')
FONT = os.path.join(os.getcwd(), 'font', 'Gamer.ttf')
SCORE_TEXT_POS_X = 230
SCORE_TEXT_POS_Y = 20
LIFES_TEXT_POS_X = 230
LIFES_TEXT_POS_Y = 55
SCREEN_CAPTION = 'PINOUT'
FPS = 60
