from tkinter import *
import tkinter

class TkinterGUI(object):

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


    def __init__(self):
        self.root = Tk()
        # self.root.geometry("200x250")
        self.root.title('Legolas')
        self.root.iconbitmap('celtic_tree.ico')


        # topFrame = Frame(self.root).pack()
        # bottomFrame = Frame(self.root).pack(side=BOTTOM)
        #
        # button1 = Button(topFrame, text="Button1", fg="red").pack(side=TOP)
        # button2 = Button(topFrame, text="Button2", fg="blue").pack(side=TOP)
        # button3 = Button(bottomFrame, text="Button3", fg="green").pack(side=TOP)
        # button4 = Button(bottomFrame, text="Button4", fg="purple").pack(side=TOP)
        #
        # l1 = Label(self.root, text="Napis_1", bg="red", fg="white").pack()
        # l2 = Label(self.root, text="Napis_2", bg="black", fg="green").pack(fill=X)
        # l3 = Label(self.root, text="Napis_3", bg="grey", fg="blue").pack(side=LEFT, fill=Y)


        # l1 = Label(self.root, text="Name", bg="red", fg="white").grid(row=0, sticky=E)
        # l2 = Label(self.root, text="Password", bg="black", fg="green").grid(row=1, sticky=E)
        # l3 = Label(self.root, text="Napis_3", bg="grey", fg="blue").grid(row=2, sticky=W)
        #
        # entry1 = Entry(self.root).grid(row=0, column = 1)
        # entry2 = Entry(self.root).grid(row=1, column = 1)
        #
        # c = Checkbutton(self.root, text="text").grid(columnspan=2)


        # def printName():
        #     print("Hello my name is Paul!")
        # btn1=Button(self.root, text="Print my name", command=printName).pack()


        # def printName(event):
        #     print("Hello my name is Paul!")
        # btn1 = Button(self.root, text="Print my name")
        # btn1.bind("<Button-1>", printName)         # <Button-1> oznacza lewy przycisk myszy
        # btn1.pack()


        # def leftClick(event):
        #     print("Left")
        #
        # def middleClick(event):
        #     print("Middle")
        #
        # def rightClick(event):
        #     print("Right")
        #
        # frame = Frame(self.root, width=300, height=250)
        # frame.bind("<Button-1>", leftClick)
        # frame.bind("<Button-2>", middleClick)
        # frame.bind("<Button-3>", rightClick)
        # frame.pack()


        



        self.root.mainloop()

