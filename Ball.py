import pygame

#Creating ball
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./sprites/ball.png')
        self.rect = self.image.get_rect(center=(300,400))

group_objects = pygame.sprite.Group()
group_objects.add(Ball())
