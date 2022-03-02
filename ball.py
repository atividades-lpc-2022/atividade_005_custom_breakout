from config import BALL_SPRITE
import pygame


class Ball(pygame.sprite.Sprite):
    pos_x = 300
    pos_y = 400

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(BALL_SPRITE)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

