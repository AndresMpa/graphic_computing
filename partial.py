# Libraries
import pygame as pg
import figure as fig
import library as lib

if __name__ == '__main__':
    # Basic vars
    pg.init()
    run = True
    window = lib.new_window("Figure")
    fps = lib.frames_per_second_basics()

    # Creating the figure
    figure_object = []

    # Appending each piece of figure
    figure_1 = fig.Left
    figure_1 = lib.screen_into_cartesian_for_array(figure_1)
    figure_object.append(figure_1)

    figure_2 = fig.Center
    figure_2 = lib.screen_into_cartesian_for_array(figure_2)
    figure_object.append(figure_2)

    figure_3 = fig.Right
    figure_3 = lib.screen_into_cartesian_for_array(figure_3)
    figure_object.append(figure_3)

    # Setting an assistant for rotting
    figure_object_rotted = figure_object

    # Creating other var
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

        # Drawing issues
        lib.fill(window)
        lib.cartesian_plane(window)
        for stage, section in enumerate(figure_object):
            for figure_iterated, values in enumerate(figure_object[stage]):
                lib.polygons_filled(window, figure_object_rotted[stage][figure_iterated], lib.cts.PALETTE_1[stage])
        lib.frames_per_second(fps, 10)
    pg.quit()
