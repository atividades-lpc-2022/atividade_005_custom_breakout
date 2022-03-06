from config import LEFT_PADDLE_SPRITE, LEFT_PADDLE_UP_SPRITE, INITIAL_LEFT_PADDLE_X_POS,\
    INITIAL_LEFT_PADDLE_Y_POS
import pygame


class LeftPaddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(LEFT_PADDLE_SPRITE)
        self.rect = self.image.get_rect(center=(INITIAL_LEFT_PADDLE_X_POS, INITIAL_LEFT_PADDLE_Y_POS))

    def paddle_up(self):
        self.image = pygame.image.load(LEFT_PADDLE_UP_SPRITE)

    def paddle_down(self):
        self.image = pygame.image.load(LEFT_PADDLE_SPRITE)
