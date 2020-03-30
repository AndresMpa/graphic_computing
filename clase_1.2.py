import pygame as pg
import random as rm

pg.init()
run = True
points = []
red = pg.Color(255, 0, 0)
green = pg.Color(0, 255, 0)
blue = pg.Color(0, 0, 255)
white = pg.Color(255, 255, 255)


def color_rm():
    x = rm.randint(0, 3)
    color_picked = [red, green, blue, white]
    return color_picked[x]


def size_rm():
    size = rm.randint(5, 100)
    return size


window = pg.display.set_mode((800, 600))
pg.display.set_caption("Lines by clicks")

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            points.append(pg.mouse.get_pos())
            if len(points) == 2:
                pg.draw.line(window, color_rm(), points[0], points[1], size_rm())
                points.pop()
                points.pop()
        pg.display.flip()
pg.quit()
