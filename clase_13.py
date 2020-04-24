import pygame as pg
import library as lib
import objects as obj

if __name__ == '__main__':
    pg.init()
    run = True
    window = lib.new_window("Environment")
    fps = lib.frames_per_second_basics()

    # Groups
    players = pg.sprite.Group()
    enemies = pg.sprite.Group()
    shots_players = pg.sprite.Group()
    shots_enemies = pg.sprite.Group()

    player = obj.Player([lib.cts.width / 2 - 35, lib.cts.height - 35])
    players.add(player)

    speed = 5
    direction = 0

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    player.velocity[1] += speed
                    direction = 3
                if event.key == pg.K_w:
                    player.velocity[1] -= speed
                    direction = 1
                if event.key == pg.K_d:
                    player.velocity[0] += speed
                    direction = 0
                if event.key == pg.K_a:
                    player.velocity[0] -= speed
                    direction = 2
            if event.type == pg.KEYUP:
                player.velocity = [0, 0]

        # Updates
        players.update(direction)

        # Drawing issues

        lib.fill(window)

        players.draw(window)

        lib.frames_per_second(fps, 2)
    pg.quit()
