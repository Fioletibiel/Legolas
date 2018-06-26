from tkinter import *
from tkinter import filedialog
from graphviz import render
from graphviz import *
from tkinter import *
from PIL import ImageTk, Image
import random
import string


class OdczytZapis(object):


    def __init__(self):
        self.root = Toplevel()

    node_name = 'a'
    l_ggn = 0
    l_gge = 0
    l_random = 0
    g = Graph(format='png')
    tablica_nazw_wierzcholkow = []
    wybrana_randomowa_przed_chwila = 'a'
    tablica_wybranych_randomowych_od = []
    tablica_wybranych_randomowych_do = []

    def Pic2DOT():
        plik_DOT = filedialog.asksaveasfilename(
            filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")),
            title="Proszę wybierz plik, do którego chcesz zapisać kod DOT.")
        if plik_DOT:
            try:
                print("Plik został zapisany pomyślnie.")
                OdczytZapis.g.render(plik_DOT)
            except:
                showerror("Open Source File", "Failed to read file\n'%s'" % plik_DOT)

    # def zwieksz_node_name():
    #     aski = ord(OdczytZapis.node_name)
    #     aski += 1
    #     OdczytZapis.node_name = chr(aski)
    #
    # def losowa_inna_niz_randomowo_od():
    #     while True:
    #         r = random.choice(OdczytZapis.tablica_nazw_wierzcholkow)
    #         b = False
    #         if r != OdczytZapis.wybrana_randomowa_przed_chwila[0]:
    #             b = True
    #         if b == True:
    #             break
    #     return r
    #
    # def randomowo_od():
    #     r_od = OdczytZapis.tablica_nazw_wierzcholkow[-1]
    #     OdczytZapis.tablica_wybranych_randomowych_od.append(r_od)
    #     OdczytZapis.wybrana_randomowa_przed_chwila = r_od
    #     return r_od
    #
    # def randomowo_do():
    #     r_do = OdczytZapis.losowa_inna_niz_randomowo_od()
    #     OdczytZapis.tablica_wybranych_randomowych_do.append(r_do)
    #     return r_do
    #
    # def gen_tree_plus_node():
    #     OdczytZapis.g.node(str(OdczytZapis.node_name))
    #     OdczytZapis.tablica_nazw_wierzcholkow.append(str(OdczytZapis.node_name))
    #     OdczytZapis.zwieksz_node_name()
    #
    #     if OdczytZapis.l_ggn > 1:
    #         OdczytZapis.g.edge(OdczytZapis.randomowo_od(),OdczytZapis.randomowo_do())
    #
    #     obrazek = OdczytZapis.g.render('dot', 'png')
    #     return obrazek
    #
    # def liscie_od_najmniejszego_do_najwiekszego():
    #     # wyciagniecie tablicy lisci:
    #     tablica_lisci = []
    #     for i in range(len(OdczytZapis.tablica_wybranych_randomowych_od)):
    #         b = True
    #         for j in range(len(OdczytZapis.tablica_wybranych_randomowych_do)):
    #             if OdczytZapis.tablica_wybranych_randomowych_od[i] == OdczytZapis.tablica_wybranych_randomowych_do[j]:
    #                 b = False
    #         if b == True:
    #             tablica_lisci.append(OdczytZapis.tablica_wybranych_randomowych_od[i])
    #     # posortowanie tablicy lisci:
    #     tablica_lisci.sort()
    #     return tablica_lisci
    #
    # bufor_tablica_wybranych_randomowych_od = tablica_wybranych_randomowych_od
    # bufor_tablica_wybranych_randomowych_do = tablica_wybranych_randomowych_do
    # usuwany_element = 'a'
    # def liscie_od_najmniejszego_do_najwiekszego_uaktualniana():
    #     tablica_lisci = []
    #     bufor = 0
    #     for i in range(len(OdczytZapis.bufor_tablica_wybranych_randomowych_od)):
    #         if OdczytZapis.bufor_tablica_wybranych_randomowych_od[i] == OdczytZapis.usuwany_element:
    #             bufor = i
    #     OdczytZapis.bufor_tablica_wybranych_randomowych_od.remove(OdczytZapis.bufor_tablica_wybranych_randomowych_od[bufor])
    #     OdczytZapis.bufor_tablica_wybranych_randomowych_do.remove(OdczytZapis.bufor_tablica_wybranych_randomowych_do[bufor])
    #     for i in range(len(OdczytZapis.bufor_tablica_wybranych_randomowych_od)):
    #         b = True
    #         for j in range(len(OdczytZapis.bufor_tablica_wybranych_randomowych_do)):
    #             if OdczytZapis.bufor_tablica_wybranych_randomowych_od[i] == OdczytZapis.bufor_tablica_wybranych_randomowych_do[j]:
    #                 b = False
    #         if b == True:
    #             tablica_lisci.append(OdczytZapis.bufor_tablica_wybranych_randomowych_od[i])
    #     tablica_lisci.sort()
    #     return tablica_lisci
    #
    # def ten_z_ktorym_sie_laczy(usuwany_element):
    #     bufor = 0
    #     for i in range(len(OdczytZapis.tablica_wybranych_randomowych_od)):
    #         if usuwany_element == OdczytZapis.tablica_wybranych_randomowych_od[i]:
    #             bufor = i
    #     dodawany_element = OdczytZapis.tablica_wybranych_randomowych_do[bufor]
    #     return dodawany_element
    #
    # def Pic2Prufer_konwersja():
    #     tabela_Prufera = []
    #     tablica_lisci = OdczytZapis.liscie_od_najmniejszego_do_najwiekszego()
    #     tablica_lisci_pomniejszana = tablica_lisci
    #     i = 0
    #     while i < len(OdczytZapis.tablica_nazw_wierzcholkow)-2:
    #         OdczytZapis.usuwany_element = tablica_lisci_pomniejszana[0]
    #         dodawany_element = OdczytZapis.ten_z_ktorym_sie_laczy(OdczytZapis.usuwany_element)
    #         tabela_Prufera.append(dodawany_element)
    #         tablica_lisci_pomniejszana.remove(OdczytZapis.usuwany_element)
    #         tablica_lisci_pomniejszana = OdczytZapis.liscie_od_najmniejszego_do_najwiekszego_uaktualniana()
    #         i += 1
    #     trescpliku = ' '.join(str(e) for e in tabela_Prufera)
    #     return trescpliku
    # def Pic2Prufer():
    #     tresc_pliku = OdczytZapis.Pic2Prufer_konwersja()
    #     plik_Prufer = filedialog.asksaveasfilename(
    #         filetypes=(("Text Documents", "*.txt"), ("All files", "*.*")),
    #         title='Proszę wybierz plik .txt, do którego chcesz zapisać kod Prüfera.',
    #         defaultextension='.txt')
    #     if plik_Prufer:
    #         try:
    #             print("Plik został pomyślnie zapisany.")
    #             plik = open(plik_Prufer, 'w')
    #             plik.write(tresc_pliku)
    #             plik.close
    #         except:
    #             showerror("Open Source File", "Failed to save file\n'%s'" % plik_Prufer)

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def zwieksz_node_name():
        aski = ord(OdczytZapis.node_name)
        aski += 1
        OdczytZapis.node_name = chr(aski)

    def losowa_inna_niz_randomowo_od():
        while True:
            r = random.choice(OdczytZapis.tablica_nazw_wierzcholkow)
            b = False
            if r != OdczytZapis.wybrana_randomowa_przed_chwila[0]:
                b = True
            if b == True:
                break
        return r

    def randomowo_od():
        r_od = OdczytZapis.tablica_nazw_wierzcholkow[-1]
        OdczytZapis.tablica_wybranych_randomowych_od.append(r_od)
        OdczytZapis.wybrana_randomowa_przed_chwila = r_od
        return r_od

    def randomowo_do():
        r_do = OdczytZapis.losowa_inna_niz_randomowo_od()
        OdczytZapis.tablica_wybranych_randomowych_do.append(r_do)
        return r_do

    def gen_tree_plus_node():
        OdczytZapis.g.node(str(OdczytZapis.node_name))
        OdczytZapis.tablica_nazw_wierzcholkow.append(str(OdczytZapis.node_name))
        OdczytZapis.zwieksz_node_name()

        if OdczytZapis.l_ggn > 1:
            OdczytZapis.g.edge(OdczytZapis.randomowo_od(),OdczytZapis.randomowo_do())

        obrazek = OdczytZapis.g.render('dot', 'png')
        return obrazek

    #
    # def liscie_od_najmniejszego_do_najwiekszego():
    #     # wyciagniecie tablicy lisci:
    #     tablica_lisci = []
    #     for i in range(len(OdczytZapis.tablica_wybranych_randomowych_od)):
    #         b = True
    #         for j in range(len(OdczytZapis.tablica_wybranych_randomowych_do)):
    #             if OdczytZapis.tablica_wybranych_randomowych_od[i] == OdczytZapis.tablica_wybranych_randomowych_do[j]:
    #                 b = False
    #         if b == True:
    #             tablica_lisci.append(OdczytZapis.tablica_wybranych_randomowych_od[i])
    #     for i in range(len(OdczytZapis.tablica_wybranych_randomowych_do)):
    #         b = True
    #         for j in range(len(OdczytZapis.tablica_wybranych_randomowych_od)):
    #             if OdczytZapis.tablica_wybranych_randomowych_do[i] == OdczytZapis.tablica_wybranych_randomowych_od[j]:
    #                 b = False
    #         if b == True:
    #             tablica_lisci.append(OdczytZapis.tablica_wybranych_randomowych_do[i])
    #     # powyżej wytypowałem te wierzchołki, do których wchodzą krawędzie, ale nie wychodzą, oraz te, z których wychodzą krawędzie, ale żadne nie wchodzą - czyli które są tylko w zbiorze 'od', albo tylko w zbiorze 'do'...
    #     # jednak to nie wystarczy, ponieważ może tak się zdarzyć, że wierzchołek nie będący wcale liściem ma np. dwie krawędzie wchodzące, lub wychodzące i takie trzeba usunąć z tablicy_liści...
    #     # tak więc trzeba znaleźć teraz wierzchołki, które są kilka razy w zbiorze 'od' lub w zbiorze 'do' (lub wcześniej liczyć ile razy dany wierzchołek był w od oraz w do i jeśli więcej niż raz, to jest on zapamiętywany i potem usuwany):
    #     for i in range(len(OdczytZapis.tablica_wybranych_randomowych_od)):
    #         k = 0
    #         for j in range(len(OdczytZapis.tablica_wybranych_randomowych_od)):
    #             if OdczytZapis.tablica_wybranych_randomowych_od[i] == OdczytZapis.tablica_wybranych_randomowych_od[j]:
    #                 k+=1
    #         if k>1:
    #             tablica_lisci.remove(OdczytZapis.tablica_wybranych_randomowych_od[i])
    #     for i in range(len(OdczytZapis.tablica_wybranych_randomowych_do)):
    #         k = 0
    #         for j in range(len(OdczytZapis.tablica_wybranych_randomowych_do)):
    #             if OdczytZapis.tablica_wybranych_randomowych_do[i] == OdczytZapis.tablica_wybranych_randomowych_do[j]:
    #                 k+=1
    #         if k>1:
    #             tablica_lisci.remove(OdczytZapis.tablica_wybranych_randomowych_do[i])
    #     # posortowanie tablicy lisci:
    #     tablica_lisci.sort()
    #     return tablica_lisci
    #
    # bufor_tablica_wybranych_randomowych_od = tablica_wybranych_randomowych_od.copy()
    # bufor_tablica_wybranych_randomowych_do = tablica_wybranych_randomowych_do.copy()
    # usuwany_element = 'a'
    # def liscie_od_najmniejszego_do_najwiekszego_uaktualniana():
    #     tablica_lisci = []
    #     bufor = 0
    #     for i in range(len(OdczytZapis.bufor_tablica_wybranych_randomowych_od)):
    #         if OdczytZapis.bufor_tablica_wybranych_randomowych_od[i] == OdczytZapis.usuwany_element:
    #             bufor = i
    #     OdczytZapis.bufor_tablica_wybranych_randomowych_od.remove(OdczytZapis.bufor_tablica_wybranych_randomowych_od[bufor])
    #     OdczytZapis.bufor_tablica_wybranych_randomowych_do.remove(OdczytZapis.bufor_tablica_wybranych_randomowych_do[bufor])
    #     for i in range(len(OdczytZapis.bufor_tablica_wybranych_randomowych_od)):
    #         b = True
    #         for j in range(len(OdczytZapis.bufor_tablica_wybranych_randomowych_do)):
    #             if OdczytZapis.bufor_tablica_wybranych_randomowych_od[i] == OdczytZapis.bufor_tablica_wybranych_randomowych_do[j]:
    #                 b = False
    #         if b == True:
    #             tablica_lisci.append(OdczytZapis.bufor_tablica_wybranych_randomowych_od[i])
    #     tablica_lisci.sort()
    #     return tablica_lisci
    #
    # def ten_z_ktorym_sie_laczy(usuwany_element):
    #     bufor = 0
    #     for i in range(len(OdczytZapis.tablica_wybranych_randomowych_od)):
    #         if usuwany_element == OdczytZapis.tablica_wybranych_randomowych_od[i]:
    #             bufor = i
    #     for i in range(len(OdczytZapis.tablica_wybranych_randomowych_do)):
    #         if usuwany_element == OdczytZapis.tablica_wybranych_randomowych_do[i]:
    #             bufor = i
    #     dodawany_element = OdczytZapis.tablica_wybranych_randomowych_do[bufor]
    #     # ta funkcja do poprawy!!!
    #     return dodawany_element
    #
    # def Pic2Prufer_konwersja():
    #     tabela_Prufera = []
    #     tablica_lisci = OdczytZapis.liscie_od_najmniejszego_do_najwiekszego()
    #     tablica_lisci_pomniejszana = tablica_lisci.copy()
    #     i = 0
    #     while i < len(OdczytZapis.tablica_nazw_wierzcholkow)-2:
    #         OdczytZapis.usuwany_element = tablica_lisci_pomniejszana[0]
    #         dodawany_element = OdczytZapis.ten_z_ktorym_sie_laczy(OdczytZapis.usuwany_element)
    #         tabela_Prufera.append(dodawany_element)
    #         tablica_lisci_pomniejszana.remove(OdczytZapis.usuwany_element)
    #         tablica_lisci_pomniejszana = OdczytZapis.liscie_od_najmniejszego_do_najwiekszego_uaktualniana()
    #         i += 1
    #     trescpliku = ' '.join(str(e) for e in tabela_Prufera)
    #     return trescpliku
    # def Pic2Prufer():
    #     tresc_pliku = OdczytZapis.Pic2Prufer_konwersja()
    #     plik_Prufer = filedialog.asksaveasfilename(
    #         filetypes=(("Text Documents", "*.txt"), ("All files", "*.*")),
    #         title='Proszę wybierz plik .txt, do którego chcesz zapisać kod Prüfera.',
    #         defaultextension='.txt')
    #     if plik_Prufer:
    #         try:
    #             print("Plik został pomyślnie zapisany.")
    #             plik = open(plik_Prufer, 'w')
    #             plik.write(tresc_pliku)
    #             plik.close
    #         except:
    #             showerror("Open Source File", "Failed to save file\n'%s'" % plik_Prufer)