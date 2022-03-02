from config import RIGHT_OBJECT_SPRITE
import pygame


class RightObject(pygame.sprite.Sprite):
    pos_x = 475
    pos_y = 620

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(RIGHT_OBJECT_SPRITE)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
