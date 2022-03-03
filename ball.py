from config import BALL_SPRITE
import pygame


class Ball(pygame.sprite.Sprite):
    pos_x = float
    pos_y = float
    x_velocity: float
    y_velocity: float
    x_initial_velocity: float
    y_initial_velocity: float

    def __init__(self):
        super().__init__()
        self.pos_x = 300
        self.pos_y = 400
        self.x_velocity = 3
        self.x_initial_velocity = 3
        self.y_initial_velocity = 3
        self.y_velocity = -3
        self.image = pygame.image.load(BALL_SPRITE)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

    def is_colliding_with_screen(self, width: float, height: float):
        if self.pos_x <= 0 or self.pos_x >= width:
            self.x_velocity *= -1
        if self.pos_y <= 0 or self.pos_y >= height:
            self.y_velocity *= -1

    def is_colliding(self, sprite: pygame.sprite.Sprite):
        x = sprite.rect.x
        y = sprite.rect.y
        width = sprite.rect.width
        height = sprite.rect.height
        x_size = x + width
        y_size = y + height

        if x <= self.pos_x <= x_size:
            self.x_velocity *= -1
        if y <= self.pos_y <= y_size:
            self.y_velocity *= -1

    # def increase_velocity(self, paddle: Paddle):
    #     velocityIncrease = (self.pos_x - paddle.x)/paddle.width
    #     self.x_velocity = self.x_initial_velocity * (1 + velocityIncrease)
    #     self.y_velocity = self.y_initial_velocity * (1 + velocityIncrease)

    def update(self):
        # if self.x_velocity > self.x_initial_velocity:
        #     self.x_velocity -= 0.25
        # elif self.x_velocity <= self.x_initial_velocity:
        #     self.x_velocity = self.x_initial_velocity

        # if self.y_velocity > self.y_initial_velocity:
        #     self.y_velocity -= 0.25
        # elif self.y_velocity <= self.y_initial_velocity:
        #     self.y_velocity = self.y_initial_velocity

        self.pos_x += 1 * self.x_velocity
        self.pos_y += 1 * self.y_velocity
        self.image = pygame.image.load(BALL_SPRITE)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
