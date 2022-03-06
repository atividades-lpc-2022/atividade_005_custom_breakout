from config import LEFT_OBJECT_SPRITE, LEFT_OBJECT_X_POS, LEFT_OBJECT_Y_POS
import pygame


class LeftObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(LEFT_OBJECT_SPRITE)
        self.rect = self.image.get_rect(center=(LEFT_OBJECT_X_POS, LEFT_OBJECT_Y_POS))
