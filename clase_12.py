import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    window = lib.new_window("Mandala")
    fps = lib.frames_per_second_basics()

    radius = 1000
    direction = 2
    sides = 7
    angle = 2

    figure = lib.regular_figures([radius / sides, radius / sides], sides)
    rotted_figures = []
    lines = []

    for iterator, value in enumerate(figure):
        rotted_figures.append(lib.screen_into_cartesian(figure[iterator]))

    step = 0
    for iterator, value in enumerate(rotted_figures):
        if step >= len(rotted_figures):
            step = 1
        lines.append(rotted_figures[step])
        step += 2

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    sides += 1
                    figure = lib.regular_figures([radius / sides, radius / sides], sides)
                    rotted_figures = []
                    lines = []

                    for iterator, value in enumerate(figure):
                        rotted_figures.append(lib.screen_into_cartesian(figure[iterator]))

                    step = 0
                    for iterator, value in enumerate(rotted_figures):
                        if step >= len(rotted_figures):
                            step = 1
                        lines.append(rotted_figures[step])
                        step += 2
                if event.button == 3:
                    sides -= 1
                    figure = lib.regular_figures([radius / sides, radius / sides], sides)
                    rotted_figures = []
                    lines = []

                    for iterator, value in enumerate(figure):
                        rotted_figures.append(lib.screen_into_cartesian(figure[iterator]))

                    step = 0
                    for iterator, value in enumerate(rotted_figures):
                        if step >= len(rotted_figures):
                            step = 1
                        lines.append(rotted_figures[step])
                        step += 2
                if event.button == 4:
                    direction = 2
                if event.button == 5:
                    direction = -2
            for iterator, value in enumerate(figure):
                rotted_figures[iterator] = lib.cartesian_into_screen(figure[iterator])
                rotted_figures[iterator] = lib.clockwise(figure[iterator], angle)
                rotted_figures[iterator] = lib.screen_into_cartesian(rotted_figures[iterator])
            angle += direction

            step = 0
            for iterator, value in enumerate(rotted_figures):
                if step >= len(rotted_figures):
                    step = 1
                lines[iterator] = rotted_figures[step]
                step += 2

            lib.fill(window)
            lib.polygons(window, rotted_figures, lib.random_color())
            lib.polygons(window, lines, lib.random_color())
        lib.frames_per_second(fps, 12)
    pg.quit()
