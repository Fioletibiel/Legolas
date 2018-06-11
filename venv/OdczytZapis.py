from tkinter import *
from tkinter import filedialog
from graphviz import render
from graphviz import *
from tkinter import *
from PIL import ImageTk, Image
from Prufer import Prufer


class OdczytZapis(object):


    def __init__(self):
        self.root = Toplevel()

    def DOT2Pic():
        root2 = Toplevel()
        plik_DOT = filedialog.askopenfilename(filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")), title="Proszę wybierz plik z kodem DOT")
        if plik_DOT:
            try:
                print("Plik został wczytany pomyślnie.")
            except:
                showerror("Open Source File", "Failed to read file\n'%s'" % plik_DOT)
            obrazek = render('dot', 'png', plik_DOT)
            obrazek = ImageTk.PhotoImage(Image.open(obrazek))
            panel = Label(root2, image=obrazek)
            panel.image = obrazek
            panel.pack(side="top", fill="both", expand="yes")

    def Prufer2Pic():
        root2 = Toplevel()
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
        panel = Label(root2, image=obrazek)
        panel.image = obrazek
        panel.pack(side="top", fill="both", expand="yes")

    l_ggn = 0
    def gen_graf_plus_node():
        g = Graph(format='png')
        g.node(str(l_ggn))
        OdczytZapis.l_ggn+=1
        obrazek = g.render('dot', 'png')
        print(obrazek)

    # def random_node_name():
    #     i = random.randomint(1,100)
    #     return i
    #
    # l_gge = 'a'
    # def gen_graf_plus_edge():
    #     g = Graph(format='png')
    #     g.edge(label=OdczytZapis.l_gge, tail_name=, head_name=)
    #     OdczytZapis.l_gge+=1
    #     obrazek = g.render('dot', 'png')
    #     print(obrazek)

    # def gen_graf_minus_node():
    #     g = Graph(format='png')
    #     OdczytZapis.l_ggn -= 1
    #     obrazek = g.render('dot', 'png')
    #     print(obrazek)
    #
    # def gen_graf_minus_node():
    #     g = Graph(format='png')
    #     OdczytZapis.l_gge -= 1
    #     obrazek = g.render('dot', 'png')
    #     print(obrazek)



    def DOT2Prufer():
        plik_DOT = filedialog.askopenfilename(filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")), title="Proszę wybierz plik z kodem DOT")
        if plik_DOT:
            try:
                print("Plik został wczytany pomyślnie.")
            except:
                showerror("Open Source File", "Failed to read file\n'%s'" % plik_DOT)
            tresc_pliku = open(plik_DOT, 'w')
            tresc_pliku = Prufer.DOT2Prufer(tresc_pliku)
            plik_Prufer = filedialog.asksaveasfilename(
                filetypes=(("Text Documents", "*.txt"), ("All files", "*.*")),
                title='Proszę wybierz plik .txt, do którego chcesz zapisać kod Prüfera.',
                defaultextension='.txt')
            if plik_Prufer:
                try:
                    print("Plik został pomyślnie zapisany.")
                except:
                    showerror("Open Source File", "Failed to save file\n'%s'" % plik_Prufer)
                plik = open(plik_Prufer, 'w')
                plik.write(tresc_pliku)
                plik.close()

    def Prufer2DOT():
        plik_Prufer = filedialog.askopenfilename(filetypes=(("Text Documents", "*.txt"), ("All files", "*.*")), title="Proszę wybierz plik .txt z kodem Prüfera")
        if plik_Prufer:
            try:
                print("Plik został wczytany pomyślnie.")
            except:
                showerror("Open Source File", "Failed to read file\n'%s'" % plik_Prufer)
            Prufer.checkifPrufer(plik_Prufer)
            tresc_pliku = open(plik_Prufer, 'w')
            Prufer.Prufer2DOT(tresc_pliku)
            plik_DOT = filedialog.asksaveasfilename(filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")),title='Proszę wybierz plik .txt, do którego chcesz zapisać kod DOT.',defaultextension='.txt')
            if plik_DOT:
                try:
                    print("Plik został pomyślnie zapisany.")
                except:
                    showerror("Open Source File", "Failed to save file\n'%s'" % plik_DOT)
                plik = open(plik_DOT, 'w')
                plik.write(tresc_pliku)
                plik.close()

    def Pic2DOT():
        pass

    def Pic2Prufer():
        pass


    def Kurs():
        plik_DOT = filedialog.asksaveasfilename(filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")),title='Proszę wybierz plik .txt, do którego chcesz zapisać kod DOT namalowanego grafu.',defaultextension='.txt')
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