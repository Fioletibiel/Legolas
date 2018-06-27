from tkinter import *
import tkinter
from tkinter import filedialog
from OdczytZapis import OdczytZapis
from OdczytZapis import *
from graphviz import render
from graphviz import *
from PIL import ImageTk, Image
import networkx as nx
import numpy as np


class TkinterGUI(object):

    tablica_dodanych_a = []
    tablica_dodanych_m = []
    tablica_dodanych_wierzcholkow = []

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

        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        def znajdz_najmniejsza_nierowna_ciagowi(ciag_b, ciag_a, x):
            main_list = np.setdiff1d(ciag_b, ciag_a)
            minimum = min(j for j in main_list if j != x)
            return minimum
        def tworz_alfabet():
            alfabet = []
            czar = 'a'
            for i in range(24):
                alfabet.append(czar)
                aski = ord(czar)
                aski += 1
                czar = chr(aski)
            return alfabet
        def Prufer2Pic_konwersja(tresc_pliku):
            a2 = tresc_pliku.split()
            a = [] * len(a2)
            alfabet = tworz_alfabet()
            no_i = "int czy string?"
            a_int = []
            ar = [] * len(a2)
            try:
                for i in range(len(a2)):
                    bufor_a_2 = int(a2[i])
                    a_int.append(bufor_a_2)
                no_i = "inty"
                a = a_int
            except ValueError:
                # print("Zamiana znaków etykiet na liczby...")
                no_i = "stringi"
            if no_i=="inty":
                ar = a.copy()
            elif no_i=="stringi":
                ar = a2.copy()
            else:
                print("Coś poszło nie tak - Wczytany plik nie składa się ani z integerów, ani ze stringów.")
            print("Wczytany plik zawiera "+str(no_i)+".")
            print("a wynosi: "+str(a))
            # poniżej zamiana stringów na inty, w przypadku, gdy wczytana tablica jest ze stringów
            if isinstance(ar[0], str) and ar[0] != None:
                for i in range(len(a2)):
                    for j in range(len(alfabet)):
                        if a2[i] == alfabet[j]:
                            bufor = j
                    a.append(bufor+1)
            # poniżej robi się listę b kolejnych liczb o dwie więcej, niż w liście a
            b = []
            for i in range(len(a)+2):
                b.append(i+1)
            # teraz zaczyna sie dopasowywanie:
            OdczytZapis.g = Graph(format='png')
            m = [] * len(a)
            # for i in range(len(a)):
            #     m.append(znajdz_najmniejsza_nierowna_ciagowi(b, a, a[0]))
            #     for j in range(len(TkinterGUI.tablica_dodanych_wierzcholkow)):
            #         if len(TkinterGUI.tablica_dodanych_wierzcholkow)==0:
            #             OdczytZapis.g.node(str(a[0]))
            #             TkinterGUI.tablica_dodanych_wierzcholkow.append(a[0])
            #         elif TkinterGUI.tablica_dodanych_wierzcholkow[j] != a[0]:
            #             OdczytZapis.g.node(str(a[0]))
            #             TkinterGUI.tablica_dodanych_wierzcholkow.append(a[0])
            #     for j in range(len(TkinterGUI.tablica_dodanych_wierzcholkow)):
            #         if TkinterGUI.tablica_dodanych_wierzcholkow[j] != m[i]:
            #             OdczytZapis.g.node(str(m[i]))
            #             TkinterGUI.tablica_dodanych_wierzcholkow.append(m)
            #     OdczytZapis.g.edge(str(a[0]),str(m[i]))
            #     print("a"+str(i)+": "+str(a))
            #     print("b" + str(i) + ": " + str(b))
            #     a.remove(a[0])
            #     b.remove(m[i])
            # # teraz dodajemy krawędź z dwóch ostatnich elementów ciągu Prüfera
            # for j in range(len(TkinterGUI.tablica_dodanych_wierzcholkow)):
            #     if TkinterGUI.tablica_dodanych_wierzcholkow[j] != b[0]:
            #         OdczytZapis.g.node(str(b[0]))
            #         TkinterGUI.tablica_dodanych_wierzcholkow.append(b[0])
            #     if TkinterGUI.tablica_dodanych_wierzcholkow[j] != b[1]:
            #         OdczytZapis.g.node(str(b[1]))
            #         TkinterGUI.tablica_dodanych_wierzcholkow.append(b[1])
            # OdczytZapis.g.edge(str(b[0]),str(b[1]))
            # print("a final: " + str(a))
            # print("b final: " + str(b))
            for i in range(len(a)):
                m.append(znajdz_najmniejsza_nierowna_ciagowi(b, a, a[0]))
                for j in range(len(TkinterGUI.tablica_dodanych_wierzcholkow)):
                    if len(TkinterGUI.tablica_dodanych_wierzcholkow)==0:
                        if isinstance(ar[0],int):
                            OdczytZapis.g.node(str(a[0]))
                            TkinterGUI.tablica_dodanych_wierzcholkow.append(a[0])
                        elif isinstance(ar[0], str):
                            for k in range(len(alfabet)):
                                if a[0] == (k+1):
                                    bufor = k
                            OdczytZapis.g.node(alfabet[bufor])
                            TkinterGUI.tablica_dodanych_wierzcholkow.append(a[0])
                    elif TkinterGUI.tablica_dodanych_wierzcholkow[j] != a[0]:
                        if isinstance(ar[0],int):
                            OdczytZapis.g.node(str(a[0]))
                            TkinterGUI.tablica_dodanych_wierzcholkow.append(a[0])
                        elif isinstance(ar[0], str):
                            for k in range(len(alfabet)):
                                if a[0] == (k+1):
                                    bufor = k
                            OdczytZapis.g.node(alfabet[bufor])
                            TkinterGUI.tablica_dodanych_wierzcholkow.append(a[0])
                for j in range(len(TkinterGUI.tablica_dodanych_wierzcholkow)):
                    if TkinterGUI.tablica_dodanych_wierzcholkow[j] != m[i]:
                        if isinstance(ar[0],int):
                            OdczytZapis.g.node(str(m[i]))
                            TkinterGUI.tablica_dodanych_wierzcholkow.append(m[i])
                        elif isinstance(ar[0], str):
                            for k in range(len(alfabet)):
                                if m[i] == (k+1):
                                    bufor = k
                            OdczytZapis.g.node(alfabet[bufor])
                            TkinterGUI.tablica_dodanych_wierzcholkow.append(m[i])
                print("FLAGA")
                if isinstance(ar[0], int):
                    OdczytZapis.g.edge(str(a[0]), str(m[i]))
                elif isinstance(ar[0], str):
                    for k in range(len(alfabet)):
                        if a[0] == (k + 1):
                            bufor_a = k
                    for k in range(len(alfabet)):
                        if m[i] == (k + 1):
                            bufor_m = k
                    OdczytZapis.g.edge(alfabet[bufor_a],alfabet[bufor_m])
                print("a"+ str(i) +": "+ str(a))
                print("b" + str(i) + ": " + str(b))
                # a.remove(a[0])
                a.pop(0)
                b.remove(m[i])
            # teraz dodajemy krawędź z dwóch ostatnich elementów ciągu Prüfera
            for j in range(len(TkinterGUI.tablica_dodanych_wierzcholkow)):
                if TkinterGUI.tablica_dodanych_wierzcholkow[j] != b[0]:
                    if isinstance(ar[0], int):
                        OdczytZapis.g.node(str(b[0]))
                        TkinterGUI.tablica_dodanych_wierzcholkow.append(b[0])
                    elif isinstance(ar[0], str):
                        for k in range(len(alfabet)):
                            if b[0] == (k + 1):
                                bufor = k
                        OdczytZapis.g.node(alfabet[bufor])
                        TkinterGUI.tablica_dodanych_wierzcholkow.append(b[0])
                    # OdczytZapis.g.node(str(b[0]))
                    # TkinterGUI.tablica_dodanych_wierzcholkow.append(b[0])
                if TkinterGUI.tablica_dodanych_wierzcholkow[j] != b[1]:
                    if isinstance(ar[0], int):
                        OdczytZapis.g.node(str(b[1]))
                        TkinterGUI.tablica_dodanych_wierzcholkow.append(b[1])
                    elif isinstance(ar[0], str):
                        for k in range(len(alfabet)):
                            if b[1] == (k + 1):
                                bufor = k
                        OdczytZapis.g.node(alfabet[bufor])
                        TkinterGUI.tablica_dodanych_wierzcholkow.append(b[1])
                    # OdczytZapis.g.node(str(b[1]))
                    # TkinterGUI.tablica_dodanych_wierzcholkow.append(b[1])
            if isinstance(ar[0], int):
                print("ar 2: " + str(ar))
                OdczytZapis.g.edge(str(b[0]), str(b[1]))
            elif isinstance(ar[0], str):
                for k in range(len(alfabet)):
                    if b[0] == (k + 1):
                        bufor_b0 = k
                for k in range(len(alfabet)):
                    if b[1] == (k + 1):
                        bufor_b1 = k
                OdczytZapis.g.edge(alfabet[bufor_b0], alfabet[bufor_b1])
            print("a final: " + str(a))
            print("b final: " + str(b))
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
            plik_DOT = "abc"
            OdczytZapis.g.render(plik_DOT)
            img_update = render('dot', 'png', plik_DOT)
            img_update = ImageTk.PhotoImage(Image.open(img_update))
            tlo.configure(image=img_update)
            tlo.image = img_update
        def Prufer2DOT():
            plik_Prufer = filedialog.askopenfilename(filetypes=(("Text Documents", "*.txt"), ("All files", "*.*")),
                                                     title="Proszę wybierz plik .txt z kodem Prüfera.")
            if plik_Prufer:
                try:
                    print("Plik został wczytany pomyślnie.")
                except:
                    showerror("Open Source File", "Failed to read file\n'%s'" % plik_Prufer)
            with open(plik_Prufer, 'r') as myfile:
                tresc_pliku = myfile.read()
            Prufer2Pic_konwersja(tresc_pliku)
            plik_DOT = filedialog.asksaveasfilename(
                filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")),
                title="Proszę wybierz plik, do którego chcesz zapisać kod DOT.")
            if plik_DOT:
                try:
                    print("Plik został zapisany pomyślnie.")
                    OdczytZapis.g.render(plik_DOT)
                except:
                    showerror("Open Source File", "Failed to read file\n'%s'" % plik_DOT)

        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        def DOT2Prufer_konwersja(plik_DOT):
            return plik_Prufer
        def DOT2Prufer():
            plik_DOT = filedialog.askopenfilename(
                filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")),
                title="Proszę wybierz plik z kodem DOT.")
            if plik_DOT:
                try:
                    print("Plik został wczytany pomyślnie.")
                except:
                    showerror("Open Source File", "Failed to read file\n'%s'" % plik_DOT)
            tresc_pliku = DOT2Prufer_konwersja(plik_DOT)
            plik_Prufer = filedialog.asksaveasfilename(
                filetypes=(("Text Documents", "*.txt"), ("All files", "*.*")),
                title='Proszę wybierz plik .txt, do którego chcesz zapisać kod Prüfera.',
                defaultextension='.txt')
            if plik_Prufer:
                try:
                    print("Plik został pomyślnie zapisany.")
                    plik = open(plik_Prufer, 'w')
                    plik.write(tresc_pliku)
                    plik.close
                except:
                    showerror("Open Source File", "Failed to save file\n'%s'" % plik_Prufer)

        # Opcjonalnie do zrobienia DOT2Prufer_konwersja():
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        bufor_od = OdczytZapis.tablica_wybranych_randomowych_od.copy()
        bufor_do = OdczytZapis.tablica_wybranych_randomowych_do.copy()
        usuwany_element = 'a'
        def liscie_od_najmniejszego_do_najwiekszego(od, do):
            # wyciagniecie tablicy lisci:
            tablica_lisci = []
            for i in range(len(od)):
                b = True
                for j in range(len(do)):
                    if od[i] == do[j]:
                        b = False
                if b == True:
                    tablica_lisci.append(od[i])
            for i in range(len(do)):
                b = True
                for j in range(len(od)):
                    if do[i] == od[j]:
                        b = False
                if b == True:
                    tablica_lisci.append(do[i])
            # powyżej wytypowałem te wierzchołki, do których wchodzą krawędzie, ale nie wychodzą, oraz te, z których wychodzą krawędzie, ale żadne nie wchodzą - czyli które są tylko w zbiorze 'od', albo tylko w zbiorze 'do'...
            # jednak to nie wystarczy, ponieważ może tak się zdarzyć, że wierzchołek nie będący wcale liściem ma np. dwie krawędzie tylko wchodzące, lub tylko wychodzące i takie wierzchołki trzeba usunąć z tablicy_liści...
            # tak więc trzeba znaleźć teraz wierzchołki, które są kilka razy w zbiorze 'od' lub w zbiorze 'do' (lub wcześniej liczyć ile razy dany wierzchołek był w od oraz w do i jeśli więcej niż raz, to jest on zapamiętywany i potem usuwany):
            for i in range(len(od)):
                k = 0
                for j in range(len(od)):
                    if od[i] == od[j]:
                        k += 1
                if k > 1:
                    tablica_lisci.remove(od[i])
            for i in range(len(do)):
                k = 0
                for j in range(len(do)):
                    if do[i] == do[j]:
                        k += 1
                if k > 1:
                    tablica_lisci.remove(do[i])
            # posortowanie tablicy lisci:
            tablica_lisci.sort()
            return tablica_lisci
        def liscie_od_najmniejszego_do_najwiekszego_uaktualniana(od, do):
            for i in range(len(od)):
                if od[i] == usuwany_element:    # jeśli którykolwiek wierzchołek 'od' jest równy usuwanemu wierzchołkowi, to usuwa się go ze zbioru wierzchołków 'od' oraz odpowiadającego mu wierzchołka ze zbioru wierzchołków 'do'...
                    od.remove(od[i])
                    do.remove(do[i])
            for i in range(len(do)):
                if do[i] == usuwany_element:    # to samo, co wyżej, tylko tym razem poczynając od zbioru wierzchołków 'do'...
                    od.remove(od[i])
                    do.remove(do[i])
            tablica_lisci = liscie_od_najmniejszego_do_najwiekszego(od, do)    # uaktualnia tablicę liści z pomniejszonych zbiorów wierzchołków 'od' i 'do'.
            return tablica_lisci
        def ten_z_ktorym_sie_laczy(usuwany_element, od, do):
            for i in range(len(od)):
                if od[i] == usuwany_element:
                    dodawany_element = do[i]

            for i in range(len(do)):
                if do[i] == usuwany_element:
                    dodawany_element = od[i]
            return dodawany_element
        def jesli_obecny_to_usun(lista, element):
            buf_lista = lista.copy()
            for i in range(len(lista)):
                if lista[i]==element:
                    buf_lista.pop(i)
            return buf_lista
        def Pic2Prufer_konwersja():
            tabela_Prufera = []
            tablica_lisci = liscie_od_najmniejszego_do_najwiekszego(bufor_od, bufor_do)
            tablica_lisci_pomniejszana = tablica_lisci.copy()
            i = 0
            while i < len(OdczytZapis.tablica_nazw_wierzcholkow) - 2:
                usuwany_element = tablica_lisci_pomniejszana[0]
                dodawany_element = ten_z_ktorym_sie_laczy(usuwany_element, bufor_od, bufor_do)
                tabela_Prufera.append(dodawany_element)
                # bufor_od = jesli_obecny_to_usun(bufor_od, usuwany_element)
                # bufor_do = jesli_obecny_to_usun(bufor_do, usuwany_element)
                # tablica_lisci_pomniejszana = liscie_od_najmniejszego_do_najwiekszego(bufor_od, bufor_do)
                tablica_lisci_pomniejszana = liscie_od_najmniejszego_do_najwiekszego_uaktualniana(bufor_od,bufor_do)
                i += 1
            trescpliku = ' '.join(str(e) for e in tabela_Prufera)
            return trescpliku
        def Pic2Prufer():
            tresc_pliku = Pic2Prufer_konwersja()
            plik_Prufer = filedialog.asksaveasfilename(
                filetypes=(("Text Documents", "*.txt"), ("All files", "*.*")),
                title='Proszę wybierz plik .txt, do którego chcesz zapisać kod Prüfera.',
                defaultextension='.txt')
            if plik_Prufer:
                try:
                    print("Plik został pomyślnie zapisany.")
                    plik = open(plik_Prufer, 'w')
                    plik.write(tresc_pliku)
                    plik.close
                except:
                    showerror("Open Source File", "Failed to save file\n'%s'" % plik_Prufer)

        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        def Tekst2Wynik_konwersja(tresc_pliku):
            tekst = tresc_pliku.split()
            n = tekst[0]
            m = tekst[1]
            # print("n: "+str(n)+" i m: "+str(m))
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

            kopia_a = a
            kopia_b = b
            def odejmowanie_dwoch_tablic(a,b):
                c = []
                for i in range(len(a)):
                    bool = True
                    for j in range(len(b)):
                        if a[i] == b[j]:
                            bool = False
                    if bool == True:
                        c.append(a[i])
                return c
            def aktualny_semestr(a,b,c,d):
                prawidziwe_a = c
                prawdziwe_b = d
                kopia_a = a
                kopia_b = b
                tablica_semestru = []
                tablica_sasiadow_semestru = []
                for i in range(len(kopia_b)):
                    bool = True
                    for j in range(len(kopia_a)):
                        if kopia_b[i] == kopia_a[j]:
                            bool = False
                    if bool == True:
                        tablica_semestru.append(kopia_b[i])
                        bufor = 0
                        for k in range(len(prawdziwe_b)):
                            if prawdziwe_b[k] == kopia_b[k]:
                                bufor = k
                        tablica_sasiadow_semestru.append(prawidziwe_a[k])
                kopia_a = odejmowanie_dwoch_tablic(kopia_a,tablica_sasiadow_semestru)
                kopia_b = odejmowanie_dwoch_tablic(kopia_b,tablica_semestru)
                return tablica_semestru, kopia_a, kopia_b
            licz = 1
            bufor_tablica_semestru = []
            while True:
                tablica_semestru, kopia_a, kopia_b = aktualny_semestr(kopia_a, kopia_b, a, b)
                if bufor_tablica_semestru != tablica_semestru:
                    bufor_tablica_semestru = tablica_semestru
                    print("Semestr "+str(licz)+": "+str(tablica_semestru))
                    licz +=1
                else:
                    break

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

        # Do zrobienia:
        # 1) Poprawić Pic2Prüfer():
        # 2) Sprawdzić, czy Tekst2Wynik działa poprawnie na większych drzewach, ponieważ te przykładowe Michała coś u mnie nie działały...
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        menu = Menu(self.root)
        self.root.config(menu=menu)
        subMenu1 = Menu(menu)
        menu.add_cascade(label="Kod Prüfera", menu=subMenu1)
        subMenu1.add_command(label="DOT->Picture", command=DOT2Pic)
        subMenu1.add_command(label="Picture->DOT", command=OdczytZapis.Pic2DOT)
        subMenu1.add_command(label="Prüfer->Picture", command=Prufer2Pic)
        subMenu1.add_command(label="Picture->Prüfer", command=Pic2Prufer)
        subMenu1.add_command(label="Prüfer->DOT", command=Prufer2DOT)
        # subMenu1.add_command(label="DOT->Prüfer", command=DOT2Prufer)


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