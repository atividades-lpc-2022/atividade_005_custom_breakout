import pygame

pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()


class Ball:
    def __init__(self, cord_x, cord_y, width, height):
        self.rect = pygame.rect.Rect(cord_x, cord_y, width, height)


circle = Ball(20, 20, 50, 50)
vector = pygame.math.Vector2(1, 1)
velocity = 3
ball_X, ball_Y = 310, 310
ball_Rad = 8


run = True
while run:

    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    min_x, max_x = 20, screen.get_width() - 20
    min_y, max_y = 20, screen.get_height() - 20

    ball_X += vector[0] * velocity
    ball_Y += vector[1] * velocity

    ball = pygame.Rect((0, 0), (ball_Rad * 2, ball_Rad * 2))

    # Ball collision with walls
    if ball_X - ball_Rad < min_x:
        ball_X = ball_Rad + min_x
        vector[0] = -vector[0]

    if ball_Y - ball_Rad < min_y:
        ball_Y = ball_Rad + min_y
        vector[1] = -vector[1]

    if ball_X + ball_Rad > max_x:
        ball_X = max_x - ball_Rad
        vector[0] = -vector[0]

    if ball_Y + ball_Rad > max_y:
        ball_Y = max_y - ball_Rad
        vector[1] = -vector[1]
        # ball under the paddle = 3 attempts (GAME OVER)
        """score += 1
        if score == 4:
            pygame.display.update()
            pygame.time.wait(2000)
            run = False"""

    # Ball collision with paddle
    """if pygame.sprite.collide_mask(ball, paddle):
             ball.rect.x += ball.velocity[0]
             ball.rect.y -= ball.velocity[1]
             ball.bounce()"""

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (round(ball_X), round(ball_Y)), ball_Rad)
    pygame.display.update()

pygame.quit()
exit()
