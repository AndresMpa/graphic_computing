import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    fps = lib.frames_per_second_basics()
    window = lib.new_window("3D Figure", lib.cts.size)

    # Variables
    direction = 2
    angle = direction

    # Reference axis
    fixed_point = [0, 0]
    fixed_point = lib.screen_into_cartesian(fixed_point)

    # Front & Back
    one_face_1 = [[100, 100], [100, -200], [-100, -200], [-100, 100]]
    one_face_2 = [[100, 100], [100, -200], [-100, -200], [-100, 100]]
    # Sides
    one_face_3 = [[100, 100], [100, 100], [100, -200], [100, -200]]
    one_face_4 = [[-100, -100], [-100, -100], [-100, -200], [-100, -200]]
    # Up & Down
    one_face_5 = [[100, -200], [100, -200], [-100, -200], [-100, -200]]
    one_face_6 = [[100, 100], [100, 100], [-100, 100], [-100, 100]]

    # Big cube
    Figure_1 = [one_face_1, one_face_2, one_face_3, one_face_4, one_face_5, one_face_6]
    Figure_1_rotted = Figure_1
    print Figure_1_rotted

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                # Transformation: Cartesian point into screen point
                for iterator, section in enumerate(Figure_1_rotted):
                    for iteration, value in enumerate(Figure_1_rotted[iterator]):
                        Figure_1_rotted[iterator][iteration] = lib.cartesian_into_screen(
                            Figure_1_rotted[iterator][iteration])
                if event.button == 1:
                    # Change angle to positive direction
                    direction = 1
                if event.button == 3:
                    # Change angle to negative direction
                    direction = -1
                if event.button == 4:
                    # Rote in X
                    angle += direction

                    for iterator, section in enumerate(Figure_1_rotted):
                        Figure_1_rotted[iterator] = lib.rotting_with_fixed_point(
                            Figure_1_rotted[iterator], fixed_point, angle)
                if event.button == 5:
                    # Rote in Y
                    pass

        # Transformation: Screen point into cartesian point
        for iterator, section in enumerate(Figure_1_rotted):
            for iteration, value in enumerate(Figure_1_rotted[iterator]):
                Figure_1_rotted[iterator][iteration] = lib.screen_into_cartesian(Figure_1_rotted[iterator][iteration])

        # Drawing issues
        for iterator, section in enumerate(Figure_1_rotted):
            lib.polygons(window, Figure_1_rotted[iterator])

        lib.frames_per_second(fps, 12)
    pg.quit()
