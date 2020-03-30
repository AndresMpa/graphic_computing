import pygame as pg
import library as lib

if __name__ == '__main__':

    pg.init()
    run = True

    # Plane issues
    cont = 0
    origin = lib.cts.Origin
    transformation_scale = [-500, 0]
    triangle = [lib.cts.E, lib.cts.F, lib.cts.G]

    # Clock
    fps = lib.frames_per_second_basics()

    # Window
    window = lib.new_window("Translation")

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.KEYDOWN:
                if cont == 0:
                    transformation_scale = [-500, 0]
                elif cont == 1:
                    transformation_scale = [0, 300]
                elif cont == 2:
                    transformation_scale = [500, 0]
                elif cont == 3:
                    transformation_scale = [0, -300]
                    cont = -1
                cont += 1
                triangle[0] = lib.translation(triangle[0], transformation_scale)
                triangle[1] = lib.translation(triangle[1], transformation_scale)
                triangle[2] = lib.translation(triangle[2], transformation_scale)

            lib.fill(window)
            lib.polygons(window, triangle)

        lib.cartesian_plane(window, origin)
        fps.tick(60)
        lib.flip()
    pg.quit()
