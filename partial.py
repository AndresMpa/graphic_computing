import pygame as pg
import figure as fig
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    window = lib.new_window("Figure")
    fps = lib.frames_per_second_basics()

    figure_object = []
    model = fig.Left_caps
    model = lib.screen_into_cartesian_for_array(model, lib.cts.Origin)
    print model

    print lib.cartesian_into_polar(model[0][0])
    for iteration in enumerate(model):
        for iterator in enumerate(model):
            model[iteration][iterator] = lib.cartesian_into_polar(model[iteration][iterator])
    print model
    figure_object.append(model)
    figure_object_rotted = figure_object

    direction = 1
    angle = direction

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 4:
                    pass

                if event.button == 5:
                    pass

        lib.fill(window)
        lib.cartesian_plane(window)

        for stage, section in enumerate(figure_object):
            for figure_iterated, values in enumerate(figure_object[stage]):
                lib.polygons_filled(window, figure_object_rotted[stage][figure_iterated], lib.cts.PALETTE_1[stage])
        lib.frames_per_second(fps, 10)
    pg.quit()
