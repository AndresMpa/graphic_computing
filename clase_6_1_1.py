import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    triangle = [lib.cts.E, lib.cts.F, lib.cts.G]
    window = lib.new_window("Scaling with fixed point - Triangle")
    lib.polygons(window, triangle)
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                triangle = lib.scaling_with_fixed_point(triangle, triangle[1], [2, 2])
                lib.polygons(window, triangle, lib.cts.RED)
        lib.flip()
    pg.quit()
