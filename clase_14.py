import pygame as pg
import library as lib


class Player(pg.sprite.Sprite):
    def __init__(self, matrix, position):
        super(Player, self).__init__()
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


if __name__ == '__main__':
    pg.init()
    run = True
    window = lib.new_window("Sprites and animations")
    fps = lib.frames_per_second_basics()

    sprites = pg.image.load("Images/animals.png")

    players = pg.sprite.Group()

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
    players.add(player)

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

        players.update()

        lib.fill(window)

        players.draw(window)

        lib.frames_per_second(fps, 0, 12)
    pg.quit()
