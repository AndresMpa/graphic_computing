# coding=utf-8
import pygame as pg
import library as lib


class Player(pg.sprite.Sprite):
    def __init__(self, position, sprite_sets, collides):
        super(Player, self).__init__()

        # Animation issues
        self.action = 3
        self.current_animation = 1

        # Player images
        self.set = sprite_sets
        self.image = self.set[self.action][self.current_animation]

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0.0, 0.0]

        # Collision
        self.collides = collides
        self.floor = False

        # Control
        self.gravity_force = 0.9
        self.speed = 0
        self.live = []

    def animate(self, key_pressed):
        if self.current_animation < 2 and key_pressed:
            self.current_animation += 1
        else:
            self.current_animation = 1
        self.image = self.set[self.action][self.current_animation]

    def get_position(self):
        return [self.rect.x, self.rect.y]

    def gravity(self):
        if self.velocity[1] == 0:
            self.velocity[1] = self.gravity_force
        else:
            self.velocity[1] += self.gravity_force

    def update(self, key_pressed):
        self.animate(key_pressed)

        self.rect.x += self.velocity[0]

        if not self.floor:
            self.gravity()
        if self.rect.bottom > lib.cts.height:
            self.floor = True
            self.velocity[1] = 0
            self.rect.bottom = lib.cts.height

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


class Walls(pg.sprite.Sprite):
    def __init__(self, position, large=None):
        super(Walls, self).__init__()

        # Player images
        if large is None:
            large = [100, 10]
        self.large = large
        self.image = pg.Surface(self.large)
        self.image.fill(lib.cts.WHITE)

        # Position issues
        self.direction = 0
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]


if __name__ == '__main__':
    # init()
    pg.init()
    pg.font.init()

    # Whiles
    run = True

    # Windows constants
    window = lib.new_window("Platforms")
    fps = lib.frames_per_second_basics()

    # Groups
    # while writing
    title_group = pg.sprite.Group()
    text_group = pg.sprite.Group()

    # while playing
    players_group = pg.sprite.Group()
    walls_group = pg.sprite.Group()

    # Variables
    speed = 3
    key = None

    # Adding walls
    wall = Walls([250, 550], [10, 100])
    walls_group.add(wall)
    wall = Walls([350, 450], [100, 100])
    walls_group.add(wall)
    wall = Walls([550, 350], [100, 100])
    walls_group.add(wall)
    wall = Walls([650, 150], [50, 10])
    walls_group.add(wall)
    wall = Walls([700, 250], [50, 15])
    walls_group.add(wall)
    wall = Walls([900, 150], [80, 10])
    walls_group.add(wall)
    wall = Walls([1150, 350], [20, 10])
    walls_group.add(wall)

    # Adding a player
    player = Player([88, lib.cts.height - lib.cts.height / 3], lib.cts.Luke, walls_group)
    player.speed = speed

    players_group.add(player)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                key = 1
                if event.key == pg.K_w:
                    player.velocity[1] -= player.speed * 5
                    player.floor = False
                if event.key == pg.K_d:
                    player.velocity[0] += player.speed
                    player.action = 0
                if event.key == pg.K_a:
                    player.velocity[0] -= player.speed
                    player.action = 2
            if event.type == pg.KEYUP:
                player.velocity[0] = 0
                key = 0

        # Drawing

        players_group.update(key)
        walls_group.update()
        lib.fill(window)
        walls_group.draw(window)
        players_group.draw(window)

        lib.frames_per_second(fps, 1)

    pg.quit()
