from config import LEFT_TRIANGLE_SPRITE
import pygame


class LeftTriangle(pygame.sprite.Sprite):
    pos_x = 50
    pos_y = 665

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(LEFT_TRIANGLE_SPRITE)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
