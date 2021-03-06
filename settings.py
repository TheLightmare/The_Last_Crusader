import pygame as pg

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 2048   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 1200  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "The Last Crusader"
BGCOLOR = DARKGREY

TILESIZE = 64  # taille (en pixels) d'une "tile"
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = "Pwall.png"
GRASS_IMG = "grass.png"
SLAB_IMG = "Pslab.png"

# Mob settings

MOB_IMG = "pnj_left.png"
MOB_SPEED = 300
MOB_HIT_RECT = pg.Rect(0, 0, 64, 150)

# player settings
PLAYER_SPEED = 400
PLAYER_IMG = "crusader_right.png"
PLAYER_HIT_RECT = pg.Rect(0, 0, 128, 150)
