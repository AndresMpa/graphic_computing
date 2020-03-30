import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    sides = 2
    angle = 500
    rotted = angle
    direction = -10

    fps = lib.frames_per_second_basics()
    window = lib.new_window("3D figures rotting (Using a circle)")
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    sides += 1
                if event.button == 3:
                    sides -= 1
                if event.button == 4:
                    rotted += direction
                if event.button == 5:
                    rotted -= direction
            figure_1 = lib.regular_figures([rotted / sides, angle / sides], sides)
            figure_2 = lib.regular_figures([rotted / sides, angle / sides], sides)

            if rotted == -angle:
                direction = 10
            elif rotted == angle:
                direction = -10

            lib.fill(window)

            for iterator, value in enumerate(figure_1):
                figure_1[iterator] = lib.screen_into_cartesian(figure_1[iterator])
                figure_2[iterator] = lib.screen_into_cartesian(figure_2[iterator], lib.cts.Default)

            lines = lib.lines_in_figures(figure_1, figure_2)
            lib.polygons(window, figure_1, lib.random_color())
            lib.polygons(window, figure_2, lib.random_color())
            for iterator, value in enumerate(lines):
                lib.polygons(window, lines[iterator], lib.random_color())

        fps.tick(5)
        lib.flip()
    pg.quit()
