from tkinter import *
from tkinter import filedialog

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





    # def odczyt(self):
    #     # plik = open('nazwa_pliku')
    #     # try:
    #     #     tekst = plik.read()
    #     # finally:
    #     #     plik.close()
    #     # print(tekst)
    #
    #     # self.root.nazwa_pliku = filedialog.askopenfilename(title='wybierz plik .txt z zakodowanym grafem, lub z kodem Prüfera',filetypes=("Text Documents","*.txt"))
    #     # return self.root.nazwa_pliku
    #
    #     # self.root.nazwa_pliku = filedialog.askopenfilenames(parent=self)
    #     # self.title_count.set('{{file(s)'.format(len(self.selected_files)))
    #
    #     self.root.nazwa_pliku = filedialog.askopenfilename(filetypes=(("Text Documents", "*.txt"),("All files", "*.*")),title = "Wybierz plik .txt z kode")
    #     if fname:
    #         try:
    #             print("""here it comes: self.settings["template"].set(fname)""")
    #         except:                     # <- naked except is a bad idea
    #             showerror("Open Source File", "Failed to read file\n'%s'" % fname)
    #         return
    #
    # def zapis(self):
    #     # plik = open('plik', 'w')
    #     # plik.write("tresc")
    #     # plik.close()
    #     self.root.nazwa_pliku = filedialog.asksavefilename(title='wybierz plik .txt, do którego chcesz zapisać zakodowany graf, lub kod Prüfera',filetypes=("Text Documents","*.txt"))
    #     return self.root.nazwa_pliku
    #     # x = input('Podaj x: ')