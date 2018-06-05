import time
import pygame as pg

class GUI(object):

    def __init__(self):
        self.tps_max = 100

        pg.init()
        self.wyswietlacz = pg.display.set_mode((1280,720))
        pg.display.set_caption('Legolas')
        ikonka = pg.image.load('celtic_tree.gif')
        pg.display.set_icon(ikonka)

        self.tps_clock = pg.time.Clock()
        self.tps_delta = 0.0

        self.kolor_szary = (200, 200, 200)
        self.prostokat_1 = pg.Rect(10, 10, 150, 90)
        self.prostokat_2 = pg.Rect(10, 110, 150, 90)
        self.prostokat_3 = pg.Rect(10, 210, 150, 90)

        while True:
            for wydarzenie in pg.event.get():
                if wydarzenie.type == pg.QUIT:
                    exit(0)
                elif wydarzenie.type == pg.KEYDOWN and wydarzenie.key == pg.K_ESCAPE:
                    exit(0)

            self.tps_delta +=self.tps_clock.tick()/1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.klik()
                self.tps_delta -= 1 / self.tps_max

            self.wyswietlacz.fill((255, 255, 255))
            self.wyswietlanie()
            # pg.display.update()d
            pg.display.flip()

    def klik(self):
        # klawisz = pg.key.get_pressed()
        # if klawisz[pg.K_d]:
        #     self.prostokat.x += 3
        # elif klawisz[pg.K_a]:
        #     self.prostokat.x -= 3
        # elif klawisz[pg.K_w]:
        #     self.prostokat.y -= 3
        # elif klawisz[pg.K_s]:
        #     self.prostokat.y += 3
        pass

    def wyswietlanie(self):
        pg.draw.rect(self.wyswietlacz, self.kolor_szary, self.prostokat_1)
        pg.draw.rect(self.wyswietlacz, self.kolor_szary, self.prostokat_2)
        pg.draw.rect(self.wyswietlacz, self.kolor_szary, self.prostokat_3)