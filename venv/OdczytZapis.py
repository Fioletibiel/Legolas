from tkinter import *
from tkinter import filedialog
from DOT import DOT


class OdczytZapis(object):

    def __init__(self):
        self.root = Tk()

    def odczytPrufer():
        plik_Prufer = filedialog.askopenfilename(
            filetypes=(("Text Documents", "*.txt"), ("All files", "*.*")),
            title="Proszę wybierz plik .txt z kodem Prüfera")
        if plik_Prufer:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
            except:  # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % plik_Prufer)
            return
        return plik_Prufer

    def odczytDOT():
        plik_DOT = filedialog.askopenfilename(
            filetypes=(("Text Documents", "*.txt"), ("All files", "*.*")), title="Proszę wybierz plik .txt z kodem DOT")
        if plik_DOT:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
            except:  # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % plik_DOT)
            return
        return plik_DOT

    def zapisPrufer():
        plik_Prufer = filedialog.asksaveasfilename(
            filetypes=(("Text Documents", "*.txt"), ("All files", "*.*")),
            title='Proszę wybierz plik .txt, do którego chcesz zapisać kod Prüfera namalowanego grafu.',
            defaultextension='.txt')
        if plik_Prufer:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
            except:  # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % plik_Prufer)
            return
        return plik_Prufer
        plik = open(plik_Prufer, 'w')
        plik.write("tresc")
        plik.close()

    def zapisDOT():
        plik_DOT = filedialog.asksaveasfilename(filetypes=(("Text Documents", "*.txt"), ("All files", "*.*")),
                                                        title='Proszę wybierz plik .txt, do którego chcesz zapisać kod DOT namalowanego grafu.',
                                                        defaultextension='.txt')
        if plik_DOT:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
            except:  # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % plik_DOT)
            return
        return plik_DOT
        plik = open(plik_DOT, 'w')
        plik.write("tresc")
        plik.close()