from config import BALL_SPRITE, INITIAL_BALL_X_POS, INITIAL_BALL_Y_POS
from random import randint
import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(BALL_SPRITE)
        self.rect = self.image.get_rect(center=(INITIAL_BALL_X_POS, INITIAL_BALL_Y_POS))
        self.x_velocity = 6
        self.y_velocity = 6

    def update(self):
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

    def bounce(self):
        self.x_velocity = -self.x_velocity
        self.y_velocity = randint(-8, 8)

    def collide_with_screen(self, screen_width, screen_height):
        if self.rect.right >= screen_width or self.rect.left <= 0:
            self.x_velocity *= -1
        if self.rect.top <= 0:
            self.y_velocity *= -1
        if self.rect.bottom >= screen_height:
            self.rect.x = INITIAL_BALL_X_POS
            self.rect.y = INITIAL_BALL_Y_POS
            self.y_velocity = 6

    def collide_with_brick(self, brick_collision_list):
        for brick in brick_collision_list:
            self.bounce()
            brick.kill()

    def collide_with_right_paddle(self, right_paddle):
        if pygame.sprite.collide_mask(self, right_paddle):
            self.rect.x -= self.x_velocity
            self.rect.y -= self.y_velocity
            self.bounce()

    def collide_with_left_paddle(self, left_paddle):
        if pygame.sprite.collide_mask(self, left_paddle):
            self.rect.x -= self.x_velocity
            self.rect.y -= self.y_velocity
            self.bounce()

    def collide_with_right_object(self, right_object):
        if pygame.sprite.collide_mask(self, right_object):
            self.rect.x -= self.x_velocity
            self.rect.y -= self.y_velocity
            self.bounce()

    def collide_with_left_object(self, left_object):
        if pygame.sprite.collide_mask(self, left_object):
            self.rect.x -= self.x_velocity
            self.rect.y -= self.y_velocity
            self.bounce()

    def collide_with_right_triangle(self, right_triangle):
        if pygame.sprite.collide_mask(self, right_triangle):
            self.rect.x -= self.x_velocity
            self.rect.y -= self.y_velocity
            self.bounce()

    def collide_with_left_triangle(self, left_triangle):
        if pygame.sprite.collide_mask(self, left_triangle):
            self.rect.x -= self.x_velocity
            self.rect.y -= self.y_velocity
            self.bounce()
