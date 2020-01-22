import pygame as pg
from settings import *
from tilemap import collide_hit_rect
vec = pg.math.Vector2

def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if sprite.vel.x > 0:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if sprite.vel.x < 0:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if sprite.vel.y > 0:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if sprite.vel.y < 0:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y


class Spritesheet:
    def __init__(self, filename) :
        self.spritesheet = pg.image.load(filename).convert()
    def get_image(self, x, y, width, height) :
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        return image

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.walking = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.direction = 0
        
        self.image = self.game.player_img.get_image(0, 0, 180, 150)
        #self.image.set_colorkey((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.rot = 0

    def load_images(self) :
        self.standing_frames_r = [self.game.player_img.get_image(0, 0, 180, 150), self.game.player_img.get_image(180, 0, 180, 150)]

        for frame in self.standing_frames_r :
            frame.set_colorkey((0, 255, 0))
        
        self.standing_frames_l = []
        for frame in self.standing_frames_r :
            frame.set_colorkey((0, 255, 0))
            self.standing_frames_l.append(pg.transform.flip(frame, True, False))
        
    def get_keys(self):
            self.vel = vec(0, 0)
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                self.vel.x = -PLAYER_SPEED
            if keys[pg.K_RIGHT] or keys[pg.K_d]:
                self.vel.x = PLAYER_SPEED
            if keys[pg.K_UP] or keys[pg.K_w]:
                self.vel.y = -PLAYER_SPEED
            if keys[pg.K_DOWN] or keys[pg.K_s]:
                self.vel.y = PLAYER_SPEED
            if self.vel.x != 0 and self.vel.y != 0:
                self.vel *= 0.7071

    def update(self):
        self.animate()
        self.get_keys()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center

    def animate(self) :
        now = pg.time.get_ticks()
        if self.vel.x != 0 :
            self.walking = True
        else :
            self.walking = False

        if self.walking :
            if now - self.last_update > 200 :
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_frames_r)
            if self.vel.x > 0 :
                self.image = self.standing_frames_r[self.current_frame]
                self.direction = 0
            else :
                self.image = self.standing_frames_l[self.current_frame]
                self.direction = 1
                
        if not self.walking :
            if now - self.last_update > 200 :
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_frames_r)
                if self.direction == 0 :
                    self.image = self.standing_frames_r[self.current_frame]
                else :
                    self.image = self.standing_frames_l[self.current_frame]
                    
        
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Grass(pg.sprite.Sprite) :
    def __init__(self, game, x, y) :
        self.groups = game.all_sprites, game.grass
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.grass_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Slab(pg.sprite.Sprite) :
    def __init__(self, game, x, y) :
        self.groups = game.all_sprites, game.slab
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.slab_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Mob(pg.sprite.Sprite) :
    def __init__(self, game, x, y) :
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.rot = 0
        
    def update(self) :
        self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
        #self.image = pg.transform.rotate(self.game.mob_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.acc = vec(MOB_SPEED, 0).rotate(-self.rot)
        self.acc += self.vel * -1
        self.vel += self.acc * self.game.dt
        self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center

