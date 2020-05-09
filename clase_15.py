import pygame as pg
import library as lib


class Player(pg.sprite.Sprite):
    def __init__(self, matrix, position, movement_limit):
        super(Player, self).__init__()
        self.matrix = matrix

        self.action = 1
        self.current_animation = 0
        self.limits = [3, 3, 2, 4, 1, 3, 4, 4, 6, 0]

        self.image = self.matrix[self.action][self.current_animation]
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = position
        self.movement_limit = movement_limit
        self.velocity = [0, 0]

    def animate(self):
        if self.current_animation < self.limits[self.action]:
            self.current_animation += 1
        else:
            self.current_animation = 0
            self.action = 1
        self.image = self.matrix[self.action][self.current_animation]

    def update(self):
        self.animate()
        self.rect.x += self.velocity[0]
        if self.rect.bottom < self.movement_limit:
            self.velocity[1] = 0
            self.rect.bottom = self.movement_limit + 5
        else:
            self.rect.y += self.velocity[1]


class Objects(pg.sprite.Sprite):
    def __init__(self, position, large=None):
        super(Objects, self).__init__()

        # Player images
        if large is None:
            large = [50, 50]
        self.image = pg.Surface(large)
        self.image.fill(lib.cts.BLUE)

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.block_velocity = [0, 0]

    def update(self):
        self.rect.x += self.block_velocity[0]
        self.rect.y += self.block_velocity[1]


if __name__ == '__main__':
    pg.init()
    run = True
    window = lib.new_window("Sprites and animations")
    fps = lib.frames_per_second_basics()

    sprites = pg.image.load("Images/ken.png")

    players = pg.sprite.Group()
    blocks = pg.sprite.Group()

    animations = []

    speed = 3
    background_limit = 300

    for lanes in range(10):
        lane = []
        for col in range(7):
            square = sprites.subsurface(70 * col, 80 * lanes, 70, 80)
            lane.append(square)
        animations.append(lane)

    player = Player(animations, [500, 500], background_limit)
    players.add(player)

    block = Objects([700, 500], [30, 80])
    blocks.add(block)

    combo = ''

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    player.velocity[1] += speed
                    player.action = 9
                if event.key == pg.K_w:
                    player.velocity[1] -= speed
                    player.action = 2
                    combo += 'w'
                if event.key == pg.K_d:
                    player.velocity[0] += speed
                    player.action = 3
                if event.key == pg.K_a:
                    player.velocity[0] -= speed
                    player.action = 1

                if event.key == pg.K_e:
                    player.velocity[0] += speed
                    player.action = 2
                    player.current_animation = 0
                    combo += 'e'

                if event.key == pg.K_q:
                    player.action = 9
                    combo += 'q'

                if event.key == pg.K_SPACE:
                    player.velocity[0] += speed
                    player.action = 8
            if event.type == pg.KEYUP:
                player.velocity = [0, 0]

            if len(combo) >= 3:
                if combo == 'qwe':
                    print "Hadoken!"
            else:
                combo = ''

        list_collides = pg.sprite.spritecollide(player, blocks, False)

        for block in list_collides:
            if player.action == 2:
                if block.rect.bottom - 10 < player.rect.bottom < block.rect.bottom + 10:
                    block.block_velocity[0] = 5

        for block in blocks:
            if block.block_velocity[0] > 0:
                block.block_velocity[0] -= 1

        players.update()
        blocks.update()

        lib.fill(window)

        lib.line(window, [0, background_limit], [lib.cts.width, background_limit])
        lib.line(window, [(player.rect.left - 20), player.rect.bottom], [(player.rect.right + 20), player.rect.bottom])
        lib.line(window, [(block.rect.left - 20), block.rect.bottom], [(block.rect.right + 20), block.rect.bottom])

        blocks.draw(window)
        players.draw(window)

        lib.frames_per_second(fps, 0, 12)
    pg.quit()
