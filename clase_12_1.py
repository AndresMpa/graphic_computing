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

    # Front & Back

    # Figure one
    BigCube_Front = [[200, 200], [200, -400], [-200, -400], [-200, 200]]
    BigCube_Back = [[200, 200], [200, -400], [-200, -400], [-200, 200]]

    # Figure two
    FaceFront_Right = [[400, 200], [400, -100], [200, -100], [200, 200]]
    FaceBack_Right = [[400, 200], [400, -100], [200, -100], [200, 200]]

    # Figure three
    FaceFront_Left = [[-200, 200], [-200, -100], [-400, -100], [-400, 200]]
    FaceBack_Left = [[-200, 200], [-200, -100], [-400, -100], [-400, 200]]

    # Sides

    # Figure one
    BigCube_Right = [[200, 200], [200, -400], [200, -400], [200, 200]]
    BigCube_Left = [[-200, 200], [-200, -400], [-200, -400], [-200, 200]]

    # Figure two
    FaceRight_Right = [[400, 200], [400, -100], [400, -100], [400, 200]]
    FaceLeft_Right = [[200, 200], [200, -100], [200, -100], [200, 200]]

    # Figure three
    FaceRight_Left = [[-200, 200], [-200, -100], [-200, -100], [-200, 200]]
    FaceLeft_Left = [[-400, 200], [-400, -100], [-400, -100], [-400, 200]]

    # Up & Down

    # Figure one
    BigCube_Up = [[200, -400], [-200, -400], [-200, -400], [200, -400]]
    BigCube_Down = [[200, 200], [-200, 200], [-200, 200], [200, 200]]

    # Figure two
    FacetUp_Right = [[400, -100], [200, -100], [200, -100], [400, -100]]
    FaceDown_Right = [[400, 200], [200, 200], [200, 200], [400, 200]]

    # Figure three
    FaceUp_Left = [[-200, -100], [-400, -100], [-400, -100], [-200, -100]]
    FaceDown_Left = [[-200, 200], [400, 200], [-400, 200], [-200, 200]]

    # Big cube
    Figure_1 = [BigCube_Front, BigCube_Back, BigCube_Right, BigCube_Left, BigCube_Up, BigCube_Down]

    # Small right
    Figure_2 = [FaceFront_Right, FaceBack_Right, FaceRight_Right, FaceLeft_Right, FacetUp_Right, FaceDown_Right]

    # Small left
    Figure_3 = [FaceFront_Left, FaceBack_Left, FaceRight_Left, FaceLeft_Left, FaceUp_Left, FaceDown_Left]

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
                if event.button == 1:
                    # Change angle to positive direction
                    direction = direction_value
                if event.button == 3:
                    # Change angle to negative direction
                    direction = -direction_value
                if event.button == 4:
                    # Rote in X
                    Fixed_for_big_cube = cruz(Figure_1_rotted[0])
                    angle += direction
                    Figure_1_rotted[0] = lib.rotting_with_fixed_point(Figure_1[0], Fixed_for_big_cube[0], angle)
                    Figure_1_rotted[1] = lib.rotting_with_fixed_point(Figure_1[1], Fixed_for_big_cube[0], angle)

                    print Figure_1_rotted[0]

                if event.button == 5:
                    # Rote in Y
                    pass

        # Drawing issues

        lib.fill(window)
        lib.polygons_filled(window, Figure_1_rotted[0], lib.cts.RED)
        lib.polygons_filled(window, Figure_1_rotted[1], lib.cts.WHITE)
        lib.polygons_filled(window, Figure_1_rotted[2], lib.cts.GREEN)
        lib.polygons_filled(window, Figure_1_rotted[3], lib.cts.GREEN)
        lib.polygons_filled(window, Figure_1_rotted[4], lib.cts.WHITE)
        lib.polygons_filled(window, Figure_1_rotted[5], lib.cts.WHITE)

        lib.frames_per_second(fps, 12)
    pg.quit()
