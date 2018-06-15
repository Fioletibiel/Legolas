from tkinter import *
import tkinter
from tkinter import filedialog
from OdczytZapis import OdczytZapis
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

        def DOT2Pic():
            plik_DOT = filedialog.askopenfilename(filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")), title="Proszę wybierz plik z kodem DOT")
            if plik_DOT:
                try:
                    print("Plik został wczytany pomyślnie.")
                except:
                    showerror("Open Source File", "Failed to read file\n'%s'" % plik_DOT)
                obrazek = render('dot', 'png', plik_DOT)
                obrazek = ImageTk.PhotoImage(Image.open(obrazek))
                tlo.configure(image=obrazek)
                tlo.image = obrazek

        def Prufer2Pic():
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
            tlo.configure(image=obrazek)
            tlo.image = obrazek

        menu = Menu(self.root)
        self.root.config(menu=menu)
        subMenu1 = Menu(menu)
        menu.add_cascade(label="Kod Prüfera", menu=subMenu1)
        subMenu1.add_command(label="DOT->Picture", command=DOT2Pic)
        subMenu1.add_command(label="Picture->DOT", command=OdczytZapis.Pic2DOT)
        subMenu1.add_command(label="Prüfer->Picture", command=Prufer2Pic)
        subMenu1.add_command(label="Picture->Prüfer", command=OdczytZapis.Pic2Prufer)

        # subMenu1.add_command(label="DOT->Prüfer", command=OdczytZapis.DOT2Prufer)
        # subMenu1.add_command(label="Prüfer->DOT", command=OdczytZapis.Prufer2DOT)
        subMenu2 = Menu(menu)
        menu.add_cascade(label="Kursy", menu=subMenu2)
        subMenu2.add_command(label="Tekst->Wynik", command=OdczytZapis.Tekst2Wynik())
        subMenu2.add_command(label="Picture->Wynik", command=OdczytZapis.Pic2Wynik)

        img = Image.open("obrazki\PJATK_tlo_transparentne_wodne.png")
        # img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        tlo = Label(self.root, image=img)
        tlo.image = img
        tlo.pack(side="top", fill="both", expand="yes")


        def nastepny_wierzcholek(event):
            OdczytZapis.l_ggn += 1
            graf = OdczytZapis.gen_tree_plus_node()
            img_update = Image.open(graf)
            img_update = ImageTk.PhotoImage(img_update)
            tlo.configure(image=img_update)
            tlo.image = img_update
        def reset_tla(event):
            img_update = Image.open("obrazki\PJATK_tlo_transparentne_wodne.png")
            img_update = ImageTk.PhotoImage(img_update)
            tlo.configure(image=img_update)
            tlo.image = img_update
            OdczytZapis.node_name = 'a'
            OdczytZapis.l_ggn = 0
            OdczytZapis.g = Graph(format='png')
            OdczytZapis.tablica_nazw_wierzcholkow = []
            OdczytZapis.tablica_wybranych_przed_chwila = []

        self.root.bind("<Button-1>", nastepny_wierzcholek)
        self.root.bind("<Button-3>", reset_tla)


        self.root.mainloop()