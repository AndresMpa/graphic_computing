import pygame as pg
import library as lib


class Player(pg.sprite.Sprite):
    def __init__(self, matrix, position):
        super(Player, self).__init__()

        self.radius = 50

        self.matrix = matrix

        self.direction = 0
        self.current_animation = 0

        self.image = self.matrix[self.direction][self.current_animation]
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]

    def animate(self):
        self.current_animation += 1
        if self.current_animation == 3:
            self.current_animation = 0
        self.image = self.matrix[self.direction][self.current_animation]

    def update(self):
        if self.velocity != [0, 0]:
            self.animate()
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


class Mouse(pg.sprite.Sprite):
    def __init__(self, matrix, position):
        super(Mouse, self).__init__()

        self.radius = 50

        self.matrix = matrix

        self.id = 0

        self.direction = 0
        self.current_animation = 9

        self.image = self.matrix[self.direction][self.current_animation]
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]

    def animate(self):
        self.current_animation += 1
        if self.current_animation == 11:
            self.current_animation = 9
        self.image = self.matrix[self.direction][self.current_animation]

    def update(self):
        if self.velocity != [0, 0]:
            self.animate()
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


class Generator(pg.sprite.Sprite):
    def __init__(self, position, large=None):
        super(Generator, self).__init__()

        # Player images
        if large is None:
            large = [50, 50]
        self.image = pg.Surface(large)
        self.image.fill(lib.cts.BLUE)

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.tmp = lib.rd.randrange(100)

    def update(self):
        self.tmp -= 1


class Walls(pg.sprite.Sprite):
    def __init__(self, position, large=None):
        super(Walls, self).__init__()

        # Player images
        if large is None:
            large = [50, 50]
        self.large = large
        self.image = pg.Surface(self.large)
        self.image.fill(lib.cts.WHITE)

        # Position issues
        self.direction = 0
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]

    def change_position(self):
        self.rect.x = lib.random_range(10, 1150)
        self.rect.y = lib.random_range(10, 550)

    def get_direction(self):
        velocity = [0, 0]
        if self.direction == 0:
            velocity[0] = 0
            velocity[1] = 3
        if self.direction == 1:
            velocity[1] = 0
            velocity[0] = -3
        if self.direction == 2:
            velocity[1] = 0
            velocity[0] = 3
        if self.direction == 3:
            velocity[0] = 0
            velocity[1] = -3
        return velocity


if __name__ == '__main__':
    pg.init()
    run = True
    window = lib.new_window("Mouse eater")
    fps = lib.frames_per_second_basics()

    sprites = pg.image.load("Images/animals.png")

    walls_group = pg.sprite.Group()
    mouses_group = pg.sprite.Group()
    players_group = pg.sprite.Group()
    generators_group = pg.sprite.Group()

    animations = []

    cat = 0
    bird = 6

    speed = 3

    for lanes in range(8):
        lane = []
        for col in range(12):
            square = sprites.subsurface(32 * col, 32 * lanes, 32, 32)
            lane.append(square)
        animations.append(lane)

    player = Player(animations, [500, 500])
    players_group.add(player)

    thing = Generator([200, 400])
    generators_group.add(thing)

    wall = Walls([100, 25], [400, 10])
    wall.direction = 2
    walls_group.add(wall)

    wall = Walls([900, 100], [10, 600])
    wall.direction = 0
    walls_group.add(wall)

    wall = Walls([100, 500], [400, 10])
    wall.direction = 1
    walls_group.add(wall)

    mouse_number = 0

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    player.velocity[1] += speed
                    player.direction = 0
                if event.key == pg.K_w:
                    player.velocity[1] -= speed
                    player.direction = 3
                if event.key == pg.K_d:
                    player.velocity[0] += speed
                    player.direction = 2
                if event.key == pg.K_a:
                    player.velocity[0] -= speed
                    player.direction = 1
            if event.type == pg.KEYUP:
                player.velocity = [0, 0]

        list_objects = pg.sprite.coll(player, mouses_group, True)

        for generator in generators_group:
            if generator.tmp < 0:
                mouse_direction = lib.rd.randrange(500)

                mouse = Mouse(animations, generator.rdect.center)
                mouse_number += 1
                mouse.id = mouse_number

                if mouse_direction < 250:
                    if mouse_direction % 2 == 0:
                        mouse.velocity[0] = 3
                        mouse.direction = 2
                    else:
                        mouse.velocity[0] = -3
                        mouse.direction = 1
                else:
                    if mouse_direction % 2 == 0:
                        mouse.velocity[1] = 3
                        mouse.direction = 0
                    else:
                        mouse.velocity[1] = -3
                        mouse.direction = 3

                mouses_group.add(mouse)

                generator.tmp = lib.rd.randrange(100)
                generator.rect.x, generator.rect.y = lib.random_position()

        for mouse in mouses_group:
            if pg.sprite.collide_circle(mouse, player):
                print 'near ', mouse.id
            list_mouses = pg.sprite.spritecollide(mouse, walls_group, False)
            for wall in list_mouses:
                mouse.velocity = wall.get_direction()
                mouse.direction = wall.direction
                wall.change_position()
            if mouse.rect.x < -25:
                mouses_group.remove(mouse)
            if mouse.rect.x > lib.cts.width:
                mouses_group.remove(mouse)
            if mouse.rect.y < -25:
                mouses_group.remove(mouse)
            if mouse.rect.y > lib.cts.height:
                mouses_group.remove(mouse)

        walls_group.update()
        mouses_group.update()
        players_group.update()
        generators_group.update()

        lib.fill(window)

        walls_group.draw(window)
        mouses_group.draw(window)
        players_group.draw(window)
        generators_group.draw(window)

        lib.frames_per_second(fps, 0, 20)
    pg.quit()
