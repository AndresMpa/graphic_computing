import pygame as pg
import library as lib
import objects as obj

if __name__ == '__main__':
    pg.init()
    run = True
    window = lib.new_window("Player")

    fps = lib.frames_per_second_basics()
    player = obj.Player()
    direction = 0
    position = [0, 0]
    speed = 7

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    position[1] += speed
                    direction = 3
                if event.key == pg.K_w:
                    position[1] -= speed
                    direction = 1
                if event.key == pg.K_d:
                    position[0] += speed
                    direction = 0
                if event.key == pg.K_a:
                    position[0] -= speed
                    direction = 2
            if event.type == pg.KEYUP:
                position = [0, 0]

        lib.fill(window)
        player.update(window, position[0], position[1], direction)
        lib.frames_per_second(fps)
        lib.flip()
    pg.quit()
