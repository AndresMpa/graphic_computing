import pygame as pg

# Window size
width = 1200
height = 600

# Points
Default = [800, 200]
Origin = [600, 300]
size = [500, 200]
A = [-50, -100]
B = [-100, 50]
C = [100, 100]
D = [50, -100]
E = [700, 150]
F = [900, 180]
G = [50, 100]
H = [850, 30]

# Color
# RGB
RED = pg.Color(255, 0, 0)
GREEN = pg.Color(0, 255, 0)
BLUE = pg.Color(0, 0, 255)
# BASICS
HIGH = pg.Color(200, 200, 200)
MIDDLE = pg.Color(155, 155, 155)
LOW = pg.Color(55, 55, 55)
# ELEMENTARY
BLACK = pg.Color(0, 0, 0)
WHITE = pg.Color(255, 255, 255)
# EXTRAS
GOLD = pg.Color(210, 175, 55)
# COLOR PALETTE DEFAULT
PALETTE = [RED, GREEN, BLUE, HIGH, MIDDLE, LOW, WHITE]
# COLOR PALETTE #1
PALETTE_1 = [WHITE, GREEN, BLUE]
# COLOR PALETTE #2
PALETTE_2 = [RED, RED, GREEN, GREEN, BLUE, BLUE]

# IMAGES

# Heroes

Ship = pg.image.load("Images/ship.png")

Angel = [
    [pg.image.load("Images/Heroes/Angel/e1.png"),
     pg.image.load("Images/Heroes/Angel/e2.png"),
     pg.image.load("Images/Heroes/Angel/e3.png")],
    [pg.image.load("Images/Heroes/Angel/n1.png"),
     pg.image.load("Images/Heroes/Angel/n2.png"),
     pg.image.load("Images/Heroes/Angel/n3.png")],
    [pg.image.load("Images/Heroes/Angel/o1.png"),
     pg.image.load("Images/Heroes/Angel/o2.png"),
     pg.image.load("Images/Heroes/Angel/o3.png")],
    [pg.image.load("Images/Heroes/Angel/s1.png"),
     pg.image.load("Images/Heroes/Angel/s2.png"),
     pg.image.load("Images/Heroes/Angel/s3.png")],
    [pg.image.load("Images/Heroes/Angel/t1.png"),
     pg.image.load("Images/Heroes/Angel/t2.png"),
     pg.image.load("Images/Heroes/Angel/t3.png")],
    pg.image.load("Images/Heroes/Angel/t.png")]

Escanor = [
    [pg.image.load("Images/Heroes/Escanor/e1.png"),
     pg.image.load("Images/Heroes/Escanor/e2.png"),
     pg.image.load("Images/Heroes/Escanor/e3.png")],
    [pg.image.load("Images/Heroes/Escanor/n1.png"),
     pg.image.load("Images/Heroes/Escanor/n2.png"),
     pg.image.load("Images/Heroes/Escanor/n3.png")],
    [pg.image.load("Images/Heroes/Escanor/o1.png"),
     pg.image.load("Images/Heroes/Escanor/o2.png"),
     pg.image.load("Images/Heroes/Escanor/o3.png")],
    [pg.image.load("Images/Heroes/Escanor/s1.png"),
     pg.image.load("Images/Heroes/Escanor/s2.png"),
     pg.image.load("Images/Heroes/Escanor/s3.png")],
    [pg.image.load("Images/Heroes/Escanor/t1.png"),
     pg.image.load("Images/Heroes/Escanor/t2.png"),
     pg.image.load("Images/Heroes/Escanor/t3.png")],
    pg.image.load("Images/Heroes/Escanor/t.png")]

Luke = [
    [pg.image.load("Images/Heroes/Luke/e1.png"),
     pg.image.load("Images/Heroes/Luke/e2.png"),
     pg.image.load("Images/Heroes/Luke/e3.png")],
    [pg.image.load("Images/Heroes/Luke/n1.png"),
     pg.image.load("Images/Heroes/Luke/n2.png"),
     pg.image.load("Images/Heroes/Luke/n3.png")],
    [pg.image.load("Images/Heroes/Luke/o1.png"),
     pg.image.load("Images/Heroes/Luke/o2.png"),
     pg.image.load("Images/Heroes/Luke/o3.png")],
    [pg.image.load("Images/Heroes/Luke/s1.png"),
     pg.image.load("Images/Heroes/Luke/s2.png"),
     pg.image.load("Images/Heroes/Luke/s3.png")],
    [pg.image.load("Images/Heroes/Luke/t1.png"),
     pg.image.load("Images/Heroes/Luke/t2.png"),
     pg.image.load("Images/Heroes/Luke/t3.png")],
    pg.image.load("Images/Heroes/Luke/t.png"),
    pg.image.load("Images/Heroes/Luke/in_combat.png")]

