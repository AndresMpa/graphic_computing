import pygame as pg
import figure as fig
import library as lib


def cross(figure):  # Debe ser de 4 lados (vector con 4 puntos)
    cont = 0
    cross_array = []
    while cont <= 3:
        if cont + 1 == 4:
            point = lib.scaling_with_fixed_point([figure[cont], figure[0]], figure[cont], [0.5, 0.5])
            cross_array.append(point[1])
        else:
            point = lib.scaling_with_fixed_point([figure[cont], figure[cont + 1]], figure[cont], [0.5, 0.5])
            cross_array.append(point[1])
        cont += 1

    return cross_array


if __name__ == '__main__':
    pg.init()
    run = True
    fps = lib.frames_per_second_basics()
    window = lib.new_window("3D Figure", lib.cts.size)

    # Variables
    direction_value = 5
    direction = direction_value
    angle = direction

    # Reference axis
    fixed_point = [0, 0]
    fixed_point = lib.screen_into_cartesian(fixed_point)

    # Rotted figures
    Figure_1 = fig.Figure_1
    Figure_2 = fig.Figure_2
    Figure_3 = fig.Figure_3

    # Transformation: Screen point into cartesian point
    for stage_1, section in enumerate(Figure_1):
        for iteration, value in enumerate(Figure_1[stage_1]):
            Figure_1[stage_1][iteration] = lib.screen_into_cartesian(
                Figure_1[stage_1][iteration], [600, 250])

    for stage_2, section in enumerate(Figure_2):
        for iteration, value in enumerate(Figure_2[stage_2]):
            Figure_2[stage_2][iteration] = lib.screen_into_cartesian(
                Figure_2[stage_2][iteration], [600, 250])

    for stage_3, section in enumerate(Figure_3):
        for iteration, value in enumerate(Figure_3[stage_3]):
            Figure_3[stage_3][iteration] = lib.screen_into_cartesian(
                Figure_3[stage_3][iteration], [600, 250])

    Figure_1_rotted = Figure_1
    Figure_2_rotted = Figure_2
    Figure_3_rotted = Figure_3

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                angle += direction
                rotting_assistant = []
                if event.button == 4:
                    # Rote in X
                    for stage_1, value in enumerate(Figure_1_rotted):
                        rotting_assistant.append(lib.rotting_with_fixed_point(
                            Figure_1[stage_1], Figure_1[0][0], angle))

                    Figure_1_rotted = rotting_assistant
                    rotting_assistant = []

                    for stage_2, value in enumerate(Figure_2_rotted):
                        rotting_assistant.append(lib.rotting_with_fixed_point(
                            Figure_2[stage_2], Figure_2[0][0], angle))

                    Figure_2_rotted = rotting_assistant
                    rotting_assistant = []

                    for stage_3, value in enumerate(Figure_3_rotted):
                        rotting_assistant.append(lib.rotting_with_fixed_point(
                            Figure_3[stage_3], Figure_3[0][0], angle))

                    Figure_3_rotted = rotting_assistant
                    rotting_assistant = []

                if event.button == 5:
                    # Rote in Y
                    pass

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    # Change angle to positive direction
                    direction = direction_value
                if event.key == pg.K_s:
                    # Change angle to negative direction
                    direction = -direction_value
                if event.key == pg.K_k:
                    # Scale the figure
                    pass

        # Drawing issues

        lib.fill(window)
        for stage_1, section in enumerate(Figure_1_rotted):
            lib.polygons_filled(window, Figure_1_rotted[stage_1], lib.cts.PALETTE_2[stage_1])
        for stage_2, section in enumerate(Figure_2_rotted):
            lib.polygons_filled(window, Figure_2_rotted[stage_2], lib.cts.PALETTE_2[stage_2])
        for stage_3, section in enumerate(Figure_3_rotted):
            lib.polygons_filled(window, Figure_3_rotted[stage_3], lib.cts.PALETTE_2[stage_3])
        lib.frames_per_second(fps, 12)
    pg.quit()