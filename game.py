from config import *
from screen import Screen
import pygame
import sys

stop = False


def run(brick_collision_sound, paddles_collision_sound, walls_and_triangles_collision_sound, game_over_sound,
        win_game_sound):
    global stop

    clock = pygame.time.Clock()
    screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WALLPAPER, SCREEN_CAPTION, brick_collision_sound,
                    paddles_collision_sound, walls_and_triangles_collision_sound, game_over_sound, win_game_sound)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        stop = screen.update()
        if stop:
            return
        pygame.display.flip()  # updates the contents of the entire display
        clock.tick(FPS)
