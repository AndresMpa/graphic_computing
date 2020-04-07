import pygame as pg
import library as lib
import objects as obj

if __name__ == '__main__':
    pg.init()
    run = True
    window = lib.new_window("RPG")
    fps = lib.frames_per_second_basics()

    # Groups
    players = pg.sprite.Group()
    enemies = pg.sprite.Group()
    shots = pg.sprite.Group()

    player = obj.PlayerShip([lib.cts.width - 35, lib.cts.height - 35])
    players.add(player)

    number_of_enemies = 10
    for i in range(number_of_enemies):
        new_enemy = obj.EnemyShip(lib.random_position())
        enemies.add(new_enemy)

    position = [0, 0]
    direction = 0
    speed = 3

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    pass
                if event.key == pg.K_w:
                    pass
                if event.key == pg.K_d:
                    position[0] += speed
                    direction = 0
                if event.key == pg.K_a:
                    position[0] -= speed
                    direction = 2
            if event.type == pg.KEYUP:
                position = [0, 0]

        # Collide
        list_objects = pg.sprite.spritecollide(player, enemies, True)

        lib.fill(window)

        # Drawing issues
        players.update(window, position[0], position[1], direction)
        players.draw(window)

        enemies.update(window, position[0], position[1])
        enemies.draw(window)

        shots.draw(window, position[0], position[1])

        lib.frames_per_second(fps)
    pg.quit()
