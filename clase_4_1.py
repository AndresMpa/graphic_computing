import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    point = []
    window = lib.new_window("Rotting point")
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                point = pg.mouse.get_pos()
                lib.point(window, point)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    point = lib.counterclockwise(point, 5)
                    lib.point(window, point, lib.cts.GREEN)
                if event.key == pg.K_DOWN:
                    point = lib.clockwise(point, 5)
                    lib.point(window, point, lib.cts.BLUE)
        lib.flip()
    pg.quit()
