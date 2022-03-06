from time import sleep
import pygame

from config import FONT, FPS

class StartScren:
  def __init__(self, width: int, height: int, background_path: str):
    self.width = width
    self.height = height
    self.background_path = background_path
    self.surface = pygame.display.set_mode(size=(width, height))

  def update(self, text: str):
    background_image = pygame.image.load(self.background_path)
    background_shape = background_image.get_rect()
    self.surface.blit(background_image, background_shape)

    font = pygame.font.Font(FONT, 60)
    start_text = font.render(text, True, (255, 255, 255))
    self.surface.blit(start_text, (self.width/2 - start_text.get_width()/2, self.height/2))

    pygame.display.update()
    sleep(1)