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


class EnemyShip(pg.sprite.Sprite):
    def __init__(self, position):
        super(EnemyShip, self).__init__()

        # Player images
        self.down = 0
        self.image = cts.Snake

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]

    def movement(self, pos_x, pos_y):
        self.rect.x += pos_x
        if self.down == 3:
            self.rect.y += pos_y
            self.down = 0

    def update(self, window, pos_x, pos_y):
        self.movement(pos_x, pos_y)


class Shot(pg.sprite.Sprite):
    def __init__(self, position):
        super(Shot, self).__init__()

        # Shot images
        self.image = pg.Surface([20, 20])
        self.image.fill(cts.RED)

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
