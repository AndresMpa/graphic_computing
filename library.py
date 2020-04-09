import math as mt
import random as rd
import pygame as pg
import constants as cts


# Screen topics

def new_window(title="Title", size=None):
    if size is None:
        size = [cts.width, cts.height]
    pg.display.set_caption(title)
    return pg.display.set_mode(size)


def flip():
    pg.display.flip()


def fill(window, color=cts.BLACK):
    window.fill(color)


def fill_and_flip(window, color=cts.BLACK):
    window.fill(color)
    pg.display.flip()


def frames_per_second_basics():
    return pg.time.Clock()


def frames_per_second(clock, options=2, frames=60):
    if options == 0:
        clock.tick(frames)
    elif options == 1:
        clock.tick(30)
    elif options == 2:
        clock.tick(60)
    elif options == 3:
        clock.tick(120)
    elif options == 4:
        clock.tick(244)
    elif options == 5:
        clock.tick(420)
    elif options == 6:
        clock.tick(620)
    elif options == 7:
        clock.tick(980)
    elif options == 8:
        clock.tick(1080)
    elif options == 9:
        clock.tick(1200)
    elif options == 10:
        clock.tick(1500)
    flip()


def create_color(r=255, g=255, b=255):
    return pg.Color(r, g, b)


def random_color():
    r = int(rd.randint(0, 255))
    g = int(rd.randint(0, 255))
    b = int(rd.randint(0, 255))
    return create_color(r, g, b)


def write(txt, screen, coord, selected_font=1):
    font_1 = pg.font.SysFont("Alba super", 150)
    font_2 = pg.font.SysFont("04b, 30", 50)
    if selected_font == 1:
        write_text = font_1.render(txt, 0, random_color())
        screen.blit(write_text, coord)
    if selected_font == 2:
        write_text = font_2.render(txt, 0, random_color())
        screen.blit(write_text, coord)


def bubble(vector, pos=1):
    for iterator in range(len(vector)):
        for iteration in range(iterator):
            if vector[iteration][pos] > vector[iteration + 1][pos]:
                aux = vector[iteration]
                vector[iteration] = vector[iteration + 1]
                vector[iteration + 1] = aux
    return vector


# Basic figures

def point(window, coord, color=cts.WHITE, size=5):
    pg.draw.circle(window, color, coord, size)


def line(window, coord_start, coord_end, color=cts.WHITE, size=3):
    pg.draw.line(window, color, coord_start, coord_end, size)


def triangle(window, axe_1, axe_2, axe_3, color=cts.WHITE, size=3):
    pg.draw.lines(window, color, axe_1, [axe_2, axe_3], size)


def more_figures(window, axe_1, axes, color=cts.WHITE, size=3):
    pg.draw.lines(window, axe_1, axes, color, size)


def polygons(window, points, color=cts.WHITE, size=3):
    pg.draw.polygon(window, color, points, size)


def polygons_filled(window, points, color=cts.WHITE):
    pg.draw.polygon(window, color, points)


# 3D figures

def solids(window, figure, color):
    for iterator, value in enumerate(figure):
        if iterator + 1 < len(figure):
            line(window, figure[iterator], figure[iterator + 1], color, 5)


def lines_in_figures(figure_origin, figure_destine):
    lines = []
    for iterator, value in enumerate(figure_origin):
        lines.append([figure_origin[iterator], figure_destine[iterator]])
    return lines


# Vectors

def random_position():
    x = rd.randrange(0, (cts.width - 35))
    y = rd.randrange(0, (cts.height - 35))
    return [x, y]


def vectors(window, pos_start, pos_end, color=cts.WHITE, size=5):
    point(window, pos_start, color, 10)
    line(window, pos_start, pos_end, color, size)
    point(window, pos_end, color, 10)


def vector_sum(vector_a, vector_b):
    return [(vector_a[0] + vector_b[0]), (vector_a[1] + vector_b[1])]


