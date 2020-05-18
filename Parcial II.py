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
        elif self.thing == 21:
            self.image = lib.cts.Player_house

    def update(self):
        self.rect.x += self.thing_velocity[0]
        self.rect.y += self.thing_velocity[1]


class Buffs(pg.sprite.Sprite):
    def __init__(self, position, buff):
        super(Buffs, self).__init__()

        # Settings
        self.radio = 10

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

    def get_buff(self):
        return self.image

    def update(self):
        self.rect.x += self.buff_velocity[0]
        self.rect.y += self.buff_velocity[1]


class SimpleEnemy(pg.sprite.Sprite):
    def __init__(self, position, sprite_sets):
        super(SimpleEnemy, self).__init__()

        # Enemy images
        self.set = sprite_sets
        self.image = lib.cts.Enemy_1

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]
        self.angle = 0

        # Statistics
        self.life = 5
        self.enemy_attacks = lib.cts.Enemy_1_attacks

    def get_position(self):
        return [self.rect.x, self.rect.y]

    def enemy_attack(self, chose):
        return lib.write(self.enemy_attacks[chose], 30, 2)

    def update(self, scenario_velocity):
        self.rect.x += self.velocity[0] * lib.mt.cos(self.angle) - scenario_velocity[0]
        self.rect.y += self.velocity[1] * lib.mt.sin(self.angle) + scenario_velocity[1]


class NonPlayableCharacters(pg.sprite.Sprite):
    def __init__(self, position, npc):
        super(NonPlayableCharacters, self).__init__()

        # Player images
        self.image = lib.cts.Manuela
        self.change_image(npc)

        # Position issues
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.npc_velocity = [0, 0]

    def change_image(self, background):
        if background == 1:
            self.image = lib.cts.Manuela
        elif background == 2:
            self.image = lib.cts.Balzar

    def update(self):
        self.rect.x += self.npc_velocity[0]
        self.rect.y += self.npc_velocity[1]


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

    def move_enemies(self, enemy_list):
        for iteration, value in enumerate(enemy_list):
            enemy_list[iteration][0] -= self.background_velocity[0]
            enemy_list[iteration][1] += self.background_velocity[1]

        return enemy_list

    def update(self):
        self.rect.x -= self.background_velocity[0]
        self.rect.y += self.background_velocity[1]
        self.screen.blit(self.image, [self.rect.x, self.rect.y])