Serafin = [
    [pg.image.load("Images/Heroes/Serafin/e1.png"),
     pg.image.load("Images/Heroes/Serafin/e2.png"),
     pg.image.load("Images/Heroes/Serafin/e3.png")],
    [pg.image.load("Images/Heroes/Serafin/n1.png"),
     pg.image.load("Images/Heroes/Serafin/n2.png"),
     pg.image.load("Images/Heroes/Serafin/n3.png")],
    [pg.image.load("Images/Heroes/Serafin/o1.png"),
     pg.image.load("Images/Heroes/Serafin/o2.png"),
     pg.image.load("Images/Heroes/Serafin/o3.png")],
    [pg.image.load("Images/Heroes/Serafin/s1.png"),
     pg.image.load("Images/Heroes/Serafin/s2.png"),
     pg.image.load("Images/Heroes/Serafin/s3.png")],
    [pg.image.load("Images/Heroes/Serafin/t1.png"),
     pg.image.load("Images/Heroes/Serafin/t2.png"),
     pg.image.load("Images/Heroes/Serafin/t3.png")],
    pg.image.load("Images/Heroes/Serafin/t.png")]

Sofia = [
    [pg.image.load("Images/Heroes/Sofia/e1.png"),
     pg.image.load("Images/Heroes/Sofia/e2.png"),
     pg.image.load("Images/Heroes/Sofia/e3.png")],
    [pg.image.load("Images/Heroes/Sofia/n1.png"),
     pg.image.load("Images/Heroes/Sofia/n2.png"),
     pg.image.load("Images/Heroes/Sofia/n3.png")],
    [pg.image.load("Images/Heroes/Sofia/o1.png"),
     pg.image.load("Images/Heroes/Sofia/o2.png"),
     pg.image.load("Images/Heroes/Sofia/o3.png")],
    [pg.image.load("Images/Heroes/Sofia/s1.png"),
     pg.image.load("Images/Heroes/Sofia/s2.png"),
     pg.image.load("Images/Heroes/Sofia/s3.png")],
    [pg.image.load("Images/Heroes/Sofia/t1.png"),
     pg.image.load("Images/Heroes/Sofia/t2.png"),
     pg.image.load("Images/Heroes/Sofia/t3.png")],
    pg.image.load("Images/Heroes/Sofia/t.png")]

Sonia = [
    [pg.image.load("Images/Heroes/Sonia/e1.png"),
     pg.image.load("Images/Heroes/Sonia/e2.png"),
     pg.image.load("Images/Heroes/Sonia/e3.png")],
    [pg.image.load("Images/Heroes/Sonia/n1.png"),
     pg.image.load("Images/Heroes/Sonia/n2.png"),
     pg.image.load("Images/Heroes/Sonia/n3.png")],
    [pg.image.load("Images/Heroes/Sonia/o1.png"),
     pg.image.load("Images/Heroes/Sonia/o2.png"),
     pg.image.load("Images/Heroes/Sonia/o3.png")],
    [pg.image.load("Images/Heroes/Sonia/s1.png"),
     pg.image.load("Images/Heroes/Sonia/s2.png"),
     pg.image.load("Images/Heroes/Sonia/s3.png")],
    [pg.image.load("Images/Heroes/Sonia/t1.png"),
     pg.image.load("Images/Heroes/Sonia/t2.png"),
     pg.image.load("Images/Heroes/Sonia/t3.png")],
    pg.image.load("Images/Heroes/Sonia/t.png")]

