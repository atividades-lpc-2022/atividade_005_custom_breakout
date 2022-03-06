from ball import Ball
from right_paddle import RightPaddle
from left_paddle import LeftPaddle
from right_triangle import RightTriangle
from left_triangle import LeftTriangle
from right_object import RightObject
from left_object import LeftObject
from brick import Brick
from config import *
import pygame


def update_hud(lifes, score):
    font = pygame.font.Font(FONT, 60)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    lifes_text = font.render(f'Lifes: {lifes}', True, (255, 255, 255))
    return score_text, lifes_text


class Screen:
    surface: pygame.Surface
    all_sprites_group: pygame.sprite.Group
    bricks_group: pygame.sprite.Group
    ball: Ball
    right_paddle: RightPaddle
    left_paddle: LeftPaddle
    right_object: RightObject
    left_object: LeftObject
    right_triangle: RightTriangle
    left_triangle: LeftTriangle
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
        images_list = [RED_BRICK_SPRITE, BLUE_BRICK_SPRITE, GREEN_BRICK_SPRITE, YELLOW_BRICK_SPRITE]
        pos_x = 30
        pos_y = 150
        for i in range(4):
            for j in range(8):
                brick = Brick(pos_x, pos_y, images_list[i])
                self.bricks_group.add(brick)
                self.all_sprites_group.add(brick)
                pos_x += 77
            pos_x = 30
            pos_y += 50

    def update(self):
        self.surface.blit(self.wallpaper, (0, 0))
        self.ball.collide_with_screen(self.width, self.height)
        self.ball.collide_with_right_paddle(self.right_paddle)
        self.ball.collide_with_left_paddle(self.left_paddle)
        self.ball.collide_with_right_object(self.right_object)
        self.ball.collide_with_left_object(self.left_object)
        self.ball.collide_with_right_triangle(self.right_triangle)
        self.ball.collide_with_left_triangle(self.left_triangle)
        brick_collision_list = pygame.sprite.spritecollide(self.ball, self.bricks_group, False)
        self.ball.collide_with_brick(brick_collision_list)
        self.all_sprites_group.update()
        self.all_sprites_group.draw(self.surface)
        (score_text, lifes_text) = update_hud(self.lifes, self.score)
        self.surface.blit(score_text, (SCORE_TEXT_POS_X, SCORE_TEXT_POS_Y))
        self.surface.blit(lifes_text, (LIFES_TEXT_POS_X, LIFES_TEXT_POS_Y))
