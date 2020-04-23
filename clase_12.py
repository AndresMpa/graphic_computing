import pygame as pg
import library as lib
import objects as obj

if __name__ == '__main__':
    pg.init()
    run = True
    end = True
    intro = True
    playing = True
    txt = "New game"
    window = lib.new_window("RPG")
    fps = lib.frames_per_second_basics()

    while run and intro:
        pg.font.init()
        txt = "NEW GAME"
        write = lib.write(txt, 60, 2)
        window.blit(write, [350, 200])
        txt = "Press any key"
        write = lib.write(txt, 30, 2)
        window.blit(write, [400, 300])

        lib.frames_per_second(fps, 5)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                intro = False

    # Groups
    players = pg.sprite.Group()
    enemies = pg.sprite.Group()
    shots_players = pg.sprite.Group()
    shots_enemies = pg.sprite.Group()

    player = obj.PlayerShip([lib.cts.width / 2 - 35, lib.cts.height - 35])
    players.add(player)

    enemy_type = 0
    invaders_start = [10, 10]

    while enemy_type <= 2:
        for _ in range(0, 12):
            enemy = obj.EnemyShip([invaders_start[0], invaders_start[1]], enemy_type)
            invaders_start[0] += 80
            enemies.add(enemy)
        enemy_type += 1
        invaders_start = [10, invaders_start[1] + 50]

    position = [0, 0]
    direction = 0
    score = 0
    speed = 1

    while run and playing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    player.velocity[0] += speed
                if event.key == pg.K_a:
                    player.velocity[0] -= speed
            if event.type == pg.KEYUP:
                player.velocity = [0, 0]
            if event.type == pg.MOUSEBUTTONDOWN:
                position = player.get_position()
                players_shot = obj.Shot([position[0] + 25, position[1]])
                shots_players.add(players_shot)

        # Control

        list_object = pg.sprite.spritecollide(player, enemies, True)

        for enemy in enemies:
            if enemy.tmp <= 0:
                position = enemy.get_position()
                shot = obj.Shot([position[0] + 25, position[1] + 15], 1)
                shots_enemies.add(shot)
                enemy.tmp = lib.random_range(100, 300)

        for shot in shots_players:
            list_enemies = pg.sprite.spritecollide(shot, enemies, True)
            if shot.rect.y < -10:
                shots_players.remove(shot)
            for enemy in shots_enemies:
                shots_enemies.remove(shot)
                score += 100

        for shot in shots_enemies:
            list_players = pg.sprite.spritecollide(shot, players, False)
            if shot.rect.y > (lib.cts.height + 10):
                shots_enemies.remove(shot)
            for player in list_players:
                player.life -= 1

        for player in players:
            if player.life < 0:
                playing = False

        # Updates
        players.update()
        enemies.update()
        shots_enemies.update()
        shots_players.update()

        # Drawing issues

        lib.fill(window)

        players.draw(window)
        enemies.draw(window)
        shots_enemies.draw(window)
        shots_players.draw(window)

        txt = str(score)
        write = lib.write(txt, 10, 2)
        window.blit(write, [0, 0])
        txt = "Press any key"
        write = lib.write(txt, 30, 2)
        window.blit(write, [400, 300])

        lib.frames_per_second(fps, 2)

    while run and end:
        lib.fill(window)
        pg.font.init()
        txt = "GAME OVER"
        write = lib.write(txt, 60, 2)
        window.blit(write, [350, 200])
        txt = "Press any key"
        write = lib.write(txt, 30, 2)
        window.blit(write, [400, 300])

        lib.frames_per_second(fps, 5)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
                end = False
