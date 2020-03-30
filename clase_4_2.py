import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    angle = 5
    r, g, b = 254, 1, 1
    color_direction_red = 1
    color_direction_green = 1
    color_direction_blue = 1
    point = [650, 350]
    origin = lib.cts.Origin
    fps = lib.frames_per_second_basics()
    window = lib.new_window("Animation")
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                origin = pg.mouse.get_pos()
        point_rotted = lib.clockwise(lib.cts.A, angle)
        lib.point(window, lib.screen_into_cartesian(point_rotted, origin), lib.random_color(r, g, b))
        angle += 1
        r += color_direction_red
        g += color_direction_green
        b += color_direction_blue

        if r == 255:
            color_direction_red *= -1
        elif r <= 0:
            color_direction_red = 1

        if g == 255:
            color_direction_green *= -1
        elif g <= 0:
            color_direction_green = 1

        if b == 255:
            color_direction_blue *= -1
        elif b <= 0:
            color_direction_blue = 1

        lib.cartesian_plane(window, lib.cts.Origin)
        fps.tick(60)
        lib.flip()
    pg.quit()
