from config import RIGHT_OBJECT_SPRITE, RIGHT_OBJECT_X_POS, RIGHT_OBJECT_Y_POS
import pygame


class RightObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(RIGHT_OBJECT_SPRITE)
        self.rect = self.image.get_rect(center=(RIGHT_OBJECT_X_POS, RIGHT_OBJECT_Y_POS))
