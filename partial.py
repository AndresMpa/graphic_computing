import pygame as pg
import figure as fig
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    window = lib.new_window("Figure")
    fps = lib.frames_per_second_basics()

    angle = 1
    figure = fig.Model
    print figure
    figure = lib.screen_into_cartesian_for_array(figure, lib.cts.size)
    print figure

    rotting_figure = figure

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                lib.fill(window)
                rotting_figure[0] = lib.rotting_with_fixed_point(figure[0], figure[0][1], angle)
                rotting_figure[1] = lib.rotting_with_fixed_point(figure[1], figure[1][1], angle)
                angle += 5

        lib.fill(window)

        lib.cartesian_plane(window)

        for stage_1, section in enumerate(figure):
            lib.polygons_filled(window, rotting_figure[stage_1], lib.random_color())
        lib.frames_per_second(fps, 2)
    pg.quit()
