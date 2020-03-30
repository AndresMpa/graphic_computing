import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    radius = 150
    angle = 5

    base = [lib.screen_into_cartesian(lib.polar_into_cartesian(radius, 30)),
            lib.screen_into_cartesian([0, 0]),
            lib.screen_into_cartesian(lib.polar_into_cartesian(radius, 180))]
    rotting_base = base

    ceil = []
    for iterator, value in enumerate(base):
        ceil.append(lib.translation(base[iterator], [0, -radius]))
    ceil.append(lib.translation(ceil[0], [-radius, 0]))
    rotting_ceil = ceil

    lines = lib.lines_in_figures(base, ceil)

    fps = lib.frames_per_second_basics()
    window = lib.new_window("3D figures rotting using polar system")
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                lib.fill(window)
                rotting_base = lib.rotting_with_fixed_point(base, base[1], angle)
                rotting_ceil = lib.rotting_with_fixed_point(ceil, ceil[1], angle)
                lines = lib.lines_in_figures(rotting_base, rotting_ceil)
                angle += 5

        lib.solids(window, rotting_base, lib.random_color())
        lib.polygons(window, rotting_ceil, lib.random_color(), 5)
        for iterator, value in enumerate(lines):
            lib.polygons(window, lines[iterator], lib.random_color(), 5)
        lib.frames_per_second(fps, 0, 24)
        lib.flip()
    pg.quit()
