import pygame as pg

# Window size
width = 1200
height = 600

# Points
Origin = [600, 300]
Default = [800, 200]
size = [1200, 600]
A = [50, 100]
B = [-100, 50]
C = [-50, -100]
D = [50, -100]
E = [700, 150]
F = [850, 30]
G = [900, 180]
H = [100, 100]

# Color
# RGB
RED = pg.Color(255, 0, 0)
GREEN = pg.Color(0, 255, 0)
BLUE = pg.Color(0, 0, 255)
# BASICS
HIGH = pg.Color(200, 200, 200)
MIDDLE = pg.Color(155, 155, 155)
LOW = pg.Color(55, 55, 55)
# ELEMENTARY
BLACK = pg.Color(0, 0, 0)
WHITE = pg.Color(255, 255, 255)
# COLOR PALETTE #1
PALETTE = [RED, GREEN, BLUE, HIGH, MIDDLE, LOW, WHITE]
# COLOR PALETTE #2
PALETTE_2 = [RED, RED, GREEN, GREEN, BLUE, BLUE]

# Images

Luke = [
    [pg.image.load("Luke/e1.png"),
     pg.image.load("Luke/e2.png"),
     pg.image.load("Luke/e3.png")],
    [pg.image.load("Luke/n1.png"),
     pg.image.load("Luke/n2.png"),
     pg.image.load("Luke/n3.png")],
    [pg.image.load("Luke/o1.png"),
     pg.image.load("Luke/o2.png"),
     pg.image.load("Luke/o3.png")],
    [pg.image.load("Luke/s1.png"),
     pg.image.load("Luke/s2.png"),
     pg.image.load("Luke/s3.png")],
    [pg.image.load("Luke/t1.png"),
     pg.image.load("Luke/t2.png"),
     pg.image.load("Luke/t3.png")],
    pg.image.load("Luke/t.png")]

Snake = pg.image.load("1.png")
