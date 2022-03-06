from time import sleep
from config import *
from screen import Screen
from start_screen import StartScren
import pygame
import sys

is_playing = False

def listen_global_events():
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                global is_playing
                is_playing = True
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def run():
    pygame.init()

    start_screen = StartScren(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WALLPAPER)
    clock = pygame.time.Clock()


    while not is_playing:
        listen_global_events()
        start_screen.update("Press Space to Start")
        start_screen.update("") 
        pygame.display.update() 
        clock.tick(FPS)

    start_screen.update("Get Ready!")
    start_screen.update("3")
    start_screen.update("2")
    start_screen.update("1")

    screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WALLPAPER, SCREEN_CAPTION, GAME_LIFES)

    while is_playing:
        listen_global_events()
        screen.update()
        pygame.display.flip()  # updates the contents of the entire display
        clock.tick(FPS)
