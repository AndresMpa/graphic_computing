import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    scale = []
    window = lib.new_window("Scaling vectors")
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                scale.append(pg.mouse.get_pos())
                if len(scale) == 2:
                    lib.vectors(window, scale[0], scale[1])
                    scale[1] = lib.cartesian_into_screen(scale[1])
                    scale[1] = lib.scale(scale[1], 2)
                    lib.vectors(window, scale[0], lib.screen_into_cartesian(scale[1]))
                    scale = []
        lib.cartesian_plane(window, lib.cts.Origin)
        lib.flip()
    pg.quit()
