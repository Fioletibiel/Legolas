from tkinter import *
import tkinter
from OdczytZapis import OdczytZapis as oz
from OdczytZapis import *
from Graf import Graf
from DOT import DOT
from graphviz import render
from graphviz import *
from PIL import ImageTk, Image


class TkinterGUI(object):

    def __init__(self):
        self.root = Tk()
        # self.root.geometry("200x250")
        self.root.title('GIZ projekt, Autor: Paweł Kamiński')
        self.root.iconbitmap('obrazki\PJATK_icon_transparent.ico')

        menu = Menu(self.root)
        self.root.config(menu=menu)
        subMenu1 = Menu(menu)
        menu.add_cascade(label="Kod Prüfera", menu=subMenu1)
        subMenu1.add_command(label="DOT->Graf", command=oz.DOT2Pic)
        subMenu1.add_command(label="Prüfer->Graf", command=oz.Prufer2Pic)
        subMenu1.add_command(label="DOT->Prüfer", command=oz.DOT2Prufer)
        subMenu1.add_command(label="Prüfer->DOT", command=oz.Prufer2DOT)
        subMenu2 = Menu(menu)
        menu.add_cascade(label="Lista kursów", menu=subMenu2)
        subMenu2.add_command(label="Do zrobienia 1", command=oz.Kurs)
        subMenu2.add_command(label="Do zrobienia 2", command=oz.Kurs)

        img = Image.open("obrazki\PJATK_tlo_transparentne_wodne.png")
        # img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        tlo = Label(self.root, image=img)
        tlo.image = img
        tlo.pack(side="top", fill="both", expand="yes")

        def nastepny_wierzcholek_na_tlo(event):
            graf = oz.gen_graf_plus_node()
            img_update = Image.open(graf)
            img_update = ImageTk.PhotoImage(img_update)
            tlo.configure(image=img_update)
            tlo.image = img_update
        def nastepna_krawedz_na_tlo(event):
            graf = oz.gen_graf_plus_edge()
            img_update = Image.open(graf)
            img_update = ImageTk.PhotoImage(img_update)
            tlo.configure(image=img_update)
            tlo.image = img_update
        def reset_tla(event):
            img_update = Image.open("obrazki\PJATK_tlo_transparentne_wodne.png")
            img_update = ImageTk.PhotoImage(img_update)
            tlo.configure(image=img_update)
            tlo.image = img_update
            oz.l_ggn = 'a'
            oz.l_gge = 1
            oz.g = Graph(format='png')
            oz.tablica_nazw_wierzcholkow = []
            oz.tablica_wybranych_przed_chwila = []
        def poprzedni_wierzcholek_na_tlo(event):
            graf = oz.gen_graf_minus_node()
            img_update = Image.open(graf)
            img_update = ImageTk.PhotoImage(img_update)
            tlo.configure(image=img_update)
            tlo.image = img_update
        def poprzednia_krawedz_na_tlo(event):
            graf = oz.gen_graf_minus_edge()
            img_update = Image.open(graf)
            img_update = ImageTk.PhotoImage(img_update)
            tlo.configure(image=img_update)
            tlo.image = img_update
        self.root.bind("<Button-1>", nastepny_wierzcholek_na_tlo)
        self.root.bind("<Button-3>", nastepna_krawedz_na_tlo)
        self.root.bind("<Button-2>", reset_tla)
        # self.root.bind("<Double-Button-1>", poprzedni_wierzcholek_na_tlo)
        # self.root.bind("<Double-Button-3>", poprzednia_krawedz_na_tlo)

        # frame = Frame(self.root, width=300, height=250)
        # frame.bind("<Button-1>", nastepny_graf_na_tlo)
        # frame.bind("<Button-2>", reset_tla)
        # frame.bind("<Button-3>", poprzedni_graf_na_tlo)
        # frame.pack()

        # def gen_graf_plus_node_test2():
        #     l_ggn = 'a'
        #     g = Graph(format='png')
        #     g.node(str(l_ggn))
        #     aski = ord(l_ggn)
        #     aski += 1
        #     l_ggn = chr(aski)
        #     g.node(str(l_ggn))
        #     aski = ord(l_ggn)
        #     aski += 1
        #     l_ggn = chr(aski)
        #     obrazek = g.render('dot', 'png')
        #     print(obrazek)
        # gen_graf_plus_node_test2()

        self.root.mainloop()