import pygame as pg

# Window size
width = 1200
height = 600

# Points
Default = [800, 200]
Origin = [600, 300]
size = [500, 200]
A = [-50, -100]
B = [-100, 50]
C = [100, 100]
D = [50, -100]
E = [700, 150]
F = [900, 180]
G = [50, 100]
H = [850, 30]

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
# COLOR PALETTE DEFAULT
PALETTE = [RED, GREEN, BLUE, HIGH, MIDDLE, LOW, WHITE]
# COLOR PALETTE #1
PALETTE_1 = [WHITE, GREEN, BLUE]
# COLOR PALETTE #2
PALETTE_2 = [RED, RED, GREEN, GREEN, BLUE, BLUE]

# Images

Angel = [
    [pg.image.load("Images/Angel/e1.png"),
     pg.image.load("Images/Angel/e2.png"),
     pg.image.load("Images/Angel/e3.png")],
    [pg.image.load("Images/Angel/n1.png"),
     pg.image.load("Images/Angel/n2.png"),
     pg.image.load("Images/Angel/n3.png")],
    [pg.image.load("Images/Angel/o1.png"),
     pg.image.load("Images/Angel/o2.png"),
     pg.image.load("Images/Angel/o3.png")],
    [pg.image.load("Images/Angel/s1.png"),
     pg.image.load("Images/Angel/s2.png"),
     pg.image.load("Images/Angel/s3.png")],
    [pg.image.load("Images/Angel/t1.png"),
     pg.image.load("Images/Angel/t2.png"),
     pg.image.load("Images/Angel/t3.png")],
    pg.image.load("Images/Angel/t.png")]

Escanor = [
    [pg.image.load("Images/Escanor/e1.png"),
     pg.image.load("Images/Escanor/e2.png"),
     pg.image.load("Images/Escanor/e3.png")],
    [pg.image.load("Images/Escanor/n1.png"),
     pg.image.load("Images/Escanor/n2.png"),
     pg.image.load("Images/Escanor/n3.png")],
    [pg.image.load("Images/Escanor/o1.png"),
     pg.image.load("Images/Escanor/o2.png"),
     pg.image.load("Images/Escanor/o3.png")],
    [pg.image.load("Images/Escanor/s1.png"),
     pg.image.load("Images/Escanor/s2.png"),
     pg.image.load("Images/Escanor/s3.png")],
    [pg.image.load("Images/Escanor/t1.png"),
     pg.image.load("Images/Escanor/t2.png"),
     pg.image.load("Images/Escanor/t3.png")],
    pg.image.load("Images/Escanor/t.png")]

Luke = [
    [pg.image.load("Images/Luke/e1.png"),
     pg.image.load("Images/Luke/e2.png"),
     pg.image.load("Images/Luke/e3.png")],
    [pg.image.load("Images/Luke/n1.png"),
     pg.image.load("Images/Luke/n2.png"),
     pg.image.load("Images/Luke/n3.png")],
    [pg.image.load("Images/Luke/o1.png"),
     pg.image.load("Images/Luke/o2.png"),
     pg.image.load("Images/Luke/o3.png")],
    [pg.image.load("Images/Luke/s1.png"),
     pg.image.load("Images/Luke/s2.png"),
     pg.image.load("Images/Luke/s3.png")],
    [pg.image.load("Images/Luke/t1.png"),
     pg.image.load("Images/Luke/t2.png"),
     pg.image.load("Images/Luke/t3.png")],
    pg.image.load("Images/Luke/t.png")]

Serafin = [
    [pg.image.load("Images/Serafin/e1.png"),
     pg.image.load("Images/Serafin/e2.png"),
     pg.image.load("Images/Serafin/e3.png")],
    [pg.image.load("Images/Serafin/n1.png"),
     pg.image.load("Images/Serafin/n2.png"),
     pg.image.load("Images/Serafin/n3.png")],
    [pg.image.load("Images/Serafin/o1.png"),
     pg.image.load("Images/Serafin/o2.png"),
     pg.image.load("Images/Serafin/o3.png")],
    [pg.image.load("Images/Serafin/s1.png"),
     pg.image.load("Images/Serafin/s2.png"),
     pg.image.load("Images/Serafin/s3.png")],
    [pg.image.load("Images/Serafin/t1.png"),
     pg.image.load("Images/Serafin/t2.png"),
     pg.image.load("Images/Serafin/t3.png")],
    pg.image.load("Images/Serafin/t.png")]

