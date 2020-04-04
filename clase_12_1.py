import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    fps = lib.frames_per_second_basics()
    window = lib.new_window("Mandala", lib.cts.size)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass
                if event.button == 3:
                    pass
                if event.button == 4:
                    pass
                if event.button == 5:
                    pass

        lib.frames_per_second(fps, 12)
    pg.quit()
