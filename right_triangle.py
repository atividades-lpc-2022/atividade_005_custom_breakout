from config import RIGHT_TRIANGLE_SPRITE
import pygame


class RightTriangle(pygame.sprite.Sprite):
    pos_x = 520
    pos_y = 730

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(RIGHT_TRIANGLE_SPRITE)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
