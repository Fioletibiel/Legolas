from sympy import combinatorics


class Prufer(object):

    def __init__(self):
        pass

    def Prufer2DOT(tresc_pliku):
        return tresc_pliku

    def DOT2Prufer(tresc_pliku):
        combinatorics.Prufer(tresc_pliku)
        return tresc_pliku

    def checkifPrufer(tresc_pliku):
        return tresc_pliku

    # def DOT2Prufer():
    #     plik_DOT = filedialog.askopenfilename(filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")), title="Proszę wybierz plik z kodem DOT")
    #     if plik_DOT:
    #         try:
    #             print("Plik został wczytany pomyślnie.")
    #         except:
    #             showerror("Open Source File", "Failed to read file\n'%s'" % plik_DOT)
    #         tresc_pliku = open(plik_DOT, 'w')
    #         tresc_pliku = Prufer.DOT2Prufer(tresc_pliku)
    #         plik_Prufer = filedialog.asksaveasfilename(
    #             filetypes=(("Text Documents", "*.txt"), ("All files", "*.*")),
    #             title='Proszę wybierz plik .txt, do którego chcesz zapisać kod Prüfera.',
    #             defaultextension='.txt')
    #         if plik_Prufer:
    #             try:
    #                 print("Plik został pomyślnie zapisany.")
    #             except:
    #                 showerror("Open Source File", "Failed to save file\n'%s'" % plik_Prufer)
    #             plik = open(plik_Prufer, 'w')
    #             plik.write(tresc_pliku)
    #             plik.close()
    #
    # def Prufer2DOT():
    #     plik_Prufer = filedialog.askopenfilename(filetypes=(("Text Documents", "*.txt"), ("All files", "*.*")), title="Proszę wybierz plik .txt z kodem Prüfera")
    #     if plik_Prufer:
    #         try:
    #             print("Plik został wczytany pomyślnie.")
    #         except:
    #             showerror("Open Source File", "Failed to read file\n'%s'" % plik_Prufer)
    #         Prufer.checkifPrufer(plik_Prufer)
    #         tresc_pliku = open(plik_Prufer, 'w')
    #         Prufer.Prufer2DOT(tresc_pliku)
    #         plik_DOT = filedialog.asksaveasfilename(filetypes=(("Text Documents", "*.txt"), ("DOT Files", "*.dot"), ("All files", "*.*")),title='Proszę wybierz plik .txt, do którego chcesz zapisać kod DOT.',defaultextension='.txt')
    #         if plik_DOT:
    #             try:
    #                 print("Plik został pomyślnie zapisany.")
    #             except:
    #                 showerror("Open Source File", "Failed to save file\n'%s'" % plik_DOT)
    #             plik = open(plik_DOT, 'w')
    #             plik.write(tresc_pliku)
    #             plik.close()