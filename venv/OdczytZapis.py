from tkinter import *
from tkinter import filedialog


class OdczytZapis(object):

    def __init__(self):
        self.root = Tk()


    def odczytDOT():
        plik_DOT = filedialog.askopenfilename(
            filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")), title="Proszę wybierz plik z kodem DOT")
        if plik_DOT:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
            except:
                showerror("Open Source File", "Failed to read file\n'%s'" % plik_DOT)
            return
        return plik_DOT


    def zapisPrufer():
        plik_Prufer = filedialog.asksaveasfilename(
            filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")),
            title='Proszę wybierz plik .txt, do którego chcesz zapisać kod Prüfera namalowanego grafu.',
            defaultextension='.txt')
        if plik_Prufer:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
            except:
                showerror("Open Source File", "Failed to read file\n'%s'" % plik_Prufer)
            return
        return plik_Prufer
        plik = open(plik_Prufer, 'w')
        plik.write("tresc")
        plik.close()


    def zapisKurs():
        plik_DOT = filedialog.asksaveasfilename(filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")),
                                                        title='Proszę wybierz plik .txt, do którego chcesz zapisać kod DOT namalowanego grafu.',
                                                        defaultextension='.txt')
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