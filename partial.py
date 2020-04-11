import pygame as pg
import figure as fig
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    window = lib.new_window("Figure")
    fps = lib.frames_per_second_basics()
    rotting = 2

    figure_object = []
    figure_1 = fig.Left_caps
    figure_1 = lib.screen_into_cartesian_for_array(figure_1, lib.cts.Origin)
    figure_object.append(figure_1)

    figure_2 = fig.Center_caps
    figure_2 = lib.screen_into_cartesian_for_array(figure_2, lib.cts.Origin)
    figure_object.append(figure_2)

    figure_3 = fig.Right_caps
    figure_3 = lib.screen_into_cartesian_for_array(figure_3, lib.cts.Origin)
    figure_object.append(figure_3)
    figure_object_rotted = figure_object

    direction = 1
    angle = direction

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                figure_object_rotted = figure_object
                if event.button == 4:
                    angle += direction
                    for stage, section in enumerate(figure_object):
                        for figure_iterated, values in enumerate(figure_object[stage]):
                            figure_object_rotted[stage][figure_iterated] = lib.translation_for_array(
                                figure_object_rotted[stage][figure_iterated],
                                [lib.cts.Origin[0] - figure_object[stage][figure_iterated][3][0],
                                 lib.cts.Origin[1] - figure_object[stage][figure_iterated][3][1]])

                    figure_object_rotted[0][0] = lib.rotting_with_fixed_point(
                        figure_object_rotted[0][0],
                        figure_object_rotted[0][0][3],
                        angle)
                    figure_object_rotted[0][1] = lib.rotting_with_fixed_point(
                        figure_object_rotted[0][1],
                        figure_object_rotted[0][1][3],
                        angle)

                    figure_object_rotted[1][0] = lib.rotting_with_fixed_point(
                        figure_object_rotted[1][0],
                        figure_object_rotted[1][0][3],
                        angle)
                    figure_object_rotted[1][1] = lib.rotting_with_fixed_point(
                        figure_object_rotted[1][1],
                        [figure_object_rotted[1][1][3][0] - figure_object_rotted[2][1][3][0],
                         figure_object_rotted[1][1][3][1] - figure_object_rotted[2][1][3][1]],
                        angle)

                    figure_object_rotted[2][0] = lib.rotting_with_fixed_point(
                        figure_object_rotted[2][0],
                        figure_object_rotted[2][0][3],
                        angle)
                    figure_object_rotted[2][1] = lib.rotting_with_fixed_point(
                        figure_object_rotted[2][1],
                        figure_object_rotted[2][1][3],
                        angle)

                    figure_object = []
                    figure_1 = fig.Left_caps
                    figure_1 = lib.screen_into_cartesian_for_array(figure_1, lib.cts.Origin)
                    figure_object.append(figure_1)

                    figure_2 = fig.Center_caps
                    figure_2 = lib.screen_into_cartesian_for_array(figure_2, lib.cts.Origin)
                    figure_object.append(figure_2)

                    figure_3 = fig.Right_caps
                    figure_3 = lib.screen_into_cartesian_for_array(figure_3, lib.cts.Origin)
                    figure_object.append(figure_3)

                    for stage, section in enumerate(figure_object):
                        for figure_iterated, values in enumerate(figure_object[stage]):
                            figure_object_rotted[stage][figure_iterated] = lib.translation_for_array(
                                figure_object_rotted[stage][figure_iterated],
                                [figure_object[stage][figure_iterated][3][0] - lib.cts.Origin[0],
                                 figure_object[stage][figure_iterated][3][1] - lib.cts.Origin[1]])
                if event.button == 5:
                    angle -= direction
                    for stage, section in enumerate(figure_object):
                        for figure_iterated, values in enumerate(figure_object[stage]):
                            figure_object_rotted[stage][figure_iterated] = lib.translation_for_array(
                                figure_object_rotted[stage][figure_iterated],
                                [lib.cts.Origin[0] - figure_object[stage][figure_iterated][3][0],
                                 lib.cts.Origin[1] - figure_object[stage][figure_iterated][3][1]])

                    figure_object_rotted[rotting][0] = lib.rotting_with_fixed_point(
                        figure_object_rotted[rotting][0],
                        figure_object_rotted[rotting][0][3],
                        angle)

                    figure_object_rotted[rotting][1] = lib.rotting_with_fixed_point(
                        figure_object_rotted[rotting][1],
                        figure_object_rotted[rotting][1][3],
                        angle)

                    figure_object = []
                    figure_1 = fig.Left_caps
                    figure_1 = lib.screen_into_cartesian_for_array(figure_1, lib.cts.Origin)
                    figure_object.append(figure_1)

                    figure_2 = fig.Center_caps
                    figure_2 = lib.screen_into_cartesian_for_array(figure_2, lib.cts.Origin)
                    figure_object.append(figure_2)

                    figure_3 = fig.Right_caps
                    figure_3 = lib.screen_into_cartesian_for_array(figure_3, lib.cts.Origin)
                    figure_object.append(figure_3)

                    for stage, section in enumerate(figure_object):
                        for figure_iterated, values in enumerate(figure_object[stage]):
                            figure_object_rotted[stage][figure_iterated] = lib.translation_for_array(
                                figure_object_rotted[stage][figure_iterated],
                                [figure_object[stage][figure_iterated][3][0] - lib.cts.Origin[0],
                                 figure_object[stage][figure_iterated][3][1] - lib.cts.Origin[1]])

        lib.fill(window)
        lib.cartesian_plane(window)
        lib.point(window, figure_object[0][0][3])
        lib.point(window, figure_object[0][1][3])

        for stage, section in enumerate(figure_object):
            for figure_iterated, values in enumerate(figure_object[stage]):
                lib.polygons_filled(window, figure_object_rotted[stage][figure_iterated], lib.cts.PALETTE_1[stage])
        lib.frames_per_second(fps, 10)
    pg.quit()