class Player(pg.sprite.Sprite):
    def __init__(self, position, sprite_sets, collides):
        super(Player, self).__init__()

        # Animation
        self.action = 3
        self.current_animation = 1

        # Player images
        self.set = sprite_sets
        self.image = self.set[self.action][self.current_animation]

        # Position
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]

        self.statistics = [0, 0]

        # Control
        self.speed = 0
        self.collides = collides

        # Statistics
        self.lvl = 1
        self.live = 0
        self.energy = 0
        self.extra_live = 0
        self.drake_smash = 0
        self.extra_energy = 0

    def animate(self, key_pressed):
        if self.current_animation < 2 and key_pressed:
            self.current_animation += 1
        else:
            self.current_animation = 1
        self.image = self.set[self.action][self.current_animation]

    def get_position(self):
        return [self.rect.x, self.rect.y]

    def use_extras(self, choose):
        if choose == 1:
            self.extra_live -= 1
            self.live += 5
        if choose == 2:
            self.extra_energy -= 1
            self.energy += 5
        if choose == 3:
            self.drake_smash -= 1

    def show_statistics(self, screen):
        for _ in range(self.live):
            screen.blit(lib.cts.Hearts, [self.statistics[0], self.statistics[1]])
            self.statistics[0] += 15

        self.statistics = [0, 25]

        for _ in range(self.energy):
            screen.blit(lib.cts.Extra_energy, [self.statistics[0], self.statistics[1]])
            self.statistics[0] += 15

        self.statistics = [1170, 0]

        for _ in range(self.drake_smash):
            screen.blit(lib.cts.Drake_smash, [self.statistics[0], self.statistics[1]])
            self.statistics[0] -= 20

        self.statistics = [0, 0]

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

        self.show_statistics(screen)


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
    death = False
    field_1 = False
    field_2 = True
    field_3 = True
    in_combat = False
    start_menu = True

    # Windows constants
    window = lib.new_window("Intro")
    fps = lib.frames_per_second_basics()

    # Groups
    # while writing
    abilities_in_combat = pg.sprite.Group()
    dialogue_group = pg.sprite.Group()
    title_group = pg.sprite.Group()
    text_group = pg.sprite.Group()

    # while playing
    enemies_in_combat = pg.sprite.Group()
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
    catchable = 0
    enemy_ability = None

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

    for _ in text_group:
        text_group.remove(_)

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

    first_life = Buffs([560, 225], 1)
    buffs_group.add(first_life)

    # Adding a player

    player = Player([scenario.rect.x + 155, scenario.rect.y + 55], lib.cts.Luke, things_group)
    player.speed = speed

    players_group.add(player)

    # Adding text interactions

    potion = Texts([300, 500], window, lib.cts.dialogue_1, 30, 2)
    text_group.add(potion)

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
                if event.key == pg.K_e and catchable:
                    for _ in buffs_group:
                        buffs_group.remove(_)
                    player.live = 10
                    catchable = 0
            if event.type == pg.KEYUP:
                player.velocity = [0, 0]
                key = 0

        # Next room condition
        if player.rect.bottom == 462 and player.rect.left < 505 and player.rect.right > 472:
            room_1 = False

        # Drawing
        lib.fill(window)

        scenario.update()

        if 550 < player.rect.x < 585 and 270 > player.rect.y > 230:
            if potion.y < 490:
                potion.velocity = [0, 0]

            text_group.update()

            catchable = 1
        else:
            text_group.rect = [300, 500]
            catchable = 0

        things_group.update()
        things_group.draw(window)

        buffs_group.update()
        buffs_group.draw(window)

        players_group.update(key, window)
        players_group.draw(window)

        lib.frames_per_second(fps, 1)

    # Cleaning

    for _ in things_group:
        things_group.remove(_)

    for _ in buffs_group:
        buffs_group.remove(_)

    for _ in text_group:
        text_group.remove(_)

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

    # Adding buffs

    energy = Buffs([705, 405], 2)
    buffs_group.add(energy)

    smash = Buffs([885, 185], 3)
    buffs_group.add(smash)

    # Adding text interactions

    potion = Texts([250, 70], window, lib.cts.dialogue_2, 30, 2)
    potion.velocity = [0, 1]
    text_group.add(potion)

    ring = Texts([250, 70], window, lib.cts.dialogue_3, 30, 2)
    ring.velocity = [0, 1]
    text_group.add(ring)

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
                if event.key == pg.K_e and catchable:
                    catchable = 0
                    player.energy = 10
                    buffs_group.remove(energy)
                if event.key == pg.K_q and catchable:
                    catchable = 0
                    player.drake_smash += 1
                    buffs_group.remove(smash)
            if event.type == pg.KEYUP:
                player.velocity = [0, 0]
                key = 0

        # Next room condition
        if player.rect.bottom == 520 and player.rect.left < 450 and player.rect.right > 430:
            room_2 = False

        # Drawing
        lib.fill(window)

        scenario.update()

        if 665 < player.rect.x < 690 and 385 > player.rect.y > 360:
            if potion.y > 80:
                potion.velocity = [0, 0]

            potion.update()

            catchable = 1
        else:
            potion.rect = [250, 70]

            if 870 < player.rect.x < 900 and player.rect.y <= 232:
                if ring.y > 80:
                    ring.velocity = [0, 0]

                ring.update()

                catchable = 1
            else:
                ring.rect = [250, 70]
                catchable = 0

        things_group.update()
        things_group.draw(window)

        buffs_group.update()
        buffs_group.draw(window)

        players_group.update(key, window)
        players_group.draw(window)

        lib.frames_per_second(fps, 1)

    # Cleaning

    for _ in things_group:
        things_group.remove(_)

    for _ in text_group:
        text_group.remove(_)

    # Background settings
    current_scenario = 3
    scenario.background = current_scenario

    # Background position
    scenario.change_image()
    scenario.rect.x, scenario.rect.y = [-100, -250]

    # Repositioning player
    player.rect.x = 700
    player.rect.y = 350

    angle = 0
    radio = 300
    distance = [0, 0]
    first_enemy_position = [[1400, 600]]

    enemy = SimpleEnemy(first_enemy_position[0], 1)
    enemies_group.add(enemy)

    # Adding things

    flower = Things([685, 20], 20)
    things_group.add(flower)

    flower = Things([685, 35], 20)
    things_group.add(flower)

    flower = Things([705, 20], 20)
    things_group.add(flower)

    flower = Things([705, 35], 20)
    things_group.add(flower)

    flower = Things([705, 50], 20)
    things_group.add(flower)

    flower = Things([705, 65], 20)
    things_group.add(flower)

    flower = Things([725, 20], 20)
    things_group.add(flower)

    flower = Things([725, 35], 20)
    things_group.add(flower)

    flower = Things([725, 50], 20)
    things_group.add(flower)

    flower = Things([725, 65], 20)
    things_group.add(flower)

    flower = Things([725, 80], 20)
    things_group.add(flower)

    flower = Things([725, 95], 20)
    things_group.add(flower)

    flower = Things([745, 20], 20)
    things_group.add(flower)

    flower = Things([745, 35], 20)
    things_group.add(flower)

    flower = Things([745, 50], 20)
    things_group.add(flower)

    flower = Things([745, 65], 20)
    things_group.add(flower)

    flower = Things([745, 80], 20)
    things_group.add(flower)

    flower = Things([745, 95], 20)
    things_group.add(flower)

    flower = Things([765, 20], 18)
    things_group.add(flower)

    flower = Things([765, 35], 18)
    things_group.add(flower)

    flower = Things([765, 50], 18)
    things_group.add(flower)

    flower = Things([765, 65], 18)
    things_group.add(flower)

    flower = Things([765, 80], 18)
    things_group.add(flower)

    flower = Things([765, 95], 18)
    things_group.add(flower)

    flower = Things([785, 20], 18)
    things_group.add(flower)

    flower = Things([785, 35], 18)
    things_group.add(flower)

    flower = Things([785, 50], 18)
    things_group.add(flower)

    flower = Things([785, 65], 18)
    things_group.add(flower)

    flower = Things([785, 80], 18)
    things_group.add(flower)

    flower = Things([785, 95], 18)
    things_group.add(flower)

    flower = Things([785, 20], 18)
    things_group.add(flower)

    flower = Things([785, 35], 18)
    things_group.add(flower)

    flower = Things([805, 50], 18)
    things_group.add(flower)

    flower = Things([805, 65], 18)
    things_group.add(flower)

    flower = Things([805, 80], 18)
    things_group.add(flower)

    flower = Things([805, 95], 18)
    things_group.add(flower)

    flower = Things([805, 20], 18)
    things_group.add(flower)

    flower = Things([805, 35], 18)
    things_group.add(flower)

    flower = Things([805, 50], 18)
    things_group.add(flower)

    flower = Things([805, 65], 18)
    things_group.add(flower)

    flower = Things([825, 80], 18)
    things_group.add(flower)

    flower = Things([825, 95], 18)
    things_group.add(flower)

    flower = Things([825, 20], 18)
    things_group.add(flower)

    flower = Things([825, 35], 18)
    things_group.add(flower)

    flower = Things([825, 50], 18)
    things_group.add(flower)

    flower = Things([825, 65], 18)
    things_group.add(flower)

    flower = Things([825, 80], 18)
    things_group.add(flower)

    flower = Things([825, 95], 18)
    things_group.add(flower)

    house = Things([500, 0], 21)
    things_group.add(house)

    # Adding text

    new_text_position = [30, 450]
    for _ in range(0, len(lib.cts.dialogue_4)):
        warden = Texts(new_text_position, window, lib.cts.dialogue_4[_], 30, 2, lib.cts.BLACK)
        warden.velocity = [0, 0]
        new_text_position[1] += 25
        text_group.add(warden)

    new_text_position = [450, 450]
    for _ in range(0, len(lib.cts.dialogue_5)):
        dialogue = Texts(new_text_position, window, lib.cts.dialogue_5[_], 30, 2, lib.cts.BLACK)
        dialogue.velocity = [0, 0]
        new_text_position[1] += 25
        dialogue_group.add(dialogue)

    Manuela = NonPlayableCharacters([750, 300], 1)
    NPCs_group.add(Manuela)

    new_text_position = [50, 450]
    abilities = Texts(new_text_position, window, lib.cts.Player_attacks[0], 30, 2)
    abilities.velocity = [0, 0]
    abilities_in_combat.add(abilities)
    new_text_position[1] += 100

    abilities = Texts(new_text_position, window, lib.cts.Player_attacks[1], 30, 2)
    abilities.velocity = [0, 0]
    abilities_in_combat.add(abilities)
    new_text_position[1] += 50

    new_text_position = [350, 450]

    abilities = Texts(new_text_position, window, lib.cts.Player_attacks[2], 30, 2)
    abilities.velocity = [0, 0]
    abilities_in_combat.add(abilities)
    new_text_position[1] += 100

    abilities = Texts(new_text_position, window, lib.cts.Player_attacks[3], 30, 2)
    abilities.velocity = [0, 0]
    abilities_in_combat.add(abilities)

    catchable = 1

    while run and field_1 or in_combat:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        while field_1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
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
                    if event.key == pg.K_e and catchable:
                        catchable = 0
                        player.velocity = [0, 0]
                if event.type == pg.KEYUP:
                    player.velocity = [0, 0]
                    key = 0

            # Control

            # Next field condition
            if player.rect.x == 1150 and 360 < player.rect.y < 520:
                if scenario.rect[0] == -600 and scenario.rect[1] == -625:
                    in_combat = False
                    field_1 = False

            # Background

            if player.rect.x > scenario.screen_limits[0]:
                player.rect.x = scenario.screen_limits[0]
                if scenario.rect.x > scenario.background_limits[0]:
                    scenario.background_velocity[0] = 5
                    for _ in things_group:
                        _.thing_velocity[0] = -5
                    Manuela.npc_velocity[0] = -5

                else:
                    scenario.background_velocity[0] = 0
                    for _ in things_group:
                        _.thing_velocity[0] = 0
                    Manuela.npc_velocity[0] = 0
            else:
                if player.rect.x < lib.cts.width - scenario.screen_limits[0]:
                    player.rect.x = lib.cts.width - scenario.screen_limits[0]
                    if scenario.rect.x < lib.cts.width + scenario.background_limits[0] * 2:
                        scenario.background_velocity[0] = -5
                        for _ in things_group:
                            _.thing_velocity[0] = 5
                        Manuela.npc_velocity[0] = 5
                    else:
                        scenario.background_velocity[0] = 0
                        for _ in things_group:
                            _.thing_velocity[0] = 0
                        Manuela.npc_velocity[0] = 0
                else:
                    if scenario.rect.x > lib.cts.width + scenario.background_limits[0]:
                        scenario.background_velocity[0] = 5
                        for _ in things_group:
                            _.thing_velocity[0] = -5
                        Manuela.npc_velocity[0] = -5
                    else:
                        scenario.background_velocity[0] = 0
                        for _ in things_group:
                            _.thing_velocity[0] = 0
                        Manuela.npc_velocity[0] = 0

            if player.rect.y > scenario.screen_limits[1]:
                player.rect.y = scenario.screen_limits[1]
                if scenario.rect.y > scenario.background_limits[1]:
                    scenario.background_velocity[1] = -5
                    for _ in things_group:
                        _.thing_velocity[1] = -5
                    Manuela.npc_velocity[1] = -5
                else:
                    scenario.background_velocity[1] = 0
                    for _ in things_group:
                        _.thing_velocity[1] = 0
                    Manuela.npc_velocity[1] = 0
            else:
                if player.rect.y < lib.cts.height - scenario.screen_limits[1]:
                    player.rect.y = lib.cts.height - scenario.screen_limits[1]
                    if scenario.rect.y < 0:
                        scenario.background_velocity[1] = 5
                        for _ in things_group:
                            _.thing_velocity[1] = 5
                        Manuela.npc_velocity[1] = 5
                    else:
                        scenario.background_velocity[1] = 0
                        for _ in things_group:
                            _.thing_velocity[1] = 0
                        Manuela.npc_velocity[1] = 0
                else:
                    if scenario.rect.y > lib.cts.height + scenario.background_limits[1]:
                        scenario.background_velocity[1] = -5
                        for _ in things_group:
                            _.thing_velocity[1] = -5
                        Manuela.npc_velocity[1] = -5
                    else:
                        scenario.background_velocity[1] = 0
                        for _ in things_group:
                            _.thing_velocity[1] = 0
                        Manuela.npc_velocity[1] = 0

            # Enemies

            enemy_collide = pg.sprite.spritecollide(player, enemies_group, True)

            for enemy in enemy_collide:
                enemies_in_combat.add(enemy)
                in_combat = True
                field_1 = False

            i = 0
            for enemy in enemies_group:
                distance = move_enemy(first_enemy_position[i], player.rect)
                if lib.mt.sqrt(lib.mt.pow(distance[0], 2) + lib.mt.pow(distance[1], 2)) > radio:
                    distance = move_enemy(first_enemy_position[i], enemy.rect)
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
                i += 1

            # Drawing
            lib.fill(window)

            scenario.update()

            first_enemy_position = scenario.move_enemies(first_enemy_position)

            things_group.update()
            things_group.draw(window)

            players_group.update(key, window)
            players_group.draw(window)

            enemies_group.update(scenario.background_velocity)
            enemies_group.draw(window)

            if 750 + scenario.rect.x < player.rect.x < 953 + scenario.rect.x:
                if 350 + scenario.rect.y > player.rect.y > 217 + scenario.rect.y:
                    window.blit(lib.cts.Dialog_box, [0, 400])
                    text_group.update()

            if 700 < player.rect.x < 750 and 330 < player.rect.y < 370 and catchable:
                window.blit(lib.cts.Dialog_box, [400, 400])
                dialogue_group.update()

            NPCs_group.update()
            NPCs_group.draw(window)

            lib.frames_per_second(fps, 1)

        turn = 1

        while in_combat:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    run = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    print pg.mouse.get_pos()
                if event.type == pg.KEYDOWN and turn == 1:
                    if event.key == pg.K_q:
                        print 'Sword'
                        turn = 0
                        player.energy -= 1
                    if event.key == pg.K_w:
                        print 'Hit'
                        turn = 0
                        player.energy -= 1
                    if event.key == pg.K_e:
                        print 'Transformation'
                        turn = 0
                        player.energy -= 1
                    if event.key == pg.K_r:
                        print 'Dragon fire ball'
                        turn = 0
                        player.energy -= 1
                    if event.key == pg.K_SPACE:
                        field_1 = True
                        in_combat = False

            # Control

            if turn == 0 and cont == 0:
                for enemy in enemies_in_combat:
                    enemy_ability = enemy.enemy_attack(lib.random_range(1, 3))

            for enemy in enemies_in_combat:
                if enemy.life == 0:
                    enemies_in_combat.remove(enemy)

            if len(enemies_in_combat) == 0:
                in_combat = False
                field_1 = True

            if player.live == 0 or player.energy == 0:
                in_combat = False
                field_1 = True
                death = True

            lib.fill(window)

            window.blit(lib.cts.Battle_ground, [0, 0])

            if turn == 1:
                window.blit(lib.cts.Dialog_box, [0, 400])
                player.show_statistics(window)
                abilities_in_combat.update()
                cont = 0
            else:
                window.blit(lib.cts.Dialog_box, [400, 400])
                window.blit(enemy_ability, [450, 450])
                if cont > 100:
                    turn = 1
                cont += 1

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
    radio = 600
    distance = [0, 0]
    first_enemy_position = [[400, 300], [600, 500]]

    enemy = SimpleEnemy(first_enemy_position[0], 1)
    enemies_group.add(enemy)

    enemy = SimpleEnemy(first_enemy_position[1], 1)
    enemies_group.add(enemy)

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

    while run and field_2 or in_combat:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        while field_2:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
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
            if player.rect.x == 1150 and 360 < player.rect.y < 520:
                if scenario.rect[0] == -600 and scenario.rect[1] == -625:
                    in_combat = False
                    field_2 = False

            # Collides

            buff_collides = pg.sprite.spritecollide(player, buffs_group, True)

            # Enemies

            enemy_collide = pg.sprite.spritecollide(player, enemies_group, True)

            for enemy in enemy_collide:
                enemies_in_combat.add(enemy)
                in_combat = True
                field_1 = False

            i = 0
            for enemy in enemies_group:
                distance = move_enemy(first_enemy_position[i], player.rect)
                if lib.mt.sqrt(lib.mt.pow(distance[0], 2) + lib.mt.pow(distance[1], 2)) > radio:
                    distance = move_enemy(first_enemy_position[i], enemy.rect)
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
                i += 1

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
            lib.fill(window)

            scenario.update()

            first_enemy_position = scenario.move_enemies(first_enemy_position)

            things_group.update()
            things_group.draw(window)

            players_group.update(key, window)
            players_group.draw(window)

            enemies_group.update(scenario.background_velocity)
            enemies_group.draw(window)

            lib.frames_per_second(fps, 1)

        turn = 1

        new_text_position = [50, 750]
        for _ in range(0, len(lib.cts.euphoria_intro)):
            new_text = Texts(new_text_position, window, lib.cts.euphoria_intro[_], 30, 2)
            new_text_position[1] += 50
            text_group.add(new_text)

        while in_combat:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    run = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    print pg.mouse.get_pos()
                if event.type == pg.KEYDOWN and turn == 1:
                    if event.key == pg.K_q:
                        print 'Sword'
                        turn = 0
                    if event.key == pg.K_w:
                        print 'Hit'
                        turn = 0
                    if event.key == pg.K_e:
                        print 'Transformation'
                        turn = 0
                    if event.key == pg.K_r:
                        print 'Dragon fire ball'
                        turn = 0
                    if event.key == pg.K_SPACE:
                        in_combat = False
                        field_2 = True

            # Control

            if turn == 0:
                for enemy in enemies_in_combat:
                    enemy.attack()
                turn = 1

            for enemy in enemies_in_combat:
                if enemy.life == 0:
                    enemies_in_combat.remove(enemy)

            if len(enemies_in_combat) == 0:
                in_combat = False
                field_2 = True

            if player.live == 0:
                field_1 = True
                in_combat = False

            lib.fill(window)

            window.blit(lib.cts.Battle_ground, [0, 0])

            if turn == 1:
                window.blit(lib.cts.Dialog_box, [0, 400])

            lib.frames_per_second(fps, 1)

    for _ in enemies_group:
        enemies_group.remove(_)

    for _ in things_group:
        things_group.remove(_)

    for _ in buffs_group:
        buffs_group.remove(_)

    # Background
    current_scenario = 5
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
            lib.fill(window)

            scenario.update()

            things_group.update()
            things_group.draw(window)

            players_group.update(key, window)
            players_group.draw(window)

            enemies_group.update(scenario.background_velocity)
            enemies_group.draw(window)

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

            window.blit(lib.cts.Dialog_box, [400, 800])

            window.blit(lib.cts.Field_0, [0, 0])

            lib.frames_per_second(fps, 1)

    if not run and death:
        run = True

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
