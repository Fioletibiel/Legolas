from graphviz import render
from tkinter import *
from OdczytZapis import *
from PIL import ImageTk, Image


class DOT(object):

    def __init__(self):
        self.root = Toplevel()

        graf = OdczytZapis.odczytDOT()
        obrazek = render('dot', 'png', graf)
        obrazek = ImageTk.PhotoImage(Image.open(obrazek))
        panel = Label(self.root, image=obrazek)
        panel.image = obrazek
        panel.pack(side="top", fill="both", expand="yes")

        # img = ImageTk.PhotoImage(Image.open('kot.png'))
        # panel = Label(self.root, image=img)
        # panel.image = img
        # panel.pack(side="top", fill="both", expand="yes")