from config import RIGHT_TRIANGLE_SPRITE
import pygame


class RightTriangle(pygame.sprite.Sprite):
    pos_x = 550
    pos_y = 665

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(RIGHT_TRIANGLE_SPRITE)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
