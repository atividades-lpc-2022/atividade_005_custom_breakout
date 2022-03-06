from config import RIGHT_PADDLE_SPRITE, INITIAL_RIGHT_PADDLE_X_POS, INITIAL_RIGHT_PADDLE_Y_POS
import pygame


class RightPaddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(RIGHT_PADDLE_SPRITE)
        self.rect = self.image.get_rect(center=(INITIAL_RIGHT_PADDLE_X_POS, INITIAL_RIGHT_PADDLE_Y_POS))
