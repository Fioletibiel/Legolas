import time
import pygame as pg

class PyGameGUI(object):

    def __init__(self):
        self.tps_max = 100

        pg.init()
        self.wyswietlacz = pg.display.set_mode((1280,720))
        pg.display.set_caption('Legolas')
        ikonka = pg.image.load('celtic_tree.gif')
        pg.display.set_icon(ikonka)

        self.tps_clock = pg.time.Clock()
        self.tps_delta = 0.0

        self.kolor_szary = (200, 200, 200)
        self.prostokat_1 = pg.Rect(10, 10, 150, 90)
        self.prostokat_2 = pg.Rect(10, 110, 150, 90)
        self.prostokat_3 = pg.Rect(10, 210, 150, 90)

        while True:
            for wydarzenie in pg.event.get():
                if wydarzenie.type == pg.QUIT:
                    exit(0)
                elif wydarzenie.type == pg.KEYDOWN and wydarzenie.key == pg.K_ESCAPE:
                    exit(0)

            self.tps_delta +=self.tps_clock.tick()/1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.klik()
                self.tps_delta -= 1 / self.tps_max

            self.wyswietlacz.fill((255, 255, 255))
            self.wyswietlanie()
            # pg.display.update()d
            pg.display.flip()

    def klik(self):
        # klawisz = pg.key.get_pressed()
        # if klawisz[pg.K_d]:
        #     self.prostokat.x += 3
        # elif klawisz[pg.K_a]:
        #     self.prostokat.x -= 3
        # elif klawisz[pg.K_w]:
        #     self.prostokat.y -= 3
        # elif klawisz[pg.K_s]:
        #     self.prostokat.y += 3
        pass

    def wyswietlanie(self):
        pg.draw.rect(self.wyswietlacz, self.kolor_szary, self.prostokat_1)
        pg.draw.rect(self.wyswietlacz, self.kolor_szary, self.prostokat_2)
        pg.draw.rect(self.wyswietlacz, self.kolor_szary, self.prostokat_3)



# Przeklejone dla przejrzystości z TkinterGUI:

    # def __init__(self):
    #     self.root = Tk()
    #     self.root.geometry("200x250")
    #     self.root.title('Legolas')
    #     self.root.iconbitmap('celtic_tree.ico')
    #
    #     l1 = Label(self.root, text = "Napis_1").grid(row=0).pack(side=TOP)
    #     l2 = Label(self.root, text = "Napis_2").grid(row=1).pack(side=TOP)
    #
    #     ent = Entry(self.root).grid(row=0, column=1).pack(side=TOP)
    #     var_chk = IntVar()
    #     rd1 = Radiobutton(self.root, text = "Radiobutton_1", variable = var_chk, value=1).grid(row=1, column=1, sticky=W).pack(side=TOP)
    #     rd2 = Radiobutton(self.root, text = "Radiobutton_2", variable = var_chk, value=2).grid(row=1, column=1, sticky=E).pack(side=TOP)
    #     btn = Button(self.root, text="Przycisk", bg="black", fg="blue").grid(row=2, columnspan=2, command = show_data).pack(side=TOP)
    #     txt = Text(self.root, width=250, height=10, wrap=WORD).grid(row=3, columnspan=2, sticky=W).pack(side=TOP)
    #
    #     self.root.mainloop()
    #
    # def show_data(self):
    #     txt.delete(0.0, 'end')
    #     txtName = ent.get()
    #     gender = var_chk.get()
    #
    #     if gender ==1:
    #         gender = "sir"
    #     else:
    #         gender = "ma'm"
    #
    #     sentence = "Hello, " + str(txtName) + "\nHow are you " + gender + "?"
    #     txt.insert(0.0, sentence)


    # def __init__(self):
    #     self.root = Tk()
    #     # self.root.geometry("200x250")
    #     self.root.title('GIZ projekt')
    #     self.root.iconbitmap('celtic_tree.ico')
    #
    #
    #     # topFrame = Frame(self.root).pack()
    #     # bottomFrame = Frame(self.root).pack(side=BOTTOM)
    #     #
    #     # button1 = Button(topFrame, text="Button1", fg="red").pack(side=TOP)
    #     # button2 = Button(topFrame, text="Button2", fg="blue").pack(side=TOP)
    #     # button3 = Button(bottomFrame, text="Button3", fg="green").pack(side=TOP)
    #     # button4 = Button(bottomFrame, text="Button4", fg="purple").pack(side=TOP)
    #     #
    #     # l1 = Label(self.root, text="Napis_1", bg="red", fg="white").pack()
    #     # l2 = Label(self.root, text="Napis_2", bg="black", fg="green").pack(fill=X)
    #     # l3 = Label(self.root, text="Napis_3", bg="grey", fg="blue").pack(side=LEFT, fill=Y)
    #
    #
    #     # l1 = Label(self.root, text="Name", bg="red", fg="white").grid(row=0, sticky=E)
    #     # l2 = Label(self.root, text="Password", bg="black", fg="green").grid(row=1, sticky=E)
    #     # l3 = Label(self.root, text="Napis_3", bg="grey", fg="blue").grid(row=2, sticky=W)
    #     #
    #     # entry1 = Entry(self.root).grid(row=0, column = 1)
    #     # entry2 = Entry(self.root).grid(row=1, column = 1)
    #     #
    #     # c = Checkbutton(self.root, text="text").grid(columnspan=2)
    #
    #
    #     # def printName():
    #     #     print("Hello my name is Paul!")
    #     # btn1=Button(self.root, text="Print my name", command=printName).pack()
    #
    #
    #     # def printName(event):
    #     #     print("Hello my name is Paul!")
    #     # btn1 = Button(self.root, text="Print my name")
    #     # btn1.bind("<Button-1>", printName)         # <Button-1> oznacza lewy przycisk myszy
    #     # btn1.pack()
    #
    #
    #     # def leftClick(event):
    #     #     print("Left")
    #     #
    #     # def middleClick(event):
    #     #     print("Middle")
    #     #
    #     # def rightClick(event):
    #     #     print("Right")
    #     #
    #     # frame = Frame(self.root, width=300, height=250)
    #     # frame.bind("<Button-1>", leftClick)
    #     # frame.bind("<Button-2>", middleClick)
    #     # frame.bind("<Button-3>", rightClick)
    #     # frame.pack()
    #
    #     # self.root.mainloop()
