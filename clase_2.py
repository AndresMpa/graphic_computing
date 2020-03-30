import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    origin = lib.cts.Origin
    window = lib.new_window("Cartesian plane")

    # Cartesian plane by default settings

    lib.cartesian_plane(window, origin)

    # Points without transformation

    A = lib.cts.A
    B = lib.cts.B
    C = lib.cts.C
    D = lib.cts.D
    lib.point(window, A, lib.cts.WHITE)
    lib.point(window, B, lib.cts.BLUE)
    lib.point(window, C, lib.cts.RED)
    lib.point(window, D, lib.cts.GREEN)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                lib.fill(window)
                origin = pg.mouse.get_pos()
                lib.cartesian_plane(window, origin)
                lib.point(window, lib.screen_into_cartesian(lib.cts.A, origin), lib.cts.WHITE)
                lib.point(window, lib.screen_into_cartesian(lib.cts.B, origin), lib.cts.BLUE)
                lib.point(window, lib.screen_into_cartesian(lib.cts.C, origin), lib.cts.RED)
                lib.point(window, lib.screen_into_cartesian(lib.cts.D, origin), lib.cts.GREEN)
        lib.flip()
    pg.quit()