Taun = [
    [pg.image.load("Images/Heroes/Taun/e1.png"),
     pg.image.load("Images/Heroes/Taun/e2.png"),
     pg.image.load("Images/Heroes/Taun/e3.png")],
    [pg.image.load("Images/Heroes/Taun/n1.png"),
     pg.image.load("Images/Heroes/Taun/n2.png"),
     pg.image.load("Images/Heroes/Taun/n3.png")],
    [pg.image.load("Images/Heroes/Taun/o1.png"),
     pg.image.load("Images/Heroes/Taun/o2.png"),
     pg.image.load("Images/Heroes/Taun/o3.png")],
    [pg.image.load("Images/Heroes/Taun/s1.png"),
     pg.image.load("Images/Heroes/Taun/s2.png"),
     pg.image.load("Images/Heroes/Taun/s3.png")],
    [pg.image.load("Images/Heroes/Taun/t1.png"),
     pg.image.load("Images/Heroes/Taun/t2.png"),
     pg.image.load("Images/Heroes/Taun/t3.png")],
    pg.image.load("Images/Heroes/Taun/t.png")]

Xerath = [
    [pg.image.load("Images/Heroes/Xerath/e1.png"),
     pg.image.load("Images/Heroes/Xerath/e2.png"),
     pg.image.load("Images/Heroes/Xerath/e3.png")],
    [pg.image.load("Images/Heroes/Xerath/n1.png"),
     pg.image.load("Images/Heroes/Xerath/n2.png"),
     pg.image.load("Images/Heroes/Xerath/n3.png")],
    [pg.image.load("Images/Heroes/Xerath/o1.png"),
     pg.image.load("Images/Heroes/Xerath/o2.png"),
     pg.image.load("Images/Heroes/Xerath/o3.png")],
    [pg.image.load("Images/Heroes/Xerath/s1.png"),
     pg.image.load("Images/Heroes/Xerath/s2.png"),
     pg.image.load("Images/Heroes/Xerath/s3.png")],
    [pg.image.load("Images/Heroes/Xerath/t1.png"),
     pg.image.load("Images/Heroes/Xerath/t2.png"),
     pg.image.load("Images/Heroes/Xerath/t3.png")],
    pg.image.load("Images/Heroes/Xerath/t.png")]

# NPCs

Saku = pg.image.load("Images/Characters/npc/Saku.png")
Spidy = pg.image.load("Images/Characters/npc/Spidy.png")
Elise = pg.image.load("Images/Characters/npc/Elise.png")
Goldi = pg.image.load("Images/Characters/npc/Goldi.png")
Helen = pg.image.load("Images/Characters/npc/Helen.png")
Marian = pg.image.load("Images/Characters/npc/Marian.png")
Balzar = pg.image.load("Images/Characters/npc/Balzar.png")
Manuela = pg.image.load("Images/Characters/npc/Manuela.png")
Clarissa = pg.image.load("Images/Characters/npc/Clarissa.png")
Elizabeth = pg.image.load("Images/Characters/npc/Elizabeth.png")

# Enemies

Enemy_1 = [pg.image.load("Images/Characters/Enemies/1_1.png"),
           pg.image.load("Images/Characters/Enemies/1_2.png"),
           pg.image.load("Images/Characters/Enemies/1_3.png")]
Enemy_2 = [pg.image.load("Images/Characters/Enemies/2_1.png"),
           pg.image.load("Images/Characters/Enemies/2_2.png"),
           pg.image.load("Images/Characters/Enemies/2_3.png")]
Enemy_3 = [pg.image.load("Images/Characters/Enemies/3_1.png"),
           pg.image.load("Images/Characters/Enemies/3_2.png"),
           pg.image.load("Images/Characters/Enemies/3_3.png")]

random_enemies_1 = [[pg.image.load("Images/Things/raccoon_e_1.png"),
                     pg.image.load("Images/Things/raccoon_e_2.png"),
                     pg.image.load("Images/Things/raccoon_e_3.png")],
                    [pg.image.load("Images/Things/raccoon_n_1.png"),
                     pg.image.load("Images/Things/raccoon_n_2.png"),
                     pg.image.load("Images/Things/raccoon_n_3.png")],
                    [pg.image.load("Images/Things/raccoon_o_1.png"),
                     pg.image.load("Images/Things/raccoon_o_2.png"),
                     pg.image.load("Images/Things/raccoon_o_3.png")],
                    [pg.image.load("Images/Things/raccoon_s_1.png"),
                     pg.image.load("Images/Things/raccoon_s_2.png"),
                     pg.image.load("Images/Things/raccoon_s_3.png")]]

