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
            self.image = lib.cts.Plant_2
        elif self.thing == 19:
            self.image = lib.cts.Plant_1
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
        self.velocity = [0, 0]

    def change_image(self):
        if self.buff == 1:
            self.image = lib.cts.Extra_life
        elif self.buff == 2:
            self.image = lib.cts.Extra_energy
        elif self.buff == 3:
            self.image = lib.cts.Drake_smash
        elif self.buff == 4:
            self.image = lib.cts.Wings
        elif self.buff == 5:
            self.image = lib.cts.Coffee

    def get_buff(self):
        return self.image

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


class Generator(pg.sprite.Sprite):
    def __init__(self, position):
        super(Generator, self).__init__()

        self.image = lib.cts.Hole
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]

        self.temp = 60

    def update(self):
        self.temp -= 1
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


class GeneratedEnemy(pg.sprite.Sprite):
    def __init__(self, position, sprite_sets):
        super(GeneratedEnemy, self).__init__()

        # Settings
        self.current_animation = 1
        self.current_direction = 0

        # Setting sprites sets
        self.angle = lib.rd.randrange(360)
        self.velocity = [6, 6]

        # Images
        self.set = sprite_sets
        self.image = self.set[self.current_direction][self.current_animation]

        # Position
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def selected(self):
        if self.angle <= 315:
            self.current_direction = 3
        if self.angle <= 225:
            self.current_direction = 2
        if self.angle <= 135:
            self.current_direction = 1
        if self.angle <= 45:
            self.current_direction = 0

    def animate(self):
        self.selected()
        if self.velocity != [0, 0]:
            if self.current_animation < 2:
                self.current_animation += 1
            else:
                self.current_animation = 0
        self.image = self.set[self.current_direction][self.current_animation]

    def update(self, scenario_velocity):
        self.rect.x += self.velocity[0] * lib.mt.cos(lib.mt.radians(self.angle))
        self.rect.y -= self.velocity[1] * lib.mt.sin(lib.mt.radians(self.angle))
        self.rect.x -= scenario_velocity[0]
        self.rect.y += scenario_velocity[1]
        self.animate()


class SimpleEnemy(pg.sprite.Sprite):
    def __init__(self, position, sprite_sets):
        super(SimpleEnemy, self).__init__()

        # Statistics
        self.life = 0
        self.dodge = 0
        self.damage = 0
        self.lose_turn = 0
        self.progressive_damage = 0

        self.enemy_attacks = None

        self.statistics = [1110, 0]

        # Animation
        self.current_animation = 1

        # Enemy images
        self.set = sprite_sets
        self.attacks_set = sprite_sets
        self.change_images()
        self.image = self.set[self.current_animation]

        # Position
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]
        self.angle = 0

    def get_position(self):
        return [self.rect.x, self.rect.y]

    def enemy_attack(self, damage):
        if self.attacks_set == 1:
            chosen = lib.random_range(0, 3)
            if chosen == 0:
                # mordida
                lib.music_play(lib.cts.Snake_Attack)
                self.damage = 2
            if chosen == 1:
                # veneno
                lib.music_play(lib.cts.Snake_Poison)
                self.progressive_damage += 3
            if chosen == 2:
                self.dodge = True
            if self.dodge:

                # esquivar
                lib.music_play(lib.cts.Dodge)
                self.dodge = False
            else:
                self.life -= damage

            attack = lib.write(self.enemy_attacks[chosen], 30, 2)
            return attack
        if self.attacks_set == 2:
            chosen = lib.random_range(0, 3)
            if chosen == 0:
                # Grita SMAH!!
                lib.music_play(lib.cts.Smash)
                self.damage = 4
            if chosen == 1:
                # Sonido como de gruñido
                lib.music_play(lib.cts.Growl)
                self.lose_turn = 1
            if chosen == 2:
                # Esta comido algo duro
                lib.music_play(lib.cts.Eating)
                self.life += 1

            self.life -= damage

            attack = lib.write(self.enemy_attacks[chosen], 30, 2)
            return attack
        if self.attacks_set == 3:
            chosen = lib.random_range(0, 4)
            if chosen == 0:
                # proyectil arcano
                lib.music_play(lib.cts.Magic_Spell)
                self.damage = 4
            if chosen == 1:
                # Amaterasu de naruto, algo similar
                lib.music_play(lib.cts.Amaterasu)
                self.progressive_damage = 2
            if chosen == 2:
                self.dodge = True
                self.life += 1
            if chosen == 3:
                # Me perteneces pero en ingles
                lib.music_play(lib.cts.Youre_Mine, 0, 3.0)
                self.lose_turn = 1

            if self.dodge:

                # Barrera magica
                lib.music_play(lib.cts.Magic_Shield)
                self.dodge = False
            else:
                self.life -= damage

            attack = lib.write(self.enemy_attacks[chosen], 30, 2)
            return attack

    def change_images(self):
        if self.set == 1:
            self.life = 5
            self.set = lib.cts.Enemy_1
            self.enemy_attacks = lib.cts.Enemy_1_attacks
        elif self.set == 2:
            self.life = 8
            self.set = lib.cts.Enemy_2
            self.enemy_attacks = lib.cts.Enemy_2_attacks
        elif self.set == 3:
            self.life = 12
            self.set = lib.cts.Enemy_3
            self.enemy_attacks = lib.cts.Enemy_3_attacks

    def show_statistics(self, screen):
        for _ in range(self.life):
            screen.blit(lib.cts.Hearts, [self.statistics[0], self.statistics[1]])
            self.statistics[0] -= 20
        self.statistics = [1180, 0]

    def in_combat(self, screen):
        if self.attacks_set == 1:
            screen.blit(lib.cts.Enemy_1_in_combat, [700, 50])
        if self.attacks_set == 2:
            screen.blit(lib.cts.Enemy_2_in_combat, [700, 100])
        if self.attacks_set == 3:
            screen.blit(lib.cts.Enemy_3_in_combat, [600, 200])

    def animate(self):
        if self.velocity != [0, 0]:
            if self.current_animation < 2:
                self.current_animation += 1
            else:
                self.current_animation = 0
        else:
            self.current_animation = 1
        self.image = self.set[self.current_animation]

    def update(self, scenario_velocity):
        self.animate()
        self.rect.x += self.velocity[0] * lib.mt.cos(self.angle) - scenario_velocity[0]
        self.rect.y += self.velocity[1] * lib.mt.sin(self.angle) + scenario_velocity[1]


class Boss(pg.sprite.Sprite):
    def __init__(self, position):
        super(Boss, self).__init__()

        # Animation
        self.current_animation = 1

        # Boss images
        self.set = lib.cts.Enemy_3
        self.image = self.set[self.current_animation]

        # Position
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.velocity = [0, 0]
        self.angle = 0

        # Setting
        self.temp = 100
        self.cont = 40

    def get_position(self):
        return [self.rect.x, self.rect.y]

    def animate(self):
        if self.velocity != [0, 0]:
            if self.current_animation < 2:
                self.current_animation += 1
            else:
                self.current_animation = 0
        else:
            self.current_animation = 1
        self.image = self.set[self.current_animation]

    def update(self, scenario_velocity):
        self.animate()
        self.cont -= 1
        self.temp -= 1
        self.rect.x += self.velocity * lib.mt.cos(self.angle)
        self.rect.y += self.velocity * lib.mt.sin(self.angle)
        self.rect.x -= scenario_velocity[0]
        self.rect.y += scenario_velocity[1]


