from config import RIGHT_PADDLE_SPRITE
import pygame


class RightPaddle(pygame.sprite.Sprite):
    pos_x = 375
    pos_y = 699

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(RIGHT_PADDLE_SPRITE)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