random_enemies_2 = [[pg.image.load("Images/Things/worm_e_1.png"),
                     pg.image.load("Images/Things/worm_e_2.png"),
                     pg.image.load("Images/Things/worm_e_3.png")],
                    [pg.image.load("Images/Things/worm_n_1.png"),
                     pg.image.load("Images/Things/worm_n_2.png"),
                     pg.image.load("Images/Things/worm_n_3.png")],
                    [pg.image.load("Images/Things/worm_o_1.png"),
                     pg.image.load("Images/Things/worm_o_2.png"),
                     pg.image.load("Images/Things/worm_o_3.png")],
                    [pg.image.load("Images/Things/worm_s_1.png"),
                     pg.image.load("Images/Things/worm_s_2.png"),
                     pg.image.load("Images/Things/worm_s_3.png")]]

# In combat

Enemy_1_in_combat = pg.image.load("Images/Characters/Enemies/1_in_combat.png")
Enemy_2_in_combat = pg.image.load("Images/Characters/Enemies/2_in_combat.png")
Enemy_3_in_combat = pg.image.load("Images/Characters/Enemies/3_in_combat.png")

# Others

Snake = pg.image.load("Images/snaky.png")

Invaders = [pg.image.load("Images/1.png"),
            pg.image.load("Images/2.png"),
            pg.image.load("Images/3.png"),
            pg.image.load("Images/mother.png")]

# Backgrounds / Scenarios

House_1 = pg.image.load("Images/Places/bedroom.png")
House_1_position = [width / 3, height / 3]
House_2 = pg.image.load("Images/Places/living_room.png")
House_2_position = [width / 5, height / 5]
Field_0 = pg.image.load("Images/Places/f_0.png")
Field_1 = pg.image.load("Images/Places/f_1.png")
Field_2 = pg.image.load("Images/Places/f_2.png")
Town_1 = pg.image.load("Images/Places/town1.png")
Town_2 = pg.image.load("Images/Places/town2.png")
Town_3 = pg.image.load("Images/Places/town3.png")
Battle_ground = pg.image.load("Images/Places/battle_ground.jpg")
Fields_position = [0, 0]

background = pg.image.load("Images/f_1.png")

# Things

Bed = pg.image.load("Images/Things/bed.png")
Tree = pg.image.load("Images/Things/tree.png")
Hole = pg.image.load("Images/Things/hole.png")
Bush = pg.image.load("Images/Things/bush.png")
Table = pg.image.load("Images/Things/table.png")
Apple = pg.image.load("Images/Things/apple.png")
Plant_1 = pg.image.load("Images/Things/plant_1.png")
Plant_2 = pg.image.load("Images/Things/plant_2.png")
Limit_1 = pg.image.load("Images/Things/limit_1.png")
Limit_2 = pg.image.load("Images/Things/limit_2.png")
Chair_e = pg.image.load("Images/Things/chair_e.png")
Chair_n = pg.image.load("Images/Things/chair_n.png")
Chair_s = pg.image.load("Images/Things/chair_s.png")
Chair_w = pg.image.load("Images/Things/chair_w.png")
Flower = pg.image.load("Images/Things/pink_flower.png")
Combat_box = pg.image.load("Images/Things/combat_box.png")
Dialog_box = pg.image.load("Images/Things/dialog_box.png")
Drake_smash = pg.image.load("Images/Things/drake_smash.png")
Nightstand_1 = pg.image.load("Images/Things/nightstand1.png")
Nightstand_2 = pg.image.load("Images/Things/nightstand2.png")
Decoration_1 = pg.image.load("Images/Things/decoration1.png")
Decoration_2 = pg.image.load("Images/Things/decoration2.png")
Decoration_3 = pg.image.load("Images/Things/decoration3.png")
Decoration_4 = pg.image.load("Images/Things/decoration4.png")
Decoration_5 = pg.image.load("Images/Things/decoration5.png")
Room_limit_1 = pg.image.load("Images/Things/room_limit_1.png")
Room_limit_2 = pg.image.load("Images/Things/room_limit_2.png")
Player_house = pg.image.load("Images/Things/player_house.png")