def counterclockwise(vector, angle):
    """
    x = xcos(&) + ysen(&)
    y = -xsen(&) + ycos(&)
    """
    angle = mt.radians(angle)
    comp_x = vector[0] * mt.cos(angle) + vector[1] * mt.sin(angle)
    comp_y = -vector[0] * mt.sin(angle) + vector[1] * mt.cos(angle)
    return [int(comp_x), int(comp_y)]


def clockwise(vector, angle):
    """
    x = xcos(&) - ysen(&)
    y = xsen(&) + ycos(&)
    """
    angle = mt.radians(angle)
    comp_x = vector[0] * mt.cos(angle) - vector[1] * mt.sin(angle)
    comp_y = vector[0] * mt.sin(angle) + vector[1] * mt.cos(angle)
    return [int(comp_x), int(comp_y)]


# Planes

def cartesian_plane(window, origin=cts.Origin, limits=None, color=cts.WHITE, size=3):
    if limits is None:
        limits = [cts.width, cts.height]
    pg.draw.line(window, color, [origin[0], 0], [origin[0], limits[1]], size)
    pg.draw.line(window, color, [0, origin[1]], [limits[0], origin[1]], size)


# Transformations

def screen_into_cartesian(screen_point, origin=None):
    if origin is None:
        origin = [cts.Origin[0], cts.Origin[1]]
    cartesian_x = screen_point[0] + origin[0]
    cartesian_y = -screen_point[1] + origin[1]

    return [cartesian_x, cartesian_y]


def screen_into_cartesian_for_array(screen_point, origin=None):
    if origin is None:
        origin = [cts.Origin[0], cts.Origin[1]]
    for iterator, section in enumerate(screen_point):
        for iteration, value in enumerate(screen_point[iterator]):
            screen_point[iterator][iteration] = screen_into_cartesian(
                screen_point[iterator][iteration], origin)


def cartesian_into_screen(screen_point, cartesian_point=None):
    if cartesian_point is None:
        cartesian_point = [cts.Origin[0], cts.Origin[1]]
    screen_x = screen_point[0] - cartesian_point[0]
    screen_y = -screen_point[1] + cartesian_point[1]

    return [screen_x, screen_y]


def cartesian_into_screen_for_array(screen_points, cartesian_point=None):
    if cartesian_point is None:
        cartesian_point = [cts.Origin[0], cts.Origin[1]]
    for iterator, section in enumerate(screen_points):
        for iteration, value in enumerate(screen_points[iterator]):
            screen_points[iterator][iteration] = cartesian_into_screen(
                screen_points[iterator][iteration], cartesian_point)


def cartesian_into_polar(cartesian_point):
    angle = mt.atan2(cartesian_point[1], cartesian_point[0])
    radius = mt.sqrt(mt.pow(cartesian_point[0], 2) + mt.pow(cartesian_point[1], 2))

    return [radius, angle]


def polar_into_cartesian(radius, angle):
    angle = mt.radians(angle)
    pos_x = radius * mt.cos(angle)
    pos_y = radius * mt.sin(angle)

    return [int(pos_x), int(pos_y)]


def scale(scalable_point, scale_value=None):
    if scale_value is None:
        scale_value = [2, 2]
    scale_x = int(scalable_point[0] * scale_value[0])
    scale_y = int(scalable_point[1] * scale_value[1])

    return [scale_x, scale_y]


def translation(screen_point, transformation):
    """
    :param screen_point: x, y
    :param transformation: tx, ty
    :return: [x + tx, y + ty]
    """
    translated = [screen_point[0] + transformation[0], screen_point[1] + transformation[1]]
    return translated


"""
It work with an array of positions
"""


def scaling_with_fixed_point(screen_points, fixed_point, scale_value=None):
    if scale_value is None:
        scale_value = [2, 2]

    transformation = []
    iterator = 0

    while iterator < len(screen_points):
        transformation.append(translation(screen_points[iterator], [-fixed_point[0], -fixed_point[1]]))
        iterator += 1

    iterator = 0

    while iterator < len(screen_points):
        transformation[iterator] = scale(transformation[iterator], scale_value)
        iterator += 1

    iterator = 0

    while iterator < len(screen_points):
        transformation[iterator] = translation(transformation[iterator], fixed_point)
        iterator += 1

    return transformation


