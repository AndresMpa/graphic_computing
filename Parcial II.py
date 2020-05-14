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


class Things(pg.sprite.Sprite):
    def __init__(self, position, selected_thing):
        super(Things, self).__init__()

        self.thing = selected_thing
        self.image = lib.cts.Tree
        self.change_image()

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.thing_velocity = [0, 0]

        # Control
        self.move = 0
        self.take = 0

    def change_image(self):
        if self.thing == 1:
            self.image = lib.cts.Room_limit_1
        elif self.thing == 2:
            self.image = lib.cts.Room_limit_2
        elif self.thing == 3:
            self.image = lib.cts.Bed
        elif self.thing == 4:
            self.image = lib.cts.Decoration_1
        elif self.thing == 5:
            self.image = lib.cts.Decoration_2
        elif self.thing == 6:
            self.image = lib.cts.Decoration_3
        elif self.thing == 7:
            self.image = lib.cts.Nightstand_1
        elif self.thing == 8:
            self.image = lib.cts.Nightstand_2
        elif self.thing == 9:
            self.image = lib.cts.Nightstand_3
        elif self.thing == 10:
            self.image = lib.cts.Tree
        elif self.thing == 11:
            self.image = lib.cts.Bush
        elif self.thing == 12:
            self.image = lib.cts.Plant_1
        elif self.thing == 13:
            self.image = lib.cts.Plant_2
        elif self.thing == 14:
            self.image = lib.cts.Flower

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


class Gates(pg.sprite.Sprite):
    def __init__(self, position):
        super(Gates, self).__init__()

        self.image = pg.Surface([100, 100])
        self.image.fill(lib.cts.BLUE)

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.thing_velocity = [0, 0]

    def update(self):
        self.rect.x += self.thing_velocity[0]
        self.rect.y += self.thing_velocity[1]


class SimpleEnemy(pg.sprite.Sprite):
    def __init__(self, position, sprite_sets):
        super(SimpleEnemy, self).__init__()

        # Player images
        self.set = sprite_sets
        self.image = lib.cts.Enemy_1

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]
        self.angle = 0

    def get_position(self):
        return [self.rect.x, self.rect.y]

    def update(self):
        self.rect.x += self.velocity[0] * lib.mt.cos(self.angle)
        self.rect.y += self.velocity[1] * lib.mt.sin(self.angle)


class NonPlayableCharacters(pg.sprite.Sprite):
    def __init__(self, position, npc):
        super(NonPlayableCharacters, self).__init__()

        # Player images
        self.image = lib.cts.Tree
        self.change_image(npc)

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.thing_velocity = [0, 0]

    def change_image(self, background):
        if background == 1:
            self.image = lib.cts.Tree
        elif background == 2:
            self.image = lib.cts.Bush

    def update(self):
        self.rect.x += self.thing_velocity[0]
        self.rect.y += self.thing_velocity[1]


class Scenarios(pg.sprite.Sprite):
    def __init__(self, background, screen):
        super(Scenarios, self).__init__()

        self.screen = screen
        self.image = lib.cts.House_1
        self.background = background
        self.change_image(self.background)
        self.background_limits = self.image.get_rect()

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = [0, 0]
        self.background_velocity = [0, 0]

        self.screen_limits = [lib.cts.width - 50, lib.cts.height - 50]
        self.background_limits = [(lib.cts.width - self.background_limits[2]),
                                  (lib.cts.height - self.background_limits[3])]

        self.npc = []
        self.gates = []
        self.buffs = []
        self.things = []
        self.enemies = []
        self.players_position = []

    def change_image(self, background):
        if self.background == 1:
            # House, bedroom
            self.image = lib.cts.House_1
            self.background_limits = self.image.get_rect()

            # Things related
            self.npc = []
            self.gates = [(Gates([100, 500])), (Gates([100, 500]))]
            self.buffs = [Buffs([100, 1], 1)]
            self.things = []
            self.enemies = []
            self.players_position = [100, 100]
        elif self.background == 2:
            # House, Living room
            self.image = lib.cts.House_2
            self.background_limits = self.image.get_rect()

            # Things related
            self.npc = []
            self.gates = [(Gates([100, 500])), (Gates([100, 500]))]
            self.buffs = [Buffs([100, 1])]
            self.things = []
            self.enemies = []
            self.players_position = [100, 100]
        elif self.background == 3:
            # Battle field #1, Intro, NPC
            self.image = lib.cts.Field_0
            self.background_limits = self.image.get_rect()

            # Things related
            self.npc = [(NonPlayableCharacters([300, 500], 1))]
            self.gates = [(Gates([100, 500])), (Gates([100, 500]))]
            self.buffs = [Buffs([100, 1])]
            self.things = []
            self.enemies = []
            self.players_position = [100, 100]
        elif self.background == 4:
            # Battle field #2, Battle
            self.image = lib.cts.Field_1
            self.background_limits = self.image.get_rect()

            # Things related
            self.npc = []
            self.gates = [(Gates([100, 500])), (Gates([100, 500]))]
            self.buffs = [Buffs([100, 1])]
            self.things = []
            self.enemies = []
            self.players_position = [100, 100]
        elif self.background == 5:
            # Battle field #3, Battle
            self.image = lib.cts.Field_2
            self.background_limits = self.image.get_rect()

            # Things related
            self.npc = []
            self.gates = [(Gates([100, 500])), (Gates([100, 500]))]
            self.buffs = [Buffs([100, 1])]
            self.things = []
            self.enemies = []
            self.players_position = [100, 100]

    def update(self):
        self.rect.x += self.background_velocity[0]
        self.rect.y += self.background_velocity[1]
        self.screen.blit(self.image, [self.rect.x, self.rect.y])


