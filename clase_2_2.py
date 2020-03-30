import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    origin = lib.cts.Origin
    window = lib.new_window("Vectors")

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                lib.vectors(window, origin, pg.mouse.get_pos())
        lib.cartesian_plane(window, origin)
        lib.flip()
    pg.quit()
