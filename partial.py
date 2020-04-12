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

    # Creating the main figure & its copy
    figure_object = []
    figure_object_rotted = []

    # Appending each piece of figure
    figure_1 = fig.Left_caps
    figure_1 = lib.screen_into_cartesian_for_array(figure_1)
    figure_object.append(figure_1)
    figure_object_rotted.append(figure_1)

    figure_2 = fig.Center_caps
    figure_2 = lib.screen_into_cartesian_for_array(figure_2)
    figure_object.append(figure_2)
    figure_object_rotted.append(figure_2)

    figure_3 = fig.Right_caps
    figure_3 = lib.screen_into_cartesian_for_array(figure_3)
    figure_object.append(figure_3)
    figure_object_rotted.append(figure_3)

    lines_1 = lib.lines_in_figures(figure_object_rotted[0][0], figure_object_rotted[0][1])
    lines_2 = lib.lines_in_figures(figure_object_rotted[1][0], figure_object_rotted[1][1])
    lines_3 = lib.lines_in_figures(figure_object_rotted[2][0], figure_object_rotted[2][1])

    # Creating other var
    direction = 1
    angle = direction

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                for stage, section in enumerate(figure_object):
                    for figure_iterated, values in enumerate(figure_object[stage]):
                        figure_object_rotted[stage][figure_iterated] = lib.translation_for_array(
                            figure_object[stage][figure_iterated],
                            [figure_object[stage][figure_iterated][3][0] - lib.cts.Origin[0],
                             figure_object[stage][figure_iterated][3][1] - lib.cts.Origin[1]])

                # Remaking the main figure
                figure_object = []

                # Appending each piece of figure
                figure_1 = fig.Left_caps
                figure_1 = lib.screen_into_cartesian_for_array(figure_1)
                figure_object.append(figure_1)

                figure_2 = fig.Center_caps
                figure_2 = lib.screen_into_cartesian_for_array(figure_2)
                figure_object.append(figure_2)

                figure_3 = fig.Right_caps
                figure_3 = lib.screen_into_cartesian_for_array(figure_3)
                figure_object.append(figure_3)

                if event.button == 4:
                    angle += direction
                    figure_object_rotted[0][0] = lib.rotting_with_fixed_point(
                        figure_object_rotted[0][0],
                        figure_object_rotted[0][0][3],
                        angle)
                    figure_object_rotted[1][0] = lib.rotting_with_fixed_point(
                        figure_object_rotted[1][0],
                        figure_object_rotted[0][0][3],
                        angle)
                    figure_object_rotted[2][0] = lib.rotting_with_fixed_point(
                        figure_object_rotted[2][0],
                        figure_object_rotted[0][0][3],
                        angle)

                    figure_object_rotted[0][1] = lib.rotting_with_fixed_point(
                        figure_object_rotted[0][1],
                        figure_object_rotted[0][1][3],
                        angle)
                    figure_object_rotted[1][1] = lib.rotting_with_fixed_point(
                        figure_object_rotted[1][1],
                        figure_object_rotted[0][1][3],
                        angle)
                    figure_object_rotted[2][1] = lib.rotting_with_fixed_point(
                        figure_object_rotted[2][1],
                        figure_object_rotted[0][1][3],
                        angle)

                    figure_object_rotted[0][1] = lib.rotting_with_fixed_point(
                        figure_object_rotted[0][1],
                        figure_object_rotted[0][1][3],
                        angle)
                    figure_object_rotted[0][1] = lib.rotting_with_fixed_point(
                        figure_object_rotted[0][1],
                        figure_object_rotted[0][1][3],
                        angle)

                    figure_object_rotted[1][0] = lib.rotting_with_fixed_point(
                        figure_object_rotted[1][0],
                        figure_object_rotted[2][0][3],
                        angle)
                    figure_object_rotted[1][1] = lib.rotting_with_fixed_point(
                        figure_object_rotted[1][1],
                        figure_object_rotted[1][1][3],
                        angle)

                    figure_object_rotted[2][0] = lib.rotting_with_fixed_point(
                        figure_object_rotted[2][0],
                        figure_object_rotted[2][0][3],
                        angle)
                    figure_object_rotted[2][1] = lib.rotting_with_fixed_point(
                        figure_object_rotted[2][1],
                        figure_object_rotted[2][1][3],
                        angle)

                    """
                    for stage, section in enumerate(figure_object):
                        for figure_iterated, values in enumerate(figure_object[stage]):
                            figure_object_rotted[stage][figure_iterated] = lib.rotting_with_fixed_point(
                                figure_object_rotted[stage][figure_iterated],
                                figure_object_rotted[stage][figure_iterated][3],
                                angle)
                    """
                if event.button == 5:
                    angle -= direction
                    for stage, section in enumerate(figure_object):
                        for figure_iterated, values in enumerate(figure_object[stage]):
                            figure_object_rotted[stage][figure_iterated] = lib.rotting_with_fixed_point(
                                figure_object_rotted[stage][figure_iterated],
                                figure_object_rotted[stage][figure_iterated][3],
                                angle)

                for stage, section in enumerate(figure_object):
                    for figure_iterated, values in enumerate(figure_object[stage]):
                        figure_object_rotted[stage][figure_iterated] = lib.translation_for_array(
                            figure_object_rotted[stage][figure_iterated],
                            [lib.cts.Origin[0] - figure_object[stage][figure_iterated][3][0],
                             lib.cts.Origin[1] - figure_object[stage][figure_iterated][3][1]])

                lines_1 = lib.lines_in_figures(figure_object_rotted[0][0], figure_object_rotted[0][1])
                lines_2 = lib.lines_in_figures(figure_object_rotted[1][0], figure_object_rotted[1][1])
                lines_3 = lib.lines_in_figures(figure_object_rotted[2][0], figure_object_rotted[2][1])

        # Drawing issues
        lib.fill(window)
        # Lines
        for iterator, value in enumerate(lines_1):
            lib.polygons(window, lines_1[iterator], lib.cts.PALETTE_1[0], 5)
        for iterator, value in enumerate(lines_2):
            lib.polygons(window, lines_2[iterator], lib.cts.PALETTE_1[1], 5)
        for iterator, value in enumerate(lines_3):
            lib.polygons(window, lines_3[iterator], lib.cts.PALETTE_1[2], 5)

        # Caps
        for stage, section in enumerate(figure_object):
            for figure_iterated, values in enumerate(figure_object[stage]):
                lib.polygons(window, figure_object_rotted[stage][figure_iterated],
                             lib.cts.PALETTE_1[stage])
        lib.frames_per_second(fps, 10)
    pg.quit()
