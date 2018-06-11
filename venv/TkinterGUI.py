from tkinter import *
import tkinter
from OdczytZapis import OdczytZapis
from OdczytZapis import *
from Graf import Graf
from DOT import DOT
from graphviz import render
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
        subMenu1.add_command(label="DOT->Graf", command=OdczytZapis.DOT2Pic)
        subMenu1.add_command(label="Prüfer->Graf", command=OdczytZapis.Prufer2Pic)
        subMenu1.add_command(label="DOT->Prüfer", command=OdczytZapis.DOT2Prufer)
        subMenu1.add_command(label="Prüfer->DOT", command=OdczytZapis.Prufer2DOT)
        subMenu2 = Menu(menu)
        menu.add_cascade(label="Lista kursów", menu=subMenu2)
        subMenu2.add_command(label="Do zrobienia 1", command=OdczytZapis.Kurs)
        subMenu2.add_command(label="Do zrobienia 2", command=OdczytZapis.Kurs)

        img = Image.open("obrazki\PJATK_tlo_transparentne_wodne.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        tlo = Label(self.root, image=img)
        tlo.image = img
        tlo.pack(side="top", fill="both", expand="yes")

        def nastepny_graf_na_tlo(event):
            # img_update = Image.open(OdczytZapis.gen_graf_plus_node)
            # img_update = img_update.resize((250, 250), Image.ANTIALIAS)
            # img_update = ImageTk.PhotoImage(img_update)
            # tlo.configure(image=img_update)
            # tlo.image = img_update
            print(OdczytZapis.gen_graf_plus_node)
        def reset_tla(event):
            img_update = Image.open("obrazki\PJATK_tlo_transparentne_wodne.png")
            img_update = img_update.resize((250, 250), Image.ANTIALIAS)
            img_update = ImageTk.PhotoImage(img_update)
            tlo.configure(image=img_update)
            tlo.image = img_update
        def poprzedni_graf_na_tlo(event):
            img_update = Image.open("obrazki\PJATK_tlo_transparentne_wodne_3.png")
            img_update = img_update.resize((250, 250), Image.ANTIALIAS)
            img_update = ImageTk.PhotoImage(img_update)
            tlo.configure(image=img_update)
            tlo.image = img_update
        self.root.bind("<Button-1>", nastepny_graf_na_tlo)
        self.root.bind("<Button-2>", reset_tla)
        self.root.bind("<Button-3>", poprzedni_graf_na_tlo)

        # frame = Frame(self.root, width=300, height=250)
        # frame.bind("<Button-1>", nastepny_graf_na_tlo)
        # frame.bind("<Button-2>", reset_tla)
        # frame.bind("<Button-3>", poprzedni_graf_na_tlo)
        # frame.pack()

        self.root.mainloop()