class Attack(pg.sprite.Sprite):
    def __init__(self, position):
        super(Attack, self).__init__()

        # Bullet creation
        self.image = pg.Surface([10, 10])
        self.image.fill(lib.cts.WHITE)

        #
        self.rect = self.image.get_rect()
        self.velocity = 0
        self.angle = 0

        # Setting
        self.rect.x, self.rect.y = position

    def update(self, scenario_velocity):
        self.rect.x += self.velocity * lib.mt.cos(self.angle)
        self.rect.y += self.velocity * lib.mt.sin(self.angle)
        self.rect.x -= scenario_velocity[0]
        self.rect.y += scenario_velocity[1]


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
        self.damage = 0
        self.collides = collides

        # Statistics
        self.lvl = 1
        self.live = 10
        self.energy = 0
        self.wings_buff = 0
        self.extra_live = 0
        self.drake_smash = 10
        self.extra_energy = 1
        self.transformation = False

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

    def in_combat(self, screen):
        if self.transformation:
            screen.blit(self.set[5], [50, 50])
        else:
            screen.blit(self.set[6], [50, 200])

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

        self.statistics = [1170, 20]

        for _ in range(self.extra_live):
            screen.blit(lib.cts.Extra_life, [self.statistics[0], self.statistics[1]])
            self.statistics[0] -= 20

        self.statistics = [1170, 40]

        for _ in range(self.extra_energy):
            screen.blit(lib.cts.Extra_energy, [self.statistics[0], self.statistics[1]])
            self.statistics[0] -= 20

        self.statistics = [1170, 60]

        for _ in range(self.wings_buff):
            screen.blit(lib.cts.Wings, [self.statistics[0], self.statistics[1]])
            self.statistics[0] -= 20

        self.statistics = [0, 0]

    def update(self, key_pressed, screen):
        self.animate(key_pressed)

        if self.velocity[0] != 0 and self.wings_buff > 0:
            self.rect.x += self.velocity[0] * self.wings_buff * 2
        else:
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

        if self.velocity[1] != 0 and self.wings_buff > 0:
            self.rect.y += self.velocity[1] * self.wings_buff * 2
        else:
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


def attack_bomb(boss_attacking):
    direction = 0
    while direction <= 360:
        bullet = Attack(boss_attacking.rect.center)
        bullet.velocity = 8
        bullet.angle = direction
        attack_group.add(bullet)

        bullet = Attack(boss_attacking.rect.center)
        bullet.velocity = -8
        bullet.angle = direction
        attack_group.add(bullet)
        direction += 30


def attack_angelic_bomb(boss_attacking):
    direction = 0
    while direction < 360:
        bullets = Attack(boss_attacking.rect.center)
        bullets.velocity = 7
        bullets.angle = direction
        attack_group.add(bullets)

        bullets = Attack(boss_attacking.rect.center)
        bullets.velocity = -7
        bullets.angle = direction
        attack_group.add(bullets)

        bullets = Attack(boss_attacking.rect.center)
        bullets.velocity = 7
        bullets.angle = direction
        attack_group.add(bullets)

        bullets = Attack(boss_attacking.rect.center)
        bullets.velocity = -7
        bullets.angle = direction
        attack_group.add(bullets)
        direction += 3


def attack_spiral(boss_attacking):
    bullets = Attack(boss_attacking.rect.center)
    bullets.velocity = 10
    bullets.angle = 0
    attack_group.add(bullets)
    for bullets in attack_group:
        bullets.angle += 0.2


