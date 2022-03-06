from config import RED_BRICK_SPRITE, BLUE_BRICK_SPRITE, GREEN_BRICK_SPRITE, RED_BRICK_VALUE, BLUE_BRICK_VALUE, \
    GREEN_BRICK_VALUE, YELLOW_BRICK_VALUE
import pygame


class Brick(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        if image == RED_BRICK_SPRITE:
            self.value = RED_BRICK_VALUE
        elif image == BLUE_BRICK_SPRITE:
            self.value = BLUE_BRICK_VALUE
        elif image == GREEN_BRICK_SPRITE:
            self.value = GREEN_BRICK_VALUE
        else:
            self.value = YELLOW_BRICK_VALUE
