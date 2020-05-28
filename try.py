import pygame as pg
import library as lib

Ancho = 800
Alto = 600
NEGRO = [0, 0, 0]
VERDE = [0, 255, 0]
BLANCO = [255, 255, 255]
AMARILLO = [255, 255, 0]


class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super(Player, self).__init__()

        self.image = pg.Surface([60, 60])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.vidas = 0

    def RetPos(self):
        x = self.rect.x
        y = self.rect.y
        return [x, y]

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely


class Generator(pg.sprite.Sprite):
    def __init__(self, position):
        super(Generator, self).__init__()

        self.image = lib.cts.Hole
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.temp = 60

    def update(self):
        self.temp -= 1


class GeneratedEnemy(pg.sprite.Sprite):
    def __init__(self, position, sprite_sets):
        super(GeneratedEnemy, self).__init__()

        # Settings
        self.current_animation = 1
        self.current_direction = 0

        # Setting sprites sets
        self.angle = lib.rd.randrange(360)
        self.velocity = [4, 4]

        # Images
        self.set = sprite_sets
        self.image = self.set[self.current_direction][self.current_animation]

        # Position
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def selected(self):
        if self.rect.x > 0 or self.rect.y > 0:
            self.current_direction = 3
        if self.rect.x > 0 or self.rect.y < 0:
            self.current_direction = 1
        if self.rect.x < 0 or self.rect.y > 0:
            self.current_direction = 2
        if self.rect.x < 0 or self.rect.y < 0:
            self.current_direction = 0

    def animate(self):
        self.selected()
        if self.velocity != [0, 0]:
            if self.current_animation < 2:
                self.current_animation += 1
            else:
                self.current_animation = 0
        self.image = self.set[self.current_direction][self.current_animation]

    def update(self):
        self.rect.x += self.velocity[0] * lib.mt.cos(self.angle)
        self.rect.y += self.velocity[1] * lib.mt.sin(self.angle)
        self.animate()


if __name__ == '__main__':
    pg.init()
    ventana = pg.display.set_mode([Ancho, Alto])

    players_group = pg.sprite.Group()
    generators_group = pg.sprite.Group()
    random_enemies_group = pg.sprite.Group()

    player = Player([100, 100])
    players_group.add(player)

    generator = Generator([300, 300])
    generators_group.add(generator)

    reloj = pg.time.Clock()
    fin = False

    while not fin:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                fin = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    player.velx = 5
                    player.vely = 0
                if event.key == pg.K_LEFT:
                    player.velx = -5
                    player.vely = 0
                if event.key == pg.K_UP:
                    player.velx = 0
                    player.vely = -5
                if event.key == pg.K_DOWN:
                    player.velx = 0
                    player.vely = 5
            if event.type == pg.KEYUP:
                player.velx = 0
                player.vely = 0

        # control
        for generator in generators_group:
            if generator.temp < 0:
                raccoon = GeneratedEnemy(generator.rect.center, lib.cts.random_enemies_1)
                random_enemies_group.add(raccoon)
                generator.temp = 60

        for raccoon in random_enemies_group:
            if raccoon.rect.x < -50:
                random_enemies_group.remove(raccoon)
            if raccoon.rect.y < -50:
                random_enemies_group.remove(raccoon)
            if raccoon.rect.x > lib.cts.width:
                random_enemies_group.remove(raccoon)
            if raccoon.rect.y > lib.cts.height:
                random_enemies_group.remove(raccoon)

        players_group.update()
        generators_group.update()
        random_enemies_group.update()
        ventana.fill(NEGRO)
        random_enemies_group.draw(ventana)
        generators_group.draw(ventana)
        players_group.draw(ventana)
        pg.display.flip()
        reloj.tick(20)
