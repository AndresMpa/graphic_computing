import pygame as pg
import library as lib
import constants as cts


class Player(pg.sprite.Sprite):
    def __init__(self, position, sprite_sets=lib.cts.Luke, collides=[]):
        super(Player, self).__init__()

        # Animation
        self.action = 3
        self.current_animation = 1

        # Player images
        self.set = sprite_sets
        self.image = self.set[self.action][self.current_animation]

        # Position
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]

        # Control
        self.speed = 0
        self.collides = collides

    def animate(self, key_pressed):
        if self.current_animation < 2 and key_pressed:
            self.current_animation += 1
        else:
            self.current_animation = 1
        self.image = self.set[self.action][self.current_animation]

    def get_position(self):
        return [self.rect.x, self.rect.y]

    def update(self, key_pressed):
        self.animate(key_pressed)

        self.rect.x += self.velocity[0]
        list_collide = pg.sprite.spritecollide(self, self.collides, False)

        for things in list_collide:
            if self.velocity[0] > 0:
                if self.rect.right > things.rect.left:
                    self.rect.right = things.rect.left
                    self.velocity[0] = 0
            else:
                if self.rect.left < things.rect.right:
                    self.rect.left = things.rect.right
                    self.velocity[0] = 0

        self.rect.y += self.velocity[1]
        list_collide = pg.sprite.spritecollide(self, self.collides, False)

        for things in list_collide:
            if self.velocity[1] > 0:
                if self.rect.bottom > things.rect.top:
                    self.rect.bottom = things.rect.top
                    self.velocity[1] = 0

            else:
                if self.rect.top < things.rect.bottom:
                    self.rect.top = things.rect.bottom
                    self.velocity[1] = 0


class Objects(pg.sprite.Sprite):
    def __init__(self, position):
        super(Objects, self).__init__()

        # Player images
        self.image = cts.Tree

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.block_velocity = [0, 0]

    def update(self):
        self.rect.x += self.block_velocity[0]
        self.rect.y += self.block_velocity[1]


class Enemy(pg.sprite.Sprite):
    def __init__(self, position):
        super(Enemy, self).__init__()

        # Player images
        self.image = cts.Snake

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]

    def movement(self, pos_x, pos_y):
        """
        self.rect.x += pos_x - 1
        self.rect.y += pos_y - 1
        """
        pass

    def update(self, window, pos_x, pos_y):
        self.movement(pos_x, pos_y)


class PlayerShip(pg.sprite.Sprite):
    def __init__(self, position):
        super(PlayerShip, self).__init__()

        # Player images
        self.image = cts.Ship

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]

        # Other settings
        self.life = 0

    def get_position(self):
        return [self.rect.x, self.rect.y]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


class EnemyShip(pg.sprite.Sprite):
    def __init__(self, position, enemy_type):
        super(EnemyShip, self).__init__()

        # Player images
        self.image = cts.Invaders[enemy_type]

        # Position issues
        self.down = 0
        self.direction = 1
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]
        self.tmp = lib.random_range(40, 100)

    def get_position(self):
        return [self.rect.x, self.rect.y]

    def update(self):
        self.tmp -= 1
        if self.rect.x > (cts.width - self.rect.width):
            self.rect.x = cts.width - self.rect.width
            self.velocity[0] = -5
        if self.rect.x < 0:
            self.rect.x = 0
            self.velocity[0] = 5
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


class Shot(pg.sprite.Sprite):
    def __init__(self, position, shot_class=0):
        super(Shot, self).__init__()

        # Shot images
        self.type = shot_class
        self.image = cts.Player_Shots
        self.shot_type()

        # Position issues
        self.velocity = 5
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def shot_type(self):
        if self.type == 0:
            self.image = cts.Player_Shots
        else:
            self.image = cts.Invader_Shots

    def movement(self):
        if self.type == 0:
            self.rect.y -= self.velocity
        else:
            self.rect.y += self.velocity

    def update(self):
        self.movement()
