from config import BRICK_SPRITE
import pygame


class Brick(pygame.sprite.Sprite):
    pos_x: int
    pos_y: int

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(BRICK_SPRITE)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
