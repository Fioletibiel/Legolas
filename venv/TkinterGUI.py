from tkinter import *
import tkinter
from tkinter import filedialog
from OdczytZapis import OdczytZapis
from OdczytZapis import *
from graphviz import render
from graphviz import *
from PIL import ImageTk, Image
import networkx as nx


class TkinterGUI(object):

    tablica_dodanych_a = []
    tablica_dodanych_m = []

    def __init__(self):
        self.root = Tk()
        # self.root.geometry("200x250")
        self.root.title('GIZ projekt, Autor: Paweł Kamiński')
        self.root.iconbitmap('obrazki\PJATK_icon_transparent.ico')

        def DOT2Pic():
            plik_DOT = filedialog.askopenfilename(filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")), title="Proszę wybierz plik z kodem DOT.")
            if plik_DOT:
                try:
                    print("Plik został wczytany pomyślnie.")
                except:
                    showerror("Open Source File", "Failed to read file\n'%s'" % plik_DOT)
                obrazek = render('dot', 'png', plik_DOT)
                obrazek = ImageTk.PhotoImage(Image.open(obrazek))
                tlo.configure(image=obrazek)
                tlo.image = obrazek


        def znajdz_najmniejsza_nierowna(ciag, x):
            m = min(j for j in ciag if j != x)
            return m
        def Prufer2Pic_konwersja(tresc_pliku):
            a3 = tresc_pliku.split()
            alfabet = []
            czar = 'a'
            for i in range(24):
                alfabet.append(czar)
                aski = ord(czar)
                aski += 1
                czar = chr(aski)
            a_int = []
            a_chr = []
            a = [] * len(a3)
            no_i = "int czy string?"
            try:
                for i in range(len(a3)):
                    bufor_a_3 = int(a3[i])
                    a_int.append(bufor_a_3)
                no_i = "int"
                a2 = a_int
            except ValueError:
                print("Oops!")
            try:
                if no_i != "int":
                    for i in range(len(a3)):
                        print("Typ: "+str(a3[i])+" to "+str(type(a3[i])))
                        bufor_a_trzy = chr(a3[i])
                        a_chr.append(bufor_a_trzy)
                    a2 = a_chr
            except ValueError:
                print("Oops!")
            if type(a2[0]) == chr and a2[0] != None:
                for i in range(len(a2)):
                    for j in range(alfabet):
                        if a2[i] == alfabet[j]:
                            bufor = j
                    a[i] = j+1
            else:
                a = a2
            # a = []
            # for i in range(len(a3)):
            #     print(a3[i])
            #     a.append(int(a3[i]))

            b = []
            for i in range(len(a)+2):
                b.append(i+1)
            # teraz zaczyna sie dopasowywanie:
            OdczytZapis.g = Graph(format='png')
            dlugosc_ciagu = len(a)
            for i in range(dlugosc_ciagu):
                m = znajdz_najmniejsza_nierowna(b, a[i])
                for j in range(len(TkinterGUI.tablica_dodanych_a)):
                    if TkinterGUI.tablica_dodanych_a[j] != a[i]:
                        OdczytZapis.g.node(a[i])
                        TkinterGUI.tablica_dodanych_a.append(a[i])
                for j in range(len(TkinterGUI.tablica_dodanych_m)):
                    if TkinterGUI.tablica_dodanych_m[j] != m:
                        OdczytZapis.g.node(m)
                        TkinterGUI.tablica_dodanych_m.append(m)
                OdczytZapis.g.edge(str(a[i]),str(m))
                a.remove(a[i])
                b.remove(m)
            OdczytZapis.g.node(b[-1])
            OdczytZapis.g.node(b[-2])
            OdczytZapisg.edge(b[-1],b[-2])
        def Prufer2Pic():
            plik_Prufer = filedialog.askopenfilename(filetypes=(("Text Documents", "*.txt"), ("All files", "*.*")), title="Proszę wybierz plik .txt z kodem Prüfera.")
            if plik_Prufer:
                try:
                    print("Plik został wczytany pomyślnie.")
                except:
                    showerror("Open Source File", "Failed to read file\n'%s'" % plik_Prufer)
            with open(plik_Prufer, 'r') as myfile:
                tresc_pliku = myfile.read()
            Prufer2Pic_konwersja(tresc_pliku)
            img_update = render('dot', 'png', OdczytZapis.g)
            img_update = ImageTk.PhotoImage(Image.open(img_update))
            tlo.configure(image=img_update)
            tlo.image = img_update


        def Tekst2Wynik_konwersja(tresc_pliku):
            tekst = tresc_pliku.split()
            n = tekst[0]
            m = tekst[1]
            print("n: "+str(n)+" i m: "+str(m))
            a = []
            b = []
            for i in range(len(tekst)):
                if i+1>2 and (i+1)%2==1:
                    a.append(tekst[i])
                elif i+1>2 and (i+1)%2==0:
                    b.append(tekst[i])
                else:
                    pass
            # print("Tabela a:")
            # print(a)
            # print("Tabela b:")
            # print(b)

            # DOT = "graph {\n"
            # for i in range(len(a)):
            #     DOT += str(b[i])+" -> "+str(a[i])+";\n"
            # DOT += "}"
            # print(DOT)
            # G = nx.DiGraph(nx.read_dot(DOT))
            # C = nx.simple_cycles(G)
            # if len(C) < 1:
            #     wynik = "yes"
            # else:
            #     wynik = "no"
            # for i in C:
            #     print(i)
            g = {}
            for i in range(len(a)):
                g[b[i]]=a[i]
            # print(g)


            # Semestr 1: 1, 9, 11, 13, 15
            # Semestr 2: 0, 8, 10
            # Semestr 3: 3, 4, 5, 6
            # Semestr 4: 2, 7, 12
            # Semestr 5: 14

            def cyclic(g):
                path = set()
                visited = set()
                def visit(vertex):
                    if vertex in visited:
                        return False
                    visited.add(vertex)
                    path.add(vertex)
                    for neighbour in g.get(vertex, ()):
                        if neighbour in path or visit(neighbour):
                            return True
                    path.remove(vertex)
                    return False
                return any(visit(v) for v in g)
            cykliczny = cyclic(g)
            print(cykliczny)
            if cykliczny == True:
                wynik = "nie"
            elif cykliczny == False:
                wynik = "tak"
            return wynik
        def Tekst2Wynik():
            plik_kursy = filedialog.askopenfilename(filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")), title="Proszę wybierz plik z listą kursów.")
            if plik_kursy:
                try:
                    print("Plik został wczytany pomyślnie.")
                except:
                    showerror("Open Source File", "Failed to read file\n'%s'" % plik_kursy)
            with open(plik_kursy, 'r') as myfile:
                tresc_pliku = myfile.read()
            wynik = Tekst2Wynik_konwersja(tresc_pliku)
            if wynik == "tak":
                img_update = ImageTk.PhotoImage(Image.open("Obrazki\wynik_tak.png"))
                tlo.configure(image=img_update)
                tlo.image = img_update
            elif wynik =="nie":
                img_update = ImageTk.PhotoImage(Image.open("Obrazki\wynik_nie.png"))
                tlo.configure(image=img_update)
                tlo.image = img_update
            else:
                print("Coś poszło nie tak :/")


        # Poprawić:
        # 1) Prufer2Pic():

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
        subMenu2.add_command(label="Tekst->Wynik", command=Tekst2Wynik)

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