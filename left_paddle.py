from config import LEFT_PADDLE_SPRITE
import pygame


class LeftPaddle(pygame.sprite.Sprite):
    pos_x = 225
    pos_y = 699

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(LEFT_PADDLE_SPRITE)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
