from ball import Ball
from right_paddle import RightPaddle
from left_paddle import LeftPaddle
from right_triangle import RightTriangle
from left_triangle import LeftTriangle
from right_object import RightObject
from left_object import LeftObject
from brick import Brick
from config import (
    FONT,
    SCORE_TEXT_POS_X,
    SCORE_TEXT_POS_Y,
    LIFES_TEXT_POS_X,
    LIFES_TEXT_POS_Y,
)
import pygame


def update_hud(lifes, score):
    font = pygame.font.Font(FONT, 60)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    lifes_text = font.render(f"Lifes: {lifes}", True, (255, 255, 255))
    return score_text, lifes_text


class Screen:
    surface: pygame.Surface
    all_sprites_group: pygame.sprite.Group
    bricks_group: pygame.sprite.Group
    ball: Ball
    right_paddle: RightPaddle
    left_paddle: LeftPaddle
    left_triangle: LeftTriangle
    right_triangle: RightTriangle
    left_object: LeftObject
    right_object: RightObject
    lifes = int
    score = 0

    def __init__(self, width, height, wallpaper, caption, lifes):
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode((width, height))
        self.wallpaper = pygame.image.load(wallpaper)
        self.all_sprites_group = pygame.sprite.Group()
        self.right_paddle = RightPaddle()
        self.all_sprites_group.add(self.right_paddle)
        self.left_paddle = LeftPaddle()
        self.all_sprites_group.add(self.left_paddle)
        self.right_triangle = RightTriangle()
        self.all_sprites_group.add(self.right_triangle)
        self.left_triangle = LeftTriangle()
        self.all_sprites_group.add(self.left_triangle)
        self.right_object = RightObject()
        self.all_sprites_group.add(self.right_object)
        self.left_object = LeftObject()
        self.all_sprites_group.add(self.left_object)
        self.bricks_group = pygame.sprite.Group()
        self.add_bricks()
        self.ball = Ball()
        self.all_sprites_group.add(self.ball)
        self.lifes = lifes
        pygame.display.set_caption(caption)

    def add_bricks(self):
        pos_x = 160
        pos_y = 200
        for i in range(4):
            for j in range(5):
                self.bricks_group.add(Brick(pos_x, pos_y))
                self.all_sprites_group.add(Brick(pos_x, pos_y))
                pos_x += 70
            pos_x = 160
            pos_y += 50

    def update(self):
        self.surface.blit(self.wallpaper, (0, 0))
        self.all_sprites_group.draw(self.surface)

        self.ball.update()

        # Add ball's collisions
        for brick in self.bricks_group:
            is_colliding = pygame.sprite.collide_rect(brick, self.ball)
            if is_colliding:
                self.ball.y_velocity *= -1
                brick.kill()

        self.ball.is_colliding_with_screen(self.width, self.height)

        (score_text, lifes_text) = update_hud(self.lifes, self.score)
        self.surface.blit(score_text, (SCORE_TEXT_POS_X, SCORE_TEXT_POS_Y))
        self.surface.blit(lifes_text, (LIFES_TEXT_POS_X, LIFES_TEXT_POS_Y))
