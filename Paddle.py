import pygame

pygame.init()

size = (600, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pinout")
clock = pygame.time.Clock()


# creating the right paddle
class RightPaddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.right_paddle_1 = pygame.image.load("rightpaddle.png").convert()
        self.right_paddle_2 = pygame.image.load("rightpaddleup.png").convert_alpha()
        self.right_move = [self.right_paddle_1, self.right_paddle_2]
        self.right_index = 0
        self.image = self.right_move[self.right_index]
        self.rect = self.image.get_rect(midright=(450, 700))

    def right_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.right_index = 1
            if self.right_index >= len(self.right_move): self.right_index = 0
            self.image = self.right_move[int(self.right_index)]

    def update(self):
        self.right_input()


# creating the left paddle
class LeftPaddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        left_frame_1 = pygame.image.load("leftpaddle.png").convert()
        left_frame_2 = pygame.image.load("leftpaddleup.png").convert_alpha()
        self.left_move = [left_frame_1, left_frame_2]
        self.left_index = 0
        self.image = self.left_move[self.left_index]
        self.rect = self.image.get_rect(midleft=(150, 700))


right_paddle = pygame.sprite.Group()
right_paddle.add(RightPaddle())
left_paddle = pygame.sprite.Group()
left_paddle.add(LeftPaddle())
all_sprites_list = pygame.sprite.Group(right_paddle, left_paddle)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    all_sprites_list.update()
    right_paddle.update()
    right_paddle.draw(screen)
    left_paddle.draw(screen)
    right_paddle.update()
    clock.tick(60)
    pygame.display.update()