# Buffs
Wings = pg.image.load("Images/Things/wings.png")
Hearts = pg.image.load("Images/Things/heart.png")
Coffee = pg.image.load("Images/Things/coffee.png")
Extra_life = pg.image.load("Images/Things/extra_life.png")
Extra_energy = pg.image.load("Images/Things/extra_energy.png")

# Effects

Explosion_1 = pg.image.load("Images/Effects/1.png")
Explosion_2 = pg.image.load("Images/Effects/2.png")
Explosion_3 = pg.image.load("Images/Effects/3.png")

Player_Shots = pg.image.load("Images/shot.png")
Invader_Shots = pg.image.load("Images/invader_shot.png")

# Texts

euphoria = "Euphoria"

euphoria_intro = ["Once upon a time, a lost continent; where",
                  "people around the big castle of Esfitia",
                  "used to live placefully like farmers,",
                  "warrior, markers and other Professions",
                  "",
                  "",
                  "One day, everyone near to the castle",
                  "saw a weird coming darkness the",
                  "the king, got worry about that",
                  "so, sent different ships to face",
                  "them...",
                  "",
                  "",
                  "Those ship never come back...",
                  "",
                  "",
                  "The cataclysm have just started",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "Heroes...",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "Were able to safe our world, but",
                  "each one of they have a story...",
                  "this is one of them",
                  "",
                  "",
                  "",
                  "",
                  "Luke, the dragons son",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "         ( Somebody in the front door )",
                  "",
                  "",
                  "",
                  "",
                  "               Z Z Z Z Z Z Z.... ",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "I'll defeat... ",
                  "",
                  "",
                  "",
                  "",
                  "       ( Fall from his bed )",
                  "",
                  "",
                  "",
                  "",
                  "What the...?",
                  "Who's knowing knock?"]

skip = "Click to skip"

dialogue_1 = "I should take this... (Press E)"

dialogue_2 = "I will need this... (Press E)"

dialogue_2_1 = "   This is really heavy..."

dialogue_3 = "...grandpa's ring... (Press Q)"

dialogue_3_1 = "COFFEE!!! (Press R to drink)"

dialogue_4 = ["I don't want to step on my",
              "",
              "garden"]

dialogue_5 = ["LUUUUUUUUUUUKKKKEEEEEEE!!",
              "",
              "There are monster in the",
              "",
              "town... Safe us!!!", ]

dialogue_6 = ["I need to be a dragon to",
              "",
              "use dragon fire"]

dialogue_7 = ["I don't have enough energy",
              "",
              "or material..."]

dialogue_7_1 = "You won"

dialogue_7_2 = "Fill hole (Press E)"

dialogue_7_3 = "You found a potion"

dialogue_8 = ["I'm Balzar the cataclysm herald",
              "I can help, if the destroy those",
              "monster I will tell you how to",
              "stop the cataclysm"]

dialogue_9 = ["Now, I'm free... Thank you...",
              "Well you can die in peace. Those",
              "Idiots wanted kidnap people...",
              "IT BETTER KILL THEM RIGHT NOW!!!"]

lvl_info = ["Go out", "Check the front door",
            "Talk with Manuela", "Save the town",
            "Defeat the monsters",
            "Talk with the weird guy",
            "Defeat all the monster",
            "Survive!!",
            "Defeat Balzar"]

Player_attacks = ["Q. Hit (1/1)",
                  "W. Sword (4/3)",
                  "E. Transformation (5)",
                  "R. Dragon fire (6/3)",
                  "T. Inventory",
                  "F. Skip turn"]

Player_inventory = ["A. Dragon rings (It kills an enemy)",
                    "S. Live potion (You recover 5 life points)",
                    "D. Mana potion (You recover 5 energy points)"]

Enemy_1_attacks = ["Bite",
                   "Poison",
                   "Dodge"]

Enemy_2_attacks = ["SMASH!",
                   "Gurrrr!",
                   "EAT!"]

Enemy_3_attacks = ["Skull attack!",
                   "Amaterasu",
                   "You can't hurt me",
                   "NEW PET!"]

Death = "You have been slave"

Death_interaction = ["",
                     "",
                     "",
                     "",
                     "Luke was defeat...",
                     "",
                     "",
                     "",
                     "",
                     "He was a heroes, but no all the heroes",
                     "",
                     "are able to safe the world..."]
