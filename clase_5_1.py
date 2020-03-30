import pygame as pg
import library as lib

if __name__ == '__main__':

    pg.init()
    run = True

    # Angle used
    angle = 2

    origin = lib.cts.Origin
    points = [lib.cartesian_into_screen(lib.cts.E),
              lib.cartesian_into_screen(lib.cts.F),
              lib.cartesian_into_screen(lib.cts.G)]
    rotted_points = points

    # Clock
    fps = lib.frames_per_second_basics()

    # Window
    window = lib.new_window("Rotting triangle")

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 4:
                    rotted_points[0] = lib.counterclockwise(rotted_points[0], angle)
                    rotted_points[1] = lib.counterclockwise(rotted_points[1], angle)
                    rotted_points[2] = lib.counterclockwise(rotted_points[2], angle)
                if event.button == 5:
                    rotted_points[0] = lib.clockwise(rotted_points[0], angle)
                    rotted_points[1] = lib.clockwise(rotted_points[1], angle)
                    rotted_points[2] = lib.clockwise(rotted_points[2], angle)

            lib.fill(window, lib.cts.BLACK)
            lib.polygons(window, [
                lib.screen_into_cartesian(rotted_points[0], origin),
                lib.screen_into_cartesian(rotted_points[1], origin),
                lib.screen_into_cartesian(rotted_points[2], origin)
            ])

        lib.cartesian_plane(window, lib.cts.Origin)
        fps.tick(1080)
        lib.flip()
    pg.quit()