if __name__ == '__main__':
    # init()

    pg.init()
    pg.font.init()
    pg.mixer.init()

    # Whiles

    run = True
    end = True
    death = False
    intro = False
    room_1 = False
    room_2 = False
    field_1 = False
    field_2 = False
    field_3 = True
    in_combat = False
    start_menu = True

    # Windows constants

    window = lib.new_window("Intro")
    fps = lib.frames_per_second_basics()

    # Groups

    # while writing

    statistics_information = pg.sprite.Group()
    inventory_information = pg.sprite.Group()
    attacks_information = pg.sprite.Group()
    abilities_in_combat = pg.sprite.Group()
    enemies_in_combat = pg.sprite.Group()
    holes_dialogue = pg.sprite.Group()
    dialogue_group = pg.sprite.Group()
    title_group = pg.sprite.Group()
    text_group = pg.sprite.Group()
    win_group = pg.sprite.Group()

    # while playing

    random_enemies_group = pg.sprite.Group()
    generators_group = pg.sprite.Group()
    players_group = pg.sprite.Group()
    enemies_group = pg.sprite.Group()
    flowers_group = pg.sprite.Group()
    attack_group = pg.sprite.Group()
    things_group = pg.sprite.Group()
    buffs_group = pg.sprite.Group()
    boss_group = pg.sprite.Group()
    NPCs_group = pg.sprite.Group()

    # Variables

    key = 0
    cont = 0
    speed = 5
    catchable = 0
    enemy_ability = None

    # Enemies variables

    angle = 0
    radio = 300
    distance = [0, 0]

    # Boss variables

    attack_before_pause = 4
    temp_while_shoting = 20
    attack_direction = 0
    current_attack = 1

    # Intro

    # Game title

    Title = Texts([300, 250], window, lib.cts.euphoria, 200)
    Title.velocity = [0, 0]
    title_group.add(Title)

    # Game intro

    new_text_position = [50, 750]
    for _ in range(0, len(lib.cts.euphoria_intro)):
        lib.music_play(lib.cts.Intro_3)
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
                lib.music_stop()
            if event.type == pg.MOUSEBUTTONDOWN:
                intro = False
                lib.music_stop()

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

    # Cleaning and Updating window

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

            # Player movement & Interactions

            if event.type == pg.KEYDOWN:
                key = 1
                if event.key == pg.K_s:
                    player.velocity[1] += player.speed
                    player.action = 3
                    lib.music_play(lib.cts.Running_Loud, -1, 1.0)
                if event.key == pg.K_w:
                    player.velocity[1] -= player.speed
                    player.action = 1
                    lib.music_play(lib.cts.Running_Loud, -1, 1.0)
                if event.key == pg.K_d:
                    player.velocity[0] += player.speed
                    player.action = 0
                    lib.music_play(lib.cts.Running_Loud, -1, 1.0)
                if event.key == pg.K_a:
                    player.velocity[0] -= player.speed
                    player.action = 2
                    lib.music_play(lib.cts.Running_Loud, -1, 1.0)
                if event.key == pg.K_e and catchable:
                    for _ in buffs_group:
                        lib.music_play(lib.cts.Drink)
                        buffs_group.remove(_)
                    player.live = 10
                    catchable = 0
            if event.type == pg.KEYUP:
                lib.music_stop()
                player.velocity = [0, 0]
                key = 0

        # Next room condition

        if player.rect.bottom == 462 and player.rect.left < 505 and player.rect.right > 472:
            room_1 = False

        # Drawing

        lib.fill(window)

        scenario.update()

        if 550 < player.rect.x < 585 and 270 > player.rect.y > 230 and len(buffs_group) == 1:
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
    lib.music_play(lib.cts.Wooden_Door)

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

    right_limit = Things([920, 212], 1)
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

    coffee = Buffs([745, 435], 5)
    buffs_group.add(coffee)

    # Adding text interactions

    potion = Texts([250, 70], window, lib.cts.dialogue_2, 30, 2)
    potion.velocity = [0, 1]
    text_group.add(potion)

    ring_without_potion = Texts([250, 70], window, lib.cts.dialogue_2_1, 30, 2)
    ring_without_potion.velocity = [0, 1]
    text_group.add(ring_without_potion)

    ring = Texts([250, 70], window, lib.cts.dialogue_3, 30, 2)
    ring.velocity = [0, 1]
    text_group.add(ring)

    cup = Texts([250, 70], window, lib.cts.dialogue_3_1, 30, 2)
    cup.velocity = [0, 1]
    text_group.add(cup)

    while run and room_2:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            # Player movement & interactions

            if event.type == pg.KEYDOWN:
                key = 1
                if event.key == pg.K_s:
                    player.velocity[1] += player.speed
                    player.action = 3
                    lib.music_play(lib.cts.Running_Loud, -1, 1.0)
                if event.key == pg.K_w:
                    player.velocity[1] -= player.speed
                    player.action = 1
                    lib.music_play(lib.cts.Running_Loud, -1, 1.0)
                if event.key == pg.K_d:
                    player.velocity[0] += player.speed
                    player.action = 0
                    lib.music_play(lib.cts.Running_Loud, -1, 1.0)
                if event.key == pg.K_a:
                    player.velocity[0] -= player.speed
                    player.action = 2
                    lib.music_play(lib.cts.Running_Loud, -1, 1.0)
                if event.key == pg.K_e and catchable:
                    buffs_group.remove(energy)
                    text_group.remove(potion)
                    lib.music_play(lib.cts.Drink)
                    if len(buffs_group) > 1:
                        player.energy += 5
                    catchable = 0
                if event.key == pg.K_q and len(buffs_group) == 2 and catchable:
                    buffs_group.remove(smash)
                    lib.music_play(lib.cts.Drink)
                    if len(buffs_group) > 0:
                        player.drake_smash += 1
                    catchable = 0
                if event.key == pg.K_r and catchable and player.live > 1:
                    player.energy += 1
                    player.live -= 1
                    catchable = 0
                    lib.music_play(lib.cts.Drink)
            if event.type == pg.KEYUP:
                player.velocity = [0, 0]
                key = 0

        # Next field condition

        if player.rect.bottom == 520 and player.rect.left < 450 and player.rect.right > 430:
            room_2 = False

        # Drawing

        lib.fill(window)

        scenario.update()

        if 665 < player.rect.x < 690 and 385 > player.rect.y > 360:
            if potion.y > 80:
                potion.velocity = [0, 0]

            if len(buffs_group) > 2:
                potion.update()

            catchable = 1
        else:
            potion.rect = [250, 70]

            if 870 < player.rect.x < 900 and player.rect.y <= 232:
                if ring.y > 80:
                    ring.velocity = [0, 0]

                if ring_without_potion.y > 80:
                    ring_without_potion.velocity = [0, 0]

                if len(buffs_group) == 3:
                    ring_without_potion.update()
                else:
                    if len(buffs_group) == 2:
                        ring.update()
                        catchable = 1
            else:
                ring_without_potion.rect = [250, 70]
                ring.rect = [250, 70]
                catchable = 0

        if 760 < player.rect.x < 780 and 455 > player.rect.y > 420:
            if cup.y > 80:
                cup.velocity = [0, 0]

            if player.live > 1:
                cup.update()

            catchable = 1
        else:
            if len(buffs_group) == 1:
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

    for _ in buffs_group:
        buffs_group.remove(_)

    # Background settings

    current_scenario = 3
    scenario.background = current_scenario
    lib.music_play(lib.cts.Wooden_Door)
    # Background position

    scenario.change_image()
    scenario.rect.x, scenario.rect.y = [-100, -250]

    # Repositioning player

    player.rect.x = 700
    player.rect.y = 350

    # Adding enemies

    angle = 0
    radio = 300
    distance = [0, 0]

    first_enemy_position = [[1400, 600]]

    enemy = SimpleEnemy(first_enemy_position[0], 1)
    enemies_group.add(enemy)

    # Adding things

    flowers = [[685, 20], [685, 35], [705, 20], [705, 35], [705, 50],
               [705, 65], [725, 20], [725, 35], [725, 50], [725, 65],
               [725, 80], [725, 95], [745, 20], [745, 35], [745, 50],
               [745, 65], [745, 80], [745, 95], [765, 20], [765, 35],
               [765, 50], [765, 65], [765, 80], [765, 95], [785, 20],
               [785, 35], [785, 50], [785, 65], [785, 80], [785, 95],
               [805, 50], [805, 65], [805, 80], [805, 95], [805, 20],
               [805, 35], [825, 80], [825, 95], [825, 20], [825, 35],
               [825, 50], [825, 65]]

    for _ in range(len(flowers)):
        flower = Things(flowers[_], lib.rd.randrange(19, 21))
        things_group.add(flower)

    trees = [[100, 800], [75, 80], [350, -180], [1450, 400]]

    for _ in range(len(trees)):
        flower = Things(trees[_], lib.rd.randrange(16, 17))
        things_group.add(flower)

    house = Things([500, 0], 21)
    things_group.add(house)

    # NPCs

    Manuela = NonPlayableCharacters([750, 300], 1)
    NPCs_group.add(Manuela)

    # Generators

    cont = [[1500, 30]]

    for _ in range(len(cont)):
        generator = Generator(cont[_])
        generators_group.add(generator)

    # Text interactions

    new_text_position = [30, 450]

    for _ in range(0, len(lib.cts.dialogue_4)):
        warden = Texts(new_text_position, window, lib.cts.dialogue_4[_], 30, 2)
        warden.velocity = [0, 0]
        new_text_position[1] += 25
        text_group.add(warden)

    new_text_position = [450, 450]

    for _ in range(0, len(lib.cts.dialogue_5)):
        dialogue = Texts(new_text_position, window, lib.cts.dialogue_5[_], 30, 2)
        dialogue.velocity = [0, 0]
        new_text_position[1] += 25
        dialogue_group.add(dialogue)

    holes_dialogue = Texts([450, 450], window, lib.cts.dialogue_7_2, 30, 2)
    holes_dialogue.velocity = [0, 0]

    new_text_position = [50, 450]

    for _ in range(0, len(lib.cts.Player_attacks) - 2):
        abilities = Texts(new_text_position, window, lib.cts.Player_attacks[_], 20, 2)
        abilities.velocity = [0, 0]
        abilities_in_combat.add(abilities)
        new_text_position[1] += 50

    new_text_position = [450, 450]

    for _ in range(3, len(lib.cts.Player_attacks)):
        abilities = Texts(new_text_position, window, lib.cts.Player_attacks[_], 20, 2)
        abilities.velocity = [0, 0]
        abilities_in_combat.add(abilities)
        new_text_position[1] += 50

    new_text_position = [50, 450]

    for _ in range(0, len(lib.cts.Player_inventory)):
        inventory = Texts(new_text_position, window, lib.cts.Player_inventory[_], 20, 2)
        inventory.velocity = [0, 0]
        inventory_information.add(inventory)
        new_text_position[1] += 50

    new_text_position = [50, 450]

    for _ in range(0, len(lib.cts.dialogue_6)):
        attack_information = Texts(new_text_position, window, lib.cts.dialogue_6[_], 30, 2)
        attack_information.velocity = [0, 0]
        new_text_position[1] += 25
        attacks_information.add(attack_information)

    new_text_position = [50, 450]

    for _ in range(0, len(lib.cts.dialogue_7)):
        energy_information = Texts(new_text_position, window, lib.cts.dialogue_7[_], 30, 2)
        energy_information.velocity = [0, 0]
        new_text_position[1] += 25
        statistics_information.add(energy_information)

    win = Texts([400, 300], window, lib.cts.dialogue_7_1, 80, 2, lib.cts.GOLD)
    win_group.add(win)

    # Setting variables

    catchable = True

    # Main loop (Field 1)

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

                # Player movement

                if event.type == pg.KEYDOWN:
                    key = 1
                    if event.key == pg.K_s:
                        player.velocity[1] += player.speed
                        player.action = 3
                        lib.music_play(lib.cts.Running, -1, 1.0)
                    if event.key == pg.K_w:
                        player.velocity[1] -= player.speed
                        player.action = 1
                        lib.music_play(lib.cts.Running, -1, 1.0)
                    if event.key == pg.K_d:
                        player.velocity[0] += player.speed
                        player.action = 0
                        lib.music_play(lib.cts.Running, -1, 1.0)
                    if event.key == pg.K_a:
                        player.velocity[0] -= player.speed
                        player.action = 2
                        lib.music_play(lib.cts.Running, -1, 1.0)
                    if event.key == pg.K_e:
                        catchable = False
                if event.type == pg.KEYUP:
                    player.velocity = [0, 0]
                    key = 0
                    lib.music_stop()

            # Control

            # Next field condition

            if player.rect.x == 1150 and 360 < player.rect.y < 520:
                if scenario.rect[0] == -600 and scenario.rect[1] == -625:
                    in_combat = False
                    field_1 = False

            # Scenario movement

            if player.rect.x > scenario.screen_limits[0]:
                player.rect.x = scenario.screen_limits[0]
                if scenario.rect.x > scenario.background_limits[0]:
                    scenario.background_velocity[0] = 5
                    for _ in things_group:
                        _.thing_velocity[0] = -5
                    for _ in generators_group:
                        _.velocity[0] = -5
                    for _ in buffs_group:
                        _.velocity[0] = -5
                    Manuela.npc_velocity[0] = -5

                else:
                    scenario.background_velocity[0] = 0
                    for _ in things_group:
                        _.thing_velocity[0] = 0
                    for _ in generators_group:
                        _.velocity[0] = 0
                    for _ in buffs_group:
                        _.velocity[0] = 0
                    Manuela.npc_velocity[0] = 0
            else:
                if player.rect.x < lib.cts.width - scenario.screen_limits[0]:
                    player.rect.x = lib.cts.width - scenario.screen_limits[0]
                    if scenario.rect.x < lib.cts.width + scenario.background_limits[0] * 2:
                        scenario.background_velocity[0] = -5
                        for _ in things_group:
                            _.thing_velocity[0] = 5
                        for _ in generators_group:
                            _.velocity[0] = 5
                        for _ in buffs_group:
                            _.velocity[0] = 5
                        Manuela.npc_velocity[0] = 5
                    else:
                        scenario.background_velocity[0] = 0
                        for _ in things_group:
                            _.thing_velocity[0] = 0
                        for _ in generators_group:
                            _.velocity[0] = 0
                        for _ in buffs_group:
                            _.velocity[0] = 0
                        Manuela.npc_velocity[0] = 0
                else:
                    if scenario.rect.x > lib.cts.width + scenario.background_limits[0]:
                        scenario.background_velocity[0] = 5
                        for _ in things_group:
                            _.thing_velocity[0] = -5
                        for _ in generators_group:
                            _.velocity[0] = -5
                        for _ in buffs_group:
                            _.velocity[0] = -5
                        Manuela.npc_velocity[0] = -5
                    else:
                        scenario.background_velocity[0] = 0
                        for _ in things_group:
                            _.thing_velocity[0] = 0
                        for _ in generators_group:
                            _.velocity[0] = 0
                        for _ in buffs_group:
                            _.velocity[0] = 0
                        Manuela.npc_velocity[0] = 0

            if player.rect.y > scenario.screen_limits[1]:
                player.rect.y = scenario.screen_limits[1]
                if scenario.rect.y > scenario.background_limits[1]:
                    scenario.background_velocity[1] = -5
                    for _ in things_group:
                        _.thing_velocity[1] = -5
                    for _ in generators_group:
                        _.velocity[1] = -5
                    for _ in buffs_group:
                        _.velocity[1] = -5
                    Manuela.npc_velocity[1] = -5
                else:
                    scenario.background_velocity[1] = 0
                    for _ in things_group:
                        _.thing_velocity[1] = 0
                    for _ in generators_group:
                        _.velocity[1] = 0
                    for _ in buffs_group:
                        _.velocity[1] = 0
                    Manuela.npc_velocity[1] = 0
            else:
                if player.rect.y < lib.cts.height - scenario.screen_limits[1]:
                    player.rect.y = lib.cts.height - scenario.screen_limits[1]
                    if scenario.rect.y < 0:
                        scenario.background_velocity[1] = 5
                        for _ in things_group:
                            _.thing_velocity[1] = 5
                        for _ in generators_group:
                            _.velocity[1] = 5
                        for _ in buffs_group:
                            _.velocity[1] = 5
                        Manuela.npc_velocity[1] = 5
                    else:
                        scenario.background_velocity[1] = 0
                        for _ in things_group:
                            _.thing_velocity[1] = 0
                        for _ in generators_group:
                            _.velocity[1] = 0
                        for _ in buffs_group:
                            _.velocity[1] = 0
                        Manuela.npc_velocity[1] = 0
                else:
                    if scenario.rect.y > lib.cts.height + scenario.background_limits[1]:
                        scenario.background_velocity[1] = -5
                        for _ in things_group:
                            _.thing_velocity[1] = -5
                        for _ in generators_group:
                            _.velocity[1] = -5
                        for _ in buffs_group:
                            _.velocity[1] = -5
                        Manuela.npc_velocity[1] = -5
                    else:
                        scenario.background_velocity[1] = 0
                        for _ in things_group:
                            _.thing_velocity[1] = 0
                        for _ in generators_group:
                            _.velocity[1] = 0
                        for _ in buffs_group:
                            _.velocity[1] = 0
                        Manuela.npc_velocity[1] = 0

            # Enemies

            enemy_collide = pg.sprite.spritecollide(player, enemies_group, True)

            for enemy in enemy_collide:
                lib.music_play(lib.cts.Snake_Attack)
                enemies_in_combat.add(enemy)
                player.velocity = [0, 0]
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

                if ((distance[0] >= -2) and (distance[0] <= 2)) and ((distance[1] >= -2) and (distance[1] <= 2)):
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

            # Generators

            generator_collide = pg.sprite.spritecollide(player, generators_group, False)

            for generator in generator_collide:
                if not catchable:
                    lib.music_play(lib.cts.GlassBreak)
                    potion = Buffs([generator.rect.x, generator.rect.y], lib.rd.randrange(1, 4))
                    buffs_group.add(potion)

                    lib.music_play(lib.cts.StepInGrass, 0, 3.0)
                    generators_group.remove(generator)

                    catchable = False

            for generator in generators_group:
                if generator.temp < 0:
                    raccoon = GeneratedEnemy(generator.rect.center, lib.cts.random_enemies_1)
                    random_enemies_group.add(raccoon)
                    generator.temp = 60

            # Cleaning raccoons

            for raccoon in random_enemies_group:
                if raccoon.rect.x < -50:
                    random_enemies_group.remove(raccoon)
                if raccoon.rect.y < -50:
                    random_enemies_group.remove(raccoon)
                if raccoon.rect.x > lib.cts.width:
                    random_enemies_group.remove(raccoon)
                if raccoon.rect.y > lib.cts.height:
                    random_enemies_group.remove(raccoon)

            # Generated enemies

            random_collide = pg.sprite.spritecollide(player, random_enemies_group, False)

            for random_enemies in random_collide:
                player.energy -= 1
                lib.music_play(lib.cts.Raccoon_Sound)
                random_enemies_group.remove(random_enemies)

            # Buffs

            buff_collide = pg.sprite.spritecollide(player, buffs_group, True)

            for buffs in buff_collide:
                if buffs.buff == 1:
                    player.extra_live += 1
                elif buffs.buff == 2:
                    player.extra_energy += 1
                elif buffs.buff == 3:
                    player.drake_smash += 1
                elif buffs.buff == 4:
                    player.wings_buff += 1

                buffs_group.remove(buffs)

            # Updating & Drawing

            lib.fill(window)

            scenario.update()

            first_enemy_position = scenario.move_enemies(first_enemy_position)

            generators_group.update()
            generators_group.draw(window)

            buffs_group.update()
            buffs_group.draw(window)

            random_enemies_group.update(scenario.background_velocity)
            random_enemies_group.draw(window)

            enemies_group.update(scenario.background_velocity)
            enemies_group.draw(window)

            things_group.update()
            things_group.draw(window)

            players_group.update(key, window)
            players_group.draw(window)

            NPCs_group.update()
            NPCs_group.draw(window)

            # Text interactions

            if 750 + scenario.rect.x < player.rect.x < 953 + scenario.rect.x:
                if 350 + scenario.rect.y > player.rect.y > 217 + scenario.rect.y:
                    lib.music_play(lib.cts.Hmm_Men, 0, 3.0)
                    window.blit(lib.cts.Dialog_box, [0, 400])
                    text_group.update()
                    lib.music_stop()
            if 790 + scenario.rect.x < player.rect.x < 830 + scenario.rect.x:
                if 650 + scenario.rect.y > player.rect.y > 300 + scenario.rect.y:
                    lib.music_play(lib.cts.Hmm_Men)
                    window.blit(lib.cts.Dialog_box, [400, 400])
                    dialogue_group.update()
                    lib.music_stop()
            generator_collide = pg.sprite.spritecollide(player, generators_group, False)

            for _ in generator_collide:
                lib.music_play(lib.cts.Hmm_Men, 0, 3.0)
                window.blit(lib.cts.Dialog_box, [400, 400])
                holes_dialogue.update()
                lib.music_stop()
            lib.frames_per_second(fps, 1)

        # Settings variables

        turn = 1
        catchable = True
        progressive = True

        while in_combat:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    run = False
                if event.type == pg.KEYDOWN and turn == 1:

                    # Player attacks

                    if event.key == pg.K_q:
                        if player.energy >= 1:
                            player.energy -= 1
                            player.damage = 1
                            cont = 0
                            turn = 0
                            lib.music_play(lib.cts.Punch)
                        else:
                            turn = 2
                            lib.music_play(lib.cts.Error)
                    if event.key == pg.K_w:
                        if player.energy >= 3:
                            player.energy -= 3
                            player.damage = 4
                            cont = 0
                            turn = 0
                            lib.music_play(lib.cts.Sword_Swing)
                        else:
                            turn = 2
                            lib.music_play(lib.cts.Error)
                    if event.key == pg.K_e:
                        if player.energy >= 5:
                            player.transformation = True
                            player.energy -= 5
                            player.damage = 0
                            player.live += 4
                            turn = 0
                            cont = 0
                            lib.music_play(lib.cts.Transformation_1)
                        else:
                            turn = 2
                            lib.music_play(lib.cts.Error)
                    if event.key == pg.K_r:
                        if player.energy >= 3:
                            if player.transformation:
                                player.energy -= 3
                                player.damage = 6
                                turn = 0
                                cont = 0
                                lib.music_play(lib.cts.Sound_Explosion_2)
                            else:
                                catchable = False
                                cont = 0
                                turn = 1
                        else:
                            turn = 2
                            lib.music_play(lib.cts.Error)
                    # Inventory
                    if event.key == pg.K_t:
                        lib.music_play(lib.cts.Map)
                        turn = 3
                        cont = 0

                    if event.key == pg.K_a:
                        if player.drake_smash >= 1:
                            player.use_extras(3)
                            enemy.life = 0
                            cont = 0
                            turn = 0
                            lib.music_play(lib.cts.MagicFinal)
                        else:
                            turn = 2
                            lib.music_play(lib.cts.Error)
                    if event.key == pg.K_s:
                        if player.extra_live >= 1:
                            player.use_extras(1)
                            cont = 0
                            turn = 0
                            lib.music_play(lib.cts.Drink)
                        else:
                            turn = 2
                            lib.music_play(lib.cts.Error)
                    if event.key == pg.K_d:
                        if player.extra_energy >= 1:
                            lib.music_play(lib.cts.Drink)
                            player.use_extras(2)
                            cont = 0
                            turn = 0
                        else:
                            turn = 2
                            lib.music_play(lib.cts.Error)

                    # Skip turn
                    if event.key == pg.K_f:
                        lib.music_play(lib.cts.Lost)
                        cont = 0
                        turn = 0

                    # Restating variables

                    if turn == 0:
                        player.energy += 2

                    progressive = True

            # Drawing

            lib.fill(window)

            window.blit(lib.cts.Battle_ground, [0, 0])

            # Control

            # Enemies turn

            if turn == 0:
                for enemy in enemies_in_combat:
                    if cont == 0:
                        enemy_ability = enemy.enemy_attack(player.damage)
                        player.damage = 0

                    enemy.show_statistics(window)
                    enemy.in_combat(window)

                    if enemy.life <= 0:
                        enemies_in_combat.remove(enemy)
                    else:
                        window.blit(lib.cts.Dialog_box, [400, 400])
                        window.blit(enemy_ability, [450, 450])

                if cont > 100:
                    turn = 1
                cont += 1

            if len(enemies_in_combat) == 0:
                win_group.update()

                player.transformation = False

                if cont > 100:
                    player.velocity = [0, 0]
                    key = 0

                    in_combat = False
                    field_1 = True
                cont += 1

            # Player turn

            if turn == 1:
                for enemy in enemies_in_combat:
                    lib.music_play(lib.cts.Pain)
                    player.live -= enemy.damage

                    if enemy.progressive_damage > 0 and progressive:
                        lib.music_play(lib.cts.Pain)
                        enemy.progressive_damage -= 1
                        progressive = False
                        player.live -= 1

                    enemy.damage = 0

                if player.live <= 0:
                    lib.music_play(lib.cts.Fail)
                    in_combat = False
                    field_1 = False
                    death = True
                player.in_combat(window)

                window.blit(lib.cts.Combat_box, [0, 400])

                player.show_statistics(window)

                if catchable:
                    abilities_in_combat.update()
                    cont = 0
                else:
                    attacks_information.update()
                    if cont > 100:
                        catchable = True
                        turn = 1
                    cont += 1

            # Informative turns

            if turn == 2:
                window.blit(lib.cts.Dialog_box, [0, 400])
                statistics_information.update()
                player.energy -= 2
                if cont > 100:
                    turn = 1
                cont += 1

            if turn == 3:
                window.blit(lib.cts.Dialog_box, [0, 400])
                inventory_information.update()
                if cont > 100:
                    turn = 1
                cont += 1

            lib.frames_per_second(fps, 1)

    # Cleaning

    for _ in things_group:
        things_group.remove(_)

    for _ in enemies_group:
        enemies_group.remove(_)

    for _ in text_group:
        text_group.remove(_)

    for _ in dialogue_group:
        dialogue_group.remove(_)

    for _ in NPCs_group:
        NPCs_group.remove(_)

    for _ in enemies_in_combat:
        enemies_in_combat.remove(_)

    for _ in win_group:
        win_group.remove(_)

    # Background

    current_scenario = 4
    scenario.background = current_scenario

    # Background position

    scenario.change_image()
    scenario.rect.x, scenario.rect.y = [0, -25]

    # Repositioning player

    player.rect.x = 40
    player.rect.y = 40

    # Adding enemies

    angle = 0
    radio = 200
    distance = [0, 0]
    first_enemy_position = [[500, 500], [800, 1000]]

    for _ in range(len(first_enemy_position)):
        enemy = SimpleEnemy(first_enemy_position[_], 2)
        enemies_group.add(enemy)

    # Adding things

    trees = [[265, 300], [800, 500], [550, 80], [1250, 600]]

    for _ in range(len(trees)):
        flower = Things(trees[_], lib.rd.randrange(16, 17))
        things_group.add(flower)

    cont = [[700, 200], [300, 800]]

    for _ in range(len(cont)):
        generator = Generator(cont[_])
        generators_group.add(generator)

    # Adding text interactions

    holes_dialogue = Texts([450, 450], window, lib.cts.dialogue_7_2, 30, 2)
    holes_dialogue.velocity = [0, 0]
    dialogue_group.add(holes_dialogue)

    win = Texts([400, 300], window, lib.cts.dialogue_7_1, 80, 2, lib.cts.GOLD)
    win_group.add(win)

    # Settings variables

    catchable = False

    # Main loop (Field 2)

    while run and field_2 or in_combat:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        while field_2:

            # Player control

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
                        lib.music_play(lib.cts.Running, -1, 1.0)
                    if event.key == pg.K_w:
                        player.velocity[1] -= player.speed
                        player.action = 1
                        lib.music_play(lib.cts.Running, -1, 1.0)
                    if event.key == pg.K_d:
                        player.velocity[0] += player.speed
                        player.action = 0
                        lib.music_play(lib.cts.Running, -1, 1.0)
                    if event.key == pg.K_a:
                        player.velocity[0] -= player.speed
                        player.action = 2
                        lib.music_play(lib.cts.Running, -1, 1.0)
                    if event.key == pg.K_e:
                        catchable = True
                if event.type == pg.KEYUP:
                    player.velocity = [0, 0]
                    lib.music_stop()
                    key = 0

            # Control

            # Next field condition

            if player.rect.x == 1150 and 360 < player.rect.y < 480:
                if scenario.rect[0] == -620 and scenario.rect[1] == -625:
                    in_combat = False
                    field_2 = False

            # Scenario movement

            if player.rect.x > scenario.screen_limits[0]:
                player.rect.x = scenario.screen_limits[0]
                if scenario.rect.x > scenario.background_limits[0]:
                    scenario.background_velocity[0] = 5
                    for _ in things_group:
                        _.thing_velocity[0] = -5
                    for _ in generators_group:
                        _.velocity[0] = -5

                else:
                    scenario.background_velocity[0] = 0
                    for _ in things_group:
                        _.thing_velocity[0] = 0
                    for _ in generators_group:
                        _.velocity[0] = 0
            else:
                if player.rect.x < lib.cts.width - scenario.screen_limits[0]:
                    player.rect.x = lib.cts.width - scenario.screen_limits[0]
                    if scenario.rect.x < lib.cts.width + scenario.background_limits[0] * 2:
                        scenario.background_velocity[0] = -5
                        for _ in things_group:
                            _.thing_velocity[0] = 5
                        for _ in generators_group:
                            _.velocity[0] = 5
                    else:
                        scenario.background_velocity[0] = 0
                        for _ in things_group:
                            _.thing_velocity[0] = 0
                        for _ in generators_group:
                            _.velocity[0] = 0
                else:
                    if scenario.rect.x > lib.cts.width + scenario.background_limits[0]:
                        scenario.background_velocity[0] = 5
                        for _ in things_group:
                            _.thing_velocity[0] = -5
                        for _ in generators_group:
                            _.velocity[0] = -5
                    else:
                        scenario.background_velocity[0] = 0
                        for _ in things_group:
                            _.thing_velocity[0] = 0
                        for _ in generators_group:
                            _.velocity[0] = 0
            if player.rect.y > scenario.screen_limits[1]:
                player.rect.y = scenario.screen_limits[1]
                if scenario.rect.y > scenario.background_limits[1]:
                    scenario.background_velocity[1] = -5
                    for _ in things_group:
                        _.thing_velocity[1] = -5
                    for _ in generators_group:
                        _.velocity[1] = -5
                else:
                    scenario.background_velocity[1] = 0
                    for _ in things_group:
                        _.thing_velocity[1] = 0
                    for _ in generators_group:
                        _.velocity[1] = 0
            else:
                if player.rect.y < lib.cts.height - scenario.screen_limits[1]:
                    player.rect.y = lib.cts.height - scenario.screen_limits[1]
                    if scenario.rect.y < 0:
                        scenario.background_velocity[1] = 5
                        for _ in things_group:
                            _.thing_velocity[1] = 5
                        for _ in generators_group:
                            _.velocity[1] = 5
                    else:
                        scenario.background_velocity[1] = 0
                        for _ in things_group:
                            _.thing_velocity[1] = 0
                        for _ in generators_group:
                            _.velocity[1] = 0
                else:
                    if scenario.rect.y > lib.cts.height + scenario.background_limits[1]:
                        scenario.background_velocity[1] = -5
                        for _ in things_group:
                            _.thing_velocity[1] = -5
                        for _ in generators_group:
                            _.velocity[1] = -5
                    else:
                        scenario.background_velocity[1] = 0
                        for _ in things_group:
                            _.thing_velocity[1] = 0
                        for _ in generators_group:
                            _.velocity[1] = 0

            # Enemies

            enemy_collide = pg.sprite.spritecollide(player, enemies_group, True)

            for enemy in enemy_collide:
                lib.music_play(lib.cts.Demon_Scream)
                enemies_in_combat.add(enemy)
                in_combat = True
                field_2 = False

            # Enemies movement

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

                if ((distance[0] >= -2) and (distance[0] <= 2)) and ((distance[1] >= -2) and (distance[1] <= 2)):
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

                # Generators

                generator_collide = pg.sprite.spritecollide(player, generators_group, False)

                for generator in generator_collide:
                    if catchable:
                        potion = Buffs([generator.rect.x, generator.rect.y], lib.rd.randrange(1, 4))
                        buffs_group.add(potion)

                        generators_group.remove(generator)
                        catchable = False

                for generator in generators_group:
                    if generator.temp < 0:
                        worm = GeneratedEnemy(generator.rect.center, lib.cts.random_enemies_2)
                        random_enemies_group.add(worm)
                        generator.temp = 60

                # Worms cleaning

                for worm in random_enemies_group:
                    if worm.rect.x < -50:
                        random_enemies_group.remove(worm)
                    if worm.rect.y < -50:
                        random_enemies_group.remove(worm)
                    if worm.rect.x > lib.cts.width:
                        random_enemies_group.remove(worm)
                    if worm.rect.y > lib.cts.height:
                        random_enemies_group.remove(worm)

                # Generated enemies

                random_collide = pg.sprite.spritecollide(player, random_enemies_group, False)

                for random_enemies in random_collide:
                    lib.music_play(lib.cts.worm)
                    player.live -= 1
                    random_enemies_group.remove(random_enemies)

                # Buffs

                buff_collide = pg.sprite.spritecollide(player, buffs_group, True)

                for buffs in buff_collide:
                    if buffs.buff == 1:
                        player.extra_live += 1
                    elif buffs.buff == 2:
                        player.extra_energy += 1
                    elif buffs.buff == 3:
                        player.drake_smash += 1
                    elif buffs.buff == 4:
                        player.wings_buff += 1

                    buffs_group.remove(buffs)

                # Death by worms

                if player.live <= 0:
                    lib.music_play(lib.cts.Fail)
                    in_combat = False
                    field_2 = False
                    death = True
                    run = False

            # Drawing
            lib.fill(window)

            scenario.update()

            first_enemy_position = scenario.move_enemies(first_enemy_position)

            generators_group.update()
            generators_group.draw(window)

            buffs_group.update()
            buffs_group.draw(window)

            random_enemies_group.update(scenario.background_velocity)
            random_enemies_group.draw(window)

            enemies_group.update(scenario.background_velocity)
            enemies_group.draw(window)

            things_group.update()
            things_group.draw(window)

            players_group.update(key, window)
            players_group.draw(window)

            generator_collide = pg.sprite.spritecollide(player, generators_group, False)

            for generator in generator_collide:
                window.blit(lib.cts.Dialog_box, [400, 400])
                holes_dialogue.update()

            lib.frames_per_second(fps, 1)

        turn = 1
        catchable = True
        progressive = True

        while in_combat:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    run = False
                if event.type == pg.KEYDOWN and turn == 1:

                    progressive = True

                    if event.key == pg.K_q:
                        if player.energy >= 1:
                            player.energy -= 1
                            player.damage = 1
                            cont = 0
                            turn = 0
                        else:
                            turn = 2
                    if event.key == pg.K_w:
                        if player.energy >= 3:
                            player.energy -= 3
                            player.damage = 4
                            cont = 0
                            turn = 0
                        else:
                            turn = 2
                    if event.key == pg.K_e:
                        if player.energy >= 5:
                            player.transformation = True
                            player.energy -= 5
                            player.damage = 0
                            player.live += 4
                            turn = 0
                            cont = 0
                        else:
                            turn = 2
                    if event.key == pg.K_r:
                        if player.energy >= 3:
                            if player.transformation:
                                player.energy -= 3
                                player.damage = 6
                                turn = 0
                                cont = 0
                            else:
                                catchable = False
                                cont = 0
                                turn = 1
                        else:
                            turn = 2

                    # Inventory
                    if event.key == pg.K_t:
                        turn = 3
                        cont = 0
                    if event.key == pg.K_a:
                        if player.drake_smash >= 1:
                            player.use_extras(3)
                            enemy.life = 0
                            cont = 0
                            turn = 0
                        else:
                            turn = 2
                    if event.key == pg.K_s:
                        if player.extra_live >= 1:
                            player.use_extras(1)
                            cont = 0
                            turn = 0
                        else:
                            turn = 2
                    if event.key == pg.K_d:
                        if player.extra_energy >= 1:
                            player.use_extras(2)
                            cont = 0
                            turn = 0
                        else:
                            turn = 2

                    # Skip turn
                    if event.key == pg.K_f:
                        cont = 0
                        turn = 0

                    if turn == 0:
                        player.energy += 2

            # Drawing

            lib.fill(window)

            window.blit(lib.cts.Battle_ground, [0, 0])

            # Control

            if turn == 0:
                for enemy in enemies_in_combat:
                    if cont == 0:
                        enemy_ability = enemy.enemy_attack(player.damage)
                        player.damage = 0

                    enemy.show_statistics(window)
                    enemy.in_combat(window)

                    if enemy.life <= 0:
                        enemies_in_combat.remove(enemy)
                    else:
                        window.blit(lib.cts.Dialog_box, [400, 400])
                        window.blit(enemy_ability, [450, 450])

                if cont > 100:
                    turn = 1
                cont += 1

            if len(enemies_in_combat) == 0:
                win_group.update()

                player.transformation = False

                if cont > 100:
                    player.velocity = [0, 0]
                    key = 0

                    in_combat = False
                    field_2 = True
                cont += 1

            if turn == 1:
                for enemy in enemies_in_combat:

                    player.live -= enemy.damage

                    if enemy.progressive_damage > 0 and progressive:
                        enemy.progressive_damage -= 1
                        progressive = False
                        player.live -= 1

                    enemy.damage = 0

                if player.live <= 0:
                    in_combat = False
                    field_2 = False
                    death = True

                player.in_combat(window)

                window.blit(lib.cts.Combat_box, [0, 400])

                player.show_statistics(window)

                if catchable:
                    abilities_in_combat.update()
                    cont = 0
                else:
                    attacks_information.update()
                    if cont > 100:
                        catchable = True
                        turn = 1
                    cont += 1

            if turn == 2:
                window.blit(lib.cts.Dialog_box, [0, 400])
                statistics_information.update()
                player.energy -= 2
                if cont > 100:
                    turn = 1
                cont += 1

            if turn == 3:
                window.blit(lib.cts.Dialog_box, [0, 400])
                inventory_information.update()
                if cont > 100:
                    turn = 1
                cont += 1

            lib.frames_per_second(fps, 1)

    for _ in enemies_group:
        enemies_group.remove(_)

    for _ in things_group:
        things_group.remove(_)

    for _ in generators_group:
        generators_group.remove(_)

    for _ in enemies_in_combat:
        enemies_in_combat.remove(_)

    for _ in random_enemies_group:
        random_enemies_group.remove(_)

    for _ in dialogue_group:
        dialogue_group.remove(_)

    for _ in win_group:
        win_group.remove(_)

    # Background
    current_scenario = 5
    scenario.background = current_scenario

    # Background position
    scenario.change_image()
    scenario.rect.x, scenario.rect.y = [0, -25]

    # Repositioning player
    player.rect.x = 50
    player.rect.y = 50

    angle = 0
    radio = 300
    distance = [0, 0]

    first_enemy_position = [[250, 300], [600, 500], [550, 850]]

    for _ in range(len(first_enemy_position)):
        enemy = SimpleEnemy(first_enemy_position[_], 1)
        enemies_group.add(enemy)

    Balzar = NonPlayableCharacters([200, 80], 2)
    NPCs_group.add(Balzar)
    key = 0

    new_text_position = [450, 430]
    for _ in range(0, len(lib.cts.dialogue_8)):
        new_text = Texts(new_text_position, window, lib.cts.dialogue_8[_], 25, 2)
        new_text.velocity = [0, 0]
        new_text_position[1] += 40
        text_group.add(new_text)

    new_text_position = [450, 430]
    for _ in range(0, len(lib.cts.dialogue_9)):
        new_text = Texts(new_text_position, window, lib.cts.dialogue_9[_], 25, 2)
        new_text.velocity = [0, 0]
        new_text_position[1] += 40
        dialogue_group.add(new_text)

    cont = 0

    boss_spawn = [200, 80]
    boss = Boss(boss_spawn)
    boss_group.add(boss)

    win = Texts([400, 300], window, lib.cts.dialogue_7_1, 80, 2, lib.cts.GOLD)
    win_group.add(win)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        while field_3:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    field_3 = False
                    run = False
                if event.type == pg.KEYDOWN:
                    key = 1
                    if event.key == pg.K_s:
                        player.velocity[1] += player.speed
                        player.action = 3
                        lib.music_play(lib.cts.Running, -1, 1.0)
                    if event.key == pg.K_w:
                        player.velocity[1] -= player.speed
                        player.action = 1
                        lib.music_play(lib.cts.Running, -1, 1.0)
                    if event.key == pg.K_d:
                        player.velocity[0] += player.speed
                        player.action = 0
                        lib.music_play(lib.cts.Running, -1, 1.0)
                    if event.key == pg.K_a:
                        player.velocity[0] -= player.speed
                        player.action = 2
                        lib.music_play(lib.cts.Running, -1, 1.0)
                if event.type == pg.KEYUP:
                    player.velocity = [0, 0]
                    lib.music_stop()
                    key = 0

            # Control

            # Background

            if player.rect.x > scenario.screen_limits[0]:
                player.rect.x = scenario.screen_limits[0]
                if scenario.rect.x > scenario.background_limits[0]:
                    scenario.background_velocity[0] = 5
                    for _ in things_group:
                        _.thing_velocity[0] = -5
                    Balzar.npc_velocity[0] = -5

                else:
                    scenario.background_velocity[0] = 0
                    for _ in things_group:
                        _.thing_velocity[0] = 0
                    Balzar.npc_velocity[0] = 0
            else:
                if player.rect.x < lib.cts.width - scenario.screen_limits[0]:
                    player.rect.x = lib.cts.width - scenario.screen_limits[0]
                    if scenario.rect.x < lib.cts.width * 2 + scenario.background_limits[0]:
                        scenario.background_velocity[0] = -5
                        for _ in things_group:
                            _.thing_velocity[0] = 5
                        Balzar.npc_velocity[0] = 5
                    else:
                        scenario.background_velocity[0] = 0
                        for _ in things_group:
                            _.thing_velocity[0] = 0
                        Balzar.npc_velocity[0] = 0
                else:
                    if scenario.rect.x > lib.cts.width - scenario.background_limits[0]:
                        scenario.background_velocity[0] = 5
                        for _ in things_group:
                            _.thing_velocity[0] = -5
                        Balzar.npc_velocity[0] = -5
                    else:
                        scenario.background_velocity[0] = 0
                        for _ in things_group:
                            _.thing_velocity[0] = 0
                        Balzar.npc_velocity[0] = 0

            if player.rect.y > scenario.screen_limits[1]:
                player.rect.y = scenario.screen_limits[1]
                if scenario.rect.y > scenario.background_limits[1]:
                    scenario.background_velocity[1] = -5
                    for _ in things_group:
                        _.thing_velocity[1] = -5
                    Balzar.npc_velocity[1] = -5
                else:
                    scenario.background_velocity[1] = 0
                    for _ in things_group:
                        _.thing_velocity[1] = 0
                    Balzar.npc_velocity[1] = 0
            else:
                if player.rect.y < lib.cts.height - scenario.screen_limits[1]:
                    player.rect.y = lib.cts.height - scenario.screen_limits[1]
                    if scenario.rect.y < 0:
                        scenario.background_velocity[1] = 5
                        for _ in things_group:
                            _.thing_velocity[1] = 5
                        Balzar.npc_velocity[1] = 5
                    else:
                        scenario.background_velocity[1] = 0
                        for _ in things_group:
                            _.thing_velocity[1] = 0
                        Balzar.npc_velocity[1] = 0
                else:
                    if scenario.rect.y > lib.cts.height - scenario.background_limits[1]:
                        scenario.background_velocity[1] = -5
                        for _ in things_group:
                            _.thing_velocity[1] = -5
                        Balzar.npc_velocity[1] = -5
                    else:
                        scenario.background_velocity[1] = 0
                        for _ in things_group:
                            _.thing_velocity[1] = 0
                        Balzar.npc_velocity[1] = 0

            # Enemies

            enemy_collide = pg.sprite.spritecollide(player, enemies_group, True)

            for enemy in enemy_collide:
                lib.music_play(lib.cts.Demon_Scream)
                enemies_in_combat.add(enemy)
                in_combat = True
                field_3 = False

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

                if ((distance[0] >= -2) and (distance[0] <= 2)) and ((distance[1] >= -2) and (distance[1] <= 2)):
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

            # Boss

            if len(enemies_group) == 0:
                attack_direction = 0
                i = 0
                for boss in boss_group:
                    if temp_while_shoting > 0:
                        boss.velocity = 0
                    else:
                        lib.music_play(lib.cts.Running_Loud, -1, 2.0)
                        distance = move_enemy(player.rect, boss.rect)
                        if distance[0] > 0:
                            boss.velocity = 3
                        else:
                            boss.velocity = -3

                        if ((distance[0] >= -2) and (distance[0] <= 2)) and (
                                (distance[1] >= -2) and (distance[1] <= 2)):
                            boss.velocity = 0
                        else:
                            if distance[0] == 0:
                                boss.velocity = -3
                                if distance[1] > 0:
                                    angle = lib.mt.radians(270)
                                if distance[1] < 0:
                                    angle = lib.mt.radians(90)
                            else:
                                angle = lib.mt.atan(distance[1] / distance[0])
                                boss.angle = angle
                        i += 1

                    if current_attack == 1:
                        if boss.temp < 0:
                            attack_bomb(boss)
                            temp_while_shoting = 15
                            if attack_before_pause == -2:
                                boss.temp = 200
                                attack_before_pause = 4
                            else:
                                boss.temp = 15
                                attack_before_pause -= 1

                    elif current_attack == 2:
                        if boss.temp < 0:
                            attack_angelic_bomb(boss)
                            temp_while_shoting = 15
                            if attack_before_pause == -50:
                                boss.temp = 200
                                attack_before_pause = 4
                            else:
                                boss.temp = 3
                                attack_before_pause -= 1

                    elif current_attack == 3:
                        if boss.temp < 0:
                            attack_spiral(boss)
                            temp_while_shoting = 15
                            if attack_before_pause == -200:
                                boss.temp = 200
                                attack_before_pause = 4
                            else:
                                boss.temp = 1
                                attack_before_pause -= 1

                temp_while_shoting -= 1

            attack_collide = pg.sprite.spritecollide(player, attack_group, True)

            for _ in attack_collide:
                attack_group.remove(_)
                player.live -= 1

            if player.live <= 0:
                in_combat = False
                field_3 = False
                death = True
                run = False

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

            if len(enemies_group) > 0:
                NPCs_group.update()
                NPCs_group.draw(window)

                if 200 + scenario.rect.x < player.rect.x < 250 + scenario.rect.x:
                    if 170 + scenario.rect.y > player.rect.y > 100 + scenario.rect.y:
                        window.blit(lib.cts.Dialog_box, [400, 400])
                        text_group.update()
            else:
                cont += 1

                if cont < 230:
                    lib.music_play(lib.cts.Evil_Laught_1)
                    window.blit(lib.cts.Dialog_box, [400, 400])
                    dialogue_group.update()

                if cont == 230:
                    NPCs_group.remove(Balzar)

                # if cont >= 500:
                current_attack = 2

                """

                if cont > 730:
                    current_attack = 2

                if cont > 2050:
                    current_attack = 3
                """

                if cont > 230:
                    distance = [0, 0]
                    if len(enemies_group) == 0:
                        boss_group.update(scenario.background_velocity)
                        boss_group.draw(window)

                        attack_group.update(scenario.background_velocity)
                        attack_group.draw(window)

                        for _ in attack_group:
                            if _.rect.x < 0:
                                attack_group.remove(_)
                            if _.rect.y < 0:
                                attack_group.remove(_)
                            if _.rect.x > lib.cts.width:
                                attack_group.remove(_)
                            if _.rect.y > lib.cts.height:
                                attack_group.remove(_)

            lib.frames_per_second(fps, 1)

        turn = 1
        catchable = True
        progressive = True

        while in_combat:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_combat = False
                    run = False
                if event.type == pg.KEYDOWN and turn == 1:

                    progressive = True

                    if event.key == pg.K_q:
                        if player.energy >= 1:
                            player.energy -= 1
                            player.damage = 1
                            cont = 0
                            turn = 0
                        else:
                            turn = 2
                    if event.key == pg.K_w:
                        if player.energy >= 3:
                            player.energy -= 3
                            player.damage = 4
                            cont = 0
                            turn = 0
                        else:
                            turn = 2
                    if event.key == pg.K_e:
                        if player.energy >= 5:
                            player.transformation = True
                            player.energy -= 5
                            player.damage = 0
                            player.live += 4
                            turn = 0
                            cont = 0
                        else:
                            turn = 2
                    if event.key == pg.K_r:
                        if player.energy >= 3:
                            if player.transformation:
                                player.energy -= 3
                                player.damage = 6
                                turn = 0
                                cont = 0
                            else:
                                catchable = False
                                cont = 0
                                turn = 1
                        else:
                            turn = 2

                    # Inventory
                    if event.key == pg.K_t:
                        turn = 3
                        cont = 0
                        lib.music_play(lib.cts.Map)
                    if event.key == pg.K_a:
                        if player.drake_smash >= 1:
                            player.use_extras(3)
                            enemy.life = 0
                            cont = 0
                            turn = 0
                        else:
                            turn = 2
                    if event.key == pg.K_s:
                        if player.extra_live >= 1:
                            player.use_extras(1)
                            cont = 0
                            turn = 0
                        else:
                            turn = 2
                    if event.key == pg.K_d:
                        if player.extra_energy >= 1:
                            player.use_extras(2)
                            cont = 0
                            turn = 0
                        else:
                            turn = 2

                    # Skip turn
                    if event.key == pg.K_f:
                        cont = 0
                        turn = 0

                    if turn == 0:
                        player.energy += 2

            # Drawing

            lib.fill(window)

            window.blit(lib.cts.Battle_ground, [0, 0])

            # Control

            if turn == 0:
                for enemy in enemies_in_combat:
                    if cont == 0:
                        enemy_ability = enemy.enemy_attack(player.damage)
                        player.damage = 0

                    enemy.show_statistics(window)
                    enemy.in_combat(window)

                    if enemy.life <= 0:
                        enemies_in_combat.remove(enemy)
                    else:
                        window.blit(lib.cts.Dialog_box, [400, 400])
                        window.blit(enemy_ability, [450, 450])

                if cont > 100:
                    turn = 1
                cont += 1

            if len(enemies_in_combat) == 0:
                win_group.update()

                player.transformation = False

                if cont > 100:
                    player.velocity = [0, 0]
                    key = 0

                    in_combat = False
                    field_3 = True
                cont += 1

            if turn == 1:
                for enemy in enemies_in_combat:

                    player.live -= enemy.damage

                    if enemy.progressive_damage > 0 and progressive:
                        enemy.progressive_damage -= 1
                        progressive = False
                        player.live -= 1

                    enemy.damage = 0

                if player.live <= 0:
                    in_combat = False
                    field_3 = False
                    death = True

                player.in_combat(window)

                window.blit(lib.cts.Combat_box, [0, 400])

                player.show_statistics(window)

                if catchable:
                    abilities_in_combat.update()
                    cont = 0
                else:
                    attacks_information.update()
                    if cont > 100:
                        catchable = True
                        turn = 1
                    cont += 1

            if turn == 2:
                window.blit(lib.cts.Dialog_box, [0, 400])
                statistics_information.update()
                player.energy -= 2
                if cont > 100:
                    turn = 1
                cont += 1

            if turn == 3:
                window.blit(lib.cts.Dialog_box, [0, 400])
                inventory_information.update()
                if cont > 100:
                    turn = 1
                cont += 1

            lib.frames_per_second(fps, 1)

    # Death

    for _ in title_group:
        title_group.remove(_)

    for _ in text_group:
        text_group.remove(_)

    cont = 0

    # Death title

    Title = Texts([200, 250], window, lib.cts.Death, 100)
    Title.velocity = [0, 0]
    title_group.add(Title)

    # Game end
    new_text_position = [50, 750]
    for _ in range(0, len(lib.cts.Death_interaction)):
        new_text = Texts(new_text_position, window, lib.cts.Death_interaction[_], 30, 2)
        new_text_position[1] += 50
        text_group.add(new_text)

    # Game button skip
    Skip = Texts([1080, 550], window, lib.cts.skip, 20)
    Skip.velocity = [0, 0]
    title_group.add(Skip)

    while not run and death:
        lib.music_play(lib.cts.End)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = True
            if event.type == pg.MOUSEBUTTONDOWN:
                death = False

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
            death = False

        lib.frames_per_second(fps, 2)

    pg.quit()
