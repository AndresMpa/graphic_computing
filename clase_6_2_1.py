import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    triangle = [lib.cts.E, lib.cts.F, lib.cts.G]
    triangle_rotted = []
    angle = 90
    window = lib.new_window("Rotting with fixed - Point")
    lib.polygons(window, triangle)
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                triangle_rotted = lib.rotting_with_fixed_point(triangle, triangle[2], angle)
                angle += 90
                lib.polygons(window, triangle_rotted, lib.cts.RED)
        lib.flip()
    pg.quit()
