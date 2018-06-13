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

    def DOT2Pic():
        root2 = Toplevel()
        plik_DOT = filedialog.askopenfilename(filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")), title="Proszę wybierz plik z kodem DOT")
        if plik_DOT:
            try:
                print("Plik został wczytany pomyślnie.")
            except:
                showerror("Open Source File", "Failed to read file\n'%s'" % plik_DOT)
            obrazek = render('dot', 'png', plik_DOT)
            obrazek = ImageTk.PhotoImage(Image.open(obrazek))
            panel = Label(root2, image=obrazek)
            panel.image = obrazek
            panel.pack(side="top", fill="both", expand="yes")

    def Prufer2Pic():
        root2 = Toplevel()
        plik_Prufer = filedialog.askopenfilename(filetypes=(("Text Documents", "*.txt"), ("All files", "*.*")), title="Proszę wybierz plik .txt z kodem Prüfera")
        if plik_Prufer:
            try:
                print("Plik został wczytany pomyślnie.")
            except:
                showerror("Open Source File", "Failed to read file\n'%s'" % plik_Prufer)
        tresc_pliku = open(plik_Prufer, 'w')
        Prufer.checkifPrufer(tresc_pliku)
        plik_DOT = Prufer.Prufer2DOT(tresc_pliku)
        obrazek = render('dot', 'png', plik_DOT)
        obrazek = ImageTk.PhotoImage(Image.open(obrazek))
        panel = Label(root2, image=obrazek)
        panel.image = obrazek
        panel.pack(side="top", fill="both", expand="yes")


    l_ggn = 'a'
    l_gge = 0
    g = Graph(format='png')
    tablica_nazw_wierzcholkow = []
    wybrana_randomowa_przed_chwila = 'a'
    tablica_wybranych_randomowych = []


    def randomowo_od():
        # while True:
        #     r = random.choice(OdczytZapis.tablica_nazw_wierzcholkow)
        #     b = False
        #     for i in range(len(OdczytZapis.tablica_wybranych_randomowych)):
        #         if r != OdczytZapis.tablica_wybranych_randomowych[i]:
        #             b = True
        #     if b == True:
        #         break
        r = OdczytZapis.tablica_nazw_wierzcholkow[-1]
        OdczytZapis.tablica_wybranych_randomowych.append(r)
        OdczytZapis.wybrana_randomowa_przed_chwila = r
        return r



    def gen_graf_plus_edge():
        OdczytZapis.g.edge(OdczytZapis.randomowo_od(),OdczytZapis.randomowo_do())
        obrazek = OdczytZapis.g.render('dot', 'png')
        return obrazek

    def gen_graf_plus_node():
        OdczytZapis.g.node(str(OdczytZapis.l_ggn))
        OdczytZapis.tablica_nazw_wierzcholkow.append(str(OdczytZapis.l_ggn))
        OdczytZapis.zwieksz_lggn()
        obrazek = OdczytZapis.g.render('dot', 'png')
        return obrazek





    def gen_graf_minus_node():
        g = Graph(format='png')
        OdczytZapis.l_ggn -= 1
        obrazek = g.render('dot', 'png')
        print(obrazek)

    def gen_graf_minus_node():
        g = Graph(format='png')
        OdczytZapis.l_gge -= 1
        obrazek = g.render('dot', 'png')
        print(obrazek)





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


    # def randomowo(reset):
    #     if reset == True:
    #         OdczytZapis.tablica_wybranych_przed_chwila = []
    #     while True:
    #         r = random.choice(OdczytZapis.tablica_nazw_wierzcholkow)
    #         b = True
    #         for i in range(len(OdczytZapis.tablica_wybranych_przed_chwila)):
    #             if r == OdczytZapis.tablica_wybranych_przed_chwila[i]:
    #                 b = False
    #         if b == True:
    #             break
    #     OdczytZapis.tablica_wybranych_przed_chwila.append(r)
    #     return r

    def zwieksz_lggn():
        aski = ord(OdczytZapis.l_ggn)
        aski += 1
        OdczytZapis.l_ggn = chr(aski)

    def randomowo_do():
        while True:
            r = random.choice(OdczytZapis.tablica_nazw_wierzcholkow)
            b = False
            if r != OdczytZapis.wybrana_randomowa_przed_chwila[0]:
                b = True
            if b == True:
                break
        OdczytZapis.wybrana_randomowa_przed_chwila = 'a'
        return r


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