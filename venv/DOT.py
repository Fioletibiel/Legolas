from graphviz import render
from tkinter import *
from venv.OczytZapis.py import *


class DOT(object):

    def __init__(self):
        self.root = Tk()
        obrazek = OdczytZapis.odczytDOT()
        obrazek = render('dot', 'png', obrazek)
        obrazek = ImageTk.PhotoImage(Image.open(obrazek))
        panel = tk.Label(self.root, image=obrazek)
        panel.pack(side="bottom", fill="both", expand="yes")