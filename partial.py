import pygame as pg
import figure as fig
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    window = lib.new_window("Figure")
    fps = lib.frames_per_second_basics()

    direction = 1
    angle = direction

    while run:
        figure = fig.Model
        figure = lib.screen_into_cartesian_for_array(figure, lib.cts.size)
        rotting_figure = figure

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                direction = -direction

        iterator = 0
        while iterator < len(rotting_figure):
            rotting_figure[0][iterator] = lib.translation(
                rotting_figure[0][iterator], [-lib.cts.Origin[0], -lib.cts.Origin[1]])
            iterator += 1

        rotting_figure[0] = lib.rotting_with_fixed_point(rotting_figure[0], lib.cts.Origin, angle)
        rotting_figure[1] = lib.rotting_with_fixed_point(rotting_figure[1], lib.cts.Origin, angle)
        angle += direction

        iterator = 0
        while iterator < len(rotting_figure):
            rotting_figure[0][iterator] = lib.translation(
                rotting_figure[0][iterator], [lib.cts.Origin[0], lib.cts.Origin[1]])
            iterator += 1

        lib.fill(window)

        lib.cartesian_plane(window)

        for stage_1, section in enumerate(rotting_figure):
            lib.polygons_filled(window, rotting_figure[0], lib.random_color())
        lib.frames_per_second(fps, 2)
    pg.quit()
