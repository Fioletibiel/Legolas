from tkinter import *
from tkinter import filedialog
from graphviz import render
from graphviz import *
from tkinter import *
from PIL import ImageTk, Image
from Prufer import Prufer
import random
import string


class OdczytZapis(object):


    def __init__(self):
        self.root = Toplevel()

    node_name = 'a'
    l_ggn = 0
    l_gge = 0
    l_random = 0
    g = Graph(format='png')
    tablica_nazw_wierzcholkow = []
    wybrana_randomowa_przed_chwila = 'a'
    tablica_wybranych_randomowych_od = []
    tablica_wybranych_randomowych_do = []

    def zwieksz_node_name():
        aski = ord(OdczytZapis.node_name)
        aski += 1
        OdczytZapis.node_name = chr(aski)

    def losowa_inna_niz_randomowo_od():
        while True:
            r = random.choice(OdczytZapis.tablica_nazw_wierzcholkow)
            b = False
            if r != OdczytZapis.wybrana_randomowa_przed_chwila[0]:
                b = True
            if b == True:
                break
        return r

    # def randomowo_od():
    #     r_od = random.choice(OdczytZapis.tablica_nazw_wierzcholkow)
    #     OdczytZapis.tablica_wybranych_randomowych_od.append(r_od)
    #     OdczytZapis.wybrana_randomowa_przed_chwila = r_od
    #     OdczytZapis.l_random += 1
    #     return r_od
    #
    # def randomowo_do():
    #     r_od = OdczytZapis.tablica_wybranych_randomowych_od[OdczytZapis.l_random-1]
    #     bufor_od = 0
    #     bufor_do = 0
    #     if (OdczytZapis.l_random > 1):
    #         while True:
    #             b = False
    #             r_do = OdczytZapis.losowa_inna_niz_randomowo_od()
    #             for i in range(OdczytZapis.l_random-1):
    #                 if r_do == OdczytZapis.tablica_wybranych_randomowych_do[i]:
    #                     bufor_do = i
    #             for i in range(OdczytZapis.l_random):
    #                 if r_od == OdczytZapis.tablica_wybranych_randomowych_od[i]:
    #                     bufor_od = i
    #             # if r_od != OdczytZapis.tablica_wybranych_randomowych_od[bufor_do] and r_do != OdczytZapis.tablica_wybranych_randomowych_do[bufor_od]:
    #             if r_od != OdczytZapis.tablica_wybranych_randomowych_od[bufor_do]:
    #                 b = True
    #             if b == True:
    #                 break
    #     else:
    #         r_do = OdczytZapis.losowa_inna_niz_randomowo_od()
    #     OdczytZapis.tablica_wybranych_randomowych_do.append(r_do)
    #     return r_do
    #
    # def gen_graf_plus_edge():
    #     if OdczytZapis.l_gge < OdczytZapis.l_ggn-1:
    #         OdczytZapis.g.edge(OdczytZapis.randomowo_od(),OdczytZapis.randomowo_do())
    #         obrazek = OdczytZapis.g.render('dot', 'png')
    #         return obrazek
    #     else:
    #         print("Dodatkowa krawędź nie może zostać dodana. Najpierw dodaj więcej wierzchołków.")
    #     OdczytZapis.l_gge += 1
    #
    # def gen_graf_plus_node():
    #     OdczytZapis.l_ggn += 1
    #     OdczytZapis.g.node(str(OdczytZapis.node_name))
    #     OdczytZapis.tablica_nazw_wierzcholkow.append(str(OdczytZapis.node_name))
    #     OdczytZapis.zwieksz_node_name()
    #     obrazek = OdczytZapis.g.render('dot', 'png')
    #     return obrazek

    # bufor = 0
    # def randomowo_od():
    #     r_od = random.choice(OdczytZapis.tablica_nazw_wierzcholkow)
    #     for i in range(len(OdczytZapis.tablica_wybranych_randomowych_do)):
    #         if r_od == OdczytZapis.tablica_wybranych_randomowych_do[i]:
    #             OdczytZapis.bufor = i
    #     OdczytZapis.tablica_wybranych_randomowych_od.append(r_od)
    #     OdczytZapis.wybrana_randomowa_przed_chwila = r_od
    #     OdczytZapis.l_random += 1
    #     return r_od
    #
    # # Jeżeli od będzie ten sam co któryś z poprzednich do, to nowy do nie może się równać odpowiadającemu mu od
    #
    # def randomowo_do():
    #     if OdczytZapis.l_ggn > 2:
    #         while True:
    #             b = False
    #             r_do = OdczytZapis.losowa_inna_niz_randomowo_od()
    #             for i in range(len(OdczytZapis.tablica_wybranych_randomowych_do)):
    #                 if r_do != OdczytZapis.tablica_wybranych_randomowych_do[i] and r_do != OdczytZapis.tablica_wybranych_randomowych_od[OdczytZapis.bufor]:
    #                     b = True
    #             if b == True:
    #                 break
    #     else:
    #         r_do = OdczytZapis.losowa_inna_niz_randomowo_od()
    #     OdczytZapis.tablica_wybranych_randomowych_do.append(r_do)
    #     return r_do

    def randomowo_od():
        r_od = OdczytZapis.tablica_nazw_wierzcholkow[-1]
        OdczytZapis.tablica_wybranych_randomowych_od.append(r_od)
        OdczytZapis.wybrana_randomowa_przed_chwila = r_od
        return r_od

    def randomowo_do():
        r_do = OdczytZapis.losowa_inna_niz_randomowo_od()
        OdczytZapis.tablica_wybranych_randomowych_do.append(r_do)
        return r_do

    def gen_tree_plus_node():
        OdczytZapis.g.node(str(OdczytZapis.node_name))
        OdczytZapis.tablica_nazw_wierzcholkow.append(str(OdczytZapis.node_name))
        OdczytZapis.zwieksz_node_name()

        if OdczytZapis.l_ggn > 1:
            OdczytZapis.g.edge(OdczytZapis.randomowo_od(),OdczytZapis.randomowo_do())

        obrazek = OdczytZapis.g.render('dot', 'png')
        return obrazek




    # def DOT2Pic():
    #     root2 = Toplevel()
    #     plik_DOT = filedialog.askopenfilename(filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")), title="Proszę wybierz plik z kodem DOT")
    #     if plik_DOT:
    #         try:
    #             print("Plik został wczytany pomyślnie.")
    #         except:
    #             showerror("Open Source File", "Failed to read file\n'%s'" % plik_DOT)
    #         obrazek = render('dot', 'png', plik_DOT)
    #         obrazek = ImageTk.PhotoImage(Image.open(obrazek))
    #         panel = Label(root2, image=obrazek)
    #         panel.image = obrazek
    #         panel.pack(side="top", fill="both", expand="yes")
    #
    # def Prufer2Pic():
    #     root2 = Toplevel()
    #     plik_Prufer = filedialog.askopenfilename(filetypes=(("Text Documents", "*.txt"), ("All files", "*.*")), title="Proszę wybierz plik .txt z kodem Prüfera")
    #     if plik_Prufer:
    #         try:
    #             print("Plik został wczytany pomyślnie.")
    #         except:
    #             showerror("Open Source File", "Failed to read file\n'%s'" % plik_Prufer)
    #     tresc_pliku = open(plik_Prufer, 'w')
    #     Prufer.checkifPrufer(tresc_pliku)
    #     plik_DOT = Prufer.Prufer2DOT(tresc_pliku)
    #     obrazek = render('dot', 'png', plik_DOT)
    #     obrazek = ImageTk.PhotoImage(Image.open(obrazek))
    #     panel = Label(root2, image=obrazek)
    #     panel.image = obrazek
    #     panel.pack(side="top", fill="both", expand="yes")


    def DOT2Prufer():
        plik_DOT = filedialog.askopenfilename(filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")), title="Proszę wybierz plik z kodem DOT")
        if plik_DOT:
            try:
                print("Plik został wczytany pomyślnie.")
            except:
                showerror("Open Source File", "Failed to read file\n'%s'" % plik_DOT)
            tresc_pliku = open(plik_DOT, 'w')
            tresc_pliku = Prufer.DOT2Prufer(tresc_pliku)
            plik_Prufer = filedialog.asksaveasfilename(
                filetypes=(("Text Documents", "*.txt"), ("All files", "*.*")),
                title='Proszę wybierz plik .txt, do którego chcesz zapisać kod Prüfera.',
                defaultextension='.txt')
            if plik_Prufer:
                try:
                    print("Plik został pomyślnie zapisany.")
                except:
                    showerror("Open Source File", "Failed to save file\n'%s'" % plik_Prufer)
                plik = open(plik_Prufer, 'w')
                plik.write(tresc_pliku)
                plik.close()

    def Prufer2DOT():
        plik_Prufer = filedialog.askopenfilename(filetypes=(("Text Documents", "*.txt"), ("All files", "*.*")), title="Proszę wybierz plik .txt z kodem Prüfera")
        if plik_Prufer:
            try:
                print("Plik został wczytany pomyślnie.")
            except:
                showerror("Open Source File", "Failed to read file\n'%s'" % plik_Prufer)
            Prufer.checkifPrufer(plik_Prufer)
            tresc_pliku = open(plik_Prufer, 'w')
            Prufer.Prufer2DOT(tresc_pliku)
            plik_DOT = filedialog.asksaveasfilename(filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")),title='Proszę wybierz plik .txt, do którego chcesz zapisać kod DOT.',defaultextension='.txt')
            if plik_DOT:
                try:
                    print("Plik został pomyślnie zapisany.")
                except:
                    showerror("Open Source File", "Failed to save file\n'%s'" % plik_DOT)
                plik = open(plik_DOT, 'w')
                plik.write(tresc_pliku)
                plik.close()

    def Pic2DOT():
        pass

    def Pic2Prufer():
        pass












    def Kurs():
        plik_DOT = filedialog.asksaveasfilename(filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")),title='Proszę wybierz plik .txt, do którego chcesz zapisać kod DOT namalowanego grafu.',defaultextension='.txt')
        if plik_DOT:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
            except:
                showerror("Open Source File", "Failed to read file\n'%s'" % plik_DOT)
            return
        return plik_DOT
        plik = open(plik_DOT, 'w')
        plik.write("tresc")
        plik.close()