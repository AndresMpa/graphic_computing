import pygame as pg
import figure as fig
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    window = lib.new_window("Figure")
    fps = lib.frames_per_second_basics()

    figure_object = []

    figure_1 = fig.Left
    figure_1 = lib.screen_into_cartesian_for_array(figure_1, lib.cts.Origin)
    figure_object.append(figure_1)

    figure_2 = fig.Center
    figure_2 = lib.screen_into_cartesian_for_array(figure_2, lib.cts.Origin)
    figure_object.append(figure_2)

    figure_3 = fig.Right
    figure_3 = lib.screen_into_cartesian_for_array(figure_3, lib.cts.Origin)
    figure_object.append(figure_3)

    direction = 1
    angle = direction

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for stage, section in enumerate(figure_object):
                        for figure_iterated, values in enumerate(figure_object[stage]):
                            figure_object[stage][figure_iterated] = lib.translation_for_array(
                                figure_object[stage][figure_iterated], [-100, -100])

                if event.button == 3:
                    for stage, section in enumerate(figure_object):
                        for figure_iterated, values in enumerate(figure_object[stage]):
                            figure_object[stage][figure_iterated] = lib.translation_for_array(
                                figure_object[stage][figure_iterated], [100, 100])
                if event.button == 4:
                    pass
                if event.button == 5:
                    pass

        lib.fill(window)
        for stage, section in enumerate(figure_object):
            for figure_iterated, values in enumerate(figure_object[stage]):
                lib.polygons_filled(window, figure_object[stage][figure_iterated], lib.cts.PALETTE_1[stage])

        lib.frames_per_second(fps, 2)
    pg.quit()
