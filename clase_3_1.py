import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    current_coord = [300, 300]
    window = lib.new_window("Cartesian into screen")
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                current_coord = pg.mouse.get_pos()
        lib.cartesian_plane(window, lib.cts.Origin)
        lib.point(window, lib.cartesian_into_screen(current_coord, lib.cts.Origin))
        lib.point(window, lib.cts.Origin, lib.cts.BLUE, 5)
        lib.flip()
    pg.quit()
