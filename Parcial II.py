# coding=utf-8
import pygame as pg
import library as lib


class Texts(pg.sprite.Sprite):
    def __init__(self, text_position, screen, text, size, typography=4, color=lib.cts.WHITE):
        super(Texts, self).__init__()

        # Text
        self.txt = lib.write(text, size, typography, color)
        self.screen = screen

        # Position
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

        # Images
        self.thing = selected_thing
        self.image = lib.cts.Tree
        self.change_image()

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.thing_velocity = [0, 0]

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
            self.image = lib.cts.Decoration_4
        elif self.thing == 8:
            self.image = lib.cts.Decoration_5
        elif self.thing == 9:
            self.image = lib.cts.Nightstand_1
        elif self.thing == 10:
            self.image = lib.cts.Nightstand_2
        elif self.thing == 11:
            self.image = lib.cts.Chair_e
        elif self.thing == 12:
            self.image = lib.cts.Chair_n
        elif self.thing == 13:
            self.image = lib.cts.Chair_s
        elif self.thing == 14:
            self.image = lib.cts.Chair_w
        elif self.thing == 15:
            self.image = lib.cts.Table
        elif self.thing == 16:
            self.image = lib.cts.Tree
        elif self.thing == 17:
            self.image = lib.cts.Bush
        elif self.thing == 18:
            self.image = lib.cts.Plant_1
        elif self.thing == 19:
            self.image = lib.cts.Plant_2
        elif self.thing == 20:
            self.image = lib.cts.Flower

    def update(self):
        self.rect.x += self.thing_velocity[0]
        self.rect.y += self.thing_velocity[1]


