import pygame as pg
import figure as fig
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    window = lib.new_window("Figure")
    fps = lib.frames_per_second_basics()

    figure = fig.Model
    lib.screen_into_cartesian_for_array(figure, lib.cts.size)

    rotted_figure = figure

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:

                for iteration, value in enumerate(figure):
                    for iterator, score in enumerate(figure):
                        rotted_figure[iteration][iterator] = lib.rotting_with_fixed_point(
                            rotted_figure[iteration], lib.cts.size)

        lib.fill(window)

        lib.cartesian_plane(window)

        for stage_1, section in enumerate(figure):
            lib.polygons_filled(window, figure[stage_1], lib.random_color())
        lib.frames_per_second(fps, 12)
    pg.quit()
