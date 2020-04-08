import pygame as pg
import library as lib
import objects as obj

if __name__ == '__main__':
    pg.init()
    run = True
    window = lib.new_window("Figure", lib.cts.size)
    fps = lib.frames_per_second_basics()

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        lib.frames_per_second(fps, 12)
    pg.quit()
