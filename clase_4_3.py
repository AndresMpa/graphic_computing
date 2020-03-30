import pygame as pg
import library as lib


def helpers():
    # Iteration issues
    color = 0
    starting_line_positions = 0
    ending_line_positions = len(lines) - 1
    while starting_line_positions < len(lines):
        # Transformations
        start_line = lib.screen_into_cartesian(lines[starting_line_positions], origin)
        end_line = lib.screen_into_cartesian(lines[ending_line_positions], origin)

        # Drawing issues
        lib.point(window, start_line, lib.cts.PALETTE[color], 1)
        lib.line(window, start_line, end_line, lib.cts.PALETTE[color], 1)

        # Iterating modifications
        starting_line_positions += 1
        ending_line_positions -= 1
        if color >= len(lib.cts.PALETTE) - 1:
            color = 0
        else:
            color += 1


def fill_balls(help_lines):
    starting = 0
    ending = len(lines) - 1
    number_of_balls = ((len(lines)) / 2) - 1
    angle_line = 180 / number_of_balls
    ball_angles = 0
    while starting < number_of_balls:
        balls.append(lib.Ball(lib.screen_into_cartesian(help_lines[starting]),
                              lib.screen_into_cartesian(help_lines[ending]),
                              ball_angles))
        ball_angles += angle_line
        starting += 1
        ending -= 1


def balls_moving(balls_disc):
    iterator = 0
    while iterator <= len(balls) - 1:
        balls_disc[iterator].movement(window, lib.random_color())
        iterator += 1


if __name__ == '__main__':

    pg.init()
    run = True

    # Origin by default
    origin = lib.cts.Origin
    lines = lib.line_origin(lib.cts.H, 4)

    # Balls issues
    balls = []
    fill_balls(lines)

    # Clock
    fps = lib.frames_per_second_basics()

    # Window
    window = lib.new_window("Animation - Balls rotting")

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        lib.fill(window, lib.cts.BLACK)

        helpers()
        balls_moving(balls)

        lib.frames_per_second(fps, 10)
        lib.flip()
    pg.quit()
