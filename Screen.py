import pygame
from Ball import Ball
from Brick import group_Block1,group_Block2,group_Block3,group_Block4,group_Block5
from Brick import group_Block6,group_Block7,group_Block8,group_Block9,group_Block10
from Brick import group_Block11, group_Block12, group_Block13, group_Block14, group_Block15
from Brick import group_Block16,group_Block17,group_Block18,group_Block19,group_Block20

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
    
    group_Block1.draw(screen)
    group_Block2.draw(screen)
    group_Block3.draw(screen)
    group_Block4.draw(screen)
    group_Block5.draw(screen)
    group_Block6.draw(screen)
    group_Block7.draw(screen)
    group_Block8.draw(screen)
    group_Block9.draw(screen)
    group_Block10.draw(screen)
    group_Block11.draw(screen)
    group_Block12.draw(screen)
    group_Block13.draw(screen)
    group_Block14.draw(screen)
    group_Block15.draw(screen)
    group_Block16.draw(screen)
    group_Block17.draw(screen)
    group_Block18.draw(screen)
    group_Block19.draw(screen)
    group_Block20.draw(screen)

    group_objects.draw(screen)

    pygame.display.update()