class Player(pg.sprite.Sprite):
    def __init__(self, position, sprite_sets, collides):
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
        self.collides = collides

    def animate(self, key_pressed):
        if self.current_animation < 2 and key_pressed:
            self.current_animation += 1
        else:
            self.current_animation = 1
        self.image = self.set[self.action][self.current_animation]

    def get_position(self):
        return [self.rect.x, self.rect.y]

    def update(self, key_pressed):
        self.animate(key_pressed)

        self.rect.x += self.velocity[0]
        list_collide = pg.sprite.spritecollide(self, self.collides, False)

        for things in list_collide:
            if self.velocity[0] > 0:
                if self.rect.right > things.rect.left:
                    self.rect.right = things.rect.left
                    self.velocity[0] = 0
            else:
                if self.rect.left < things.rect.right:
                    self.rect.left = things.rect.right
                    self.velocity[0] = 0

        self.rect.y += self.velocity[1]
        list_collide = pg.sprite.spritecollide(self, self.collides, False)

        for things in list_collide:
            if self.velocity[1] > 0:
                if self.rect.bottom > things.rect.top:
                    self.rect.bottom = things.rect.top
                    self.velocity[1] = 0

            else:
                if self.rect.top < things.rect.bottom:
                    self.rect.top = things.rect.bottom
                    self.velocity[1] = 0


def move_enemy(player_position, enemy_position):
    position_x = player_position[0] - enemy_position[0]
    position_y = player_position[1] - enemy_position[1]
    return [position_x, position_y]


if __name__ == '__main__':
    # init()
    pg.init()
    pg.font.init()

    # Whiles
    run = True
    end = True
    dead = True
    intro = False
    room_1 = True
    room_2 = True
    field_1 = True
    field_2 = True
    field_3 = True
    start_menu = True

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
    things_group = pg.sprite.Group()
    buffs_group = pg.sprite.Group()
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

    # Cleaning
    lib.change_window_name('Euphoria')

    for _ in title_group:
        title_group.remove(_)

    lib.fill(window)

    # Creating new objects
    current_scenario = 1
    scenario = Scenarios(current_scenario, window)
    scenario.rect.x, scenario.rect.y = [lib.cts.width / 3, lib.cts.height / 3]

    bed = Things([447, 224], 3)
    things_group.add(bed)

    decoration1 = Things([738, 207], 4)
    things_group.add(decoration1)

    decoration2 = Things([653, 203], 5)
    things_group.add(decoration2)

    nightstand_1 = Things([414, 201], 7)
    things_group.add(nightstand_1)

    nightstand_2 = Things([553, 232], 8)
    things_group.add(nightstand_2)

    top_limit = Things([412, 232], 2)
    things_group.add(top_limit)

    left_limit = Things([412, 232], 1)
    things_group.add(left_limit)

    right_limit = Things([775, 232], 1)
    things_group.add(right_limit)

    bottom_limit = Things([412, 462], 2)
    things_group.add(bottom_limit)

    player = Player([scenario.rect.x + 155, scenario.rect.y + 55], lib.cts.Luke, things_group)
    player.speed = speed

    players_group.add(player)

    while run and room_1:
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

        # Drawing

        players_group.update(key)
        things_group.update()
        lib.fill(window)
        scenario.update()
        things_group.draw(window)
        players_group.draw(window)

        lib.frames_per_second(fps, 1)

    while run and room_2:
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

        list_collides = pg.sprite.spritecollide(player, things_group, False)

        # Drawing

        players_group.update(key)
        things_group.update()
        lib.fill(window)
        scenario.update()
        things_group.draw(window)
        players_group.draw(window)

        lib.frames_per_second(fps, 1)

    angle = 0
    radio = 300
    distance = [0, 0]
    first_enemy_position = [400, 300]

    enemy = SimpleEnemy(first_enemy_position, 1)
    enemies_group.add(enemy)

    tree = Things([1600, 500], 1)
    things_group.add(tree)
    tree = Things([500, 500], 2)
    things_group.add(tree)
    tree = Things([1800, 200], 3)
    things_group.add(tree)
    tree = Things([600, 900], 4)
    things_group.add(tree)
    tree = Things([1900, 800], 5)
    things_group.add(tree)

    Title = Texts([100, 250], window, lib.cts.dead, 200)
    Title.velocity = [0, 0]
    title_group.add(Title)

    # Control
    lists_collides = pg.sprite.spritecollide(player, buffs_group, True)

    for enemy in enemies_group:
        distance = move_enemy(first_enemy_position, player.rect)
        if lib.mt.sqrt(lib.mt.pow(distance[0], 2) + lib.mt.pow(distance[1], 2)) > radio:
            distance = move_enemy(first_enemy_position, enemy.rect)
        else:
            distance = move_enemy(player.rect, enemy.rect)
        if distance[0] > 0:
            enemy.velocity = [4, 4]
        else:
            enemy.velocity = [-4, -4]

        if (distance[0] == 0) and (distance[1] == 0):
            enemy.velocity = [0, 0]
        else:
            if distance[0] == 0:
                enemy.velocity = [-4, -4]
                if distance[1] > 0:
                    angle = lib.mt.radians(270)
                if distance[1] < 0:
                    angle = lib.mt.radians(90)
            else:
                angle = lib.mt.atan(distance[1] / distance[0])
                enemy.angle = angle

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
