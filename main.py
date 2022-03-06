from config import BRICKS_COLLISION_SOUND, PADDLES_COLLISION_SOUND, WALLS_AND_TRIANGLES_SOUND, GAME_OVER_SOUND,\
    GAME_WIN_SOUND
import pygame
import game

pygame.init()
pygame.mixer.init()
brick_collision_sound = pygame.mixer.Sound(BRICKS_COLLISION_SOUND)
paddles_collision_sound = pygame.mixer.Sound(PADDLES_COLLISION_SOUND)
walls_and_triangles_collision_sound = pygame.mixer.Sound(WALLS_AND_TRIANGLES_SOUND)
game_over_sound = pygame.mixer.Sound(GAME_OVER_SOUND)
game_win_sound = pygame.mixer.Sound(GAME_WIN_SOUND)
game.run(brick_collision_sound, paddles_collision_sound, walls_and_triangles_collision_sound, game_over_sound,
         game_win_sound)
