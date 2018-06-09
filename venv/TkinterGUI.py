from tkinter import *
import tkinter
from OdczytZapis import OdczytZapis
from Graf import Graf
from DOT import DOT
from graphviz import render
from PIL import ImageTk, Image


class TkinterGUI(object):

    def __init__(self):
        self.root = Tk()
        # self.root.geometry("200x250")
        self.root.title('GIZ projekt')
        self.root.iconbitmap('obrazki\celtic_tree.ico')

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

        img = ImageTk.PhotoImage(Image.open("obrazki\celtic_tree_2_2.png"))
        panell = Label(self.root, image=img)
        panell.image = img
        panell.pack(side="top", fill="both", expand="yes")

        # bottomFrame = Frame(self.root).pack(side=BOTTOM)
        # def leftClick(event):
        #     print("Left")
        # def middleClick(event):
        #     print("Middle")
        # def rightClick(event):
        #     print("Right")
        # frame = Frame(self.root, width=300, height=250)
        # frame.bind("<Button-1>", leftClick)
        # frame.bind("<Button-2>", middleClick)
        # frame.bind("<Button-3>", rightClick)
        # frame.pack()

        self.root.mainloop()