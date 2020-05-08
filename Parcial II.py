# coding=utf-8
import pygame as pg
import library as lib
import objects as obj


class Texts:
    def __init__(self, text_position, screen, text, size, typography, color=lib.cts.WHITE):
        # Text issues
        self.txt = lib.write(text, size, typography, color)
        self.screen = screen

        # Position issues
        self.x, self.y = text_position
        self.velocity = [2, 2]

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.screen.blit(self.txt, [self.x, self.y])


if __name__ == '__main__':
    pg.init()
    pg.font.init()

    run = True
    end = True
    intro = True
    playing = True
    txt = ""
    window = lib.new_window("Intro")
    fps = lib.frames_per_second_basics()

    title_x, title_y = 350, 200

    while run and intro:
        pg.font.init()
        txt = "Euphoria"
        write = lib.write(txt, 300, 4)
        window.blit(write, [title_x, title_y])
        txt = "Xerath alguna vez conocido como el campeón de Esfitia, solía ser el protector de la cuidad costera" \
              "admirado y respetado; en ese tiempo el gran campeón era conocido por su gusto por las batallas y su" \
              "habilidad en las mismas pues de este modo defendia su ciudad, así lo fue hasta la llegada del" \
              "cataclismo... Un día con la llegada del alba la neblina que había estado azotando el mar profundo" \
              "impidiendo la salidad de barcos durante unas semanas llegó sin aviso a la costa, dejando caer sobre"

        write = lib.write(txt, 30, 1)
        window.blit(write, [400, 300])

        txt = "ella lo que el mismo Xerath describió como 'creaturas infernales', Xerath rapidamente formó a sus hombre " \
              "dispuesto a defender la ciudad de la inminente llegada de las creaturas; sin embargo la batalla fue una " \
              "masacre, anto lo cual el gran campeón superado en número y fuerzas solo pudo ver como de uno en uno caían " \
              "los suyos hasta ser el único en pie por lo que engullido en la melancolía obtuvo la unica baja enemiga de" \
              " ese día cortando la cabeza de un ogro y callendo en frente de 6 más de ellos seguro de su muerte al ver " \
              "como uno de ellos levantaba su puño con disposición de vengar al ahora muerto ogro; tal vez por eso la "

        write = lib.write(txt, 30, 1)
        window.blit(write, [400, 300])

        txt = "creatura que comandaba las fuerzas enemigas, un ser que se dejaba ver como un anciano de larga barba y " \
              "tunica viendo que uno de los suyos estaba a punto de terminar con su vida lo detuvo por lo que Xerath " \
              "incorporandose y volviendo a tomar su espada se levanto desafiante ante el anciano; este último le retó " \
              "a un combate en el que le prometía la retirada en caso de que este ganara, Xerath titubeante ante la " \
              "fuerza que pudiese tener el anciano aceptó, viendo como los ogros a su alrededor formaban un circulo " \
              "el anciano retiró sus vestimentas dejando ver su escualido cuerpo, cubierto solo con un taparrabos; " \
              "Xerath confiado de la figura del anciano y de sus propia fuerza atinó a levantar su espada para "
        write = lib.write(txt, 30, 1)
        window.blit(write, [400, 300])

        txt = "derribarlo de un tajo ante lo que el anciano tomó la espada frenando de golpe el ataque y provocando " \
              "una herida grave al ojo de Xerath; entendiendo este que Xerath quería usar su espada, el anciano invicó " \
              "un baculo con el que derribó al campeón de la ahora caída ciudad de un único golpe en el sitió de su " \
              "cortada. Para cuando Xerath despertó la ciudad había sido destriuda y un extraño ser se encontraba en " \
              "frente de él, la creatura afirmaba llamarse Xerath ante lo que el humano Xerath afirmaba que eso no era " \
              "posible pues él era Xerath, siendo que la creatura respondió 'Exacto' se introdujó en el cuerpo del " \
              "humano Xerath y ya dentro de él le explicó que aquel anciano le había concedido el don del vacio, " \
              "ahora estaba maldito"
        write = lib.write(txt, 30, 1)
        window.blit(write, [400, 300])

        lib.frames_per_second(fps, 5)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                intro = False

    # Groups
    players = pg.sprite.Group()
    enemies = pg.sprite.Group()
    shots_players = pg.sprite.Group()
    shots_enemies = pg.sprite.Group()

    player = obj.PlayerShip([lib.cts.width / 2 - 35, lib.cts.height - 35])
    players.add(player)

    enemy_type = 0
    invaders_start = [10, 10]

    while enemy_type <= 2:
        for _ in range(0, 12):
            enemy = obj.EnemyShip([invaders_start[0], invaders_start[1]], enemy_type)
            invaders_start[0] += 80
            enemies.add(enemy)
        enemy_type += 1
        invaders_start = [10, invaders_start[1] + 50]

    position = [0, 0]
    direction = 0
    score = 0
    speed = 1

    while run and playing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    player.velocity[0] += speed
                if event.key == pg.K_a:
                    player.velocity[0] -= speed
            if event.type == pg.KEYUP:
                player.velocity = [0, 0]
            if event.type == pg.MOUSEBUTTONDOWN:
                position = player.get_position()
                players_shot = obj.Shot([position[0] + 25, position[1]])
                shots_players.add(players_shot)

        # Control

        list_object = pg.sprite.spritecollide(player, enemies, True)

        for enemy in enemies:
            if enemy.tmp <= 0:
                position = enemy.get_position()
                shot = obj.Shot([position[0] + 25, position[1] + 15], 1)
                shots_enemies.add(shot)
                enemy.tmp = lib.random_range(100, 300)

        for shot in shots_players:
            list_enemies = pg.sprite.spritecollide(shot, enemies, True)
            if shot.rect.y < -10:
                shots_players.remove(shot)
            for enemy in shots_enemies:
                shots_enemies.remove(shot)
                score += 100

        for shot in shots_enemies:
            list_players = pg.sprite.spritecollide(shot, players, False)
            if shot.rect.y > (lib.cts.height + 10):
                shots_enemies.remove(shot)
            for player in list_players:
                player.life -= 1

        for player in players:
            if player.life < 0:
                playing = False

        # Updates
        players.update()
        enemies.update()
        shots_enemies.update()
        shots_players.update()

        # Drawing issues

        lib.fill(window)

        players.draw(window)
        enemies.draw(window)
        shots_enemies.draw(window)
        shots_players.draw(window)

        txt = str(score)
        write = lib.write(txt, 10, 2)
        window.blit(write, [0, 0])
        txt = "Press any key"
        write = lib.write(txt, 30, 2)
        window.blit(write, [400, 300])

        lib.frames_per_second(fps, 2)

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
