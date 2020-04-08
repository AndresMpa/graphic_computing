import pygame as pg
import figure as fig
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    window = lib.new_window("Figure", lib.cts.size)
    fps = lib.frames_per_second_basics()

    figure = lib.screen_into_cartesian_for_array(fig.Up)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            lib.polygons_filled(window, figure)

        lib.frames_per_second(fps, 12)
    pg.quit()
