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

score = 0
lifes = GAME_LIFES
start = False
game_over = False


def update_hud(screen_surface, screen_width, screen_height, game_over_sound, win_game_sound):
    global score, lifes
    font = pygame.font.Font(FONT, 60)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    lifes_text = font.render(f'Lifes: {lifes}', True, (255, 255, 255))
    msg_to_player_text = font.render('', True, (255, 255, 255))
    if lifes == 0:
        font = pygame.font.Font(FONT, 100)
        msg_to_player_text = font.render('YOU LOSE!', True, (255, 255, 255))
        screen_surface.blit(msg_to_player_text, (155, 30))
        pygame.display.update()
        game_over_sound.play()
        pygame.time.wait(2000)
        return True
    if score == 128:
        font = pygame.font.Font(FONT, 100)
        msg_to_player_text = font.render('YOU WON!', True, (255, 255, 255))
        screen_surface.blit(msg_to_player_text, (155, 30))
        pygame.display.update()
        win_game_sound.play()
        pygame.time.wait(2000)
        return True
    screen_surface.blit(score_text, (SCORE_TEXT_POS_X, SCORE_TEXT_POS_Y))
    screen_surface.blit(lifes_text, (LIFES_TEXT_POS_X, LIFES_TEXT_POS_Y))
    screen_surface.blit(msg_to_player_text, (screen_width / 2, screen_height / 2))
    pygame.display.update()
    return False


class Screen:
    def __init__(self, width, height, wallpaper, caption, brick_collision_sound, paddles_collision_sound,
                 walls_and_triangles_collision_sound, game_over_sound, win_game_sound):
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
        self.brick_collision_sound = brick_collision_sound
        self.paddles_collision_sound = paddles_collision_sound
        self.walls_and_triangles_collision_sound = walls_and_triangles_collision_sound
        self.game_over_sound = game_over_sound
        self.win_game_sound = win_game_sound
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
        global score, lifes, game_over

        self.surface.blit(self.wallpaper, (0, 0))
        lifes = self.ball.collide_with_screen(self.width, self.height, self.walls_and_triangles_collision_sound, lifes)
        self.ball.collide_with_right_paddle(self.right_paddle, self.paddles_collision_sound)
        self.ball.collide_with_left_paddle(self.left_paddle, self.paddles_collision_sound)
        self.ball.collide_with_right_object(self.right_object, self.walls_and_triangles_collision_sound)
        self.ball.collide_with_left_object(self.left_object, self.walls_and_triangles_collision_sound)
        self.ball.collide_with_right_triangle(self.right_triangle, self.walls_and_triangles_collision_sound)
        self.ball.collide_with_left_triangle(self.left_triangle, self.walls_and_triangles_collision_sound)
        brick_collision_list = pygame.sprite.spritecollide(self.ball, self.bricks_group, False)
        score = self.ball.collide_with_brick(brick_collision_list, score, self.brick_collision_sound)
        self.all_sprites_group.update()
        self.all_sprites_group.draw(self.surface)
        game_over = update_hud(self.surface, self.width, self.height, self.game_over_sound, self.win_game_sound)
        pygame.display.update()
        return game_over
