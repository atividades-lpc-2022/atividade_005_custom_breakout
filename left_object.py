from config import LEFT_OBJECT_SPRITE
import pygame


class LeftObject(pygame.sprite.Sprite):
    pos_x = 125
    pos_y = 620

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(LEFT_OBJECT_SPRITE)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
