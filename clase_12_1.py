import pygame as pg
import library as lib


def scal(screen_points, fixed_point, scale_value=None):
    if scale_value is None:
        scale_value = [0.5, 0.5]

    transformation = []
    iterator = 0

    while iterator < len(screen_points):
        transformation.append(lib.translation(screen_points[iterator], [-fixed_point[0], -fixed_point[1]]))
        iterator += 1

    iterator = 0

    while iterator < len(screen_points):
        transformation[iterator] = lib.scale(transformation[iterator], scale_value)
        iterator += 1

    iterator = 0

    while iterator < len(screen_points):
        transformation[iterator] = lib.translation(transformation[iterator], fixed_point)
        iterator += 1

    return transformation[1]


def cruz(figura):  # Debe ser de 4 lados (vector con 4 puntos)
    i = 0
    ls = []
    while i <= 3:
        if i + 1 == 4:
            ls.append(scal([figura[i], figura[0]], figura[i]))
        else:
            ls.append(scal([figura[i], figura[i + 1]], figura[i]))
        i += 1

    return ls


"""
# Transformation: Screen point into cartesian point
for iterator, section in enumerate(Figure_1_rotted):
    for iteration, value in enumerate(Figure_1_rotted[iterator]):
        print Figure_1_rotted[0]
        Figure_1_rotted[iterator][iteration] = lib.screen_into_cartesian(
            Figure_1_rotted[iterator][iteration])
"""

"""
# Transformation: Cartesian point into screen point
for iterator, section in enumerate(Figure_1_rotted):
    for iteration, value in enumerate(Figure_1_rotted[iterator]):
        Figure_1_rotted[iterator][iteration] = lib.cartesian_into_screen(
            Figure_1_rotted[iterator][iteration])
"""

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
    Figure_1_rotted = Figure_1
    Figure_2_rotted = Figure_2
    Figure_3_rotted = Figure_3

    # Transformation: Screen point into cartesian point
    for iterator, section in enumerate(Figure_1_rotted):
        for iteration, value in enumerate(Figure_1_rotted[iterator]):
            Figure_1_rotted[iterator][iteration] = lib.screen_into_cartesian(
                Figure_1_rotted[iterator][iteration], [600, 250])

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                angle += direction
                if event.button == 4:
                    # Rote in X
                    pass

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

        Figure_1_rotted[0] = lib.rotting_with_fixed_point(Figure_1[0], Figure_1[0][0], angle)
        Figure_1_rotted[1] = lib.rotting_with_fixed_point(Figure_1[1], Figure_1[0][0], angle)

        # Drawing issues

        lib.fill(window)
        for iterator, section in enumerate(Figure_1_rotted):
            lib.polygons_filled(window, Figure_1_rotted[iterator], lib.cts.PALETTE_2[iterator])
        lib.frames_per_second(fps, 12)
    pg.quit()
