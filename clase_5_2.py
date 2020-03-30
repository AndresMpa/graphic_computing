import pygame as pg
import library as lib

if __name__ == '__main__':

    pg.init()
    run = True

    # Plane issues
    origin = lib.cts.Origin
    rotting_point = lib.screen_into_cartesian(lib.cts.A, origin)
    rotted_point = lib.screen_into_cartesian(lib.cts.A, origin)

    # Angle used
    angle = 5

    # Clock
    fps = lib.frames_per_second_basics()

    # Window
    window = lib.new_window("Moving ball inside a moving plane")

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                angle = 5
                origin = pg.mouse.get_pos()
                rotting_point = lib.screen_into_cartesian(lib.cts.A, origin)
                lib.point(window, rotting_point, lib.cts.BLUE)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    rotting_point = lib.clockwise(rotting_point, angle)
                if event.key == pg.K_s:
                    rotting_point = lib.counterclockwise(rotting_point, angle)
                    lib.point(window, rotting_point, lib.cts.GREEN)
                if event.type == pg.K_SPACE:
                    lib.fill(window, lib.cts.BLACK)

            lib.point(window, rotting_point, lib.cts.GREEN)

        lib.cartesian_plane(window, origin)
        fps.tick(60)
        lib.flip()
    pg.quit()
