import pygame as pg
import library as lib
import objects as obj
import ConfigParser as Cp

if __name__ == '__main__':
    pg.init()
    run = True
    window = lib.new_window("Mapping")
    fps = lib.frames_per_second_basics()

    map_file = Cp.ConfigParser()
    map_file.read('map.map')

    """
    print 'sections ', map_file.sections()
    print 'background ', map_file.get('info', 'background')
    print 'map: ', map_file.get('info', 'map')
    map_from_file = map_file.get('info', 'map').split('\n')
    print map_file.items('.')
    print map_from_file
    """

    texture = map_file.get('info', 'background')
    image_texture = pg.image.load(texture)

    matrix = []

    for j in range(12):
        line = []
        for i in range(32):
            piece = image_texture.subsurface(i * 32, j * 32, 32, 32)
            line.append(piece)
        matrix.append(line)

    info_map = map_file.get('info', 'map')
    map_slip = info_map.split('\n')
    print map_slip
    j = 0
    for f in map_slip:
        print f
        i = 0
        for c in f:
            print c, map_file.get(c, 'tf'), map_file.get(c, 'tc'), 32 * i, 32 * j
            tf = int(map_file.get(c, 'tf'))
            tc = int(map_file.get(c, 'tc'))
            collide = int(map_file.get(c, 'collide'))
            if collide > 0:
                window.blit(matrix[tf][tc], [32 * i, 32 * j])
            i += 1
        j += 1

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        lib.frames_per_second(fps)
    pg.quit()
