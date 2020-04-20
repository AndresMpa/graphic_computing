import pygame as pg
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

    def movement(self, pos_x, pos_y, direction):
        self.next_images(direction)
        self.rect.move_ip(pos_x, pos_y)

    def next_images(self, direction):
        self.current_direction = direction
        self.current_image += 1

        if self.current_image >= 3:
            self.current_image = 0

    def update(self, window, pos_x, pos_y, direction):
        self.movement(pos_x, pos_y, direction)
        self.image = self.images[self.current_direction][self.current_image]


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

    def movement(self, pos_x, pos_y):
        self.rect.move_ip(pos_x, pos_y)

    def update(self, window, pos_x, pos_y):
        self.movement(pos_x, pos_y)


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

    def movement(self):
        """
        self.rect.x += self.direction
        if self.rect.x == cts.width - 35:
            self.direction *= -1
            self.down += 1
        if self.rect.x == 35:
            self.direction *= -1
        if self.down == 3:
            self.rect.y += 10
            self.down = 0
        """
        pass

    def update(self, window):
        self.movement()
        self.rect.move_ip(self.rect.x, self.rect.y)


def shot_type(shot_class):
    if shot_class == 0:
        return cts.Player_Shots
    else:
        return cts.Invader_Shots


class Shot(pg.sprite.Sprite):
    def __init__(self, position, shot_class=0):
        super(Shot, self).__init__()

        # Shot images
        self.type = shot_class
        self.image = shot_type(shot_class)

        # Position issues
        self.velocity = 1
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def movement(self):
        if self.type == 0:
            self.rect.y -= self.velocity
        else:
            self.rect.y += self.velocity

        self.rect.move_ip([self.rect.x, self.rect.y])

    def update(self, window):
        self.movement()
