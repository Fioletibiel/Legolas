from tkinter import *

class OdczytZapis(object):

    def __init__(self):
        self.root = Tk()

    def odczyt(self):
        # plik = open('nazwa_pliku')
        # try:
        #     tekst = plik.read()
        # finally:
        #     plik.close()
        # print(tekst)
        self.root.nazwa_pliku = filedialog.askopenfilename(title='wybierz plik .txt z zakodowanym grafem, lub z kodem Prüfera',filetypes=("dokument tekstowy","*.txt"))
        return self.root.nazwa_pliku

    def zapis(self):
        # plik = open('plik', 'w')
        # plik.write("tresc")
        # plik.close()
        self.root.nazwa_pliku = filedialog.asksavefilename(title='wybierz plik .txt, do którego chcesz zapisać zakodowany graf, lub kod Prüfera',filetypes=("dokument tekstowy","*.txt"))
        return self.root.nazwa_pliku
        # x = input('Podaj x: ')