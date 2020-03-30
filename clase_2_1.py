import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    origin = lib.cts.Origin
    window = lib.new_window("Function y = ax + b")

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        lib.function_y_equal_ax_add_b(window, lib.screen_into_cartesian([0, 0]), None)
        lib.cartesian_plane(window, origin)
        lib.flip()
    pg.quit()
