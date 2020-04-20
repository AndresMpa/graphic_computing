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
        new_enemy = obj.EnemyShip(lib.random_position(), 0)
        enemies.add(new_enemy)

    position = [0, 0]
    direction = 0
    score = 0
    speed = 1

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    position[0] += speed
                    direction = 0
                if event.key == pg.K_a:
                    position[0] -= speed
                    direction = 2
            if event.type == pg.KEYUP:
                position = [0, 0]
            if event.type == pg.MOUSEBUTTONDOWN:
                print 'balazo'
                shot = obj.Shot(player.get_position())
                shots.add(shot)

        # Control

        if player.rect.x > lib.cts.width:
            player.rect.x = 0 - player.rect.width

        # Collide

        list_collides = pg.sprite.spritecollide(player, enemies, True)
        for points in list_collides:
            score += 1

        for shot in shots:
            list_objects = pg.sprite.spritecollide(shot, players, False)
            if shot.rect.y > (lib.cts.height + 50):
                shots.remove(shot)
            for player in players:
                shots.remove(shot)
                player.life -= 1

        for player in players:
            if player.life < 0:
                run = False

        # Updates
        players.update(window, position[0], position[1])
        enemies.update(window)
        shots.update(window)

        # Drawing issues

        lib.fill(window)

        players.draw(window)
        enemies.draw(window)
        shots.draw(window)

        lib.frames_per_second(fps, 3)

    print "End"
    pg.quit()