class Buffs(pg.sprite.Sprite):
    def __init__(self, position, buff):
        super(Buffs, self).__init__()

        # Sprites
        self.image = lib.cts.Extra_life
        self.buff = buff
        self.change_image()

        # Position
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.buff_velocity = [0, 0]

    def change_image(self):
        if self.buff == 1:
            self.image = lib.cts.Extra_life
        elif self.buff == 2:
            self.image = lib.cts.Extra_energy
        elif self.buff == 3:
            self.image = lib.cts.Drake_smash

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
        self.change_image()

        self.background_limits = self.image.get_rect()

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = [0, 0]
        self.background_velocity = [0, 0]

        self.screen_limits = [lib.cts.width - 50, lib.cts.height - 50]
        self.background_limits = [(lib.cts.width - self.background_limits[2]),
                                  (lib.cts.height - self.background_limits[3])]

    def change_image(self):
        if self.background == 1:
            self.image = lib.cts.House_1
            self.background_limits = self.image.get_rect()
            self.background_limits = [(lib.cts.width - self.background_limits[2]),
                                      (lib.cts.height - self.background_limits[3])]
        elif self.background == 2:
            self.image = lib.cts.House_2
            self.background_limits = self.image.get_rect()
            self.background_limits = [(lib.cts.width - self.background_limits[2]),
                                      (lib.cts.height - self.background_limits[3])]
        elif self.background == 3:
            self.image = lib.cts.Field_0
            self.background_limits = self.image.get_rect()
            self.background_limits = [(lib.cts.width - self.background_limits[2]),
                                      (lib.cts.height - self.background_limits[3])]
        elif self.background == 4:
            self.image = lib.cts.Field_1
            self.background_limits = self.image.get_rect()
            self.background_limits = [(lib.cts.width - self.background_limits[2]),
                                      (lib.cts.height - self.background_limits[3])]
        elif self.background == 5:
            self.image = lib.cts.Field_2
            self.background_limits = self.image.get_rect()
            self.background_limits = [(lib.cts.width - self.background_limits[2]),
                                      (lib.cts.height - self.background_limits[3])]

    def update(self):
        self.rect.x -= self.background_velocity[0]
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
        self.live = 1
        self.speed = 0
        self.collides = collides

    def animate(self, key_pressed):
        if self.current_animation < 2 and key_pressed:
            self.current_animation += 1
        else:
            self.current_animation = 1
        self.image = self.set[self.action][self.current_animation]

    def get_position(self):
        return [self.rect.x, self.rect.y]

    def update(self, key_pressed, screen):
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
    intro = False
    room_1 = False
    room_2 = False
    field_1 = True
    field_2 = True
    field_3 = True
    in_combat = False
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

        # Drawing and control

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

    for _ in title_group:
        title_group.remove(_)

    lib.change_window_name('Euphoria')

    lib.fill(window)

    # Scenario settings

    # Creating a new scenario

    current_scenario = 1
    scenario = Scenarios(current_scenario, window)
    scenario.rect.x, scenario.rect.y = [lib.cts.width / 3, lib.cts.height / 3]

    # Adding things

    bed = Things([447, 224], 3)
    things_group.add(bed)

    decoration1 = Things([738, 207], 4)
    things_group.add(decoration1)

    decoration2 = Things([653, 203], 5)
    things_group.add(decoration2)

    nightstand_1 = Things([414, 201], 9)
    things_group.add(nightstand_1)

    nightstand_2 = Things([553, 232], 10)
    things_group.add(nightstand_2)

    top_limit = Things([412, 232], 2)
    things_group.add(top_limit)

    left_limit = Things([412, 232], 1)
    things_group.add(left_limit)

    right_limit = Things([775, 232], 1)
    things_group.add(right_limit)

    bottom_limit = Things([412, 462], 2)
    things_group.add(bottom_limit)

    # Adding a player

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

        # Next room condition
        if player.rect.bottom == 462 and player.rect.left < 505 and player.rect.right > 472:
            room_1 = False

        # Drawing

        players_group.update(key, window)
        things_group.update()
        lib.fill(window)
        scenario.update()
        things_group.draw(window)
        players_group.draw(window)

        lib.frames_per_second(fps, 1)

    # Cleaning

    for _ in things_group:
        things_group.remove(_)

    # Scenario settings

    # Background
    current_scenario = 2
    scenario.background = current_scenario

    # Background position
    scenario.change_image()
    scenario.rect.x, scenario.rect.y = [lib.cts.width / 5, lib.cts.height / 5]

    # Repositioning player
    player.rect.x = 712
    player.rect.y = 181

    # Adding things

    decoration4 = Things([265, 158], 7)
    things_group.add(decoration4)

    decoration3 = Things([809, 162], 6)
    things_group.add(decoration3)

    nightstand_2 = Things([585, 131], 8)
    things_group.add(nightstand_2)

    table = Things([695, 405], 15)
    things_group.add(table)

    chair_e = Things([637, 413], 11)
    things_group.add(chair_e)

    chair_n = Things([718, 483], 12)
    things_group.add(chair_n)

    chair_s = Things([716, 354], 13)
    things_group.add(chair_s)

    chair_w = Things([800, 415], 14)
    things_group.add(chair_w)

    top_limit = Things([262, 180], 2)
    things_group.add(top_limit)

    top_limit = Things([682, 180], 2)
    things_group.add(top_limit)

    left_limit = Things([262, 232], 1)
    things_group.add(left_limit)

    right_limit = Things([920, 232], 1)
    things_group.add(right_limit)

    bottom_limit = Things([262, 520], 2)
    things_group.add(bottom_limit)

    bottom_limit = Things([682, 520], 2)
    things_group.add(bottom_limit)

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

        # Next room condition
        if player.rect.bottom == 520 and player.rect.left < 450 and player.rect.right > 430:
            room_2 = False

        # Drawing

        players_group.update(key, window)
        things_group.update()
        lib.fill(window)
        scenario.update()
        things_group.draw(window)
        players_group.draw(window)

        lib.frames_per_second(fps, 1)

    # Cleaning

    for _ in things_group:
        things_group.remove(_)

    # Background
    current_scenario = 3
    scenario.background = current_scenario

    # Background position
    scenario.change_image()
    scenario.rect.x, scenario.rect.y = [0, -25]

    # Repositioning player
    player.rect.x = 712
    player.rect.y = 181

    angle = 0
    radio = 300
    distance = [0, 0]
    first_enemy_position = [400, 300]

    enemy = SimpleEnemy(first_enemy_position, 1)
    enemies_group.add(enemy)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        while field_1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    field_1 = False
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

            # Next field condition
            if 1100 > player.rect.bottom > 1150 and 1700 > player.rect.right > 1800:
                field_1 = False
                in_combat = False

            # Collides

            buff_collides = pg.sprite.spritecollide(player, buffs_group, True)

            # Enemies

            enemy_collide = pg.sprite.spritecollide(player, enemies_group, True)

            for enemy in enemy_collide:
                in_combat = True
                field_1 = False

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

            # Background

            if player.rect.x > scenario.screen_limits[0]:
                player.rect.x = scenario.screen_limits[0]
                if scenario.rect.x > scenario.background_limits[0]:
                    scenario.background_velocity[0] = 5
                else:
                    scenario.background_velocity[0] = 0
            else:
                if player.rect.x < lib.cts.width - scenario.screen_limits[0]:
                    player.rect.x = lib.cts.width - scenario.screen_limits[0]
                    if scenario.rect.x < lib.cts.width + scenario.background_limits[0] * 2:
                        scenario.background_velocity[0] = -5
                    else:
                        scenario.background_velocity[0] = 0
                else:
                    if scenario.rect.x > lib.cts.width + scenario.background_limits[0]:
                        scenario.background_velocity[0] = 5
                    else:
                        scenario.background_velocity[0] = 0

            if player.rect.y > scenario.screen_limits[1]:
                player.rect.y = scenario.screen_limits[1]
                if scenario.rect.y > scenario.background_limits[1]:
                    scenario.background_velocity[1] = -5
                else:
                    scenario.background_velocity[1] = 0
            else:
                if player.rect.y < lib.cts.height - scenario.screen_limits[1]:
                    player.rect.y = lib.cts.height - scenario.screen_limits[1]
                    if scenario.rect.y < 0:
                        scenario.background_velocity[1] = 5
                    else:
                        scenario.background_velocity[1] = 0
                else:
                    if scenario.rect.y > lib.cts.height + scenario.background_limits[1]:
                        scenario.background_velocity[1] = -5
                    else:
                        scenario.background_velocity[1] = 0

            # Drawing

            players_group.update(key, window)
            enemies_group.update()
            things_group.update()
            lib.fill(window)
            scenario.update()
            things_group.draw(window)
            enemies_group.draw(window)
            players_group.draw(window)

            lib.frames_per_second(fps, 1)

        while in_combat:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    run = False
                if event.type == pg.KEYDOWN:
                    field_1 = True
                    in_combat = False

            lib.fill(window)

            window.blit(lib.cts.Field_1, [0, 0])

            lib.frames_per_second(fps, 1)

    # Cleaning

    for _ in enemies_group:
        enemies_group.remove(_)

    for _ in things_group:
        things_group.remove(_)

    for _ in buffs_group:
        buffs_group.remove(_)

    # Background
    current_scenario = 4
    scenario.background = current_scenario

    # Background position
    scenario.change_image()
    scenario.rect.x, scenario.rect.y = [0, -25]

    # Repositioning player
    player.rect.x = 712
    player.rect.y = 181

    angle = 0
    radio = 300
    distance = [0, 0]
    first_enemy_position = [400, 300]

    enemy = SimpleEnemy(first_enemy_position, 1)
    enemies_group.add(enemy)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        while field_2:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    field_2 = False
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

            # Next field condition
            if 1100 > player.rect.bottom > 1150 and 1700 > player.rect.right > 1800:
                field_2 = False
                in_combat = False

            # Collides

            buff_collides = pg.sprite.spritecollide(player, buffs_group, True)

            # Enemies

            enemy_collide = pg.sprite.spritecollide(player, enemies_group, True)

            for enemy in enemy_collide:
                in_combat = True
                field_1 = False

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

            # Background

            if player.rect.x > scenario.screen_limits[0]:
                player.rect.x = scenario.screen_limits[0]
                if scenario.rect.x > scenario.background_limits[0]:
                    scenario.background_velocity[0] = 5
                else:
                    scenario.background_velocity[0] = 0
            else:
                if player.rect.x < lib.cts.width - scenario.screen_limits[0]:
                    player.rect.x = lib.cts.width - scenario.screen_limits[0]
                    if scenario.rect.x < lib.cts.width + scenario.background_limits[0] * 2:
                        scenario.background_velocity[0] = -5
                    else:
                        scenario.background_velocity[0] = 0
                else:
                    if scenario.rect.x > lib.cts.width + scenario.background_limits[0]:
                        scenario.background_velocity[0] = 5
                    else:
                        scenario.background_velocity[0] = 0

            if player.rect.y > scenario.screen_limits[1]:
                player.rect.y = scenario.screen_limits[1]
                if scenario.rect.y > scenario.background_limits[1]:
                    scenario.background_velocity[1] = -5
                else:
                    scenario.background_velocity[1] = 0
            else:
                if player.rect.y < lib.cts.height - scenario.screen_limits[1]:
                    player.rect.y = lib.cts.height - scenario.screen_limits[1]
                    if scenario.rect.y < 0:
                        scenario.background_velocity[1] = 5
                    else:
                        scenario.background_velocity[1] = 0
                else:
                    if scenario.rect.y > lib.cts.height + scenario.background_limits[1]:
                        scenario.background_velocity[1] = -5
                    else:
                        scenario.background_velocity[1] = 0

            # Drawing

            players_group.update(key, window)
            enemies_group.update()
            things_group.update()
            lib.fill(window)
            scenario.update()
            things_group.draw(window)
            enemies_group.draw(window)
            players_group.draw(window)

            lib.frames_per_second(fps, 1)

        while in_combat:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    run = False
                if event.type == pg.KEYDOWN:
                    field_1 = True
                    in_combat = False

            lib.fill(window)

            window.blit(lib.cts.Field_0, [0, 0])

            lib.frames_per_second(fps, 1)

    for _ in enemies_group:
        enemies_group.remove(_)

    for _ in things_group:
        things_group.remove(_)

    for _ in buffs_group:
        buffs_group.remove(_)

    # Background
    current_scenario = 4
    scenario.background = current_scenario

    # Background position
    scenario.change_image()
    scenario.rect.x, scenario.rect.y = [0, -25]

    # Repositioning player
    player.rect.x = 712
    player.rect.y = 181

    angle = 0
    radio = 300
    distance = [0, 0]
    first_enemy_position = [400, 300]

    enemy = SimpleEnemy(first_enemy_position, 1)
    enemies_group.add(enemy)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        while field_3:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    field_3 = False
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

            # Collides

            buff_collides = pg.sprite.spritecollide(player, buffs_group, True)

            # Enemies

            enemy_collide = pg.sprite.spritecollide(player, enemies_group, True)

            for enemy in enemy_collide:
                in_combat = True
                field_1 = False

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

            # Background

            if player.rect.x > scenario.screen_limits[0]:
                player.rect.x = scenario.screen_limits[0]
                if scenario.rect.x > scenario.background_limits[0]:
                    scenario.background_velocity[0] = 5
                else:
                    scenario.background_velocity[0] = 0
            else:
                if player.rect.x < lib.cts.width - scenario.screen_limits[0]:
                    player.rect.x = lib.cts.width - scenario.screen_limits[0]
                    if scenario.rect.x < lib.cts.width + scenario.background_limits[0] * 2:
                        scenario.background_velocity[0] = -5
                    else:
                        scenario.background_velocity[0] = 0
                else:
                    if scenario.rect.x > lib.cts.width + scenario.background_limits[0]:
                        scenario.background_velocity[0] = 5
                    else:
                        scenario.background_velocity[0] = 0

            if player.rect.y > scenario.screen_limits[1]:
                player.rect.y = scenario.screen_limits[1]
                if scenario.rect.y > scenario.background_limits[1]:
                    scenario.background_velocity[1] = -5
                else:
                    scenario.background_velocity[1] = 0
            else:
                if player.rect.y < lib.cts.height - scenario.screen_limits[1]:
                    player.rect.y = lib.cts.height - scenario.screen_limits[1]
                    if scenario.rect.y < 0:
                        scenario.background_velocity[1] = 5
                    else:
                        scenario.background_velocity[1] = 0
                else:
                    if scenario.rect.y > lib.cts.height + scenario.background_limits[1]:
                        scenario.background_velocity[1] = -5
                    else:
                        scenario.background_velocity[1] = 0

            # Drawing

            players_group.update(key, window)
            enemies_group.update()
            things_group.update()
            lib.fill(window)
            scenario.update()
            things_group.draw(window)
            enemies_group.draw(window)
            players_group.draw(window)

            lib.frames_per_second(fps, 1)

        while in_combat:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    run = False
                if event.type == pg.KEYDOWN:
                    field_1 = True
                    in_combat = False

            lib.fill(window)

            window.blit(lib.cts.Field_0, [0, 0])

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

    pg.quit()