"""
It work with an array of positions
"""


def rotting_with_fixed_point(screen_points, fixed_point, rotting_angle=5):
    transformation = []
    iterator = 0

    while iterator < len(screen_points):
        transformation.append(translation(screen_points[iterator], [-fixed_point[0], -fixed_point[1]]))
        iterator += 1

    iterator = 0

    while iterator < len(screen_points):
        transformation[iterator] = clockwise(transformation[iterator], rotting_angle)
        iterator += 1

    iterator = 0

    while iterator < len(screen_points):
        transformation[iterator] = translation(transformation[iterator], fixed_point)
        iterator += 1

    return transformation


def regular_figures(radius, sides):
    figures = []
    figure_angle = 360 / sides
    current_angle = 0
    while len(figures) < sides:
        figures.append(clockwise(radius, current_angle))
        current_angle += figure_angle
    return figures


# Polars

def archimedean_spiral(angle, amplitude=1):
    radius = amplitude * angle
    return int(radius) / 10


def roses(amplitude, petals, angle):
    radius = amplitude * mt.cos(petals * mt.radians(angle))
    return int(radius)


def cardioid(amplitude, angle, position=1, resize=200):
    radius = 0
    angle = mt.radians(angle)
    if position == 1:
        radius = amplitude + mt.cos(angle)
    if position == 2:
        radius = amplitude - mt.cos(angle)
    if position == 3:
        radius = amplitude + mt.sin(angle)
    if position == 4:
        radius = amplitude - mt.sin(angle)
    return int(radius * resize)


def lemiscata(amplitude, angle, position=1, resize=200):
    radius = 0
    angle = mt.radians(angle)
    if position == 1:
        radius = mt.sqrt((amplitude * amplitude) * (mt.cos(angle) * mt.cos(angle)))
    if position == 2:
        radius = mt.sqrt((-amplitude * amplitude) * (mt.cos(angle) * mt.cos(angle)))
    if position == 3:
        radius = mt.sqrt((amplitude * amplitude) * (mt.sin(angle) * mt.sin(angle)))
    if position == 4:
        radius = mt.sqrt((-amplitude * amplitude) * (mt.sin(angle) * mt.sin(angle)))
    return int(radius * resize)


# Animations

def line_origin(origin, number_of_lines=0):
    interval_angle = 180 / number_of_lines
    num_of_lines = 0
    line_angle = 0
    lines = []
    while num_of_lines <= number_of_lines:
        lines.append(counterclockwise(origin, line_angle))
        lines.append(clockwise(origin, line_angle))
        line_angle += interval_angle
        num_of_lines += 1
    return lines


class Ball:
    def __init__(self, starting_restriction, ending_restriction, angle):
        self.direction = [-1, 1]
        self.__interval__ = [starting_restriction, ending_restriction]
        self.pos_x = self.__interval__[0][0]
        self.pos_y = self.__interval__[0][1]
        self.angle = angle
        self.moving_coord = [self.pos_x, self.pos_y]
        self.moving_direction = self.direction

    def __moving_(self):
        if self.pos_x > self.__interval__[0][0]:
            self.moving_direction[0] = -1
        elif self.pos_x < self.__interval__[1][0]:
            self.moving_direction[0] = 1

        if self.pos_y < self.__interval__[0][1]:
            self.moving_direction[1] = 1
        elif self.pos_y > self.__interval__[1][1]:
            self.moving_direction[1] = -1

        self.pos_x += self.moving_direction[0]
        self.pos_y += self.moving_direction[1]

        self.moving_coord = clockwise([self.pos_x, self.pos_y], self.angle)

    def movement(self, window, color=cts.WHITE, size=5):
        self.__moving_()
        print self.moving_coord
        point(window, self.moving_coord, color, size)
