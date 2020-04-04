import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    figure = []
    sides = 2
    angle = 1000
    rotted = angle
    fps = lib.frames_per_second_basics()
    window = lib.new_window("Equilateral triangle")
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                lib.fill(window)
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 4:
                    sides += 1
                if event.button == 5:
                    sides -= 1
                    if sides < 2:
                        sides = 2
                figure = lib.regular_figures([rotted / sides, angle / sides], sides)
                if rotted <= angle:
                    rotted -= 1
                elif rotted > angle:
                    rotted = 0

                for iterator, value in enumerate(figure):
                    figure[iterator] = lib.screen_into_cartesian(figure[iterator])
                lib.polygons(window, figure, lib.random_color())
        lib.frames_per_second(fps)
        lib.flip()
    pg.quit()
