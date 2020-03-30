import pygame as pg


def lines(d_window, color, start_pos, end_pos, l_with=5):
    pg.draw.line(d_window, color, start_pos, end_pos, l_with)


def circles(d_window, color, pos, radius=5):
    pg.draw.circle(d_window, color, pos, radius)


pg.init()
run = True
white = pg.Color(255, 255, 255)
yellow = pg.Color(235, 230, 50)
black_green = pg.Color(90, 50, 30)
window = pg.display.set_mode((800, 600))
pg.display.set_caption("Window")

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            lines(window, white, (0, 0), pg.mouse.get_pos(), 20)
            lines(window, black_green, (800, 600), pg.mouse.get_pos(), 20)
            circles(window, yellow, pg.mouse.get_pos(), 20)
        pg.display.flip()
pg.quit()
