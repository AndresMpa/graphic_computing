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
        self.image = lib.cts.House_1
        self.change_image(background)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = [0, 0]

    def change_image(self, background):
        if background == 1:
            self.image = lib.cts.House_1
        elif background == 2:
            self.image = lib.cts.House_2
        elif background == 3:
            self.image = lib.cts.Field_0
        elif background == 4:
            self.image = lib.cts.Field_1
        elif background == 5:
            self.image = lib.cts.Field_2

    def update(self):
        self.screen.blit(self.image, [self.rect.x, self.rect.y])


class Player(pg.sprite.Sprite):
    def __init__(self, position, sprite_sets):
        super(Player, self).__init__()

        # Animation issues
        self.action = 3
        self.current_animation = 1

        # Player images
        self.set = sprite_sets
        self.image = self.set[self.action][self.current_animation]

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]

        # Collision
        self.blocks = None

        # Control
        self.speed = 0
        self.live = []

    def animate(self, key_pressed):
        if self.current_animation < 2 and key_pressed:
            self.current_animation += 1
        else:
            self.current_animation = 1
        self.image = self.set[self.action][self.current_animation]

    def update(self, key_pressed):
        self.animate(key_pressed)
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


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


class Things(pg.sprite.Sprite):
    def __init__(self, position, thing):
        super(Things, self).__init__()

        # Player images
        self.image = lib.cts.Tree
        self.change_image(thing)

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.thing_velocity = [0, 0]

        # Control
        self.move = 0
        self.take = 0

    def change_image(self, background):
        if background == 1:
            self.image = lib.cts.Tree
        elif background == 2:
            self.image = lib.cts.Bush
        elif background == 3:
            self.image = lib.cts.Flower
            self.take = 1
        elif background == 4:
            self.image = lib.cts.Plant_1
        elif background == 5:
            self.image = lib.cts.Plant_2

    def update(self):
        self.rect.x += self.thing_velocity[0]
        self.rect.y += self.thing_velocity[1]


class Buffs(pg.sprite.Sprite):
    def __init__(self, position, buff):
        super(Buffs, self).__init__()

        # Player images
        self.image = lib.cts.Tree
        self.change_image(buff)

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.buff_velocity = [0, 0]

    def change_image(self, buff):
        if buff == 1:
            self.image = lib.cts.Tree
        elif buff == 2:
            self.image = lib.cts.Bush
        elif buff == 3:
            self.image = lib.cts.Flower
        elif buff == 4:
            self.image = lib.cts.Plant_1
        elif buff == 5:
            self.image = lib.cts.Plant_2

    def update(self, key_pressed):
        self.rect.x += self.buff_velocity[0]
        self.rect.y += self.buff_velocity[1]


if __name__ == '__main__':
    # init()
    pg.init()
    pg.font.init()

    # Whiles
    run = True
    end = True
    dead = True
    intro = True
    playing = True

    # Windows constants
    window = lib.new_window("Intro")
    fps = lib.frames_per_second_basics()

    # Groups
    # while writing
    title_group = pg.sprite.Group()
    text_group = pg.sprite.Group()

    # while playing
    players_group = pg.sprite.Group()
    enemies_group = pg.sprite.Group()
    flowers_group = pg.sprite.Group()
    trees_group = pg.sprite.Group()
    NPCs_group = pg.sprite.Group()

    # Variables
    key = 0
    cont = 0
    speed = 5

    # Intro issues

    # Game title
    Title = Texts([300, 250], window, lib.cts.euphoria, 200)
    Title.velocity = [0, 0]
    title_group.add(Title)

    # Game intro
    new_text_position = [50, 750]
    for _ in range(0, len(lib.cts.euphoria_intro)):
        new_text = Texts(new_text_position, window, lib.cts.euphoria_intro[_], 30, 2)
        new_text_position[1] += 50
        text_group.add(new_text)

    # Game button skip
    Skip = Texts([1080, 550], window, lib.cts.skip, 20)
    Skip.velocity = [0, 0]
    title_group.add(Skip)

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
            if _.y <= 0:
                title_group.remove(_)

        if len(text_group) == 0:
            intro = False

        lib.frames_per_second(fps, 2)

    # Cleaning and changing
    lib.change_window_name('Euphoria')

    for _ in title_group:
        title_group.remove(_)

    lib.fill(window)

    # Creating new objects
    scenario = Scenarios(4, window)
    scenario.rect.x, scenario.rect.y = [0, 0]

    player = Player([scenario.rect.x + 155, scenario.rect.y + 55], lib.cts.Luke)
    player.speed = speed
    players_group.add(player)

    tree = Things([1600, 500], 1)
    trees_group.add(tree)
    tree = Things([500, 500], 2)
    trees_group.add(tree)
    tree = Things([1800, 200], 3)
    trees_group.add(tree)
    tree = Things([600, 900], 4)
    trees_group.add(tree)
    tree = Things([1900, 800], 5)
    trees_group.add(tree)

    Title = Texts([100, 250], window, lib.cts.dead, 200)
    Title.velocity = [0, 0]
    title_group.add(Title)

    while run and playing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                key = 1
                if event.key == pg.K_s:
                    player.velocity[1] += player.speed
                    player.action = 3
                if event.key == pg.K_w:
                    player.velocity[1] -= player.speed
                    player.action = 1
                if event.key == pg.K_d:
                    player.velocity[0] += player.speed
                    player.action = 0
                if event.key == pg.K_a:
                    player.velocity[0] -= player.speed
                    player.action = 2
            if event.type == pg.KEYUP:
                player.velocity = [0, 0]
                key = 0

        # Control
        list_collides = pg.sprite.spritecollide(player, buffs, True)

        if player.rect.x < 0:
            scenario.change_image(1)

        # Drawing

        if not dead:
            title_group.update()
        else:
            players_group.update(key)
            trees_group.update()
            lib.fill(window)
            scenario.update()
            trees_group.draw(window)
            players_group.draw(window)

        lib.frames_per_second(fps, 0, 10)

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

    pg.quit()
