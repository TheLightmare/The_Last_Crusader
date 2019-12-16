import pygame as pg
import sys
from settings import * # importe les fonctions contenues dans le fichier "settings.py"
from sprites import *  # importe les fonctions contenues dans le fichier "sprites.py"
from os import path # librairie pour gérer les localisations des fichiers
from tilemap import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, "sprites")
        self.map = Map(path.join(game_folder, "map.txt"))
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert()
        self.player_img.set_colorkey((0,255,0))
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert()
        self.grass_img = pg.image.load(path.join(img_folder, GRASS_IMG)).convert()
        self.slab_img = pg.image.load(path.join(img_folder, SLAB_IMG)).convert()
        self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert()
        self.mob_img.set_colorkey((0,255,0))
        
    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.grass = pg.sprite.Group()
        self.slab = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        
        for row, tiles in enumerate(self.map.data) :  # "enumerate" permet de récupérer l'index de l'élément de la liste
            for col, tile in enumerate(tiles) :
                if tile == "1" :  # s'il y a un "1" dans le fichier map.txt, on fait spawner un mur
                    Wall(self, col, row)
                elif tile == "p" : # la lettre "p" dans le fichier map.txt est le point de spawn du joueur
                    player_x = col                #self.player = Player(self, col, row)
                    player_y = row
                    Grass(self, col, row)
                elif tile == "." :
                    Grass(self, col, row)
                elif tile == "2" :
                    Slab(self, col, row)
                elif tile == "m" :
                    Grass(self, col, row)
                    Mob(self, col, row)
                    
        self.player = Player(self, player_x, player_y)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites :
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                
                
    def show_start_screen(self): # écran de démarrage du jeu !
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
