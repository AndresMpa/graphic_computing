import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    triangle = []
    window = lib.new_window("Scaling with fixed point - Whatever")
    fps = lib.frames_per_second_basics()
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                triangle.append(pg.mouse.get_pos())
            if event.type == pg.KEYDOWN:
                triangle = lib.scaling_with_fixed_point(triangle, triangle[1], [2, 2])
                lib.polygons(window, triangle, lib.cts.RED)
        lib.frames_per_second(fps, 12)
    pg.quit()
