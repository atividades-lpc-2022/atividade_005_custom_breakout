from config import *
from screen import Screen
import pygame
import sys


def run():
    clock = pygame.time.Clock()
    screen = Screen(
        SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WALLPAPER, SCREEN_CAPTION, GAME_LIFES
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.update()
        pygame.display.flip()  # updates the contents of the entire display
        clock.tick(FPS)
