# coding=utf-8
import pygame as pg
import library as lib


class Texts(pg.sprite.Sprite):
    def __init__(self, text_position, screen, text, size, typography=4, color=lib.cts.WHITE):
        super(Texts, self).__init__()

        # Text issues
        self.txt = lib.write(text, size, typography, color)
        self.screen = screen

        # Position issues
        self.x, self.y = text_position
        self.velocity = [0, -1]
        self.limit = size

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.screen.blit(self.txt, [self.x, self.y])


class Scenarios(pg.sprite.Sprite):
    def __init__(self, background, screen):
        super(Scenarios, self).__init__()

        self.screen = screen
        self.image = lib.cts.Bedroom
        self.change_image(background)
        self.rect = self.image.get_rect()

    def change_image(self, background):
        if background == 1:
            self.image = lib.cts.Bedroom
        elif background == 2:
            self.image = lib.cts.Living_room
        elif background == 3:
            self.image = lib.cts.Field_1

    def update(self):
        self.screen.blit(self.image)


class SimpleEnemy(pg.sprite.Sprite):
    def __init__(self, position, sprite_sets):
        super(SimpleEnemy, self).__init__()

        # Player images
        self.image = sprite_sets

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]

    def update(self, x_player, y_player):
        self.velocity[0], self.velocity[1] = self.velocity[1] - y_player / self.velocity[0] - x_player
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


if __name__ == '__main__':
    pg.init()
    pg.font.init()

    run = True
    end = True
    intro = True
    playing = True
    window = lib.new_window("Intro")
    fps = lib.frames_per_second_basics()

    title_group = pg.sprite.Group()
    text_group = pg.sprite.Group()
    new_text_position = [50, 750]
    txt = ""
    cont = 0

    Title = Texts([300, 250], window, lib.cts.euphoria, 200)
    Title.velocity = [0, 0]
    title_group.add(Title)

    for _ in range(0, len(lib.cts.euphoria_intro)):
        new_text = Texts(new_text_position, window, lib.cts.euphoria_intro[_], 30, 2)
        new_text_position[1] += 50
        text_group.add(new_text)

    Skip = Texts([1080, 550], window, lib.cts.skip, 20)
    Skip.velocity = [0, 0]

    while run and intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                intro = False

        lib.fill(window)

        Title.update()

        if cont >= 100:
            Title.velocity = [0, -1]
            text_group.update()
            Skip.update()

        cont += 1

        for _ in text_group:
            if _.y < 0:
                text_group.remove(_)

        for _ in title_group:
            if _.y < 200:
                title_group.remove(_)

        if len(text_group) == 0:
            intro = False

        lib.frames_per_second(fps, 2)

    # Groups
    players_group = pg.sprite.Group()
    enemies_group = pg.sprite.Group()
    flowers_group = pg.sprite.Group()
    trees_group = pg.sprite.Group()
    NPCs_group = pg.sprite.Group()

    while run and playing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                intro = False

        lib.fill(window)
        lib.frames_per_second(fps, 1)

    while run and end:
        lib.fill(window)
        pg.font.init()
        txt = "GAME OVER"
        write = lib.write(txt, 60, 2)
        window.blit(write, [350, 200])
        txt = "Press any key"
        write = lib.write(txt, 30, 2)
        window.blit(write, [400, 300])

        lib.frames_per_second(fps, 5)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
                end = False
