import pygame as pg
import library as lib
import objects as obj

if __name__ == '__main__':
    pg.init()
    run = True
    window = lib.new_window("Environment")
    fps = lib.frames_per_second_basics()

    background_velocity = [0, 0]
    background_position = [0, 0]
    background_information = lib.cts.background.get_rect()
    print background_information
    background_screen_limits = [lib.cts.width - 50, lib.cts.height - 50]
    background_limit = [(lib.cts.width - background_information[2]), (lib.cts.height - background_information[3])]

    # Groups
    players = pg.sprite.Group()
    blocks = pg.sprite.Group()

    player = obj.Player([lib.cts.width / 2 - 35, lib.cts.height - 70])
    players.add(player)

    block = obj.Objects([1300, 300])
    blocks.add(block)

    block = obj.Objects([300, 100])
    blocks.add(block)

    block = obj.Objects([100, 1300])
    blocks.add(block)

    block = obj.Objects([1300, 800])
    blocks.add(block)

    block = obj.Objects([500, 700])
    blocks.add(block)

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

            player.current_image += 1

        # Control
        if player.rect.x > background_screen_limits[0]:
            player.rect.x = background_screen_limits[0]
            if background_position[0] > background_limit[0]:
                background_velocity[0] = -5
            else:
                background_velocity[0] = 0
        else:
            if player.rect.x < lib.cts.width - background_screen_limits[0]:
                player.rect.x = lib.cts.width - background_screen_limits[0]
                if background_position[0] < lib.cts.width + background_limit[0] * 2:
                    background_velocity[0] = 5
                else:
                    background_velocity[0] = 0
            else:
                if background_position[0] > lib.cts.width + background_limit[0]:
                    background_velocity[0] = -5
                else:
                    background_velocity[0] = 0

        if player.rect.y > background_screen_limits[1]:
            player.rect.y = background_screen_limits[1]
            if background_position[1] > background_limit[1]:
                background_velocity[1] = -5
            else:
                background_velocity[1] = 0
        else:
            if player.rect.y < lib.cts.height - background_screen_limits[1]:
                player.rect.y = lib.cts.height - background_screen_limits[1]
                if background_position[1] < 0:
                    background_velocity[1] = 5
                else:
                    background_velocity[1] = 0
            else:
                if background_position[1] > lib.cts.height + background_limit[1]:
                    background_velocity[1] = -5
                else:
                    background_velocity[1] = 0

        for block in blocks:
            block.block_velocity[0] = background_velocity[0]
            block.block_velocity[1] = background_velocity[1]

        # Updates
        players.update(direction)
        blocks.update()

        # Drawing issues

        window.blit(lib.cts.background, background_position)

        players.draw(window)
        blocks.draw(window)

        lib.frames_per_second(fps, 2)

        background_position[0] += background_velocity[0]
        background_position[1] += background_velocity[1]
    pg.quit()
