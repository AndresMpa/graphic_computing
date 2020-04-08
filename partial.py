import pygame as pg
import figure as fig
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    fps = lib.frames_per_second_basics()
    window = lib.new_window("3D Figure", lib.cts.size)
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        lib.frames_per_second(fps, 12)
    pg.quit()
