import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    run = True
    angle = 0
    amplitude = 1
    fps = lib.frames_per_second_basics()
    window = lib.new_window("Lemiscata")
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                amplitude += 1
                angle = 0
                lib.fill(window)
            lib.point(window, lib.screen_into_cartesian(lib.polar_into_cartesian(
                lib.lemiscata(amplitude, angle), angle)), lib.random_color())
            angle += 1
        fps.tick(1080)
        lib.flip()
    pg.quit()
