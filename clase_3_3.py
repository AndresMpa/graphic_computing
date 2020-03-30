import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    size = 1
    scale = []
    window = lib.new_window("Scale vectors")
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                scale = pg.mouse.get_pos()
                lib.vectors(window, lib.cts.Origin, scale)
                scale = lib.cartesian_into_screen(scale)
            if event.type == pg.KEYDOWN:
                size += 1
                scale = lib.scale(scale, size)
                lib.vectors(window, lib.cts.Origin, lib.screen_into_cartesian(scale))
        lib.cartesian_plane(window, lib.cts.Origin)
        lib.flip()
    pg.quit()
