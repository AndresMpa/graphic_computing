import pygame as pg
import library as lib
import constants as cts


class Player(pg.sprite.Sprite):
    def __init__(self, position):
        super(Player, self).__init__()

        # Animations issues
        self.current_direction = 0
        self.current_image = 0

        # Player images
        self.images = cts.Luke
        self.image = self.images[self.current_direction][self.current_image]

        # Position issues
        self.rect = self.images[self.current_direction][self.current_image].get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]

        # Collision
        self.blocks = None

    def next_images(self, direction):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        self.current_direction = direction

        if self.current_image >= 3:
            self.current_image = 0

    def update(self, direction):
        self.next_images(direction)
        self.image = self.images[self.current_direction][self.current_image]


class Block(pg.sprite.Sprite):
    def __init__(self, position, width, height):
        super(Block, self).__init__()

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
