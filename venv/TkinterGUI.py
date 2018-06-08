from tkinter import *
import tkinter
from OdczytZapis import OdczytZapis


class TkinterGUI(object):

    def __init__(self):
        self.root = Tk()
        self.root.geometry("200x250")
        self.root.title('GIZ projekt')
        self.root.iconbitmap('celtic_tree.ico')



        menu = Menu(self.root)
        self.root.config(menu=menu)
        subMenu1 = Menu(menu)
        menu.add_cascade(label="Kod Prüfera", menu=subMenu1)
        subMenu1.add_command(label="Prüfer->Graf", command=OdczytZapis.odczytPrufer)
        subMenu1.add_command(label="Graf->Prüfer", command=OdczytZapis.zapisPrufer)
        subMenu2 = Menu(menu)
        menu.add_cascade(label="Kod DOT", menu=subMenu2)
        subMenu2.add_command(label="DOT->Graf", command=OdczytZapis.odczytDOT)
        subMenu2.add_command(label="Graf->DOT", command=OdczytZapis.zapisDOT)



        self.root.mainloop()