Sofia = [
    [pg.image.load("Images/Sofia/e1.png"),
     pg.image.load("Images/Sofia/e2.png"),
     pg.image.load("Images/Sofia/e3.png")],
    [pg.image.load("Images/Sofia/n1.png"),
     pg.image.load("Images/Sofia/n2.png"),
     pg.image.load("Images/Sofia/n3.png")],
    [pg.image.load("Images/Sofia/o1.png"),
     pg.image.load("Images/Sofia/o2.png"),
     pg.image.load("Images/Sofia/o3.png")],
    [pg.image.load("Images/Sofia/s1.png"),
     pg.image.load("Images/Sofia/s2.png"),
     pg.image.load("Images/Sofia/s3.png")],
    [pg.image.load("Images/Sofia/t1.png"),
     pg.image.load("Images/Sofia/t2.png"),
     pg.image.load("Images/Sofia/t3.png")],
    pg.image.load("Images/Sofia/t.png")]

Sonia = [
    [pg.image.load("Images/Sonia/e1.png"),
     pg.image.load("Images/Sonia/e2.png"),
     pg.image.load("Images/Sonia/e3.png")],
    [pg.image.load("Images/Sonia/n1.png"),
     pg.image.load("Images/Sonia/n2.png"),
     pg.image.load("Images/Sonia/n3.png")],
    [pg.image.load("Images/Sonia/o1.png"),
     pg.image.load("Images/Sonia/o2.png"),
     pg.image.load("Images/Sonia/o3.png")],
    [pg.image.load("Images/Sonia/s1.png"),
     pg.image.load("Images/Sonia/s2.png"),
     pg.image.load("Images/Sonia/s3.png")],
    [pg.image.load("Images/Sonia/t1.png"),
     pg.image.load("Images/Sonia/t2.png"),
     pg.image.load("Images/Sonia/t3.png")],
    pg.image.load("Images/Sonia/t.png")]

Taun = [
    [pg.image.load("Images/Taun/e1.png"),
     pg.image.load("Images/Taun/e2.png"),
     pg.image.load("Images/Taun/e3.png")],
    [pg.image.load("Images/Taun/n1.png"),
     pg.image.load("Images/Taun/n2.png"),
     pg.image.load("Images/Taun/n3.png")],
    [pg.image.load("Images/Taun/o1.png"),
     pg.image.load("Images/Taun/o2.png"),
     pg.image.load("Images/Taun/o3.png")],
    [pg.image.load("Images/Taun/s1.png"),
     pg.image.load("Images/Taun/s2.png"),
     pg.image.load("Images/Taun/s3.png")],
    [pg.image.load("Images/Taun/t1.png"),
     pg.image.load("Images/Taun/t2.png"),
     pg.image.load("Images/Taun/t3.png")],
    pg.image.load("Images/Taun/t.png")]

Xerath = [
    [pg.image.load("Images/Xerath/e1.png"),
     pg.image.load("Images/Xerath/e2.png"),
     pg.image.load("Images/Xerath/e3.png")],
    [pg.image.load("Images/Xerath/n1.png"),
     pg.image.load("Images/Xerath/n2.png"),
     pg.image.load("Images/Xerath/n3.png")],
    [pg.image.load("Images/Xerath/o1.png"),
     pg.image.load("Images/Xerath/o2.png"),
     pg.image.load("Images/Xerath/o3.png")],
    [pg.image.load("Images/Xerath/s1.png"),
     pg.image.load("Images/Xerath/s2.png"),
     pg.image.load("Images/Xerath/s3.png")],
    [pg.image.load("Images/Xerath/t1.png"),
     pg.image.load("Images/Xerath/t2.png"),
     pg.image.load("Images/Xerath/t3.png")],
    pg.image.load("Images/Xerath/t.png")]

Snake = pg.image.load("Images/snaky.png")

Ship = pg.image.load("Images/ship.png")

Invaders = [pg.image.load("Images/1.png"),
            pg.image.load("Images/2.png"),
            pg.image.load("Images/3.png"),
            pg.image.load("Images/mother.png")]

Invader_Shots = pg.image.load("Images/invader_shot.png")
Player_Shots = pg.image.load("Images/shot.png")

background = pg.image.load("Images/f_1.png")

Tree = pg.image.load("Images/tree.png")

# Texts

euphoria = "Euphoria"

euphoria_intro = ["Once upon a time, a lost continent; where",
                  "people around the big castle of Esfitia",
                  "used to live placefully like farmers,",
                  "warrior, markers and other Professions",
                  "",
                  "",
                  "One day, everyone near to the castle",
                  "saw a weird coming darkness the",
                  "the king, got worry about that",
                  "so, sent different ships to face",
                  "them...",
                  "",
                  "",
                  "Those ship never come back...",
                  "",
                  "",
                  "The cataclysm have just started",
                  "",
                  "",
                  "",
                  "", ]

skip = "Click to skip"
