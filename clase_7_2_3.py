import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    angle = 0
    amplitude = 1
    add_amplitude = 0.1
    fps = lib.frames_per_second_basics()
    window = lib.new_window("Archimedean Spiral")
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                amplitude += 1
                angle = 0
                lib.fill(window)
            lib.point(window, lib.screen_into_cartesian(lib.polar_into_cartesian(
                lib.archimedean_spiral(angle, amplitude), angle)), lib.random_color())
            angle += 1
        lib.cartesian_plane(window, lib.cts.Origin)
        fps.tick(1080)
        lib.flip()
    pg.quit()
