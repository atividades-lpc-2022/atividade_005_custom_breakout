import pygame
from Ball import Ball
#from Brick import Block
#from Brick import Block2
#from Brick import Block3
#from Brick import Block4
#from Brick import Block5
#from Brick import Block6
#from Brick import Block7
#from Brick import Block8
#from Brick import Block9
#from Brick import Block10
#from Brick import Block11
#from Brick import Block12
#from Brick import Block13
#from Brick import Block14
#from Brick import Block15
#from Brick import Block16
#from Brick import Block17
#from Brick import Block18
#from Brick import Block19
#from Brick import Block20

pygame.init()

width, height = 600, 800
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("PINOUT")

#Changing Wallpaper
img = pygame.image.load('sprites/wallpapper.png')

group_Block = pygame.sprite.Group()
group_objects = pygame.sprite.Group()
group_objects.add(Ball())

#Creating objects
class Right_paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./sprites/rightpaddle.png')
        self.rect = self.image.get_rect(center=(375,699))
group_objects.add(Right_paddle())

class Left_paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./sprites/leftpaddle.png')
        self.rect = self.image.get_rect(center=(225,699))
group_objects.add(Left_paddle())

class Right_triangle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./sprites/righttriangle.png')
        self.rect = self.image.get_rect(center=(520,730))
group_objects.add(Right_triangle())

class Left_triangle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./sprites/lefttriangle.png')
        self.rect = self.image.get_rect(center=(80,730))
group_objects.add(Left_triangle())

class Right_objetc(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./sprites/rightobject.png')
        self.rect = self.image.get_rect(center=(475,620))
group_objects.add(Right_objetc())

class Left_object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./sprites/leftobject.png')
        self.rect = self.image.get_rect(center=(125,620))
group_objects.add(Left_object())

vidas = 3
pontos = 0
main = True
while main:
    score = f'Score: {pontos}'
    font = pygame.font.Font('font/Gamer.ttf', 60)
    text_format = font.render(score, True, (255,255,255))

    life = f'Lifes: {vidas}'
    font2 = pygame.font.Font('font/Gamer.ttf',60)
    text_format2 = font.render(life, True, (255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
            pygame.quit()

    screen.blit(img,(0,0))
    screen.blit(text_format,(230,20))
    screen.blit(text_format2,(230, 55))
    
    group_Block.draw(screen)
    group_objects.draw(screen)

    pygame.display.update()