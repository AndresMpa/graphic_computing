import pygame as pg
import library as lib

if __name__ == '__main__':
    pg.init()
    vectors = []
    run = True
    window = lib.new_window("Adding vectors")
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                vectors.append(pg.mouse.get_pos())
                if len(vectors) == 2:
                    lib.fill(window, lib.cts.BLACK)
                    lib.vectors(window, lib.cts.Origin, vectors[0])
                    lib.vectors(window, lib.cts.Origin, vectors[1])
                    # It transforming the coord
                    vectors[0] = lib.cartesian_into_screen(vectors[0])
                    vectors[1] = lib.cartesian_into_screen(vectors[1])
                    # It appends the new vector
                    vectors.append(lib.vector_sum(vectors[1], vectors[0]))
                    vectors[2] = lib.screen_into_cartesian(vectors[2])
                    # It transform the coord
                    vectors[0] = lib.screen_into_cartesian(vectors[0])
                    vectors[1] = lib.screen_into_cartesian(vectors[1])
                    # Draws the complementary vectors
                    lib.vectors(window, lib.cts.Origin, vectors[2], lib.cts.BLUE)
                    lib.vectors(window, vectors[0], vectors[2], lib.cts.GREEN)
                    lib.vectors(window, vectors[1], vectors[2], lib.cts.GREEN)
                    vectors = []
        lib.cartesian_plane(window, lib.cts.Origin)
        lib.flip()
    pg.quit()
