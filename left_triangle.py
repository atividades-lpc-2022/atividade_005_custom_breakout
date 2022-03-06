from config import LEFT_TRIANGLE_SPRITE, LEFT_TRIANGLE_X_POS, LEFT_TRIANGLE_Y_POS
import pygame


class LeftTriangle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(LEFT_TRIANGLE_SPRITE)
        self.rect = self.image.get_rect(center=(LEFT_TRIANGLE_X_POS, LEFT_TRIANGLE_Y_POS))
