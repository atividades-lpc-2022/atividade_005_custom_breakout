from config import RIGHT_TRIANGLE_SPRITE, RIGHT_TRIANGLE_X_POS, RIGHT_TRIANGLE_Y_POS
import pygame


class RightTriangle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(RIGHT_TRIANGLE_SPRITE)
        self.rect = self.image.get_rect(center=(RIGHT_TRIANGLE_X_POS, RIGHT_TRIANGLE_Y_POS))
